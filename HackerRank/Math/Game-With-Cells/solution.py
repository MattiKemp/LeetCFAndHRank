#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gameWithCells' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def gameWithCells(n, m):
    return (n//2)*(m//2) + (m%2)*(n//2) + (n%2)*(m//2) + (n%2 and m%2)
    #total = (n//2)*(m//2) + (m%2)*(n//2) + (n%2)*(m//2)
    # corner base isn't supplied
    #if n%2 and m%2:
    #    return total + 1
    #return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = gameWithCells(n, m)

    fptr.write(str(result) + '\n')

    fptr.close()

