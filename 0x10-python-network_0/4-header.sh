#!/usr/bin/python3

# Check if URL argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Store the URL argument
url=$1

# Send a GET request to the URL with the specified header
curl -s -H "X-School-User-Id: 98" "$url"
