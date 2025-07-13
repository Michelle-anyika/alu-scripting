#!/usr/bin/python3
"""Query Reddit API for top 10 hot posts in subreddit."""
import requests


def top_ten(subreddit):
    """Print titles of first 10 hot posts or None if invalid."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'linux:alu-api:v1.0'}
    params = {'limit': 10}
    
    try:
        response = requests.get(url, headers=headers, 
                              params=params, 
                              allow_redirects=False,
                              timeout=5)
        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            for post in posts[:10]:
                print(post.get('data', {}).get('title'))
            return
    except Exception:
        pass
    print("None")
