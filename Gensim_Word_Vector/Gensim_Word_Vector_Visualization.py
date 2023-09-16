import numpy as np

import matplotlib.pyplot as plt

plt.style.use('ggplot')
from sklearn.decomposition import PCA

import gensim.downloader as api
from gensim.models import KeyedVectors


def analogy(x1, x2, y1):
    res = model.most_similar(positive=[y1, x2], negative=[x1])
    return res[0][0]


model = api.load("glove-wiki-gigaword-100")
print(type(model))
print()

print(model['bread'])
print(model['croissant'])
print()

print(model.most_similar('usa'))
print(model.most_similar('banana'))
print()

result = model.most_similar(positive=['woman', 'king'], negative=['man'])
print("{}: {:.4f}".format(*result[0]))
print()

print(analogy('man', 'king', 'woman'))
print(analogy('king', 'man', 'queen'))
print(analogy('pencil', 'sketching', 'camera'))
print(analogy('tall', 'tallest', 'long'))
