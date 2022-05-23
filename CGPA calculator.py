from tkinter import *
from tkinter.ttk import *
from pkgutil import *
# writing code needs to
# create the main window of
# the application creating
# main window object named root
root = Tk()

# giving title to the main window
root.title("CGPA Calculator")

# Open window having dimension 100x100
root.geometry('600x600')


#defining the calculation command
def calculate():
         c1 = float(txt1.get("1.0", "end-1c"))
         c2 = float(txt3.get("1.0", "end-1c"))
         c3 = float(txt5.get("1.0", "end-1c"))
         c4 = float(txt7.get("1.0", "end-1c"))
         c5 = float(txt9.get("1.0", "end-1c"))
         c6 = float(txt11.get("1.0", "end-1c"))
         c7 = float(txt13.get("1.0", "end-1c"))
         c8 = float(txt15.get("1.0", "end-1c"))

         g1 = float(txt2.get("1.0", "end-1c"))
         g2 = float(txt4.get("1.0", "end-1c"))
         g3 = float(txt4.get("1.0", "end-1c"))
         g4 = float(txt6.get("1.0", "end-1c"))
         g5 = float(txt8.get("1.0", "end-1c"))
         g6 = float(txt10.get("1.0", "end-1c"))
         g7 = float(txt12.get("1.0", "end-1c"))
         g8 = float(txt14.get("1.0", "end-1c"))
         cgpa = ((c1*g1)+(c2*g2)+(c3*g3)+(c4*g4)+(c5*g5)+(c6*g6)+(c7*g7)+(c8*g8))/(c1+c2+c3+c4+c5+c6+c7+c8)
         label11.config(text="CGPA is :" + str(cgpa))
#placing the elements:
label1 = Label(root, text ="SEM 1").place(x=30, y=70)
label2 = Label(root, text ="Credits").place(x=80, y=40)
label3 = Label(root, text ="SGPA").place(x=160, y=40)
txt1 = Text(root, height = 1, width = 5)
txt1.place(x=80, y=70)
txt2 = Text(root, height = 1, width = 5)
txt2.place(x=160, y=70)

label4 = Label(root, text ="SEM 2").place(x=30, y=120)
txt3 = Text(root, height = 1, width = 5)
txt3.place(x=80, y=120)
txt4 = Text(root, height = 1, width = 5)
txt4.place(x=160, y=120)

label5 = Label(root, text ="SEM 3").place(x=30, y=160)
txt5 = Text(root, height = 1, width = 5)
txt5.place(x=80, y=160)
txt6 = Text(root, height = 1, width = 5)
txt6.place(x=160, y=160)

label6 = Label(root, text ="SEM 4").place(x=30, y=200)
txt7 = Text(root, height = 1, width = 5)
txt7.place(x=80, y=200)
txt8 = Text(root, height = 1, width = 5)
txt8.place(x=160, y=200)

label7 = Label(root, text ="SEM 5").place(x=30, y=240)
txt9 = Text(root, height = 1, width = 5)
txt9.place(x=80, y=240)
txt10 = Text(root, height = 1, width = 5)
txt10.place(x=160, y=240)


label8 = Label(root, text ="SEM 6").place(x=30, y=280)
txt11 = Text(root, height = 1, width = 5)
txt11.place(x=80, y=280)
txt12 = Text(root, height = 1, width = 5)
txt12.place(x=160, y=280)

label9 = Label(root, text ="SEM 7").place(x=30, y=320)
txt13 = Text(root, height = 1, width = 5)
txt13.place(x=80, y=320)
txt14 = Text(root, height = 1, width = 5)
txt14.place(x=160, y=320)

label10 = Label(root, text ="SEM 8").place(x=30, y=360)
txt15 = Text(root, height = 1, width = 5)
txt15.place(x=80, y=360)
txt16 = Text(root, height = 1, width = 5)
txt16.place(x=160, y=360)

button2 = Button(root, text ="Calculate" , command = calculate).place(x=100, y=400)

label11 =Label(root, text="")
label11.place(x=100, y=440)

#setting all creddits and gpas as zero by defaukt:
txt1.insert(1.0, "0")
txt2.insert(1.0, "0")
txt3.insert(1.0, "0")
txt4.insert(1.0, "0")
txt5.insert(1.0, "0")
txt6.insert(1.0, "0")
txt7.insert(1.0, "0")
txt8.insert(1.0, "0")
txt9.insert(1.0, "0")
txt10.insert(1.0, "0")
txt11.insert(1.0, "0")
txt12.insert(1.0, "0")
txt13.insert(1.0, "0")
txt14.insert(1.0, "0")
txt15.insert(1.0, "0")
txt16.insert(1.0, "0")


# calling mainloop method which is used
# when your application is ready to run
# and it tells the code to keep displaying
root.mainloop()
