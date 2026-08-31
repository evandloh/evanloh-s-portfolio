import random
import time

print('''
    88                                        88
    ""                                        88
                                              88
    88 88        88 8b,dPPYba,   ,adPPYb,d8 88  ,adPPYba,
    88 88        88 88P'   `"8a a8"  `Y88 88 a8P_____88
    88 88        88 88     88 8b       88 88 8PP"""""""
    88 "8a,  ,a88 88      88 "8a,   ,d88 88 "8b,   ,aa
    88  `"YbbdP'Y8 88      88  `"YbbdP"Y8 88  `"Ybbd8"'
   ,88                          aa,   ,88
 888P"                           "Y8bbdP"
''')
# ^ banner art traced as best I could from the photo -- spacing is approximate

userName = input('[Welcome to the Jungle! Please enter your name!]')

print('''
###########################################################
# LARGE ASCII ART BLOCK (jungle scene, signed "_AsH")
# Far too dense and low-contrast in the photo to transcribe.
###########################################################
''')

print('Welcome', userName,'to the Jungle game!')

print('Reach a total score of 400 to win!')

time.sleep(2)

score = 0

Start = input('Would you like to venture off into the Jungle?:').lower().strip()

while Start == 'yes':

    print('You see a small door behind some trees')

    print('''
    ###########################################################
    # ASCII ART BLOCK (a door, ends with the line |mt-2_;----.___|)
    ###########################################################
    ''')

    time.sleep(2)

    answer = input('There is a lever there to open the door, and you see a dark room. Would you like to enter?: [yes or no]').lower().strip()

    if answer == 'yes':

        print('You go through the door and enter level 2!')

        time.sleep(3)

        print('When you open your eyes you see a monkey running past the trees')

        print('''
 w   c(..)o    (
  \__(-)    __)
      /\   (
     /(_)___)
     w /|
      | \
       m  m
''')

        time.sleep(2)

        score = score + 100

        answer1 = input('You happen to catch a glimpse of a gold bar in the monkeys arm, Would you like to follow the monkey?: [yes or no]').lower().strip()

        if answer1 == 'yes':

            print('you decide to follow the monkey')

            print('only to realize that there is a pack of monkeys surrounding you')

            print('You have been caught and the monkeys enjoy a delicious player soup',': Your score was ',score)
        else:
            print('You decide that the monkeys might play a trap on you and decide not to follow')

            time.sleep(3)

            print('You think you have chosen the right path but 2 days later you are dying of starvation')

            score = score + 100

            answer4 = input('You see 2 villages, one named the Haunted Village and the other named the Village of Riches! [Please enter riches: ').lower().strip()
            print('''
    ###########################################################
    # ASCII ART BLOCK (two villages, includes |_|HHHHHHHH| )
    ###########################################################
''')

            if answer4 == 'haunted village':

                print('You decide to go into the house....')

                time.sleep(5)

                print('You see artifacts on the shelves....')

                time.sleep(2)

                print('You see a weird guy sitting on the throne in the middle of the house..')

                time.sleep(2)

                print('He says he is the leader of the village and says he killed everyone who entered the village....')

                Yes = input('He says i will fight you. Do you accept?: [yes or no]').lower().strip()


                if Yes == 'yes':
                    print('You see a sword on the side of the wall and take it')

                    print('''
::::::::::::::::::::::::::::/
''')

                    time.sleep(2)

                    print('The leader lunges at you!')

                    print('You two clash!')

                    attack = input('Would you like to use upper cut or back slash?: [enter upper cut or back slash]').lower().strip()

                    time.sleep(4)

                    if attack == 'upper cut':

                        print('You have defeated the leader and won the game! Great Job!')

                        score = score + 200

                        print('Your final score is ',score)

                    else:
                        print('You choose the wrong move and get killed. You lose!','Your final score was ',score)
                else:

                    print('You have been eliminated',':Your score was ',score)

            elif answer4 == 'village of riches':

                print('You walk to the town only to find greedy people ready to beat you down')

                print('You have been eliminated ',' Your final score was ',score)
            else:
                print('Not Valid')


else:
    print('it appears nothing happened','Your score was ',score)
Start = input(' would you like to restart your adventure?:').lower().strip()
if Start == 'yes':
    print('somethhing iss happening, game  oveor!!.')
    print('''
    ###########################################################
    # ASCII ART BLOCK (rows of stick figures)
    ###########################################################
''')
