#!/usr/bin/python3
"""
Uses the GitHub API to display a user's id.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./10-my_github.py <username> <token>")
        sys.exit(1)

    username = sys.argv[1]
    token = sys.argv[2]

    url = f"https://api.github.com/users/{username}"
    headers = {'Authorization': f'token {token}'}

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        sys.exit(1)

    try:
        user_data = response.json()
        print(user_data)
        print(user_data['id'])
    except KeyError:
        print("Error: Unable to find user id.")
        sys.exit(1)
