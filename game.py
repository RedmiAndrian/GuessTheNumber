import random

print("Howdy, fellas!")
print("What is your name? : ")
name = str(input())
print("Howdy " + name + "!")
print("This is 'Guess the number' game.")
print("You have to choose a random number within a range of 1 - 10.")
print("If you want to stop, simply just type '000'.")
print("Here it goes...")
x = random.randint(1, 10)
while True:
    answer = int(input("The nummber has been generated. What is the number that you'd guess? :  "))
    if answer != x:
        if answer == 000:
            print("Thanks for playing!")
            break
        else:
            print("Oops Wrong Answer! Its :")
            print(x)
            x = random.randint(1, 10)
    else:
        print("Correct! Good Spot!!")
        x = random.randint(1, 10)
