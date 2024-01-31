#!/bin/bash
# This script takes in a URL, sends a request to that URL, and displays the size of the body of the response.

# Send a request to the provided URL and display the size of the response body in bytes
size=$(curl -sI "$1" | grep -i Content-Length | awk '{print $2}')
if [ -z "$size" ]; then
    echo "Unable to determine the size of the response body."
else
    echo "$size"
fi
