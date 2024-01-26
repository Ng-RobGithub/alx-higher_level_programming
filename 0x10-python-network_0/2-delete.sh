#!/usr/bin/python3

# Check if URL argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Store the URL argument
url=$1

# Send a DELETE request to the URL and store the response body in a temporary file
response=$(mktemp)
curl -s -X DELETE -o "$response" -w "%{http_code}" "$url"

# Check if curl command was successful
if [ $? -ne 0 ]; then
    echo "Error: Failed to send DELETE request to $url"
    rm -f "$response"  # Remove the temporary file
    exit 1
fi

# Read the status code from the response file
status_code=$(tail -n1 "$response")

# Display the body of the response
if [ "$status_code" -eq 200 ]; then
    sed '$d' "$response"  # Remove the last line (status code)
else
    echo "Error: Unexpected status code received: $status_code"
fi

# Clean up the temporary file
rm -f "$response"
