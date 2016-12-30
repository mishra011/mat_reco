import gensim
import numpy as np

d2v_model = gensim.models.doc2vec.Doc2Vec.load('science_doc2vec.model')

class vec2():

	def comp_article_features(self):
		a_f = []
		docu1 = ['1.txt', '2.txt','a1.txt','a2.txt','b1.txt','b2.txt','c1.txt']

		for doc in docu1:
			vec = d2v_model.docvecs[doc]
			a_f.append(vec)
		
		article_features = np.array(a_f)
		#print article_features.shape
		return article_features


	def comp_new_article_features(self):
		
		n_a_f = []	
		docu2 = ['c2.txt','c3.txt','c4.txt','c5.txt','d1.txt','d3.txt','new.txt']
		for doc in docu2:
			vec = d2v_model.docvecs[doc]
			n_a_f.append(vec)
			
		asd = np.array(n_a_f)
		#print asd.shape
		asd2 = zip(docu2, asd)
		
		return asd2


	def compute_query_vec(self):

		#parameters
		test_docs="war.txt"
		#inference hyper-parameters
		#start_alpha=0.01
		#infer_epoch=1000
		#alpha=start_alpha, steps=infer_epoch  # there are the parameter of infe_vector method
		test = []
		test.append(open(test_docs).readline())
		

		#infer test vectors
		
		vec = []
		veca = [str(x) for x in d2v_model.infer_vector(test)]
		vec.append(veca)
		a = np.array(vec, dtype = float)

		#print a.shape
		return a

