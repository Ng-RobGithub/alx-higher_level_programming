#!/bin/bash
# Sends a GET request to the URL passed as the first argument, with a custom header, and displays the body of the response

# Send a GET request with custom header and display the response body
curl -sH "X-School-User-Id: 98" "$1"
