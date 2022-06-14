from tkinter import *
from tkinter import messagebox
import os


def save_info():
    name_info = name_field.get()
    email_info = email_field.get()
    gender_info = var.get()
    country_info = c.get()
    state_info = s.get()
    mobile_info = mobile_field.get()

    print(name_info,email_info,gender_info,country_info,state_info,mobile_info)

    file = open("user.txt","a")
    file.write("Your Name : "+ name_info)
    file.write("\n")
    file.write("Your Email : " + email_info)
    file.write("\n")
    file.write("Your Gender : " + str(gender_info))
    file.write("\n")
    file.write("Your Country : " + country_info)
    file.write("\n")
    file.write("Your State : " + state_info)
    file.write("\n")
    file.write("Your Mobile : " + mobile_info)
    file.write("\n\n")
    file.close()

def open_file():
    os.startfile("user.txt")


root = Tk()

root.config(bg='aqua')

root.geometry("550x600")

root.title("REGISTRATION PAGE")

label_1 = Label(root,text="-:REGISTRATION PAGE:-",font=("times",30,'bold'))
label_2 = Label(root,text="Name",bg="dark gray",font=("times",20,'bold'))
name_field = Entry(root,font=("times",20,'bold'))
name = StringVar()

label_3 = Label(root,text="Email",bg="dark gray",font=("times",20,'bold'))
email_field = Entry(root,font=("times",20,'bold'))

label_4 = Label(root,text="Gendar",bg="dark gray",font=("times",20,'bold'))
var = StringVar()
Radiobutton(root,text="Male",padx=20,variable=var,value='male',font=("times",16,'bold')).place(x=190,y=250)
Radiobutton(root,text="Female",padx=20,variable=var,value='female',font=("times",16,'bold')).place(x=320,y=250)

label_5 = Label(root,text="Country",bg="dark gray",font=("times",20,'bold'))
list_of_country = ['India','US','UK','Germany','Japan','Austria','Pakistan']
c = StringVar()
droplist = OptionMenu(root,c,*list_of_country)
droplist.config(width=20,font=("times",15,'bold'))
c.set('Select Your Country')

label_6 = Label(root,text="State",bg="dark gray",font=("times",20,'bold'))
list_of_state = ['Maharashtra','UP','MP','Bihar','Delhi','Kerala','Gujarat','Rajsthan','Assam','Haryana']
s = StringVar()
droplist2 = OptionMenu(root,s,*list_of_state)
droplist2.config(width=15,font=("times",15,'bold'))
s.set('Select Your State')

label_7 = Label(root,text="Mobile",bg="dark gray",font=("times",20,'bold'))
mobile_field = Entry(root,width=20,font=("times",20,'bold'))

submit = Button(root,text="Submit",command = save_info,fg="Black",bg="Red",font=("times",15,'bold'))

view = Button(root,text="View",command = open_file,fg="Black",bg="Red",font=("times",15,'bold'))


label_1.place(x=28,y=53)
label_2.place(x=80,y=130)
name_field.place(x=180,y=130)

label_3.place(x=80,y=190)
email_field.place(x=180,y=190)

label_4.place(x=80,y=250)

label_5.place(x=80,y=310)
droplist.place(x=220,y=310)

label_6.place(x=80,y=370)
droplist2.place(x=220,y=370)

label_7.place(x=80,y=420)
mobile_field.place(x=220,y=420)

submit.place(x=150,y=480)
view.place(x=280,y=480)
root.mainloop()