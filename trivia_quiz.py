import time
score = 0


def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0


    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print('You got it!')
            still_guessing = False
            score += 10

        else:
            if attempt < 2:
                guess = input('Please try again! ')

        attempt = attempt + 1

    if attempt == 3:
        print('The answer was.....', answer)


guess1 = input('Where do Polar Bears Vote?\n \
A) California \n B) China \n C) South Hemisphere \n D) North Pole \n Type A, B, C, or D: ')

check_guess(guess1,'d')
time.sleep(3)
guess1 = input('What is the only fish that swims at night?\n \
A) Salmon \n B) Starfish \n C) Angler fish \n D) Shark \n Type A, B, C, or D: ')

check_guess(guess1,'b')
time.sleep(3)
guess1 = input('What do yu get when a chicken lays an eggon top of a barn?\n \
A) Fried Chicken \n B) Nothing \n C) Eggrol \n D) Peanut butter \n Type A, B, C, or D: ')

check_guess(guess1,'c')
time.sleep(3)
guess1 = input('Why did the chicken not cross the road?: ')

check_guess(guess1,'because there was a KFC on the other side')
time.sleep(3)
guess1 = input('What animals are on legal documents?\n \
A) Starfish \n B) Lions \n C) Seal \n D) Polar Bear \n Type A, B, C, or D: ')


check_guess(guess1,'c')

time.sleep(3)

print('This one is fun!')

guess1 = input('What do you get when you cross a snake with pie?: ')

check_guess(guess1,'A pie-thon')

print('you scored',score, 'points')
