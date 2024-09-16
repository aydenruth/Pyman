import tkinter as tk

window = tk.Tk()
window.title("Pyman")
window.geometry('900x600')

textbox = tk.Entry(master = window, text = "Enter your letter here!", width = 66, justify = "center")
lengthBox = tk.Text(width = "100", height = "20", background = "purple")
nuhUhBox = tk.Text(width = "100", height = "20", background = "blue")
pymanBox = tk.Canvas(master = window, width = 400, height = 500, background="green")

pymanBox.place(x = "0", y = "0")
lengthBox.place(x = "400")
nuhUhBox.place(x = "400", y = "250")
textbox.place(x = "0", y = "500")
window.mainloop()


