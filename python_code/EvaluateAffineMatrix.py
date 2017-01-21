# -*- coding: utf-8 -*-
import numpy as np
import csv
from ComputeAffineMatrix import ComputeAffineMatrix


# EvaluateAffineMatrix.m
# Run this script to test your ComputeAffineMatrix() function
# using sample data. You do not need to change anything in this script.
	
## Test Data (You should not change the data here)
srcPt = np.array([[0.5, 0.1], [0.4, 0.2], [0.8, 0.2]])
dstPt = np.array([[0.3, -0.2], [-0.4, -0.9], [0.1, 0.1]])

## Calls your implementation of ComputeAffineMatrix.m
H = ComputeAffineMatrix(srcPt, dstPt)

## Load data and check solution
solution = np.genfromtxt('../checkpoint/Affine_ref.csv', delimiter=',')
error = (H-solution).sum()**2;
print('Difference from reference solution: {}'.format(error))

if error < 1e-20:
	print('Accepted!')
else:
	print('There is something wrong.')
