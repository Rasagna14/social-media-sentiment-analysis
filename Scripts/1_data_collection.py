# Twitter + Reddit API Data Collection
import tweepy
import praw
import pandas as pd

# Twitter setup (replace with real keys)
auth = tweepy.OAuthHandler('API_KEY', 'API_SECRET')
auth.set_access_token('ACCESS_TOKEN', 'ACCESS_SECRET')
api = tweepy.API(auth)

tweets = []
for tweet in tweepy.Cursor(api.search_tweets, q="campaign_name", lang="en").items(50000):
    tweets.append({
        'platform': 'Twitter',
        'text': tweet.text,
        'likes': tweet.favorite_count,
        'retweets': tweet.retweet_count
    })

# Reddit setup
reddit = praw.Reddit(client_id='CLIENT_ID', client_secret='CLIENT_SECRET', user_agent='bot')
reddit_posts = []
for post in reddit.subreddit('marketing').search('campaign_name', limit=50000):
    reddit_posts.append({
        'platform': 'Reddit',
        'text': post.title + ' ' + post.selftext,
        'upvotes': post.score
    })

df = pd.DataFrame(tweets + reddit_posts)
df.to_csv('../data/collected_data.csv', index=False)
