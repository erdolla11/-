import tkinter
from tkinter import *  # Tkinter дайын Модуль,Басқаруды құру
from tkinter import messagebox, ttk

#import pymysql

# create window size: 1200x700, title_name:"basti_bet", set up icon:'man.ico'
basti_bet=tkinter.Tk()
basti_bet.title("Basti_Bet")
basti_bet.geometry("1300x680+0+0")
basti_bet.iconbitmap('man.ico')

# create title_Label:"С.Сейфуллин  Атындағы Қазақ  Агротехникалық Университеті" and set up values
title=Label(basti_bet,text="С.Сейфуллин  Атындағы \n Қазақ  Агротехникалық Университеті",bd=5,relief=RIDGE,font=("times new roman",46,"bold"),fg="white",bg="navy")
title.pack(side=TOP,fill=X)

# create System_Frame and values
System_Frame=Frame(basti_bet,bd=5,relief=RAISED,bg="LIGHT BLUE")
System_Frame.place(x=10,y=155,width=1280,height=520)

# create Kazatu_Label:"Студенттерді Басқару Жүйесі"
Name_Frame=Label(System_Frame,text="Студенттерді Басқару Жүйесі",bd=10,font=("times new roman",46,"bold"),fg="black",bg="LIGHT BLUE")
Name_Frame.grid(row=1,column=0,pady=10,padx=270,sticky="w")

# create input_Frame and values
input_Frame=Frame(basti_bet,bd=5,relief=FLAT,bg="LIGHT BLUE")
input_Frame.place(x=20,y=285,width=1260,height=230)

# create Label:"ЖСН:" and set up values
L_idnumber=Label(input_Frame,text="ЖСН:",bd=10,font=("times new roman",20),fg="black",bg="light blue")
L_idnumber.grid(row=1,column=0,padx=10)

# create Entry:"ЖСН:" and set up values
E_idnumber=Entry(input_Frame,bd=5,width=30)
E_idnumber.grid(row=1,column=1)

# create Label:"Студенттік №." and set up values
L_studentNo=Label(input_Frame,text="Студенттік №.",bd=10,font=("times new roman",20),fg="black",bg="light blue")
L_studentNo.grid(row=2,column=0,padx=10)

# create Entry:"Студенттік №." and set up values
E_studentNo=Entry(input_Frame,bd=5,width=30)
E_studentNo.grid(row=2,column=1)

# create Label:"Аты-Жөні:" and set up values
L_fullName=Label(input_Frame,text="Аты-Жөні:",bd=10,font=("times new roman",20),fg="black",bg="light blue")
L_fullName.grid(row=2,column=2,padx=15)

# create Entry:"Аты-Жөні:" and set up values
E_fullName=Entry(input_Frame,bd=5,width=40)
E_fullName.grid(row=2,column=3)

# create Label:"Курс:" and set up values
L_grade=Label(input_Frame,text="Курс:",bd=10,font=("times new roman",20),fg="black",bg="light blue")
L_grade.grid(row=2,column=4,padx=15)

# create ttk.Combobox:"Курс:" and set up values
combo_grade = ttk.Combobox(input_Frame,font=("times new roman", 14), state='readonly')
combo_grade['values'] = ("-","1","2","3","4")
combo_grade.grid(row=2, column=5)

# create Label:"Факультеті:" and set up values
L_faculty=Label(input_Frame,text="Факультеті:",bd=10,font=("times new roman",20),fg="black",bg="light blue")
L_faculty.grid(row=3,column=0,padx=10)

# create Entry:"Факультеті:" and set up values
E_faculty=Entry(input_Frame,bd=5,width=30)
E_faculty.grid(row=3,column=1)

# create Label:"Мамандық:" and set up values
L_profession=Label(input_Frame,text="Мамандық:",bd=10,font=("times new roman",20),fg="black",bg="light blue")
L_profession.grid(row=3,column=2,padx=15)

# create Entry:"Мамандық:" and set up values
E_profession=Entry(input_Frame,bd=5,width=40)
E_profession.grid(row=3,column=3)

# create Label:"Жыныс:" and set up values
L_gender=Label(input_Frame,text="Жыныс:",bd=10,font=("times new roman",20),fg="black",bg="light blue")
L_gender.grid(row=3,column=4,padx=15)

# create ttk.Combobox:"Жыныс:" and set up values
combo_gender = ttk.Combobox(input_Frame,font=("times new roman", 14), state='readonly')
combo_gender['values'] = ("man","woman")
combo_gender.grid(row=3, column=5)

# create Label:"Түскен жылы:" and set up values
L_time=Label(input_Frame,text="Түскен жылы:",bd=10,font=("times new roman",20),fg="black",bg="light blue")
L_time.grid(row=4,column=0,padx=10)

# create Entry:"Түскен жылы:" and set up values
E_time=Entry(input_Frame,bd=5,width=30)
E_time.grid(row=4,column=1)

# create Label:"Мамандық №." and set up values
L_professionNo=Label(input_Frame,text="Мамандық №.",bd=10,font=("times new roman",20),fg="black",bg="light blue")
L_professionNo.grid(row=4,column=2,padx=15)

# create Entry:"Мамандық №." and set up values
E_professionNo=Entry(input_Frame,bd=5,width=40)
E_professionNo.grid(row=4,column=3)

# create Label:"Оқу тілі:" and set up values
L_language=Label(input_Frame,text="Оқу тілі:",bd=10,font=("times new roman",20),fg="black",bg="light blue")
L_language.grid(row=4,column=4)

