from tkinter import *
from current_Temperature import *

def print_temp(city, country):
    t = get_temp(city, country)
    t = float(t.strip('°'))
    entry1.delete(0,END)
    entry1.insert(0, '%.2f°C' % ((t-32)*5/9))


root = Tk()
root.title('Weather data')

label1 = Label(root, text = 'Enter the city')
city = Entry(root, width = 25)
label2 = Label(root, text = "Enter the country's city")
country = Entry(root, width = 25)
label4 = Label(root, text = '')
label5 = Label(root, text = '')
label6 = Label(root, text = '')

label3 = Label(root, text = 'Temperature [°C]')
entry1 = Entry(root, width = 25)

temp_button = Button(root, text = 'Tell me the temperature', padx = 50, command = lambda:  print_temp(city.get(), country.get()))

label1.grid(row=0, column=0)
city.grid(row=0, column=1)
label2.grid(row=1,column=0)
country.grid(row=1,column=1)
label4.grid(row=2,column=0, columnspan=2)
temp_button.grid(row=3,column=0, columnspan=2)
label5.grid(row=4,column=0, columnspan=2)
label3.grid(row=5, column=0)
entry1.grid(row=5,column=1)
label6.grid(row=6,column=0, columnspan=2)

root.mainloop()
