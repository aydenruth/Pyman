import tkinter as tk
import random

randomChoices = ["Cat", "Bat", "Rat", "Thank", "Quark", "Interlinked", "Cells", "Within", "Gerard", "Meow", "Shoe", "Eels", "Persona", "Teeth", "Eyes"]
goodlen = 0
goodWord = ""
numLetters = "THREE"
letterBank = ["A", "B", "C", "D", "E", "F", "G"]

score = 0
random.seed()
goodWord = randomChoices[random.randint(0, 14)] 
print(goodWord)

goodlen = len(goodWord)
numLetters = "  _" * goodlen
print(numLetters)

def hangman():

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

#def formatLetters():

 #   for i in letterBank:
        #maybe an initial function to put letters into 2/3 lines, then a second one to replace any used ones



window = tk.Tk()
window.title("Pyman")
window.geometry('900x600')

#find a way to get hangman func in here & in proper scope
#usableLetters = [the whole alphabet]

textbox = tk.Entry(master = window, text = "Enter your letter here!", width = 66, justify = "center")
lengthBox = tk.Label( master = window, width = "50", height = "15", background = "purple", text = numLetters, justify = "center", font = ("Helvetica", "16"))
nuhUhBox = tk.Label(width = "100", height = "20", background = "blue", text =  )
pymanBox = tk.Canvas(master = window, width = 400, height = 500, background="green")

pymanBox.place(x = "0", y = "0")
lengthBox.place(x = "400")
nuhUhBox.place(x = "400", y = "250")
textbox.place(x = "0", y = "500")

hangman()
window.mainloop()


#number of dashes cant show up since the window pops up before the user inputs the word. 
#cut the user picking a word