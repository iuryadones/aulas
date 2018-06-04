from nltk import pos_tag
from nltk import word_tokenize
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction import FeatureHasher

from itertools import chain


def feature_extraction_1():
    measurements = [
        {'city': 'Dubai', 'temperature': 33.},
        {'city': 'London', 'temperature': 12.},
        {'city': 'San Francisco', 'temperature': 18.},
    ]

    vec = DictVectorizer()

    vectorized = vec.fit_transform(measurements)

    print(vectorized.toarray())

    print(vec.get_feature_names())

    # import ipdb; ipdb.set_trace()

def feature_extraction_2():

    pos_window = [
        {
            'word-2': 'the',
            'pos-2': 'DT',
            'word-1': 'cat',
            'pos-1': 'NN',
            'word+1': 'on',
            'pos+1': 'PP',
        },
    ]

    vec = DictVectorizer()

    pos_vectorized = vec.fit_transform(pos_window)

    print(pos_vectorized.toarray())

    print(vec.get_feature_names())


def feature_extraction_3():

    hasher = FeatureHasher(n_features=10)

    counter_words = [{'dog': 1, 'cat':2, 'elephant':4}, {'dog': 2, 'run': 5}]

    out = hasher.transform(counter_words)

    print(out.toarray())

def feature_extraction_4():

    def token_features(token, part_of_speech):
        if token.isdigit():
            yield "numeric"
        else:
            yield f"token={token.lower()}"
            yield f"token,pos={token},{part_of_speech}"
        if token[0].isupper():
            yield "uppercase_initial"
        if token.isupper():
            yield "all_uppercase"
        yield f"pos={part_of_speech}"

    text_raw = (
        "Fibonacci numbers appear to have first arisen in perhaps 200 BC in work"
        "by Pingala on enumerating possible patterns of poetry formed from"
        "syllables of two lengths."
    )

    corpus = word_tokenize(text_raw)

    print(corpus, end="\n\n")
    print(pos_tag(corpus), end='\n\n')

    raw_X = [
        [l for l in token_features(token, pos_tagger)]
        for token, pos_tagger in pos_tag(corpus)
    ]

    for _x in raw_X:
        print(_x)

    hasher = FeatureHasher(input_type='string', n_features=5)

    # analise palavra 
    raw_X = chain(raw_X)

    # analise frase
    # raw_X = chain(*raw_X)

    raw_X = [r for r in raw_X]

    print(raw_X)

    X = hasher.transform(chain(raw_X))

    print(X.toarray().flatten())


if __name__ == '__main__':
    feature_extraction_1()
    feature_extraction_2()
    feature_extraction_3()
    feature_extraction_4()

