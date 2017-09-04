#!/bin/python3

import sys
import heapq


        

n = int(input().strip())
a = []
a_i = 0
smaller = []
larger = []

for i in range(n):
    item = int(input().strip())
    if not larger or item >= larger[0]:
        heapq.heappush(larger, item)
    else:
        heapq.heappush(smaller, -item)
        
    size_diff = len(smaller) - len(larger)
    if size_diff == 2:
        transfer = -heapq.heappop(smaller)
        heapq.heappush(larger, transfer)
    if size_diff == -2:
        transfer = heapq.heappop(larger)
        heapq.heappush(smaller, -transfer)
        
    size_diff = len(smaller) - len(larger)
    if size_diff == 0:
        median = (larger[0] - smaller[0])/2
    elif size_diff == 1:
        median = -smaller[0]
    else:
        median = larger[0]
    print("%.1f" % median)
