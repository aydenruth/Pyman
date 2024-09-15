import tkinter
import random

def hangman():

    goodWord = input("Set word, or type ""1player"" to play vs computer")
    if goodWord == "1player":
      goodWord = []

    
    print(goodWord)
    score = 0

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

hangman()