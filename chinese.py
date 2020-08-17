import jieba
from nltk import sent_tokenize
import pandas as pd


def word_frequencies(text):
    sentences = text.split('。')
    word_counts = {}
    for sentence in sentences:
        tokens = list(jieba.cut(sentence, cut_all=True))
        for token in tokens:
            if token not in word_counts:
                word_counts[token] = 1
            else:
                word_counts[token] += 1

    counts_list = list(word_counts.items())
    df = pd.DataFrame(counts_list, columns=['word', 'count'])
    df.sort_values(by='count', ascending=False, inplace=True)

    return df


if __name__ == "__main__":
    # test_text = u'椅子桶椅子桶铅笔椅子。中国的塔塔尔族是近代俄罗斯鞑靼移民在中国的后代'
    with open('data/ch_test.txt', 'r') as f:
        test_text = f.read()
    df = word_frequencies(test_text)
    print(df.to_string())
