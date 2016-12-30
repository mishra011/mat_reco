
import numpy as np
class behave():
	def weight():

behaviourMatrix = [[0,0,0,0],[0,0,0,0],[0,1,0,1],[0,0,0,0],[0,0,1,1],[0,0,0,0],[1,0,1,0]]
behaviourMatrix = np.array(behaviourMatrix, dtype = float)
#initializing weight for different actions:
# till now i am considering only 4 actions
# They are click, clip, like and share.
wt_clip = .9
wt_click = .3
wt_like = .7
wt_share = .5
action = np.array([wt_clip, wt_click, wt_like, wt_share])
b = behaviourMatrix[2]
x = [a * 2 for a in b]
asd = action * b
print asd
az = np.sum(asd)
print az
pastPreference = [2,4,6]

print pastPreference
wt = np.array([])
for a in pastPreference:

	product = action * behaviourMatrix[a]
	temp_wt = np.sum(product)
	wt = np.hstack((wt, temp_wt))

print wt