import numpy as np 
from math import *
class mergeScoreList():
	"""docstring for mergeRankList"""
	

	def merge(self, Score1, Score2, lambdaa):

	# Given two rankList, one by collaborative and another by content-based filtering, gives merged output of rankList of them
	#public ArrayList<Double> merge(ArrayList<Double> rList1,ArrayList<Double> rList2,double lambda)
	
		mergeScore = (lambdaa* Score1) + (1- lambdaa)* Score2
		return mergeScore
	
	# normalizes each of the elements as (x - (mu))/(sigma) to range each output between -1 to 1
	def normalize(self, scoreList):
		mean = scoreList.mean() 
		variance  = scoreList.var()
		sd = sqrt(variance)
		if(sd == 0):
			return scoreList.astype(float)
		else:
			scoreList = (scoreList - mean)/ sd

		return scoreList.astype(float)

	

	def getMean(self, scoreList):

		return scoreList.mean() 
	
	def getVariance(self, scoreList):
	
		return scoreList.var()
	
