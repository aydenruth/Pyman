import tkinter
import random

def hangman():

    randomChoices = ["Cat", "Bat", "Rat", "Thank", "Quark", "Interlinked", "Cells", "Within", "Gerard", "Meow", "Shoe", "Eels", "Persona", "Teeth", "Eyes"]
    score = 0

    goodWord = input("Set word, or type ""1player"" to play vs computer")
    if goodWord == "1player":
      random.seed()
      goodWord = randomChoices[random.randint(0, 14)]

    for i in goodWord:
        guess = input("Enter a Letter:")
        print(i)
        if guess == i:
            score += 1
        else:
            print("yeouch")


    if score == len(goodWord):
        print("You Win!")
    else:
        print("You Lose ;'(")
