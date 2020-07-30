'''
Given an array of integers, calculate the ratios of its elements that are positive,
negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.

0.400000
0.400000
0.200000

Sample Input
-4 3 -9 0 4 1    

Sample Output
0.500000
0.333333
0.166667
'''


def plusMinus(arr):
    negative_count = 0
    zero_count = 0
    positive_count = 0

    n_numbers = len(arr)

    for n in arr:
        if n < 0:
            negative_count += 1
        elif n == 0:
            zero_count += 1
        else:
            positive_count += 1


    print(round(positive_count / n_numbers, 6))
    print(round(negative_count / n_numbers, 6))
    print(round(zero_count / n_numbers, 6))

plusMinus([-4, 3, -9, 0, 4, 1])
