import random
import time

print('The TRAP Game!!!!')

feeling_brave = True

score = 0          # <-- HIDDEN BY GLARE, value assumed 0

while feeling_brave:          # <-- keyword hidden by glare, "while" fits the logic

    ghost_door = random.randint(1,3)


    print('3 doors ahead.....')
    '''
    ###########################################################
    # ASCII ART BLOCK - three doors with a hanging figure.
    # Too low-contrast in the photo to transcribe character by
    # character. This is a triple-quoted string sitting on its
    # own (not passed to print), same as in the original.
    ###########################################################
    '''

    time.sleep(2)

    print('2 of them will let you live and 1 will make you die.....')

    time.sleep(2)

    door_num = int(input('Please enter eiher door 1, door 2, or door 3!!: '))

    if door_num == ghost_door:
        print('You have been tormented by your brain and fell into a trap. You have died not peacefully! ')
        feeling_brave = False
    elif door_num != ghost_door and door_num >= 1 and door_num <= 3:
        print('You outsmarted the doors and barely madee it into the right door! But you will choose wrong next time!')
        score += 1
    else:
        print('This is an invalid door!')
    if score >= 10:
        Art = '''
        ###########################################################
        # LARGE ASCII ART BLOCK (a scene ending with "PN" signature)
        # Not legible enough in the photo to transcribe.
        ###########################################################
        '''

        print(Art)
