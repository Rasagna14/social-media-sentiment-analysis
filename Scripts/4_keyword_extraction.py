from collections import Counter
import pandas as pd
import ast

df = pd.read_csv('../data/text_cleaned.csv')
df['tokens'] = df['tokens'].apply(lambda x: ast.literal_eval(str(x)))
all_words = [word for tokens in df['tokens'] for word in tokens if word.isalpha()]
keywords = Counter(all_words).most_common(50)

for word, freq in keywords:
    print(f"{word}: {freq}")