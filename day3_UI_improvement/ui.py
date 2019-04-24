#importing all classes from tkinter
import tkinter as tk
from tkinter import filedialog


def _from_rgb(rgb):
    #translates an rgb tuple of int to a tkinter friendly color code
    return "#%02x%02x%02x" % rgb

def getpath():
	filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
	print(filename)
	e1.insert("insert", filename)

filename = ""
root = tk.Tk()
root.title("Freeman")
root.geometry("900x400") #You want the size of the app to be 500x500
root.resizable(0, 0)
# root.configure(background="lightblue")

#For the Name of the Encrypter.
headframe  = tk.Frame(root,width=300, height=50, colormap="new")
head = tk.Label(headframe, text="`whit3 H0r5e",fg = "black") #box2
head.config(font=("Courier", 44))
head.grid(row=0,column=0)
headframe.pack()

spaceframe1 = tk.Frame(root,width=400, height=50, colormap="new")
spaceframe1.pack()


#For the password and path of the file
topframe  = tk.Frame(root)
topframe.pack()

browsebutton = tk.Button(topframe, text = "Browse", fg = "blue", command= getpath)
browsebutton.config(height = 2, width = 10,font=('Courier', 20))
browsebutton.grid(row=0,column=0)


passwrd = tk.Label(topframe, text="Password",fg = "blue") #box2
passwrd.config(height = 2, width = 10,font=('Courier', 20))
passwrd.grid(row=1,column=0)

#path entry
e1 = tk.Entry(topframe)
e1.config(width = 50,bd =5,font=('Courier', 20))
e1.grid(row=0, column=1)

#password entry
e2 = tk.Entry(topframe)
e2.config(width = 50,bd =5,show ="*",font=('Courier', 20))
e2.grid(row=1, column=1)


#for dialog sucessfull or failure
spaceframe2 = tk.Frame(root,width=400, height=40, colormap="new")
spaceframe2.pack()

#-----------------------------------------------------------------------
#For the encryption and decryption 
bottomframe = tk.Frame(root)
bottomframe.pack()

button_encrypter = tk.Button(bottomframe,text = "Encrypt", fg = "red")
button_encrypter.pack(side = "left", padx =50)
button_encrypter.config(height = 3, width = 10,font=('Courier', 20))

button_decrypter = tk.Button(bottomframe,text = "Decrypt", fg = "green")
button_decrypter.pack(side = "left", padx=50)
button_decrypter.config(height = 3, width = 10,font=('Courier', 20))


if __name__ == '__main__':
	root.mainloop()
#the above lines create the main window box but it closes within in splir second
#to keep it forever we add infinate loop