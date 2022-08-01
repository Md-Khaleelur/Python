#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    # Write your code here
    res=''
    stringInput = str("{:032b}".format(int(n)))
    # print(n,'n')
    length = len(stringInput)
    # print('length',length)
    answer = 0
    for i in range(0,length):
        if(stringInput[i]=='0'):
            res+='1'
            # print(res,'i',i)
        elif(stringInput[i]=='1'):
            res+='0'            
    # print(len(res),'res')
    for i in range(0,length):
        # print(int(res[length-1-i])*math.pow(2,i),'test')
        answer+= int(int(res[length-1-i])*math.pow(2,i))
    # print(answer)
    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
