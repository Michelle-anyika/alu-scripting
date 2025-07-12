#!/usr/bin/python3
"""
This module defines a function to query the Reddit API and
print the titles of the first 10 hot posts for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for a subreddit.

    Args:
        subreddit (str): The subreddit to search.
    """
    headers = {'User-Agent': 'ALU-Student-Agent/1.0'}
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            print(None)
            return

        posts = response.json().get('data', {}).get('children', [])
        for post in posts:
            print(post.get('data', {}).get('title'))

    except requests.RequestException:
        print(None)


