# find_missing(
#   [4, 12, 9, 5, 6],
#   [4, 9, 12, 6]
# ) => 5


def find_missing(arr1, arr2):
    equals_array = []
    missing_array = []

    # Find equal numbers and create an array with it
    for a in arr1:
        for b in arr2:
            if a == b:
                equals_array.append(a)

    # Compare the numbers from the arr1 exists in equals_array
    for num in arr1:
        if num in equals_array:
            pass
        else:
            missing_array.append(num)
    
    # Compare the numbers from the arr2 exists in equals_array
    for num in arr2:
        if num in equals_array:
            pass
        else:
            missing_array.append(num)
    
    # Return missing_array with the missing numbers
    return missing_array


print(find_missing([4, 12, 9, 5, 6], [4, 9, 12, 6]))
