from tkinter import *
from tkinter import messagebox

import ttkbootstrap as ttk
from ttkbootstrap.constants import *

######  Sent LINE ########
from songline import Sendline
token = 'oT5OnnE9KCFQW1Ygl18nro08FrLnMBXiTZJpkHssDHW'
messenger = Sendline(token)
############################

###### Write to CSV ############
import csv
from datetime import datetime

def writecsv(record_list):
    # newline='' คือให้เรียงต่อกันโดยไม่เว้นช่องว่าง
    # 'a' = append คือการบันทึกค่าไปเรื่อยๆ
    # encoding='utf-8' ให้ใช้กับภาษาไทยได้
    with open('data.csv','a',newline='',encoding='utf-8') as file:
        fw = csv.writer(file)
        fw.writerow(record_list)

###################################

GUI = Tk()

GUI.title('โปรแกรมซ่อมบำรุง by Loong')
GUI.geometry('500x500+50+50')
####FONT#####
FONT1 = ('Angsana New',20,'bold')
FONT2 = ('Angsana New',15)

#############
L = Label(GUI,text='ใบแจ้งซ่อม',font=FONT1)
L.pack()

#-------------
L = Label(GUI,text='ชื่อผู้แจ้ง',font=FONT2)
L.place(x=30,y=50)
v_name = StringVar() #ตัวแปรพิเศษใช้กับ GUI
E1 = Entry(GUI,textvariable=v_name, font=FONT2)
E1.place(x=150,y=50)

#-------------
L = Label(GUI,text='แผนก',font=FONT2)
L.place(x=30,y=100)
v_department =StringVar()
E2 = Entry(GUI,textvariable=v_department,font=FONT2)
E2.place(x=150,y=100)
#-------------

L = Label(GUI,text='อุปกรณ์/เครื่อง',font=FONT2)
L.place(x=30,y=150)
v_machine =StringVar()
E3 = Entry(GUI,textvariable=v_machine,font=FONT2)
E3.place(x=150,y=150)
#-------------

L = Label(GUI,text='อาการเสีย',font=FONT2)
L.place(x=30,y=200)
v_problem =StringVar()
E4 = Entry(GUI,textvariable=v_problem ,font=FONT2)
E4.place(x=150,y=200)

#-------------
L = Label(GUI,text='หมายเลข',font=FONT2)
L.place(x=30,y=250)
v_number =StringVar()
E5 = Entry(GUI,textvariable=v_number,font=FONT2)
E5.place(x=150,y=250)
#-------------

L = Label(GUI,text='เบอร์โทร',font=FONT2)
L.place(x=30,y=300)
v_tel =StringVar()
E6 = Entry(GUI,textvariable=v_tel,font=FONT2)
E6.place(x=150,y=300)

def save():
    name = v_name.get() # .get คือการดึงออกมาจาก StringVar
    department = v_department.get()
    machine = v_machine.get()
    problem = v_problem.get()
    number = v_number.get()
    tel = v_tel.get()

    text = '\nชื่อผู้แจ้ง: ' + name + '\n' # \n คือขึ้นบรรทัดใหม่
    text = text + 'แผนก: ' + department + '\n'
    text = text + 'อุปกรณ์/เครื่อง: ' + machine + '\n'
    text = text + 'อาการเสีย: ' + problem + '\n'
    text = text + 'หมายเลข: ' + number + '\n'
    text = text + 'โทร: ' + tel + '\n'

    dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    datalist = [dt,name,department,machine,problem,number,tel]
    writecsv(datalist) # Save to CSV

    messenger.sendtext(text) # Sent Line
    messagebox.showinfo('กำลังบันทึกข้อมูล...',text)    

B = ttk.Button(GUI, text='บันทึกใบแจ้งซ่อม',bootstyle=(INFO, OUTLINE),command=save)
B.place(x=200,y=350)


GUI.mainloop()