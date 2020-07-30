'''
Given an array of integers, find the sum of its elements.

Sample Input

6
1 2 3 4 10 11
Sample Output

31
'''

def simpleArraySum(ar):
    number = 0

    for num in ar:
        number += num
    
    return number

print(simpleArraySum([1,2,3,4,5,6]))