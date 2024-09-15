import tkinter

def hangman():

    goodWord = input("Set word:")
    print(goodWord)
    score = len(goodWord)

    for i in goodWord:
        guess = input("Enter a Letter:")
        if guess == goodWord[i]:
            score += 1
        else:
            print("yeouch")

    if score == len(goodWord):
        print("You Win!")