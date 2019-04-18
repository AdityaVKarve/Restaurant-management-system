#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 00:08:38 2019

@author: thatguy99
"""

#----Manager interface----#
import pymysql

class managerInt:
    
    def main():
        
        def update():
            conn_manager=pymysql.connect("localhost","phpmyadmin","Give me liberty or give me death","BURGERSHOT")
            cursor=conn_manager.cursor()
            inp=input("Enter task\n1-View Employee Records\n2-Edit Employee Records\n3-View Menu\n4-Edit Menu\n5-View sales\n6-View revenues\n7-View customer details\n")
            if inp==1:
                print("####EMPLOYEE RECORDS####")
                cursor_statement_1="SELECT * FROM EMPLOYEE"
                n=cursor.execute(cursor_statement_1)
                c=cursor.fetchall()
                for x in c:
                    print("Name:"+str(x[0])+" Job:"+str(x[1])+" Salary:"+str(x[2])+" Date of joining:"+str(x[3])+" Employee ID:"+str(x[4]))
                update()
            if inp==2:
                inp2=raw_input("Enter task\n1-Add Employee\n2-Edit Employee\n3-Delete Employee\nr-Go back\n")
                if int(inp2)==1:
                    name=raw_input("Enter employee name-")
                    desc=raw_input("Enter job-")
                    salary=input("Enter salary-")
                    date=raw_input("Enter date of joining(YYYY-MM-DD)-")
                    cursor_statement_2="SELECT * FROM EMPLOYEE"
                    n=cursor.execute(cursor_statement_2)
                    c=cursor.fetchall()
                    empid=len(c)+1
                    cursor_statement_3="INSERT INTO EMPLOYEE VALUES(\""+name+"\",\""+desc+"\","+str(salary)+",\""+date+"\","+str(empid)+");"
                    n1=cursor.execute(cursor_statement_3)
                    conn_manager.commit()
                    print("Employee records added.")
                    update()
                if int(inp2)==2:
                    cursor_statement_4="SELECT * FROM EMPLOYEE"
                    n=cursor.execute(cursor_statement_4)
                    c=cursor.fetchall()
                    for x in c:
                        print("Name:"+str(x[0])+" Job:"+str(x[1])+" Salary:"+str(x[2])+" Date of joining:"+str(x[3])+" Employee ID:"+str(x[4]))
                    edit=input("Enter employee ID of employee to edit(r to return)-")
                    if edit=="r":
                        update()
                    upname=raw_input("Enter new employee name-")
                    updesc=raw_input("Enter new job-")
                    upsalary=input("Enter new salary-")
                    cursor_statement_5="UPDATE EMPLOYEE SET name=\""+upname+"\",description=\""+updesc+"\",salary="+str(upsalary)+" WHERE emp_id="+str(edit)+";"
                    print(cursor_statement_5)
                    n1=cursor.execute(cursor_statement_5)
                    conn_manager.commit()
                    update()
                if int(inp2)==3:
                    cursor_statement_6="SELECT * FROM EMPLOYEE"
                    n=cursor.execute(cursor_statement_6)
                    c=cursor.fetchall()
                    for x in c:
                        print("Name:"+str(x[0])+" Job:"+str(x[1])+" Salary:"+str(x[2])+" Date of joining:"+str(x[3])+" Employee ID:"+str(x[4]))
                    delete=input("Enter employee ID of employee to delete(r to return)-")
                    if delete=="r":
                        update()
                    cursor_statement_7="DELETE FROM EMPLOYEE WHERE emp_id="+str(delete)
                    cursor.execute(cursor_statement_7)
                    conn_manager.commit()
                    print("Record deleted")
                    update()
            if inp==3:
                print("####ITEM MENU####")
                cursor_statement_8="SELECT * FROM FOOD"
                n=cursor.execute(cursor_statement_8)
                c=cursor.fetchall()
                for x in c:
                    print("ID:"+str(x[0])+" Name:"+str(x[1])+" Price:"+str(x[2])+" Description:"+str(x[3]))
                update()
            if inp==4:
                inp3=raw_input("Enter task\n1-Add item\n2-Edit item\n3-Delete item\nr-Go back\n")
                if int(inp3)==1:
                    name=raw_input("Enter item name-")
                    price=raw_input("Enter price-")
                    desc=raw_input("Enter description-")
                    cursor_statement_9="SELECT * FROM FOOD;"
                    n=cursor.execute(cursor_statement_9)
                    c=cursor.fetchall()
                    f_id=len(c)+1
                    cursor_statement_10="INSERT INTO FOOD VALUES("+str(f_id)+",\""+name+"\","+price+",\""+desc+"\");"
                    n1=cursor.execute(cursor_statement_10)
                    conn_manager.commit()
                    print("New item added.")
                    update()
                if int(inp3)==2:
                    cursor_statement_11="SELECT * FROM FOOD;"
                    n=cursor.execute(cursor_statement_11)
                    c=cursor.fetchall()
                    for x in c:
                        print("ID:"+str(x[0])+" Name:"+str(x[1])+" Price:"+str(x[2])+" Description:"+str(x[3]))
                    edit=input("Enter ID of item to edit(r to return)-")
                    if edit=="r":
                        update()
                    upname=raw_input("Enter new item name-")
                    upprice=raw_input("Enter new item price-")
                    updesc=raw_input("Enter new description-")
                    cursor_statement_12="UPDATE FOOD SET name=\""+upname+"\",description=\""+updesc+"\",price="+upprice+" WHERE food_id="+str(edit)+";"
                    n1=cursor.execute(cursor_statement_12)
                    conn_manager.commit()
                    update()
                if int(inp3)==3:
                    cursor_statement_13="SELECT * FROM FOOD"
                    n=cursor.execute(cursor_statement_13)
                    c=cursor.fetchall()
                    l=len(c)
                    for x in c:
                        print("ID:"+str(x[0])+" Name:"+str(x[1])+" Price:"+str(x[2])+" Description:"+str(x[3]))
                    delete=input("Enter item ID of item to delete(r to return)-")
                    if delete=="r":
                        update()
                    cursor_statement_14="DELETE FROM FOOD WHERE food_id="+str(delete)
                    cursor.execute(cursor_statement_14)
                    conn_manager.commit()
                    for y in c:
                        if int(y[0])>delete:
                            cursor_statement_15="UPDATE FOOD SET food_id="+str(int(y[0])-1)+" WHERE food_id="+str(y[0])+";"
                            cursor.execute(cursor_statement_15)
                            conn_manager.commit()
                    print("item deleted")
                    update()
            if inp==5:
                print("####ORDER RECORDS####")
                cursor_statement_16="SELECT * FROM RECORDS;"
                n=cursor.execute(cursor_statement_16)
                c=cursor.fetchall()
                for x in c:
                    print("Order ID:"+str(x[0])+" Revenue:"+str(x[1])+" date-"+str(x[2]))
                update()
            
            if inp==6:
                cursor_statement_17="SELECT * FROM RECORDS;"
                n=cursor.execute(cursor_statement_17)
                c=cursor.fetchall()
                current_date=c[0][2]
                revenue=0
                for x in c:
                    if x[2]==current_date:
                        revenue+=x[1]
                    else:
                        print("Date-"+str(current_date)+" Revenue for the day:"+str(revenue)+"$")
                        current_date=x[2]
                        revenue=x[1]
                print("Date-"+str(current_date)+" Revenue for the day:"+str(revenue)+"$")   
                update()
                
            if inp==7:
                print("####Customer list####")
                cursor_statement_18="SELECT * FROM CUSTOMER;"
                n=cursor.execute(cursor_statement_18)
                c=cursor.fetchall()
                for x in c:
                    print("Customer ID-"+str(x[0])+" Email-"+x[1]+" Name-"+x[2]+" "+x[3])
                
                inp4=raw_input("Select task-\n1-View revenue by customer\nr-Go back\n")                         
                if inp4=="1":
                    inp5=raw_input("Enter ID:")
                    cursor_statement_19="SELECT * FROM RECORDS;"
                    n=cursor.execute(cursor_statement_19)
                    c1=cursor.fetchall()
                    revenue=0
                    for x in c1:
                        if c[int(inp5)-1][1]==x[0].split("|")[0]:
                                revenue+=int(x[1])
                    print("Revenue generated="+str(revenue))
                    update()
        update()
            
        
    main()