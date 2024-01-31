#!/bin/bash
# Sends a DELETE request to the URL passed as the first argument and displays the body of the response

# Send a DELETE request and display the response body
curl -sX DELETE "$1"
