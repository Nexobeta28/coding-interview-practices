# Arrays
array = [1, 2, 3 ,9]

#Input
final_number = int(input('Give a number: '))

for i in array:
    for j in array:
        if (i + j) == final_number:
            print(i, '+', j, '=', final_number)