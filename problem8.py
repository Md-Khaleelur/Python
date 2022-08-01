#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    # Write your code here
    # count = {}
    # ans = []
    # for item in arr:
    #     count[item] = arr.count(item) 
        
    # for i in range(0,100):
    #     if(i not in count.keys()):
    #         count[i] = 0
        
    # for key in count:
    #     ans.append(count[key])
    
    # return ans
    output = [0] * 100
    
    for el in arr:
        output[el] += 1
        
    return output

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
