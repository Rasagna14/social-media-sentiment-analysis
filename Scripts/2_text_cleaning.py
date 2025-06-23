import pandas as pd
import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')
df = pd.read_csv('../data/collected_data.csv')
df['tokens'] = df['text'].apply(lambda x: word_tokenize(str(x).lower()))
df.to_csv('../data/text_cleaned.csv', index=False)