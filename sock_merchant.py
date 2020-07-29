#!/bin/python3

'''
John works at a clothing store.
He has a large pile of socks that he must pair by color for sale.
Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

Complete the sockMerchant function in the editor below. It must return an integer representing the number of matching pairs of socks that are available.

n: the number of socks in the pile
ar: the colors of each sock

Sample Input
9
10 20 20 10 10 30 50 10 20

Sample Output
3
'''

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.


def sockMerchant(n, ar):
    possible_colors = []
    socks = []
    pairs_socks = []

    final = 0

    # Check for every color, append it to possible colors
    # Initialize socks and pairs_socks with 0
    for color in ar:
        if color in possible_colors:
            pass
        else:
            possible_colors.append(color)
            socks.append(0)
            pairs_socks.append(0)
    
    # Check the number of socks of each type
    for sock in ar:
        index = possible_colors.index(sock)
        socks[index] += 1

    # Calculate pairs for each element of socks
    for sock in socks:
        index = socks.index(sock)
        while socks[index] >= 2:
            socks[index] -= 2
            pairs_socks[index] += 1
    
    # Sum everything in final
    for sock in pairs_socks:
        final += sock  

    # Return the sum of socks
    return final

n = 9

ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

result = sockMerchant(n, ar)

print(result)
