# -*- coding: utf-8 -*-
import numpy as np
import math

def SIFTSimpleMatcher(descriptor1, descriptor2, thresh=0.7):
	# SIFTSimpleMatcher 
	#   Match one set of SIFT descriptors (descriptor1) to another set of
	#   descriptors (decriptor2). Each descriptor from descriptor1 can at
	#   most be matched to one member of descriptor2, but descriptors from
	#   descriptor2 can be matched more than once.
	#   
	#   Matches are determined as follows:
	#   For each descriptor vector in descriptor1, find the Euclidean distance
	#   between it and each descriptor vector in descriptor2. If the smallest
	#   distance is less than thresh*(the next smallest distance), we say that
	#   the two vectors are a match, and we add the row [d1 index, d2 index] to
	#   the "match" array.
	#   
	# INPUT:
	#   descriptor1: N1 * 128 matrix, each row is a SIFT descriptor.
	#   descriptor2: N2 * 128 matrix, each row is a SIFT descriptor.
	#   thresh: a given threshold of ratio. Typically 0.7
	#
	# OUTPUT:
	#   Match: N * 2 matrix, each row is a match.
	#          For example, Match(k, :) = [i, j] means i-th descriptor in
	#          descriptor1 is matched to j-th descriptor in descriptor2.

	match = list()
	################################################################################
	#                                                                              #
	#                                YOUR CODE HERE:                               #
	#                                                                              #
	################################################################################
	len_image2 = len(descriptor2)
	for i, des1 in enumerate(descriptor1):
		dist = np.sqrt(np.sum((np.tile(des1,(len_image2,1)) - descriptor2)**2, axis=1))
		dist_sort = sorted(dist)
		ratio = dist_sort[0]/dist_sort[1];
		if ratio < thresh:
			index = np.where(dist==dist_sort[0])[0][0]
			match.append([i, index])


	################################################################################
	#                                                                              #
	#                                 END YOUR CODE                                #
	#                                                                              #
	################################################################################
	return match
