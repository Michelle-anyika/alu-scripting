#!/usr/bin/python3
"""Query Reddit API for top 10 hot posts in a subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts for a subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'linux:alu-api-advanced:v1.0 (by /u/Anonymous)'}

    response = requests.get(url, headers=headers, allow_redirects=False, timeout=5)
    
    if response.status_code == 200:
        try:
            posts = response.json()['data']['children']
            for post in posts[:10]:
                print(post['data']['title'])
        except (KeyError, ValueError):
            print(None)
    else:
        print(None)
