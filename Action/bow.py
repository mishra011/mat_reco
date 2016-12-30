import gensim
from gensim import corpora, models, similarities
from os import listdir
from os.path import isfile, join

docLabels = []
docLabels = [f for f in listdir("/home/deepak/Work/D2V/docs") if 
	f.endswith('.txt')]


#print docLabels

documents = []
for doc in docLabels:
	documents.append(open('/home/deepak/Work/D2V/docs/' + doc).read())

#print documents[6]

stoplist = set('for a of the and to in'.split())
texts = [[word for word in document.lower().split() if word not in stoplist]
		for document in documents]

#print texts[6]

from collections import defaultdict
frequency = defaultdict(int)
for text in texts:
    for token in text:
        frequency[token] += 1

texts = [[token for token in text if frequency[token] > 1]
          for text in texts]

from pprint import pprint  # pretty-printer
#pprint(texts[6])

dictionary = corpora.Dictionary(texts)
dictionary.save('/home/deepak/Work/D2V/docs/deerwester.dict')
#print dictionary

#print(dictionary.token2id)

new_doc = "I want to be great in Machine Learning"
new_vec = dictionary.doc2bow(new_doc.lower().split())
#print new_vec

corpus = [dictionary.doc2bow(text) for text in texts]
#corpora.MmCorpus.serialize('/home/deepak/Work/D2V/docs/deerwester.mm', corpus)
lsi = models.LsiModel(corpus, id2word=dictionary, num_topics=12)
vec_bow = corpus[6]
vec_lsi = lsi[vec_bow]
#print vec_lsi

#corpus = corpora.MmCorpus('/home/deepak/Work/D2V/docs/deerwester.mm')
#print corpus[6]

"""
for doc in corpus:
	print doc
"""
#print corpus[1]


#corpora.BleiCorpus.serialize('/home/deepak/Work/D2V/docs/corpus.lda-c', corpus)
#print corpus[6]

import numpy as np
#numpy_matrix = np.random.randint(10, size=[5,2])  # random matrix as an example
numpy_matrix = np.matrix(corpus)
#print numpy_matrix
#y = np.array(numpy_matrix)
#print y[0,6]

#x = '|'.join(map(str, y[0,6]))
#print x


#corpus = gensim.matutils.Dense2Corpus(numpy_matrix)
#print corpus

#numpy_matrix = gensim.matutils.corpus2dense(corpus, num_terms=1, dtype = float)
#print numpy_matrix

"""
import scipy.sparse
scipy_sparse_matrix = scipy.sparse.random(5,2)  # random sparse matrix as example
corpus = gensim.matutils.Sparse2Corpus(scipy_sparse_matrix)
scipy_csc_matrix = gensim.matutils.corpus2csc(corpus)
#print scipy_csc_matrix
"""


tfidf = models.TfidfModel(corpus)
x = tfidf[corpus[6]]
print x
tfidf.save('/home/deepak/Work/D2V/docs/foo.tfidf_model')
vec = [(0, 1), (4, 1)]
print(tfidf[vec])

index = similarities.SparseMatrixSimilarity(tfidf[corpus], num_features=2)
sims = index[vec_lsi]
#print sims
#print(list(enumerate(sims)))






