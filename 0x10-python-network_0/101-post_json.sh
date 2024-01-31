#!/bin/bash

# Sends a JSON POST request to a URL passed as the first argument
# Sends the contents of a file as the body of the request
# Displays the body of the response

# Check if the number of arguments is correct
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 URL JSON_FILE"
    exit 1
fi

# Check if the JSON file exists
if [ ! -f "$2" ]; then
    echo "File '$2' not found"
    exit 1
fi

# Read the JSON file content
json_content=$(cat "$2")

# Validate JSON syntax
if ! jq -e . >/dev/null 2>&1 <<<"$json_content"; then
    echo "Not a valid JSON"
    exit 1
fi

# Send a POST request with JSON content and display the response body
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
