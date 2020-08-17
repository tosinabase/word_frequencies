from nltk import word_tokenize, sent_tokenize
from nltk.corpus import words
import pandas as pd


def word_frequencies(text, check_by_dictionary=True):
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
    df.sort_values(by='count', ascending=False, inplace=True)

    if check_by_dictionary:
        word_dictionary = words.words()
        is_word = df['word'].apply(lambda word: word in word_dictionary)
        df = df[is_word]

    return df


if __name__ == '__main__':
    with open('data/test.txt', 'r') as f:
        test_text = f.read()
    test_df = word_frequencies(test_text)
    print(test_df)
