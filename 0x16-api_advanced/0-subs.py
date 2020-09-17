#!/usr/bin/python3
"""
a function that queries the Reddit API and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """ function number_of_subscribers"""
    header = {'User-agent': 'Holberton_school'}
    req = requests.get(
        'https://www.reddit.com/r/{}/about.json'.format(subreddit),
        headers=header, allow_redirects=False).json()
    try:
        return(req.get('data').get('subscribers'))
    except Exception:
        pass
    return(0)
