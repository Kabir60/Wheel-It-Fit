
from cProfile import label
from tkinter import *
def calculate_fitment():
    fitment.delete('1.0',END)
    issues.delete('1.0',END)

    old_width = old_tire_width.get()
    old_size = old_tire_size.get()
    old_ratio = old_tire_ratio.get()

    old_height = float (old_width * (old_ratio/100))
    old_diameter = float (old_size +(2*(old_height/(2.54*10))))

    new_width = new_tire_width.get()
    new_size = new_tire_size.get()
    new_ratio = new_tire_ratio.get()
    new_height = float (new_width * (new_ratio/100))
    new_diameter= float (new_size +(2*(new_height/(2.54*10))))

    if (new_diameter - old_diameter < 2):
        fitment.insert(END,"Yes :)")
    else:
        fitment.insert(END,"No :(")

    if(new_diameter - old_diameter > 1.5):
        issues.insert(END,"Rubbing")
    else:
        issues.insert(END,"Should be all ok ")
    return new_diameter,old_diameter

def speedo_error_amount():
    speedo.delete('1.0',END)
    new_diameter,old_diameter = calculate_fitment()
    error = new_diameter/old_diameter
    speedo.insert(END,"{:0.2f}%".format(error))

    return error


# allows creating the window object 
app = Tk()
#back ground 

bg = PhotoImage(file = "images/5547560.png")
photo = Label(app,image=bg)
photo.place(x=0,y=0,relheight=1,relwidth=1)

# old tire 
old_tire_width = IntVar()
old_tire_ratio = IntVar()
old_tire_size = IntVar()
old_tire_label = Label(app, text ='Old Tire', font = ('bold',20),bg= '#447cc4')
old_tire_label_width = Label(app, text ='Width', font = ('bold',12),padx=20,bg= '#447cc4')
old_tire_label_ratio = Label(app, text ='Ratio', font = ('bold',12),padx=20,bg= '#447cc4')
old_tire_label_size = Label(app, text ='Rim Size', font = ('bold',12),padx=20,bg= '#447cc4')
old_tire_label.grid(row = 1, column = 0, sticky= W)
old_tire_label_width.grid(row = 0, column = 1, sticky= W)
old_tire_label_ratio.grid(row = 0, column = 2, sticky= W)
old_tire_label_size.grid(row = 0, column = 3, sticky= W)
old_tire_entry1 = Entry(app, textvariable = old_tire_width,bg= '#447cc4')
old_tire_entry1.grid(row = 1, column= 1,padx=20)
old_tire_entry2 = Entry(app, textvariable = old_tire_ratio,bg= '#447cc4')
old_tire_entry2.grid(row = 1, column= 2, padx= 20)
old_tire_entry3 = Entry(app, textvariable = old_tire_size,bg= '#447cc4')
old_tire_entry3.grid(row = 1, column= 3, padx=20)

# new tire 
new_tire_width = IntVar()
new_tire_ratio = IntVar()
new_tire_size =  IntVar()
new_tire_label = Label(app, text ='New Tire', font = ('bold',20),bg= '#447cc4')
new_tire_label_width = Label(app, text ='Width', font = ('bold',12),padx=20,bg= '#447cc4')
new_tire_label_ratio = Label(app, text ='Ratio', font = ('bold',12),padx=20,bg= '#447cc4')
new_tire_label_size = Label(app, text ='Rim Size', font = ('bold',12),padx=20,bg= '#447cc4')
new_tire_label.grid(row = 3, column = 0, sticky= W)
new_tire_label_width.grid(row = 2, column = 1, sticky= W)
new_tire_label_ratio.grid(row = 2, column = 2, sticky= W)
new_tire_label_size.grid(row = 2, column = 3, sticky= W)
new_tire_entry1 = Entry(app, textvariable = new_tire_width,bg= '#447cc4')
new_tire_entry1.grid(row = 3, column= 1,padx=20)
new_tire_entry2 = Entry(app, textvariable = new_tire_ratio,bg= '#447cc4')
new_tire_entry2.grid(row = 3, column= 2, padx= 20)
new_tire_entry3 = Entry(app, textvariable = new_tire_size,bg= '#447cc4')
new_tire_entry3.grid(row = 3, column= 3, padx=20)

# will it fit box 
fitment = Text(app,height = 2,width= 15,bg= '#447cc4')
fitment.grid(row = 4, column= 2, pady=10 )
fitment_label = Label(app, text ='Will it fit?', font = ('bold',15),bg= '#447cc4')
fitment_label.grid(row = 4, column = 1, sticky= E)

# speedo error box
speedo = Text(app,height=2,width=15,bg= '#447cc4')
speedo.grid(row=5,column=2, pady=10)
speedo_label = Label(app, text ='Speedo Error', font = ('bold',15),bg= '#447cc4')
speedo_label.grid(row = 5, column = 1, sticky= E)

#issue box
issues = Text(app,height=2,width=25,bg= '#447cc4')
issues.grid(row=6,column=2, pady=10)
issues_label = Label(app, text ='Issues', font = ('bold',15),bg= '#447cc4')
issues_label.grid(row = 6, column = 1, sticky= E)

#calculate box 
cal_btn = Button(app,text='Calculate',width=12,command = lambda:[calculate_fitment(),speedo_error_amount()])
cal_btn.grid (row=7,column=3)



# changing the window sizing and title 
app.title('Wheel It Fit')
app.geometry('700x350')


#speedo_error_amount(result,r1)
# start program 
app.mainloop()