# create ttk.Combobox:"Оқу тілі:" and set up values
combo_language = ttk.Combobox(input_Frame,font=("times new roman", 14), state='readonly')
combo_language['values'] = ("Kazakh","Russian","English")
combo_language.grid(row=4, column=5)

# Button_frame
btn_Frame = Frame(System_Frame, bd=4, relief=RIDGE,bg="LIGHT BLUE")
btn_Frame.place(x=5, y=360, width=1260,height=130)

# button :"Қосу"
btnInsert = tkinter.Button(btn_Frame, text="Қосу", command=lambda: get_info('Insert'),
                           font=('times new roman', 26, 'bold'), width=8, height=1)
btnInsert.grid(row=0, column=0, pady=30, padx=35)

# button :"Өзгерту"
btnUpdate=tkinter.Button(btn_Frame,text="Өзгерту",command=lambda:get_info('Update'),font=('times new roman',26,'bold'),width=8,height=1)
btnUpdate.grid(row=0, column=1,pady=30,padx=35)

# button :"жою"
btnDelete=tkinter.Button(btn_Frame,text="жою",command=lambda:get_info('Delete'),font=('times new roman',26,'bold'),width=8,height=1)
btnDelete.grid(row=0, column=2,pady=30,padx=35)

# button :"Іздеу"
btnSelect=tkinter.Button(btn_Frame,text="Іздеу",command=lambda:get_info('Select'),font=('times new roman',26,'bold'),width=8,height=1)
btnSelect.grid(row=0, column=3,pady=30,padx=35)

def get_info(selection):

    idnumber = E_idnumber.get()
    studentNo = E_studentNo.get()
    name = E_fullName.get()
    grade = combo_grade.get()
    faculty = E_faculty.get()
    profession = E_profession.get()
    gender = combo_gender.get()
    time = E_time.get()
    professionNo = E_professionNo.get()
    language = combo_language.get()

    if selection in ('Insert'):
        con=pymysql.connect(host="localhost",user="root",password="somissyou",database="student_system")
        cur = con.cursor()
        cur.execute("insert into management(idnumber,studentNo,fullName,grade,faculty,profession,gender,time,professionNo,language) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(idnumber,studentNo,name,grade,faculty,profession,gender,time,professionNo,language))
        con.commit()
        con.close()

    elif selection in ('Update'):
        con = pymysql.connect(host="localhost", user="root", password="somissyou", database="student_system")
        cur = con.cursor()
        cur.execute("update management set grade='%s'"%(grade)+",faculty='%s'"%(faculty)+",profession='%s'"%(profession)+",gender='%s'"%(gender)+",time='%s'"%(time)+",professionNo='%s'"%(professionNo)+",language='%s'"%(language)+"where idnumber='%s'"%(idnumber)+"or studentNo='%s'"%(studentNo)+"or fullName='%s'"%(name))
        con.commit()
        con.close()

    elif selection in ('Delete'):
        con = pymysql.connect(host="localhost", user="root", password="somissyou", database="student_system")
        cur = con.cursor()
        cur.execute("delete from management where idnumber='%s'"%(idnumber)+"or studentNo='%s'"%(studentNo)+"or fullName='%s'"%(name))
        con.commit()
        con.close()

    elif selection in ('Select'):
        con = pymysql.connect(host="localhost", user="root", password="somissyou", database="student_system")
        cur = con.cursor()
        cur.execute("select idnumber,studentNo,fullName,grade,faculty,profession,gender,time,professionNo,language from management where idnumber='%s'"%(idnumber)+" or fullName='%s'"%(name)+" or studentNo='%s'"%(studentNo))
        rows = cur.fetchall()
        idnumber_fetch=''
        studentNo_fetch=''
        name_fetch = ''
        grade_fetch = ''
        faculty_fetch = ''
        profession_fetch = ''
        gender_fetch = ''
        time_fetch = ''
        professionNo_fetch=''
        language_fetch=''
        for row in rows:
            idnumber_fetch=row[0]
            studentNo_fetch = row[1]
            name_fetch = row[2]
            grade_fetch = row[3]
            faculty_fetch = row[4]
            profession_fetch = row[5]
            gender_fetch = row[6]
            time_fetch = row[7]
            professionNo_fetch = row[8]
            language_fetch = row[9]

        E_idnumber.delete(0,END)
        E_studentNo.delete(0,END)
        E_fullName.delete(0,END)
        combo_grade.delete(0,END)
        E_faculty.delete(0,END)
        E_profession.delete(0,END)
        combo_gender.delete(0,END)
        E_time.delete(0,END)
        E_professionNo.delete(0,END)
        combo_language.delete(0,END)


        E_idnumber.insert(0,idnumber_fetch)
        E_studentNo.insert(0, studentNo_fetch)
        E_fullName.insert(0, name_fetch)
        combo_grade.insert(0, grade_fetch)
        E_faculty.insert(0, faculty_fetch)
        E_profession.insert(0, profession_fetch)
        combo_gender.insert(0, gender_fetch)
        E_time.insert(0, time_fetch)
        E_professionNo.insert(0, professionNo_fetch)
        combo_language.insert(0, language_fetch)

        con.close()

def exit():
    MsgBox = tkinter.messagebox.askquestion('Шығу кнопкасы', 'Барлық ақпарат дурыс сохранить \nетілдіма,Енді бағдарламадан шығасыз ба?')
    if MsgBox == 'yes':
        basti_bet.destroy()
        return

# button :"Шығу"
btnExit=tkinter.Button(btn_Frame,text="Шығу",command=exit,font=('times new roman',26,'bold'),width=8,height=1)
btnExit.grid(row=0, column=4,pady=30,padx=35)


mainloop()
