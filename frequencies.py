from nltk import word_tokenize, sent_tokenize
import pandas as pd
from string import punctuation

with open('data/witcher.txt', 'r') as f:
    text = f.read()


sentences = sent_tokenize(text)

word_counts = {}
for sentence in sentences:
    tokens = word_tokenize(sentence)
    for token in tokens:
        if token not in word_counts:
            word_counts[token] = 1
        else:
            word_counts[token] += 1


counts_list = list(word_counts.items())
df = pd.DataFrame(counts_list, columns=['word', 'count'])
to_drop = df['word'].apply(lambda word: word in punctuation + '’...as')


df = df[~to_drop]
df.sort_values(by='count', ascending=False, inplace=True)
df.to_csv('data/counts.csv', index=False)
