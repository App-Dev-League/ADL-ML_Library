import os
import cv2
import random
import numpy as np
class ImageProcessor:
	def __init__(self,folder_path,image_width, image_height):
		self.folder_path = folder_path
		self.image_size = (image_width,image_height)
		self.training_data = []
	def resizeImages():
		#loop through the given folder
		for file in os.listdir(folder_path):
			try:
				#read in the images one by one and resize to the image dimensions
				image = cv2.imread({}.format(folderpath + file), cv2.IMREAD_UNCHANGED)
				image = cv2.resize(image,image_size)
			except:
				pass
	def renameImages(root_name):
		self.root_name = root_name
		self.counter = 0
		for file in os.listdir(folder_path):
			try:
				os.rename(file,{}.format(self.root_name + str(self.counter)))
				self.counter++
			except:
				pass
	#formats an image collection to the appropriate shape for some ML model
	def formatImageCollection(new_image_name,label):
		self.X = []
		self.y = []
		self.resizeImages()
		self.renameImages(new_image_name)
		for file in os.listdir(folder_path):
			try:
				image = cv2.imread({}.format(folderpath+file),cv2.IMREAD_UNCHANGED)
				self.training_data.append([image,label])
			except:
				pass
		#shuffle the data
		random.shuffle(training_data)
		#format into ML readable
		for i,l in training_data:
			self.X.append(i)
			self.y.append(l)
		self.X = np.array(self.X).reshape(-1,image_width,image_height,1)
	def edgeDetect():
		pass
