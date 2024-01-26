#!/usr/bin/python3

# Send a request to the URL passed as argument and display only the status code

# Send the request and save the response headers to a temporary file
curl -s -o /tmp/response_headers.txt -w "%{http_code}" "$1"

# Extract and display the status code from the response headers
status_code=$(cat /tmp/response_headers.txt)
echo "$status_code"

# Clean up the temporary file
rm /tmp/response_headers.txt
