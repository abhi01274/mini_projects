from tkinter import *
import requests



tk= Tk()

tk.geometry("450x460+370+50")
tk.config(bg="Beige")



l=Label(text="Enter the city name",width=38,height=2,font=('Times New Roman',10,'bold'))
l.place(x=90,y=20)
e= Entry(width=44)
e.place(x=92,y=70)

weather1= StringVar()
sunrise= StringVar()
wind= StringVar()
sunset= StringVar()
temperature = StringVar()


def cancel():
    tk.destroy()

def weather():
    global e
    url1 = "http://api.openweathermap.org/data/2.5/weather"
    url2 = "?q="+e.get()
    url3 = "&appid=d3658a2a2d9cbcdf70278122292c2152"
    url = url1 + url2 + url3
    response = requests.get(url)

    res1 = response.json()

    c= res1["weather"][0]["description"]
    d= res1["wind"]["speed"]
    e= res1["sys"]["sunrise"]
    f= res1["sys"]["sunset"]
    g=round(res1["main"]["temp"] -273)
    weather1.set(c)
    wind.set(d)
    sunrise.set(e)
    sunset.set(f)
    temperature.set(g)

    l1 = Label(text="Weather Condition :")
    l1.place(x=90, y=141)

    e1 = Entry(textvariable=weather1)
    e1.place(x=220, y=140)

    l2 = Label(text="Wind (in kmph) :")
    l2.place(x=90, y=180)

    e2 = Entry(textvariable=wind)
    e2.place(x=220, y=180)

    l3 = Label(text="Sunrise at :")
    l3.place(x=90, y=220)

    e3 = Entry(textvariable=sunrise)
    e3.place(x=220, y=220)

    l4 = Label(text="Sunset at :")
    l4.place(x=90, y=260)

    e4 = Entry(textvariable=sunset)
    e4.place(x=220, y=260)

    l5 = Label(text="Temperature :")
    l5.place(x=90, y=300)

    e5 = Entry(textvariable=temperature)
    e5.place(x=220, y=300)

    b.destroy()
    bz.destroy()

    ba = Button(text="Close", command=cancel, width=15)
    ba.place(x=230, y=350)



b=Button(text="Submit",command=weather,width= 15)
b.place(x=90,y=100)

bz=Button(text="Cancel",command=cancel,width= 15)
bz.place(x=250,y=100)


tk.mainloop()
