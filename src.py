import tkinter

def hangman():

    goodWord = input("Set word:")
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