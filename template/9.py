import sys, os, getpass
import heapq as hq
import math, random, functools, itertools
from collections import Counter, defaultdict, deque
input = sys.stdin.readline

# available on Google, AtCoder Python3
# not available on Codeforces
# import numpy as np
# import scipy

# if testing locally, print to terminal with a different color
OFFLINE_TEST = getpass.getuser() == "hkmac"
def log(*args):  
    if OFFLINE_TEST:
        print('\033[36m', *args, '\033[0m', file=sys.stderr)


def solve_1_(arr):

    brr = arr[:25]

    for a in arr[25:]:
        hold = False
        for x in brr[-25:]:
            for y in brr[-25:]:
                if a == x+y:
                    hold = True
        if not hold:

            crr = brr
            log(crr, a)
            for i in range(len(brr)):
                for j in range(i+1,len(brr)):
                    if sum(crr[i:j]) == a:
                        # log(crr[i:j])
                        # log(max(1930044+3461752)
                        return max(crr[i:j]) + min(crr[i:j])
        brr.append(a)

        
    return -1


def solve_1(*args):
    # screen input
    if OFFLINE_TEST:
        log("----- solving ------")
        log(*args)
        log("----- ------- ------")
    return solve_1_(*args)


overall_res = 0

def read_matrix(rows):
    return [list(map(int,input().split())) for _ in range(rows)]

def read_strings(rows):
    return [input().strip() for _ in range(rows)]

entries = []

# while True:
# for case_num in [1]:  # no loop over test case
for case_num in range(1000):

    # read line as a string
    # strr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()

    # read line as an integer
    entries.append(int(input()))
    
    # read one line and parse each word as an integer
    # lst = list(map(int,input().split()))

    # read multiple rows
    # mrr = read_matrix(k)
    # arr = read_strings(k)
    
    # strr = input().strip()
    # if strr == "EXIT":
    #     break
    # # if strr == "":
    # entries.append(strr)

overall_res = solve_1(entries)

print(overall_res)