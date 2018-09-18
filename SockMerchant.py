#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    mem = []
    count = 0
    for i in range(n):
        if ar[i] not in mem:
            count += ar.count(ar[i])//2
            print ("count: "+str(count))
            mem.append(ar[i])
            print ("mem: " + str(mem))
    return count
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)
    print result
    #fptr.write(str(result) + '\n')

    #fptr.close()
