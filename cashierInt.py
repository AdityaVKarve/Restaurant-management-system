#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 19:24:39 2019

@author: thatguy99
"""

#----CASHIER INTERFACE----#
import pymysql
import time
import threading
import os
conn_cashier=""
cursor=""
ctr=0
class cashierInterface:


    def main():
        
        def update():
            
            global cursor
            global conn_cashier
            conn_cashier=pymysql.connect("localhost","phpmyadmin","Give me liberty or give me death","BURGERSHOT")
            cursor=conn_cashier.cursor()
            orderList=[]
            # for windows 
            if os.name == 'nt': 
                _ = os.system('cls') 
  
            # for mac and linux(here, os.name is 'posix') 
            else: 
                _ = os.system('clear')
            print("----BURGERSHOT----")
            print("Pending orders- ")

            cursor_statement_1="SELECT * FROM ORDERS"
            n=cursor.execute(cursor_statement_1)
            c=cursor.fetchall() 
            global ctr
            ctr=0
            for x in c:
                chk=0;
                ctr=ctr+1
                for y in orderList:
                    if x==y:
                        chk=1
                if chk==0:
                    orderList.append(x)
                    refresh(ctr,orderList)
            inp=raw_input("Enter order number to confirm payment/press r to refresh/press v to view order details-")
            if inp=="r":
                orderList=[]
                conn_cashier.commit()
                conn_cashier.close()
                update()
            elif inp=="v":
                ord_no=raw_input("Enter order number-")
                n1=int(ord_no)-1
                data=orderList[n1][1].split("|")
                items=data[2].split()
                print("Items ordered-")
                for x in items:
                    cursor_statement_4="select name from FOOD where food_id="+str(x)+";"
                    n=cursor.execute(cursor_statement_4)
                    c=cursor.fetchall()
                    print(c[0][0])
                inp=raw_input("press r to go back")
                if inp=="r":
                    orderList=[]
                    conn_cashier.commit()
                    conn_cashier.close()
                    update()
            elif inp.isdigit():
                n1=int(inp)
                data=orderList[n1-1][1].split("|")
                items=data[2].split()
                total=0
                for x in items:
                    cursor_statement_4="select price from FOOD where food_id="+str(x)+";"
                    n=cursor.execute(cursor_statement_4)
                    c=cursor.fetchall()
                    total+=c[0][0]
                cursor_statement_4="INSERT INTO RECORDS VALUES(\""+str(orderList[n1-1][1])+"\","+str(total)+",\""+str(orderList[n1-1][2])+"\");"
                
                
                cursor_statement_2="DELETE FROM ORDERS WHERE ord_id=\""+str(orderList[n1-1][1])+"\";"
                n1=cursor.execute(cursor_statement_4) 
                conn_cashier.commit()
                n=cursor.execute(cursor_statement_2)
                conn_cashier.commit()
                conn_cashier.close()
                total=0
                update()
                
        def refresh(n2,orderList):
            global ctr
            data=orderList[0][1].split("|")
            cursor_statement_3="select fname,lname from CUSTOMER where email=\""+str(data[0])+"\";"
            n=cursor.execute(cursor_statement_3);
            c=cursor.fetchall()
            print("Order number-"+str(ctr)+" Order ID-"+str(orderList[len(orderList)-1][1])+" Email-"+str(data[0])+" "+" Name-"+str(c[0][0]))
            
        
        update()
        
        

            

        

    main()