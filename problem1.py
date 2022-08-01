#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    length = len(arr)
    positive = 0
    negative = 0
    zero = 0 
    for element in arr:
        if(element > 0):
            positive = positive + 1
        elif(element < 0):
            negative = negative + 1
        elif(element == 0):
            zero = zero+1  
    print("{0:.6f}".format(positive/length))
    print("{0:.6f}".format(negative/length))
    print("{0:.6f}".format(zero/length))
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
