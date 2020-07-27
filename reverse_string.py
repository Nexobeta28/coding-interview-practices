def reverse_1(x):
    arr = []

    for char in x:
        arr.insert(0, char)
    
    reversed = ''.join(arr)
    return reversed

def reverse_2(x):
    output_len = len(x)
    output = [None] * output_len
    output_index = output_len - 1

    for c in x:
        output[output_index] = c
        output_index -= 1
    
    return ''.join(output)

word = input('Enter your word: ')

print(reverse_1(word))