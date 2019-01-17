from gensim.models import KeyedVectors
import numpy as np

global model
global index2word_set

model = KeyedVectors.load_word2vec_format('gensim/gensim_model.bin', binary=True)
index2word_set = set(model.wv.index2word)


def avg_feature_vector(sentence, model, num_features, index2word_set):

    words = sentence.split()
    feature_vec = np.zeros((num_features,), dtype='float32')
    n_words = 0
    for word in words:
        if word in index2word_set:
            n_words += 1
            feature_vec = np.add(feature_vec, model[word])

    if (n_words > 0):
        feature_vec = np.divide(feature_vec, n_words)

    return feature_vec

print("[INFO] Model loaded...")