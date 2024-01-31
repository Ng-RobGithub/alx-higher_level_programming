#!/bin/bash
# Script that sends a POST request to the URL, and displays the body of the response
curl -sX POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
