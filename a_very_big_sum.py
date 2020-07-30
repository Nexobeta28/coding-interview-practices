'''
In this challenge, you are required to calculate and print the sum of the elements in an array,
keeping in mind that some of those integers may be quite large.

Sample Input

5
1000000001 1000000002 1000000003 1000000004 1000000005
Output

5000000015
'''

def aVeryBigSum(ar):
    number = 0
    for n in ar:
        number += n
    
    return number


print(aVeryBigSum([1000000001, 1000000002, 1000000003, 1000000004, 1000000005]))

