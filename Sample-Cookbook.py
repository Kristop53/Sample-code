import tkinter as tk
import os
import tkinter.ttk as ttk
from tkinter import scrolledtext

operation = [
    "Desserts",
    "Preservatives",
    "Dinners"
]

# Getting size of each directory for files
i, j, k=0, 0, 0
deslen, preslen, dinlen = 0, 0, 0
user = os.getlogin()
for x in os.listdir("C:\\Users\\"+user+"\\desktop\\Recipies\\Desserts\\"):
    deslen += 1
for x in os.listdir("C:\\Users\\"+user+"\\desktop\\Recipies\\Preservatives\\"):
    preslen += 1
for x in os.listdir("C:\\Users\\"+user+"\\desktop\\Recipies\\Dinners\\"):
    dinlen +=1

# Prepare arrays for files
Desserts = [None] * deslen
Preservatives = [None]*preslen
Dinners = [None]*dinlen

#Fill all arrays with files
for root, dirs, files in os.walk("C:\\Users\\"+user+"\\desktop\\Recipies\\Desserts\\"):
        for file in files:
            Desserts[i] = (os.path.join(file)) 
            i+=1

for root, dirs, files in os.walk("C:\\Users\\"+user+"\\desktop\\Recipies\\Preservatives"):
        for file in files:
            Preservatives[j] = os.path.join(file)
            j+=1
for root, dirs, files in os.walk("C:\\Users\\"+user+"\\desktop\\Recipies\\Dinners"):
        for file in files:
            Dinners[k] = os.path.join(file)
            k+=1

# Write all options depending on first selection
def Scroll_For_Options(thing):
    if first_combo.get() == "Desserts":
        second_combo.config(values=Desserts)
        second_combo.current(0)

    elif first_combo.get() == "Preservatives":
        second_combo.config(value=Preservatives)
        second_combo.current(0)

    elif first_combo.get() == "Dinners":
        second_combo.config(value= Dinners)
        second_combo.current(0)

# Open file and write in the result_label
def Writing():
    text.delete('1.0', tk.END)
    with open("C:\\Users\\"+user+"\\desktop\\Recipies\\"+first_combo.get()+"\\"+second_combo.get(), "r", encoding='utf-8') as wynik:
        stuff = wynik.read()
        text.insert(tk.END, stuff)
        wynik.close()

root = tk.Tk()
root.title("Cookbook")
root.state('zoomed')

# Get user screen width
width= root.winfo_screenwidth()
height= root.winfo_screenheight()

# Background
frame = tk.Frame(root, bg="light blue")
frame.place(relwidth=1, relheight=1)

root.geometry("%dx%d" % (width, height))

# First Dropdown
first_combo=ttk.Combobox(root, values=operation, width=40)
first_combo.current(0)
first_combo.pack()
first_combo.bind("<<ComboboxSelected>>", Scroll_For_Options)

# For the second Dropdown to show values based on the first Dropdown
second_combo=ttk.Combobox(root, values=[" "], width=40)
second_combo.current(0)
second_combo.pack(pady=20)

# Text field in which program will write with a scrollbar
text = scrolledtext.ScrolledText(root, undo=True)
text['font'] = ('Helvetica', 18)
text.pack(expand=True, fill='both')

# Button on the bottom of the screen to open selected files
opener = tk.Button(root, text="Open", command=Writing)
opener.pack(pady=0)

root.mainloop()