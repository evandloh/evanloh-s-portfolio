import math
import time
import random

num_user = int(input('How many questions do you want?: '))

print('''

1. Addition
2. Subtraction
3. Mult
4. Division

''')

score = 0

for i in range(1,num_user + 1,1):

    selection = int(input('Please enter a item number: '))
    num1 = random.randint(1,100)
    num2 = random.randint(1,100)

    if selection == 1:
        print(num1, '+', 'x', '=',num2)
        solution = num2 - num1
        user_sol = int(input('Please enter your answer: '))

        while user_sol != solution:
            user_sol = int(input('please try again: '))
        print('You got it correct')
        score = score + 1

    elif selection == 2:

        print(num1,'-','y','=',num2)
        solution = (num2 - num1) * -1
        user_sol = int(input('Please enter your answer: '))

        while user_sol != solution:
            user_sol = int(input('Please try again: '))

        print('Good job!')

        score = score + 1


    elif selection == 3:

        print(num1,'*',num2, '=')
        solution = (num1 * num2)
        user_sol = int(input('Please enter your answer: '))

        while user_sol != solution:
            user_sol = int(input('Please try again: '))

        print('Good job!')
        score = score + 1

    elif selection == 4:

        print(num1,'/',num2,'=')
        solution = (num1 / num2)
        user_sol = int(input('Please enter your answer: '))

        while user_sol != solution:
            user_sol = int(input('Please try again: '))

        print('Good job!')
        score = score + 1

    else:
        print('Does not compute')

print('You scored ',score,'out of',num_user)
