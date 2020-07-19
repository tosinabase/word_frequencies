from nltk import word_tokenize, sent_tokenize
from nltk.corpus import words
import pandas as pd

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


word_dictionary = words.words()
counts_list = list(word_counts.items())
df = pd.DataFrame(counts_list, columns=['word', 'count'])
is_word = df['word'].apply(lambda word: word in word_dictionary)
df = df[is_word]
df.sort_values(by='count', ascending=False, inplace=True)
df.to_csv('data/counts.csv', index=False)
