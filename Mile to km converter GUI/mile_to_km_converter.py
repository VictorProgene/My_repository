from tkinter import *


def button_clicked():
    print("Calculated!")
    miles = input_miles.get()
    result = float(miles) * 1.6093
    reductio = round(result, 2)
    my_label_result.config(text=reductio)


window = Tk()
window.title("Miles to Km converter")
window.minsize(width=10, height=5) #Config the window size
window.config(padx=10, pady=10) #Defines the distance from the walls

#Entry
input_miles = Entry(width=10)
print(input_miles.get())
input_miles.grid(column=1, row=0)

#Label
my_label_result = Label(text="0", font=("Arial", 12, "bold"))
my_label_result.grid(column=1, row=1)

#Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

#Label
my_label_equal = Label(text="is equal to", font=("Arial", 12, "bold"))
my_label_equal.grid(column=0, row=1)

#Label
my_label_miles = Label(text="Miles", font=("Arial", 12, "bold"))
my_label_miles.grid(column=2, row=0)

#Label
my_label_km = Label(text="Km", font=("Arial", 12, "bold"))
my_label_km.grid(column=2, row=1)











window.mainloop()