# -*- coding: utf-8 -*-
import numpy as np

def ComputeAffineMatrix(Pt1, Pt2):
	#ComputeAffineMatrix 
	#   Computes the transformation matrix that transforms a point from
	#   coordinate frame 1 to coordinate frame 2
	#Input:
	#   Pt1: N * 2 matrix, each row is a point in image 1 
	#       (N must be at least 3)
	#   Pt2: N * 2 matrix, each row is the point in image 2 that 
	#       matches the same point in image 1 (N should be more than 3)
	#Output:
	#   H: 3 * 3 affine transformation matrix, 
	#       such that H*pt1(i,:) = pt2(i,:)
	
	N = len(Pt1)
	if N is not len(Pt2):
		error('Dimensions unmatched.')
	elif N < 3:
		error('At least 3 points are required.')
	
	# Convert the input points to homogeneous coordintes.
	P1 = np.append(np.transpose(Pt1), np.ones((1,N)), axis=0)
	P2 = np.append(np.transpose(Pt2), np.ones((1,N)), axis=0)

	# Now, we must solve for the unknown H that satisfies H*P1=P2
	# But MATLAB needs a system in the form Ax=b, and A\b solves for x.
	# In other words, the unknown matrix must be on the right.
	# But we can use the properties of matrix transpose to get something
	# in that form. Just take the transpose of both sides of our equation
	# above, to yield P1'*H'=P2'. Then MATLAB can solve for H', and we can
	# transpose the result to produce H.
	
	H = []
	################################################################################
	#                                                                              #
	#                                YOUR CODE HERE:                               #
	#        Use MATLAB's "A\b" syntax to solve for H_transpose as discussed       #
	#                     above, then convert it to the final H                    #
	#                                                                              #
	################################################################################
	H = np.linalg.lstsq(np.transpose(P1), np.transpose(P2))[0]
	H = np.transpose(H)

	# P1 = np.linalg.inv(P1)
	# H = P2 @ P1

	#######################################################################
	#       END OF YOUR CODE                                              #
	#######################################################################
	
	# Sometimes numerical issues cause least-squares to produce a bottom
	# row which is not exactly [0 0 1], which confuses some of the later
	# code. So we'll ensure the bottom row is exactly [0 0 1].
	H[2,:] = [0, 0, 1]

	return H
