import random

location = [4, 5, 6]
weight = [314, 218, 181]

a = int(input('Enter the first position of the box (km): '))
b = int(input('Enter the second position of the box (km): '))
c = int(input('Enter the third position of the box (km): '))

def finder(a,b,c):
    global location
    global weight
    if [a,b,c] != location:
        print('Cargo is not found')
        location = random.sample(range(8), 3)
        a = int(input('Enter the first position of the box (km): '))
        b = int(input('Enter the second position of the box (km): '))
        c = int(input('Enter the third position of the box (km): '))
        finder(a,b,c)
    else:
        if sum(weight) == 713:
            print('Cargo is found')
        else:
            print("Cargo does not have neccessary weight")
            location = random.sample(range(8), 3)
            a = int(input('Enter the first position of the box (km): '))
            b = int(input('Enter the second position of the box (km): '))
            c = int(input('Enter the third position of the box (km): '))
            finder(a,b,c)

finder(a,b,c)
