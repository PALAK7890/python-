import random
x=random.randint(1,9)
chances=0
while chances < 5:
    guess=int(input('enter no between 1 and 9:'))
    if guess==x:
        print("congo u win")
        break
    elif guess<x:
        print("guess is low guess again")

    else:
        print("no is bigger than the no. try again")
    chances+=1
if not chances<5 :
    print("u lose")
    print(x)