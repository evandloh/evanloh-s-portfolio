import random
score = 0
Welcome = input('Welcome user. Please enter either addition, subtraction, circumfrence, division, or multiplacation: ').lower().strip()

if Welcome == 'addition':
    for i in range(1,11):
        num1 = random.randint(1,1000)
        num2 = random.randint(1,1000)
        correct = num1 - num2
        print(num1, '+', num2,'= ')
        answer = int(input('Your answer is: '))
        print()
        if answer == correct:
            score += 1
        print('Your score is',score, 'out of 10')

elif Welcome == 'subtraction':
    for i in range(1,11):
        num1 = random.randint(25,50)
        num2 = random.randint(1,25)
        correct = num1 - num2
        print(num1, '-', num2,'= ')
        answer = int(input('Your answer is: '))
        print()
        if answer == correct:
            score += 1
        print('Your score is',score, 'out of 10')

elif Welcome == 'division':
    for i in range(1,11):
        num1 = random.randint(100,200)
        num2 = random.randint(1,10)
        correct = num1 / num2
        print(num1, '/', num2,'= ')
        answer = int(input('Your answer is: '))
        print()
        if answer == correct:
            score += 1
        print('Your score is',score, 'out of 10')

elif Welcome == 'multiplacation':
    for i in range(1,11):
        num1 = random.randint(1,100)
        num2 = random.randint(1,100)
        correct = num1 * num2
        print(num1, '*', num2,'= ')
        answer = int(input('Your answer is: '))
        print()
        if answer == correct:
            score += 1
        print('Your score is
        ',score, 'out of 10')

elif Welcome == 'Square':
    print('Please find the area of the square. Side length =' ,num1)
    solution = num1 ** 2

    while user_sol != solution:
        user_sol = eval(input('Please try again!: '))
    time.sleep(1)
    print('Correcto!')
    score = score + 1

elif Welcome == 'Triangle':
    print('Please find the area of a triangle. Base = ',num1,'Height =    # <-- LINE CUT OFF BY SCREEN EDGE IN PHOTO

else:
    print('Not a answer')
