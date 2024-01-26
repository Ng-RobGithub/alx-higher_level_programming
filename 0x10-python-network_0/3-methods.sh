#!/usr/bin/python3

# Check if URL argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Store the URL argument
url=$1

# Send an OPTIONS request to the URL and display allowed methods
curl -sI -X OPTIONS "$url" | grep "Allow" | cut -d ' ' -f2-
