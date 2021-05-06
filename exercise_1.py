from tkinter import *


# Creating a blank window
root = Tk()
# Geometry changes window size
root.geometry("450x200")
# Creating a title for the program
root.title("Adding Two Numbers")

# Creating label 1
lbl1 = Label(root, text="Please enter first number: ")
# Positioning lable 1
lbl1.grid(column=1, row=1)
# Creating an entry point for the user to input a number
txtentry1 = Entry(root)
# Positioning the 1st entry point
txtentry1.grid(column=2, row=1)
# Creating label 2
lbl2 = Label(root, text="Please enter second number: ")
# Positioning label 2
lbl2.grid(column=1, row=2)
# Creating another entry point for the user to input a number
txtentry2 = Entry(root)
# Positioning the 2nd entry point
txtentry2.grid(column=2, row=2)
# Creating label 3
lbl3 = Label(root, text="Your answer: ")
# Positioning label 3
lbl3.grid(column=1, row=3)
# Creating a ready-only entry point for the answer
entry = Entry(root, bg="white", state="readonly")
# Positioning the read-only entry point
entry.grid(column=2, row=3)

# Creating a function to add two numbers put in by the user
def add_2_numbers():
    total = sum(int(i.get()) for i in (txtentry1, txtentry2))
    # Converting the entry to 'normal' in order for the answer to appear
    entry.config(state="normal")
    entry.insert(0, total)
    # Converting the answer back to read only so the user cannot add anything to the answer
    entry.config(state="readonly")


# This function make the Clear button operational
def delete():
    txtentry1.delete(0, 'end')
    txtentry2.delete(0, 'end')
    entry.config(state="normal")
    entry.delete(0, END)
    # Converting the answer back to read only
    entry.config(state="readonly")


# Creating a button to add the numbers
btnAdd = Button(root, text="Add", command=add_2_numbers)
# Positioning the Add button
btnAdd.grid(column=1, row=4)
# Creating a button to clear the numbers
btnClear = Button(root, text="Clear", command=delete)
# Positioning the Clear button
btnClear.grid(column=2, row=4)
# Creating a button to exit the program
btnExit = Button(root, text="Exit", command="exit")
# Positioning the Clear button
btnExit.grid(column=3, row=4)

root.mainloop()
