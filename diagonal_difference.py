'''
Given a square matrix,
calculate the absolute difference between the sums of its diagonals.

Sample Input
11 2  4
4  5  6
10 8 -12

Sample Output
15
'''

def diagonalDifference(arr):
    left_to_right = 0
    right_to_left = 0

    index_arr = []

    for n in range(len(arr[0])):
        left_to_right += arr[n][n]
        index_arr.append(n)

    reverse_index_arr = list(reversed(index_arr))

    for n in range(len(arr[0])):
        right_to_left += arr[index_arr[n]][reverse_index_arr[n]]
    
    return abs(left_to_right - right_to_left)

print(diagonalDifference([[11, 2, 4],
                          [4, 5, 6],
                          [10, 8, -12]]))
