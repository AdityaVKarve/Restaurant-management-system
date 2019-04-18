#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 19:19:07 2019

@author: thatguy99
"""
import Tkinter as tk
import loginScreenCust
import pymysql
import PIL.ImageTk as itk
import PIL.Image as im
import datetime
finalOrder=""
class CustMain:

    def main():
        root=tk.Tk()
        root.title("Customer main page")
        conn_customer=pymysql.connect("localhost","phpmyadmin","Give me liberty or give me death","BURGERSHOT")
        cursor=conn_customer.cursor()
        #----DEFINE METHODS----#
        #----DEFINE MYSQL STATEMENTS----#
        cursor_statement1="select * from FOOD";
        n=cursor.execute(cursor_statement1)
        c=cursor.fetchall()
        
        #----PARSE MYSQL STATEMENTS----#
        choicesBurger=[]
        choicesSalad=[]
        choicesSauce=[]
        choicesPizza=[]
        choicesDesert=[]
        choicesSide=[]
        for x in c:
            if x[3]=="Burger":
                choicesBurger.append(str(str(x[1])+" "+str(x[2])+"$"))
            if x[3]=="Salad":
                choicesSalad.append(str(str(x[1])+" "+str(x[2])+"$"))
            if x[3]=="Sauce":
                choicesSauce.append(str(str(x[1])+" "+str(x[2])+"$"))
            if x[3]=="Deserts":
                choicesDesert.append(str(str(x[1])+" "+str(x[2])+"$"))
            if x[3]=="Sides":
                choicesSide.append(str(str(x[1])+" "+str(x[2])+"$"))
            if x[3]=="Pizza":
                choicesPizza.append(str(str(x[1])+" "+str(x[2])+"$"))
        #----DEFINE RESOURCES----#
        image1 = tk.PhotoImage(file = 'logo.ppm')
        # If image is stored in the same place as the python code file,
        # otherwise you can have the directory of the image file.
        label = tk.Label(image = image1)
        label.image = image1 # yes can keep a reference - good!
        
        #-----DEFINE ART-----#
        canvas=tk.Canvas(root,width=1280,height=760,bd=0,highlightthickness=0)
        canvas.create_line(0, 200, 1280, 200, fill="gold") #(x1,y1,x2,y2,color)
        canvas.configure(bg="white")
        #----DEFINE VARIABLES----#
        UserName=tk.StringVar()
        UserName.set("Guest")
        Email=tk.StringVar()
        Email.set("Email")
        total=tk.StringVar()
        total.set("0")    
        CustomerID=tk.StringVar()
        CustomerID.set("Unknown")
        choiceBurger=tk.StringVar()
        choiceBurger.set("Burgers!")
        choiceSide=tk.StringVar()
        choiceSide.set("Sides!")
        choiceSauce=tk.StringVar()
        choiceSauce.set("Sauce!")
        choicePizza=tk.StringVar()
        choicePizza.set("Pizza!")
        choiceSalad=tk.StringVar()
        choiceSalad.set("Salads!")
        choiceDesert=tk.StringVar()
        choiceDesert.set("Deserts!")
        Invalid=tk.StringVar()
        Welcome=tk.StringVar()
        Welcome.set("Welcome!")
        label_invalid=""
        label_valid=""
        
        #----DEFINE FUNCTIONS----#
        def invalid_details():
            Invalid.set("Invalid details!")
            label_invalid=tk.Label(root,textvar=Invalid)
            label_invalid.config(background="white",foreground="red",font=("Ariel",15))
            label_invalid.place(relx=0.9,rely=0.45,anchor="center")
            #remWelcome()
        def welcome():
            Welcome.set("Welcome!")
            label_valid=tk.Label(root,textvar=Welcome)
            label_valid.config(background="white",foreground="green",font=("Ariel",15))
            label_valid.place(relx=0.9,rely=0.45,anchor="center")
        def logout():
            Invalid.set("")
            Welcome.set("")
            refresh()
        def login():
            usname=UserName.get()
            names=usname.split()
            email=Email.get()
            cursor_statement_3="select cust_id from CUSTOMER where email=\""+str(email)+"\";"
            n=cursor.execute(cursor_statement_3)
            c=cursor.fetchall()
            try:
                if c[0][0]>0 and len(names)>1:
                    CustomerID.set(c[0][0])
                    print("Valid")
                    Invalid.set("")
                    welcome()
            except IndexError:
                invalid_details()
                
        def signup():
            usname=UserName.get()
            names=usname.split()
            email=Email.get()
            cursor_statement_6="select cust_id from CUSTOMER;"
            n=cursor.execute(cursor_statement_6)
            c=cursor.fetchall()
            new_id=int(len(c))+1
            cursor_statement_7="INSERT INTO CUSTOMER VALUES("+str(new_id)+",\""+str(email)+"\",\""+str(names[0])+"\",\""+str(names[1])+"\");"
            print(cursor_statement_7)
            cursor.execute(cursor_statement_7)
            conn_customer.commit()
            login() 
        def place_order():
            now=datetime.datetime.now()
            receipt=""
            if finalOrder!="":
                receipt=str(str(Email.get())+"|"+str(now.year)+"-"+str(now.month)+"-"+str(now.day)+"|"+finalOrder)
                print(receipt)
                custid=0;
                if CustomerID=="Unknown":
                    custid=0;
                else:
                    custid=int(CustomerID.get())
                cursor_statement_4=str("INSERT INTO ORDERS VALUES ("+str(custid)+", \""+receipt+"\", \""+str(now.year)+"-"+str(now.month)+"-"+str(now.day)+"\")");
                print(cursor_statement_4)
                n=cursor.execute(cursor_statement_4)
                conn_customer.commit()
                logout()
                
        def create_order(item):
            global finalOrder
            cursor_statement2="select food_id from FOOD where name=\""+str(item)+"\"";
            n=cursor.execute(cursor_statement2)
            c=cursor.fetchall()
            orderno=int(c[0][0])
            finalOrder+=str(orderno)+" "
            
        def refresh():
            global finalOrder
            total.set("0")
            UserName.set("")
            Email.set("")
            finalOrder=""
            
        def parse_Entry(entry):
            ret=""
            ret1=""
            for x in entry:
                if x.isdigit():
                    ret+=str(x)
                elif x.isdigit()==False and x!="$":
                    ret1+=str(x)
            create_order(ret1)
            return int(ret)
        def add_Entry():
            if choiceBurger.get()!="Burgers!":
                temp=(int)(int(total.get())+parse_Entry(choiceBurger.get()))
                total.set(temp)
                choiceBurger.set("Burgers!")
            if choiceSide.get()!="Sides!":
                temp=(int)(int(total.get())+parse_Entry(choiceSide.get()))
                total.set(temp)
                choiceSide.set("Sides!")
            if choiceSauce.get()!="Sauce!":
                temp=(int)(int(total.get())+parse_Entry(choiceSauce.get()))
                total.set(temp)
                choiceSauce.set("Sauce!")
            if choicePizza.get()!="Pizza!":
                temp=(int)(int(total.get())+parse_Entry(choicePizza.get()))
                total.set(temp)
                choicePizza.set("Pizza!")
            if choiceSalad.get()!="Salads!":
                temp=(int)(int(total.get())+parse_Entry(choiceSalad.get()))
                total.set(temp)
                choiceSalad.set("Salads!")
            if choiceDesert.get()!="Deserts!":
                temp=(int)(int(total.get())+parse_Entry(choiceDesert.get()))
                total.set(temp)
                choiceDesert.set("Deserts!")
        
        #---DEFINE CANVAS---#
        root.geometry("1280x760")   
        root.config(background="white")
        
        #----DEFINE GUI----#
        entry_username=tk.Entry(root,textvariable=UserName)
        entry_username.config(width="25")
        
        label_username=tk.Label(root,text="Username:")
        label_username.config(font=("Ariel",20),foreground="gold",background="white")
        
        entry_email=tk.Entry(root,textvariable=Email)
        entry_email.config(width="25")
        
        label_email=tk.Label(root,text="Email:")
        label_email.config(font=("Ariel",20),foreground="gold",background="white")
        
        label_amount=tk.Label(root,text="TOTAL:")
        label_amount.config(font=("Ariel",20),foreground="gold",background="white")
        
        label_total=tk.Label(root,textvariable=total)
        label_total.config(font=("Ariel",20),foreground="gold",background="white")
        
        label_welcome=tk.Label(root,text="BURGERSHOT!")
        label_welcome.config(font=("Algerian",90))
        label_welcome.config(foreground="Gold", background="white") 
        
        button_Refresh=tk.Button(root,text="Refresh",command=refresh)
        button_Refresh.config(font=("Ariel",20),background="gold",foreground="white")
        button_Refresh.config(width="20")
        
        button_AddEntry=tk.Button(root,text="Add Entry!",command=add_Entry)
        button_AddEntry.config(font=("Ariel",20),background="gold",foreground="white",width=20)
        
        button_Place=tk.Button(root,text="Confirm entries!",command=place_order)
        button_Place.config(font=("Ariel",20))
        button_Place.config(background="gold",foreground="white")
        button_Place.config(width="20")
        
        button_login=tk.Button(root,text="Login",command=login)
        button_login.config(font=("Ariel",20),background="gold",foreground="white",width="7")
        
        button_signup=tk.Button(root,text="Sign Up",command=signup)
        button_signup.config(font=("Ariel",20),background="gold",foreground="white",width="7")
        
        popUp_Burger=tk.OptionMenu(root,choiceBurger,*choicesBurger)   #BURGER MENU
        popUp_Burger.config(width=20)
        popUp_Burger.config(font=("Purisa",15))
        popUp_Burger.config(background="purple",foreground="gray")
        
        popUp_Pizza=tk.OptionMenu(root,choicePizza,*choicesPizza)  #PIZZA MENU
        popUp_Pizza.config(width=20)
        popUp_Pizza.config(font=("Purisa",15))
        popUp_Pizza.config(background="purple",foreground="white")
        
        popUp_Sides=tk.OptionMenu(root,choiceSide,*choicesSide)    #SIDES MENU
        popUp_Sides.config(width=20)
        popUp_Sides.config(font=("Purisa",15))
        popUp_Sides.config(background="purple")
        popUp_Sides.config(foreground="white")
        
        popUp_Sauce=tk.OptionMenu(root,choiceSauce,*choicesSauce)  #SAUCES MENU
        popUp_Sauce.config(width=20)
        popUp_Sauce.config(font=("Purisa",15))
        popUp_Sauce.config(background="purple")
        popUp_Sauce.config(foreground="white")
            
        popUp_Salad=tk.OptionMenu(root,choiceSalad,*choicesSalad)  #SALADS MENU
        popUp_Salad.config(width=20)
        popUp_Salad.config(font=("Purisa",15))
        popUp_Salad.config(background="purple")
        popUp_Salad.config(foreground="white")
        
        popUp_Desert=tk.OptionMenu(root,choiceDesert,*choicesDesert)   #DESERTS MENU
        popUp_Desert.config(width=20)
        popUp_Desert.config(font=("Purisa",15))
        popUp_Desert.config(background="purple",foreground="white")
        
        #-----PLACE GUI---#
        label_welcome.place(relx=0.975,rely=0.1,anchor="e")
        
        label_total.place(relx=0.9, rely=0.9)
        
        label_amount.place(relx=0.8,rely=0.9)
        
        label_username.place(relx=0.675,rely=0.32,anchor="e")
        
        label_email.place(relx=0.675,rely=0.37,anchor="e")
        
        entry_username.place(relx=0.76,rely=0.32,anchor="center")
        
        entry_email.place(relx=0.76,rely=0.37,anchor="center")
        
        popUp_Burger.place(relx=0.2,rely=0.3)
        
        popUp_Pizza.place(relx=0.2,rely=0.4)
        
        popUp_Sides.place(relx=0.2,rely=0.5)
        
        popUp_Sauce.place(relx=0.2,rely=0.6)
        
        popUp_Salad.place(relx=0.2,rely=0.7)
        
        popUp_Desert.place(relx=0.2,rely=0.8)
        
        button_login.place(relx=0.615,rely=0.45,anchor="center")
        
        button_signup.place(relx=0.78,rely=0.45,anchor="center")
        
        button_Place.place(relx=0.7,rely=0.65,anchor="center")
        
        button_AddEntry.place(relx=0.7,rely=0.55,anchor="center")
        
        button_Refresh.place(relx=0.7,rely=0.75,anchor="center")
        
        canvas.place(relx=0.5,rely=0.5,anchor="center")
        
        canvas.create_image(100,150,image=image1,anchor="center")
        
        #------FIN-----#
        
        root.mainloop()
    main()
