#!/usr/bin/python3
"""
This module defines the function `number_of_subscribers`
which queries the Reddit API and returns the number of
subscribers for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    If the subreddit is invalid or not found, returns 0.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: Number of subscribers or 0 if invalid subreddit.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "ALU-Student-Agent/1.0"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            return response.json().get("data", {}).get("subscribers", 0)
        return 0
    except requests.RequestException:
        return 0
