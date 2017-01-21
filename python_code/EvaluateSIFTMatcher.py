# -*- coding: utf-8 -*-
import numpy as np
import csv
from SIFTSimpleMatcher import SIFTSimpleMatcher


## Test Data (You should not change the data here)
input_d1 = np.genfromtxt('../checkpoint/Match_input1.csv', delimiter=',')
input_d2 = np.genfromtxt('../checkpoint/Match_input2.csv', delimiter=',')

## Call my implementation of SIFTSimpleMatcher.m
M = SIFTSimpleMatcher(input_d1, input_d2);

## Load data and check solution (You should not change this part.)
solution = np.genfromtxt('../checkpoint/Match_ref.csv', delimiter=',')
print('Your error with the reference solution...')
print((M-solution).sum()**2)

if ((M-solution).sum()**2) < 1e-30:
	print('Accepted!')
else:
	print('There is something wrong.')

