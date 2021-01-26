from random import *

list = ['apple','banana','strawberry']
number = randint(0,len(list)- 1)
answer = list[number]
print(f"answer is : {answer}")

letters = ""

while True:
    print()
    succeed = True

    for w in answer:
        if w in letters:
            print(w , end = " ")
        else:
            print("_", end = " ")
            succeed = False
    print()
    if succeed:
        print("--Mission Complete--")
        break
    letter = input("Input letter > ")
    letters += letter


    if letter in answer:
        print("That's right")
    else:
        print("Wrong!")
