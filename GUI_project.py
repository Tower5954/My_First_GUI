from tkinter import *

window = Tk()
window.title('Miles to Km Converter')
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)


def button_clicked():
    new_input = int(miles_inputs.get()) * 1.6
    calculate_label.config(text=new_input)


# labels
my_label = Label(text="is equal to", font=('Ariel', 24))
my_label.grid(column=0, row=1)
my_label.config(padx=20, pady=20)

miles_label = Label(text="miles", font=('Ariel', 24) )
miles_label.grid(column=2, row=0)
miles_label.config(padx=20, pady=20)

calculate_label = Label(text="0", font=('Ariel', 24, 'bold'))
calculate_label.grid(column=1, row=1)
calculate_label.config(padx=20, pady=20)

km_label = Label(text="km", font=('Ariel', 24))
km_label.grid(column=2, row=1)
km_label.config(padx=20, pady=20)


# button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

# entry
miles_inputs = Entry(width=10)
miles_inputs.get()
miles_inputs.grid(column=1, row=0)



window.mainloop()