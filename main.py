import random

location = [4, 5, 6]
weight = [314, 218, 181]

def check_weight():
    global weight
    global location

    if sum(weight) == 713:
        print('Cargo is found')
    else:
        print("Cargo does not have neccessary weight")
        location = random.sample(range(8), 3)
        finder()

def finder():
    a = int(input('Enter the first position of the box (km): '))
    b = int(input('Enter the second position of the box (km): '))
    c = int(input('Enter the third position of the box (km): '))

    global location
    if [a,b,c] != location:
        print('Cargo is not found')
        location = random.sample(range(8), 3)
        finder()
    else:
        check_weight():

finder()
