import pandas as pd

df = pd.read_csv('../data/sentiment_scored.csv')
# Filter/save additional datasets if needed
positive = df[df['sentiment_label'] == 'Positive']
positive.to_csv('../data/positive_posts.csv', index=False)