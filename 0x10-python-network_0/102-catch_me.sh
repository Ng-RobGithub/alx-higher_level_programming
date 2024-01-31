#!/bin/bash

# Makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with "You got me!"

# Send a request to catch_me endpoint with a PUT method and a specific header
curl -s -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" "0.0.0.0:5000/catch_me" --output /dev/null
