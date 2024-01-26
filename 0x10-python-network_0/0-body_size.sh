#!/usr/bin/python3

# Send a request to the URL passed as an argument and display the size of the body of the response

# Check if the number of arguments is not equal to 1
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 URL"
    exit 1
fi

# Send a request to the URL and get the size of the body of the response
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
