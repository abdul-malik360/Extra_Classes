import random
from playsound import playsound

mylist = []

for x in range(1, 4):
    number = random.randint(1, 60)
    mylist.append(number)
    print(mylist)
    if x == 3:
        playsound("granted.mp3")