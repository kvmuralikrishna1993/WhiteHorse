#importing all classes from tkinter
import tkinter as tk
from tkinter import filedialog

def getpath():
	filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
	print(filename)
	e1.insert("insert", filename)

filename = ""
root = tk.Tk()
root.title("WorkHorse")

topframe  = tk.Frame(root)
topframe.pack()

browsebutton = tk.Button(topframe, text = "Browse", fg = "black", command= getpath).grid(row=0)
tk.Label(topframe, text="Password").grid(row=1) #box2

e1 = tk.Entry(topframe)
e2 = tk.Entry(topframe)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

bottomframe = tk.Frame(root)
bottomframe.pack()

buttonencrypter = tk.Button(bottomframe,text = "Encrypt", fg = "red")
buttondecrypter = tk.Button(bottomframe,text = "Decrypt", fg = "green")
buttonencrypter.pack(side = "left", padx = 10, pady=10)
buttondecrypter.pack(side = "left", padx=10, pady=10)


if __name__ == '__main__':
	root.mainloop()
#the above lines create the main window box but it closes within in splir second
#to keep it forever we add infinate loop