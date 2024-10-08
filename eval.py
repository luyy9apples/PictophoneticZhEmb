from gensim.models import KeyedVectors
from gensim.test.utils import datapath
import os
import sys

# word analogy reasoning
cur_dir = os.path.abspath(os.path.dirname(__file__))
data_path = os.path.join(cur_dir, 'data')

wv_path = sys.argv[1]

wv_pcwe = KeyedVectors.load_word2vec_format(wv_path)

analogy_path = os.path.join(data_path, "analogy.txt")
analogy_scores = wv_pcwe.evaluate_word_analogies(datapath(analogy_path))
print(analogy_scores[0])

# word similarity
sim240_path = os.path.join(data_path, "240.txt")
similarities = wv_pcwe.evaluate_word_pairs(datapath(sim240_path))
print(similarities)

sim297_path = os.path.join(data_path, "297.txt")
similarities297 = wv_pcwe.evaluate_word_pairs(datapath(sim297_path))
print(similarities297)
