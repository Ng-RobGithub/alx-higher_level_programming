#!/usr/bin/python3

# Send a JSON POST request to a URL passed as the first argument,
# using the contents of a file passed as the second argument,
# and display the body of the response

# Check if the correct number of arguments is provided
if [ $# -ne 2 ]; then
    echo "Usage: $0 <URL> <JSON_FILE>"
    exit 1
fi

# Check if the JSON file exists
if [ ! -f "$2" ]; then
    echo "Error: JSON file '$2' not found"
    exit 1
fi

# Send the POST request with the contents of the JSON file in the body
response=$(curl -s -X POST -H "Content-Type: application/json" -d "@$2" "$1")

# Check if the response contains "Valid JSON"
if [[ $response == *"Valid JSON"* ]]; then
    echo "Valid JSON"
else
    echo "Not a valid JSON"
fi
