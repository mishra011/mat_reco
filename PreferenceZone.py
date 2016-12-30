from math import *
import numpy as np
from CosineSimilarity import CosineSimilarity
from mergeRankList import mergeScoreList

class PreferenceZone():
	# assuming initial centriod to be the query vector
	def update_Centroid(self, centroid, pastPreference, article_Features,article_bucket_length, weight):
		
		num_Preferences = len(pastPreference)		# COUNTING the number of preferences user made
		feature_length = len(article_Features[0])	#counting the length of feature vector
		total_weight = 0
		if(num_Preferences >= article_bucket_length):	#if bucket if full or overflown 

			currCentroid = np.zeros([feature_length]) 	#initializing a temporary centroid to 0 vector
			j = 0
			for i in pastPreference:
				currCentroid = currCentroid + (article_Features[i] * weight[j])			# adding all features associated with past preference 
				total_weight += weight[j]
				j = j+1
			#currCentroid /= numPreferences
			centroid = (currCentroid + centroid)/ (total_weight + 1)		# adding intial centroid vector and calculating WEIGHTED averege
			print total_weight
			return centroid
		else:
			#when bucket is not filled
			return centroid
		

	# calulating the radius of the preference zone
	def getPreferenceRadius(self, centroid, pastPreference, article_Features):
		# radius of the preference zone is the maximun distance of a article
		radius = 0.0	# initial radius = 0
		errorAdd = 0.001   # adding the error in radius
		#calculating dist of each feature 
		for i in pastPreference:
			distance = CosineSimilarity().euclidean_distance(centroid, article_Features[i])
			#print distance
			radius = max(radius, distance) 	# updating radius 
		
		
		radius += errorAdd 	#adding error to the final value of radius
		return radius


	#getting the past preference according to behavior matrix
	def getPastPreference(self, behaviourMatrix):

		pastPreference = []	#initializing empty pastpreference list
		# the loop checks every row for any non zero entry
		# if any non zero row is found it appends it index to past-pref array
		for i in range(len(behaviourMatrix)):
			if (np.count_nonzero(behaviourMatrix[i]) > 0):
				pastPreference.append(i)			# add the potision of the non zero row to pastpreference array


		return pastPreference 		# returning an inter list of indices 

	
	def recommendation(self, new_article_Features, preferenceRadius, centroid, titles):
	
		score = np.array([])		# initializing an empty numpy array score
		#print new_article_Features.shape
		distance_score = np.array([])
		similarity_score = np.array([])
		#computing euclidean distance of every feature vector from centroid  and also computing its similarity with all freatures.
		for feature in new_article_Features:
			distance_from_centroid = CosineSimilarity().euclidean_distance(centroid, feature)
			
			# when feature lies in preference zone score will be positive else negative
			temp_score = preferenceRadius - distance_from_centroid	# then calculating current score
				#print temp_score
			distance_score = np.hstack((score, temp_score))		#adding score to np array

			similarity_with_centroid = CosineSimilarity().computeCosine(centroid, feature)
			similarity_score = np.hstack((similarity_score, similarity_with_centroid))
		normal_distance_score = mergeScoreList.normalize(distance_score)
		# merrging the two scores into one final score with lambdaa = .3
		score = mergeScoreList().merge(normal_distance_score, similarity_score, .3)	
		print "score"
		print score

		
		#print new_article_Features
		#mapping the score with article title and displaying them after sorting according to scores
		sorted_maped_reco = zip(*sorted(zip(-score,titles)))	#neagative sign to sort them in decending order
		return sorted_maped_reco    # returing maped score and title
		
