from tkinter import *

window = Tk()
window.title('My first GUI')
window.minsize(width=500, height=300)


def button_clicked():
    new_input = inputs.get()
    my_label.config(text=new_input)


# label
my_label = Label(text="I am a label", font=('Ariel', 24, 'bold'))


# change the text in the label
my_label["text"] = "new text"
# or
my_label.config(text="new text 2")
my_label.grid(column=0, row=0)

# create a button
button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

# entry
inputs = Entry(width=10)
inputs.get()
inputs.grid(column=3, row=2)

new_button = Button(text="Click me as well")
new_button.grid(column=2, row=0)

window.mainloop()
