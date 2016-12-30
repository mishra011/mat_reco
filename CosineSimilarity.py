from math import *
import numpy as np
class CosineSimilarity():
	
	# computing cosine similarity between 2 vector
	def computeCosine(self, feature1, feature2):
		#initialization of temporary variables
		dotProduct = 0.0	# magnitude of dot product
		magnitude1 = 0.0	# magnitude of feature1
		magnitude2 = 0.0	# magnitude of feature2
		
		cosineSimilarity = 0.0	
		
		
		product = np.multiply(feature1,feature2)	#product of f1 and f2 features
		dotProduct = np.sum(product)				#dot product of 2 vectors
		pow1 = np.multiply(feature1, feature1)		
		pow2 = np.multiply(feature2, feature2)
		mag1 = np.sum(pow1)					
		#print magnitude1
		mag2 = np.sum(pow2)
		#print magnitude2		
		magnitude1 = sqrt(mag1)
		magnitude2 = sqrt(mag2)
		cosineSimilarity = dotProduct / (magnitude1 * magnitude2)
		if(magnitude1 != 0.0 and magnitude2 != 0.0):
			return cosineSimilarity
		else:
			return 0.0
		#print "cosineSimilarity"
		#print cosineSimilarity
		#return cosineSimilarity
		
	#calculating euclidian distance between 2 vectors 
	def euclidean_distance(self, feature1, feature2):
		diff = feature1 - feature2
		square = diff * diff
		total = np.sum(square)
		d = sqrt(total)
		return d

	