#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
# The function accepts INTEGER_ARRAY arr as parameter.
# Print out the ratio of positive, negative, and 0 numbers in the array
# Print up to 6 decimal places

def plusMinus(arr):
    # Write your code here
    
    positive = 0
    negative = 0
    zero = 0
    total = len(arr)
    
    for i in arr:
        if i > 0:
            positive += 1
        elif i < 0:
            negative += 1
        else:
            zero += 1
            
    print('%.6f' % (positive/total))
    print('%.6f' % (negative/total))
    print('%.6f' % (zero/total))
            

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
