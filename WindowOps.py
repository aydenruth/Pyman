import tkinter as tk
import random

randomChoices = ["Cat", "Bat", "Rat", "Thank", "Quark", "Interlinked", "Cells", "Within", "Gerard", "Meow", "Shoe", "Eels", "Persona", "Teeth", "Eyes"]
score = 0
goodlen = 0
goodWord = ""

def hangman():

    goodWord = input("Set word, or type ""1player"" to play vs computer")
    if goodWord == "1player":
      random.seed()
      goodWord = randomChoices[random.randint(0, 14)] 

    goodlen = len(goodWord)

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


window = tk.Tk()
window.title("Pyman")
window.geometry('900x600')

#find a way to get hangman func in here & in proper scope
lentext = tk.StringVar()
lentext.set( " _" * goodlen)
print(lentext)

#usableLetters = [the whole alphabet]

textbox = tk.Entry(master = window, text = "Enter your letter here!", width = 66, justify = "center")
lengthBox = tk.Label(width = "100", height = "20", background = "purple", textvariable = lentext)
nuhUhBox = tk.Text(width = "100", height = "20", background = "blue")
pymanBox = tk.Canvas(master = window, width = 400, height = 500, background="green")

pymanBox.place(x = "0", y = "0")
lengthBox.place(x = "400")
nuhUhBox.place(x = "400", y = "250")
textbox.place(x = "0", y = "500")

hangman()
window.mainloop()


