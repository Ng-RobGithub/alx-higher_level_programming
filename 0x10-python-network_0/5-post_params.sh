#!/usr/bin/python3

# Check if URL argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Store the URL argument
url=$1

# Send a POST request to the URL with specified parameters
curl -s -X POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$url"
