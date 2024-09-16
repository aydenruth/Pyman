import tkinter as tk

window = tk.Tk()
window.title("Pyman")
window.geometry('900x600')

textbox = tk.Entry(master = window, text = "Enter your letter here!", width = 66, justify = "center")
pymanBox = tk.Canvas(master = window, width = 400, height = 500, background="green")
pymanBox.place(x = "0", y = "0")
textbox.place(x = "0", y = "500")
window.mainloop()


