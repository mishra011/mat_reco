
from CosineSimilarity import CosineSimilarity
from PreferenceZone import PreferenceZone
import numpy as np
from action_wt import action_wt
from vec2 import vec2

def main():
	v =vec2()
	w = action_wt()
	article_Features = v.comp_article_features()
	behaviourMatrix = [[0,0,0,0],[0,0,0,0],[0,1,0,0],[0,0,0,0],[0,0,1,1],[0,0,0,0],[0,1,0,0]]
	new_article_and_features = v.comp_new_article_features()
	centroid = v.compute_query_vec()	# initial query centroid

	
	new_article_dictionay = zip(*new_article_and_features)	# unziping the title and features
	new_article_Features = new_article_dictionay[1]	# extracting new article features
	titles = new_article_dictionay[0]		#	extracting new article features
	new_article_Features = np.array(new_article_Features, dtype = float)	#converting article features to numpy array

	article_bucket = 2			# defining bucket threshold for articles
	
	#print new_article_Features.shape
	
	p = PreferenceZone()
	pastPreference = p.getPastPreference(behaviourMatrix)
	print "pastPreference"
	print pastPreference

	weights = w.compute_weight(behaviourMatrix, pastPreference)
	print "weights"
	print weights
	
	print "initial centroid:"
	print centroid.shape
	
	
	
	preferenceRadius = p.getPreferenceRadius(centroid, pastPreference, article_Features)
	print "initial radius"
	print preferenceRadius
	

	centroid = p.update_Centroid(centroid, pastPreference, article_Features,article_bucket, weights)
	print "updated centroid:"
	print centroid[0][0]
	
	
	preferenceRadius = p.getPreferenceRadius(centroid, pastPreference, article_Features)
	print "new radius"
	print preferenceRadius
	print "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
	
	reco = p.recommendation(new_article_Features, preferenceRadius, centroid, titles)
	print "recommendation after sorting"
	print reco
	

	
if __name__ == "__main__":	

	main()
	
