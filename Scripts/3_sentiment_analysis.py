from textblob import TextBlob
import pandas as pd

df = pd.read_csv('../data/text_cleaned.csv')

def get_sentiment(text):
    return TextBlob(str(text)).sentiment.polarity

df['sentiment_score'] = df['text'].apply(get_sentiment)
df['sentiment_label'] = df['sentiment_score'].apply(lambda x: 'Positive' if x > 0 else 'Negative' if x < 0 else 'Neutral')
df.to_csv('../data/sentiment_scored.csv', index=False)