from tkcalendar import Calendar
from tkinter import *
from tkinter.ttk import *
from tkinter import *
from PIL import ImageTk, Image
from typing import List
import requests


def calendar_1():
    global cal1
    def date_entry():
        sample_date.configure(state=NORMAL)
        sample_date.delete(0, 10)
        sample_date.insert(INSERT, cal1.selection_get())
        sample_date.configure(state=DISABLED)

        print(f'Outbound Date: {cal1.selection_get()}')

    top = Toplevel(screen)

    cal1 = Calendar(top, font="Arial 14", selectmode='day', locale='en_US', disabledforeground='red',cursor="hand1")
    cal1.pack(expand=True)

    Button(top, text="OK", command=date_entry).pack()


def calendar_2():
    global cal2
    def date_entry():

        sample_date1.configure(state=NORMAL)
        sample_date1.delete(0, 10)
        sample_date1.insert(INSERT, cal2.selection_get())
        sample_date1.configure(state=DISABLED)

        print(f'Inbound Date: {cal2.selection_get()}')

    top = Toplevel(screen)

    cal2 = Calendar(top, font="Arial 14", selectmode='day', locale='en_US', disabledforeground='red',cursor="hand1")
    cal2.pack(expand=True)

    Button(top, text="OK", command=date_entry).pack()


def all_data():
    print(f'Origin Airport: {origin_airport.get()}')
    print(f'Destination Airport: {destination_airport.get()}')
    print(f'Trip Type: {Lb1.get(Lb1.curselection())}')
    print(f'No. of Adults: {adults.get()}')
    print(f'No. of Children: {children.get()}')
    print(f'No. of Infants: {infants.get()}')
    print(f'Currency: {currency.get()}')
    print(f'Cabin Class: {cabin.get()}')

    url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/pricing/v1.0"

    payload = f'''inboundDate={cal2.selection_get()}&cabinClass={cabin.get()}&children={children.get()}
&infants={infants.get()}&country=US&currency=USD&locale=en-US&originPlace={origin_airport.get()}-sky
&destinationPlace={destination_airport.get()}-sky&outboundDate={cal1.selection_get()}&adults={adults.get()}'''

    print(payload)

    headers = {
        'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
        'x-rapidapi-key': "8b2a2325a8msh11c70d529c00c6fp173b43jsnda6329451837",
        'content-type': "application/x-www-form-urlencoded"
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)


screen = Tk()
screen.geometry("477x560")
screen.configure(bg='white smoke')

screen.title("Flight Search")

Label(text="", bg='white smoke').grid(row=0, column=0)
Label(text="FLIGHT SEARCH", bg='IndianRed1').grid(row=1, column=2)

Label(text="", bg='white smoke').grid(row=2, column=0)
Label(text="Origin Airport Code", fg='navy', bg='white smoke', anchor='w', width=25).grid(row=4, column=1)
origin_airport = Entry(screen)
origin_airport.grid(row=4, column=2)

Label(text="", bg='white smoke').grid(row=5, column=0)

Label(text="", bg='white smoke').grid(row=2, column=0)
Label(text="Destination Airport Code", fg='navy', bg='white smoke', anchor='w', width=25).grid(row=6, column=1)
destination_airport = Entry(screen)
destination_airport.grid(row=6, column=2)

Label(text="", bg='white smoke').grid(row=7, column=1)
Label(text="Trip Type", fg='navy', bg='white smoke', anchor='w', width=25).grid(row=8, column=1)

travel = ['One Way','Return']
lb1 = StringVar(screen)
lb1.set(travel)
Lb1 = Listbox(height=2,listvariable=lb1)
Lb1.grid(row=8, column=2)

Label(text="No. of Adults", fg='navy', bg='white smoke', anchor='w', width=25).grid(row=10, column=1)
adults = Scale(screen, from_=0, to=10, orient=HORIZONTAL, bg='white smoke', width=15, length=124, highlightthickness=0)
adults.grid(row=10, column=2)

Label(text="No. of Children", fg='navy', bg='white smoke', anchor='w', width=25).grid(row=12, column=1)
children = Scale(screen, from_=0, to=10, orient=HORIZONTAL, bg='white smoke', width=15, length=124, highlightthickness=0)
children.grid(row=12, column=2)

Label(text="No. of Infants", fg='navy', bg='white smoke', anchor='w', width=25).grid(row=14, column=1)
infants = Scale(screen, from_=0, to=10, orient=HORIZONTAL, bg='white smoke', width=15, length=124, highlightthickness=0)
infants.grid(row=14, column=2)

Label(text="Outbound Date", fg='navy', bg='white smoke', anchor='w', width=25).grid(row=17, column=1)

Label(text="", bg='white smoke').grid(row=16, column=3)

Button(screen, text='Calendar', command=calendar_1).grid(row=17, column=4)

sample_date = Entry(screen)
sample_date.grid(row=17, column=2)

Label(text="", bg='white smoke').grid(row=18, column=0)
Label(text="Inbound Date", fg='navy', bg='white smoke', anchor='w', width=25).grid(row=19, column=1)

Button(screen, text='Calendar', command=calendar_2).grid(row=19, column=4)

sample_date1 = Entry(screen)
sample_date1.grid(row=19, column=2)

Label(text="", bg='white smoke').grid(row=20, column=0)

Label(text="Currency", fg='navy', bg='white smoke', anchor='w', width=25).grid(row=21, column=1)
currency = Entry(screen)
currency.grid(row=21, column=2)

Label(text="", bg='white smoke').grid(row=22, column=0)

Label(text="Cabin Class", fg='navy', bg='white smoke', anchor='w', width=25).grid(row=23, column=1)

Options: List[str] = ['Choose Class', 'first', 'business', 'economy']
cabin = StringVar(screen)
cabin.set(Options[0])

OM1 = OptionMenu(screen, cabin, *Options)
OM1.configure(width=15, height=0, bd=-2, bg='white')
OM1.grid(row=23, column=2)

Label(text="", bg='whitesmoke').grid(row=24, column=1)
Button(text="Find Flights", command=all_data, bg='IndianRed1', width=55).grid(row=25, column=1, columnspan=4, sticky=NSEW)


def show_image():

    canvas = Canvas(screen, width=150, height=150, bg='whitesmoke', highlightthickness=0)
    canvas.grid(row=5, column=4, rowspan=6)

    img = Image.open("paper-plane.png")
    img = img.resize((150, 150), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    canvas.create_image(78, 150, anchor=S, image=img)
    screen.mainloop()


if __name__ == '__main__':
    show_image()


screen.mainloop()
