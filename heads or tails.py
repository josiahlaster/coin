import random

playing = True

while playing == False:
    PlayAgain = input("Do you want to play again?")
    if PlayAgain == "yes":
        playing = True


while playing == True:
    number = random.randint(1,2)
    guess = input("Heads or Tails ")

    if number == 1 and guess == ("heads" or "Heads"):
        print("You've landed on Heads!!")
        throw = input ("Do want to throw agian?")

    elif number == 2 and guess == ("tails" or "Tails"):
        print("You've landed on Tails!!")
        throw = input ("Do want to throw agian?")

    elif number == 1 and guess == ("tails" or "Tails"):
        print("To bad it landed on heads")
        throw = input ("Do want to throw agian?")
    
    elif number == 2 and guess == ("heads" or "Heads"):
        print("To bad it landed on tails")
        throw = input ("Do want to throw agian?")

    else:
        print("Bad input. Ty again!!")
        throw = input ("Do want to throw agian?")

    if throw == ("yes" or "Yes" or "Y" or "y"):
        playing = True
    elif throw == ("no" or "No" or "N" or "n"):
        playing = False



