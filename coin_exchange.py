# 32 cents: 1 quarter (25), 1 nickel (5), 2 pennies (1)

def f_change(cents):
    possible_coins = {25: 0, 5: 0, 1: 0}

    while cents != 0:
        if(cents - 25 >= 0):
            possible_coins[25] += 1
            cents -= 25

        elif(cents - 5 >= 0):
            possible_coins[5] += 1
            cents -= 5

        else:
            possible_coins[1] += 1
            cents -= 1

    return possible_coins

cents = int(input('Enter your number: '))
change = f_change(cents)

print('Your change is', change[25], 'quarters,',
      change[5], 'nickels, and', change[1], 'pennies')
print('Total:',change[25]+change[5]+change[1],'coins.')
