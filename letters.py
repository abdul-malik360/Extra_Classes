import random, string

list = []

while len(list)<5:
    letters = random.choice(string.ascii_uppercase)
    if letters not in list:
        list.append(letters)
print(list)
