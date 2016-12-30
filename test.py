
from CosineSimilarity import CosineSimilarity
from PreferenceZone import PreferenceZone
import numpy as np
from action_wt import action_wt
from vec2 import vec2
from mergeRankList import mergeScoreList

def main():
	m = mergeScoreList()
	v =vec2()
	w = action_wt()
	#article_Features = v.comp_article_features()
	#behaviourMatrix = [[0,0,0,0],[0,0,0,0],[0,1,0,0],[0,0,0,0],[0,0,1,1],[0,0,0,0],[0,1,0,0]]
	#new_article_and_features = v.comp_new_article_features()
	vector = np.array([5,19,10,47,33], dtype = float)	# initial query centroid
	"""
	vector = []
	for i in range(5):	
		vector.append(centroid[0][i])
	#print vector
	vector = [a *1000 for a in vector]
	
	vector = np.array(vector)
	"""
	print vector
	v1 = m.normalize(vector)
	print v1
	
	
	

	
if __name__ == "__main__":	

	main()
	
