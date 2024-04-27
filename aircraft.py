############################################
#Menu -- Passenger Details
def passenger():
    while True:
        print('---------------------------------------------------------------------------------------------')
        print('           MENU-01            ')
        print('         PASSENGER_DETAILS    ') 
        print('---------------------------------------------------------------------------------------------')
        print("1.Add Passenger Details")
        print("2.Display Passenger Details")
        print("3.Update Passenger Details")
        print("4.Delete Passenger Details --> Cancel Booking")
        print("5.Exit")
        print('---------------------------------------------------------------------------------------------')
        ch=int(input("Enter your choice:"))
        if ch==1:
            adddata()
        elif ch==2:
            fetchdata()
        elif ch==3:
            updata()
        elif ch==4:
            deldata()
        elif ch==5:
            print('Exiting')
            break
        else:
            print('invalid choice')
def adddata():
    import mysql.connector
    while True:
        mydb=mysql.connector.connect(host="localhost",username="root",passwd="root1",database="aircraft")
        mycursor=mydb.cursor()
        mycursor.execute("select * from passenger_details")
        myresult=mycursor.fetchall()
        aadhar=[]
        for i in myresult:
            aadhar.append(i[1])   
        tot_seats=['A01','A02','A03','B01','B02','B03','C01','C02','C03','D01','D02','D03','E01','E02','E03','F01','F02','F03','G01','G02','G03','H01','H02','H03']
        print('----------------------------------------------------------')
        print('Available seats:')
        print('----------------------------------------------------------')
        l=[]
        for i in myresult:
            l.append(i[0])
        l.sort()
        avail_seat=[]
        for i in tot_seats:
            if i not in l:
                avail_seat.append(i)
                print(i)
        while True:
            sno=input('Enter passenger seat no.:')
            if sno not in avail_seat:
                print('Seat not available')
            else:
                break
        while True:
            ano=input('Enter Aadhar no.:')
            if ano in aadhar:
                print('AADHAR NUMBER NOT ORIGINAL. KINDLY ENTER VALID AADHAR NUMBER.')
            else:
                break
        fname=input('Enter first name:')
        lname=input('Enter last name:')
        gender=input('Enter gender(M/F):')
        contactno=int(input('Enter contact no.:'))
        age=int(input('Enter age:'))
        val="insert into passenger_details values(%s,%s,%s,%s,%s,%s,%s)"
        mycursor.execute(val,(sno,ano,fname,lname,gender,contactno,age))
        mydb.commit()
        ch=input('Want to enter more data?(yes/no)')
        if ch.lower()=='no':
            break
def fetchdata():
    import mysql.connector
    from prettytable import PrettyTable
    x=PrettyTable()
    mydb=mysql.connector.connect(host="localhost",username="root",passwd="root1",database="aircraft")
    mycursor=mydb.cursor()
    x.field_names=['SEAT NO','AADHAR NO','FIRST NAME','LAST NAME','GENDER','CONTACT NO','AGE']
    while True:
        print("-----------------------")
        print("ENTER 1 TO DISPLAY ALL")
        print("ENTER 2 TO DISPLAY ANY PARTICULAR RECORD")
        ch=int(input("ENTER YOUR CHOICE:"))
        if ch==1:
            mycursor.execute("select * from passenger_details")
            break0
        elif ch==2:
            a=input("ENTER AADHAR NUMBER TO SEARCH THE RECORD:")
            mycursor.execute("select* from passenger_details where aadhar_no='%s' "%(a))
            break
    myresult=mycursor.fetchall()
    for i in myresult:
        x.add_row(i)
    print(x.get_string())

def updata():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",username="root",passwd="root1",database="aircraft")
    mycursor=mydb.cursor()
    mycursor.execute("select * from passenger_details")
    myresult=mycursor.fetchall()
    tot_seats=['A01','A02','A03','B01','B02','B03','C01','C02','C03','D01','D02','D03','E01','E02','E03','F01','F02','F03','G01','G02','G03','H01','H02','H03']
    flag=0
    fname=input('Enter First Name:')
    lname=input('Enter Last Name:')
    sno=input('Enter present seat no.:')
    for i in myresult:
        if i[0]==sno and i[2]==fname and i[3]==lname:
            flag=1
        else:
            continue
    if flag==0:
        print('Kindly check details provided. Passenger not found!')
    while flag==1:
        print('----------------------------------------------------------')
        print('Available seats:')
        print('----------------------------------------------------------')
        l=[]
        for i in myresult:
            l.append(i[0])
        l.sort()
        avail_seat=[]
        for i in tot_seats:
            if i not in l:
                avail_seat.append(i)
                print(i)
        new_seat=input('Enter new seat no:')
        if new_seat not in avail_seat:
            print('Invalid choice. Kindly choose another seat.')
        else:
            val="update passenger_details set seat_no='%s' where first_name like '%s' and last_name like '%s'"%(new_seat,fname,lname)
            mycursor.execute(val)
            mydb.commit()
            print('Updation successful!')
            break
def deldata():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",username="root",passwd="root1",database="aircraft")
    mycursor=mydb.cursor()
    mycursor.execute("select * from passenger_details")
    myresult=mycursor.fetchall()
    fname=input('Enter First Name:')
    lname=input('Enter Last Name:')
    ano=input('Enter Aadhar:')
    flag=0
    for i in myresult:
         if i[1]==ano and i[2]==fname and i[3]==lname:
            flag=1
         else:
            continue
    if flag==1:
        mycursor.execute("delete from passenger_details where aadhar_no='%s' and first_name='%s' and last_name='%s' "%(ano,fname,lname))
        mydb.commit()
        print('Booking cancelled. Record deleted.')
    elif flag==0:
        print('Passenger not found!')
# menu- pilot_details
def pilot():
    while True:
        print('---------------------------------------------------------------------------------------------')
        print("       MENU-02         ")
        print('---------------------------------------------------------------------------------------------')
        print("      PILOT_DETAILS    ")
        print('---------------------------------------------------------------------------------------------')
        print("1.ADD PILOT DETAILS")
        print("2.DISPLAY PILOT DETAILS")
        print("3.UPDATE PILOT DETAILS")
        print("4.DELETE PILOT DETAILS")
        print("5.EXIT")
        choice=int(input("ENTER YOUR CHOICE:- "))
        if choice==1:
            add_pilot_details()
        elif choice==2:
            display_pilot_details()
        elif choice==3:
            update_pilot_details()
        elif choice==4:
            delete_details()
        elif choice==5:
            break
        else:
            print("invalid choice")
def add_pilot_details():
    import mysql.connector
    while True:
        mydb=mysql.connector.connect(host="localhost",user="root",password="root1",database="aircraft")
        mycursor=mydb.cursor()
        mycursor.execute("select*from pilot_details")
        myresult=mycursor.fetchall()
        l=[]
        for i in myresult:
            l.append(int(i[0]))
        while True:
            pilot_id=int(input("ENTER PILOT ID:- "))
            if pilot_id in l:
                print("THE ID YOU HAVE ENTERED ALREADY EXISTS! PLEASE ENTER A VALID ONE")
            else:
                break    
        name=input("ENTER NAME:- ")
        gender=input("ENTER GENDER:- ")
        age=int(input("ENTER AGE:- "))
        contact_details=input("ENTER CONTACT NUMBER:- ")
        qualification=input("ENTER QUALIFICATION:- ")
        working_experience=int(input("ENTER EXPERIENCE:no.of flying hours:- "))
        health_status=int(input("ENTER YOUR CURRENT HEALTH STATUS( RATE OUT OF 5 POINTS):- "))
        aircraft_kind=input("ENTER EXPERIENCE:aircraft kind:- ")
        s="insert into pilot_details values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        d=(pilot_id,name,gender,age,contact_details,qualification,working_experience,health_status,aircraft_kind)
        mycursor.execute(s,d)
        mydb.commit()
        print("details added successfully")
        c=input("DO YOU WANT TO ENTER MORE RECORDS(yes/no):- ")
        if c.lower()=='no':
            break
def display_pilot_details():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="root1",database="aircraft")
    mycursor=mydb.cursor()
    from prettytable import PrettyTable
    x=PrettyTable()
    x.field_names = ["PILOT ID","NAME","GENDER","AGE","CONTACT DETAILS","QUALIFICATION","WORKING EXPERIENCE","HEALTH STATUS","EXPERIENCE AIRCRAFT"]
    while True:
        print("-----------------------")
        print("ENTER 1 TO DISPLAY ALL")
        print("ENTER 2 TO DISPLAY ANY PARTICULAR RECORD")
        ch=int(input("ENTER YOUR CHOICE:"))
        if ch==1:
                mycursor.execute("select*from pilot_details")
                break
        elif ch==2:
            a=int(input("ENTER ID TO  SEARCH THE RECORD:"))
            mycursor.execute("select* from pilot_details where pilot_id='%s' "%(a))
            break
    myresult=mycursor.fetchall()
    for i in myresult:
        x.add_row(i)
    print(x.get_string())

def update_pilot_details():
    print("field names:[ pilot_id,name,gender,age,contact_details,qualification,working_experience,health_status,aircraft_kind]")
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",password="root1",database="aircraft")
    mycursor=mydb.cursor()
    while True:
        mycursor.execute("select*from pilot_details")
        myresult=mycursor.fetchall()
        l=[]
        for i in myresult:
            l.append(int(i[0]))
        while True:
                b=int(input("ENTER THE ID OF THE PILOT:- "))
                if b not in l:
                    print("THE ID YOU HAVE ENTERED DOESN'T EXISTS! PLEASE ENTER A VALID ONE")
                else:
                    break
        print("Kindly enter the value to be update as: <field name>=<updated value>")
        a=input("ENTER THE VALUE TO BE UPDATED:- ")
        s="update pilot_details set %s where pilot_id=%s" %(a,b)
        mycursor.execute(s)
        mydb.commit()
        print("details updated successfully")
        c=input("DO YOU WANT TO UPDATE MORE RECORDS(yes/no):- ")
        if c.lower()=='no':
            break
         
def delete_details():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",password="root1",database="aircraft")
    mycursor=mydb.cursor()
    while True:
        mycursor.execute("select*from pilot_details")
        myresult=mycursor.fetchall()
        l=[]
        for i in myresult:
            l.append(int(i[0]))
        while True:
            b=int(input("ENTER ID OF THE PILOT TO BE DELETED :-"))
            if b not in l:
                print("THE ID YOU HAVE ENTERED DOESN'T EXISTS! PLEASE ENTER A VALID ONE")
            else:
                break
        s="delete from pilot_details where pilot_id=%s" %(b)
        mycursor.execute(s)
        mydb.commit()
        print("record deleted successfully")
        c=input("DO YOU WANT TO DELETE MORE RECORDS(yes/no):- ")
        if c.lower()=='no':
            break
#crew member_details
def aircrew():
    while True:
        print('---------------------------------------------------------------------------------------------')
        print("         MENU-03          ")
        print('---------------------------------------------------------------------------------------------')
        print("      CREW MEMBER_DETAILS     ")
        print('---------------------------------------------------------------------------------------------')
        print(" 1. ADD DETAILS OF CREW MEMBERS")
        print(" 2.   DISPLAY CREW MEMBERS   ")
        print(" 3. UPDATE DETAILS OF  CREW MEMBERS")
        print(" 4. DELETE DETAILS OF  CREW MEMBERS")
        print(" 5.  TO  EXIT                     ")
        print("---------------------------------")
        ch=int(input("Enter your choice:"))
        if ch==1:
            print("       ")
            insert()
        elif ch==2:
            print("AIRCREW TABLE:")
            print("              ")
            display()
        elif ch==3:
            update()
            print("_______x________")
        elif ch==4:
            delete()
        elif ch==5:
            break
        else:
            print("invalid choice")
def insert():
        import mysql.connector
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="root1",database="aircraft")
        mycursor=mydb.cursor()
        ans='yes'
        while ans=='yes':
            mycursor.execute("select*from crewmember_details")
            myresult=mycursor.fetchall()
            q=[]
            for i in myresult:
                q.append(int(i[0]))
            while True:
                ID=int(input("ENTER CREWMEMBER ID :"))
                if ID in q:
                    print("THE ID YOU HAVE ENTERED ALREADY EXISTS ! PLEASE ENTER A VALID ID")
                else:
                    break    
            name=input("ENTER CREWMEMBER NAME:")
            qualification=input("HIGHLIGHT YOUR QUALIFICATIONS(HIGHEST ONE ONLY):")
            travelhours=int(input("ENTER THE NUMBER OF HOURS OF FLIGHT EXPERIENCE:"))
            age=int(input("ENTER YOUR AGE(IN YEARS):"))
            healthrate=int(input("ENTER YOUR CURRENT HEALTH STATUS(RATE OUT OF 5 POINTS):"))
            exp=int(input("ENTER THE NUMBER OF YEARS YOU HAVE BEEN WORKING:"))            
            contact=input("ENTER YOU CONTACT NUMBER:")
            gender=input("ENTER YOUR GENDER:")
            s="insert into crewmember_details values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            v=(ID,name,age,qualification,exp,travelhours,healthrate,contact,gender)
            mycursor.execute(s,v)
            mydb.commit()
            print("DETAILS ADDED SUCCESSFULLY")
            print("                           ")
            ans=input("do you want to continue?(yes/no):")
def display():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="root1",database="aircraft")
    mycursor=mydb.cursor()
    from prettytable import PrettyTable
    x=PrettyTable()
    x.field_names =["ID","AIRCREW NAME", "AGE", "QUALIFICATION", "EXPERIENCE","HOURS OF AIR TRAVEL","HEALTH RATE","CONTACT NO","GENDER"]
    while True:
        print("-----------------------")
        print("ENTER 1 TO DISPLAY ALL")
        print("ENTER 2 TO DISPLAY ANY PARTICULAR RECORD")
        ch=int(input("ENTER YOUR CHOICE:"))
        if ch==1:
            mycursor.execute("select*from crewmember_details")
            break
        elif ch==2:
            a=int(input("ENTER ID TO  SEARCH THE RECORD:"))
            mycursor.execute("select* from crewmember_details where ID='%s' "%(a))
            break
    myresult=mycursor.fetchall()
    l=[]
    for i in myresult:
        x.add_row(i)
    print(x.get_string())

def update():
     print("field names: [ID,name,age,qualification,exp,travelhours,healthrate,contact,gender]")
     import mysql.connector
     mydb=mysql.connector.connect(host="localhost",user="root",passwd="root1",database="aircraft")
     mycursor=mydb.cursor()
     mycursor.execute("select*from crewmember_details")
     myres=mycursor.fetchall()
     l=[]
     for i in myres:
         l.append(i[0]) 
     ans='yes'
     while ans=='yes':
         while True:
             parg=input("Enter the id of the member:")
             if parg in str(l):
                 break
             else:
                 print("ID value you have entered doesn't exists! please enter a valid ID")
         print("Kindly enter the value to be update as: <field name>=<updated value>")
         uarg=input("Enter update argument:")
         s="update crewmember_details set %s where ID=%s"%(uarg,parg)
         mycursor.execute(s)
         mydb.commit()
         print("record updated succesfully")
         ans=input("do you want to update more details(yes/no)?:")
def delete():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="root1",database="aircraft")
    mycursor=mydb.cursor()
    mycursor.execute("select*from crewmember_details")
    myres=mycursor.fetchall()
    l=[]
    for i in myres:
        l.append(i[0])
    ans='yes'
    while ans=='yes':
        while True:
            a=input("Enter the ID of the member to delete the record:")
            if a in str(l):
                s="delete from crewmember_details where ID=%s" %(a)
                mycursor.execute(s)
                mydb.commit()
                print(" THE RECORD HAS BEEN DELETED SUCCESSFULLY")
                break
            else:
                print("The ID of the member you have entered doesn't exists! please enter a valid ID:")
        ans=input("do you want to delete more records?(yes/no)")                                         
# flight summary
def selection():
    f=open('Flight_details.txt','w')
    f.write('---------------------------------------------------------------------------------------')
    f.write('FLIGHT SUMMARY')
    f.write('---------------------------------------------------------------------------------------'+'\n')
    import random
    import mysql.connector
    mydb=mysql.connector.connect(host='localhost',username='root',passwd='root1',database='aircraft')
    mycursor=mydb.cursor()
    mycursor.execute('select count(*) from passenger_details')
    pass_count=(mycursor.fetchone()[0])
    print('No.of passengers:',pass_count)
    s='No.of Passengers:'+str(pass_count)+'\n'
    f.write(s)
#flight selection
    if pass_count<=9:
        craft='Airbus A220'
        a=print('Aircraft: Airbus A220')
        f.write('Aircraft: Airbus A220'+'\n')
    elif pass_count>9 and pass_count<=15:
        craft='Boeing 787'
        a=print('Aircraft: Boeing 787')
        f.write('Aircraft: Boeing 787'+'\n')
    elif pass_count>15 and pass_count<=21:
        craft='Airbus A350'
        print('Aircraft: Airbus A350')
        f.write('Aircraft: Airbus A350'+'\n')
    elif pass_count>21 and pass_count<=60:
        craft='Boeing 747-8'
        print('Aircraft: Boeing 747-8')
        f.write('Aircraft: Boeing 747-8'+'\n')
    f.write('---------------------------------------------------------------------------------------'+'\n')
    print('Kindly use 24-hr clock system to input time(eg."23.00")')
    dept_time=float(input('Enter departure time:'))
    f.write('Departure Time:'+str(dept_time)+'\n')
    arr_time=float(input('Enter arrival time:'))
    f.write('Arrival Time:'+str(arr_time)+'\n')
    f.write('---------------------------------------------------------------------------------------'+'\n')
    origin=input('Enter origin:')
    f.write('Origin:'+origin+'\n')
    dest=input('Enter destination:')
    f.write('Destination:'+dest+'\n')
    f.write('---------------------------------------------------------------------------------------'+'\n')
#pilot selection
    craft="aircraft_kind like "+"'"+craft+"'"
    s="select pilot_id from pilot_details where health_status>3 and "+craft
    mycursor.execute(s)
    pilot_id=mycursor.fetchall()
    pilot1=[]
    for i in pilot_id:
        mycursor.execute('select*from pilot_details where pilot_id = %s'%i[0])
        p=mycursor.fetchone()
        pilot1.append(p)
    pilot=[]
    for j in pilot1:
        if (dept_time>18.00 or dept_time<6.00) and arr_time<06.00:
            if j[3]<50:
                pilot.append(j)
        else:
               pilot.append(j)
    from prettytable import PrettyTable
    x=PrettyTable()
    x.field_names=['Pilot ID','Name','Gender','Age','Contact Number','Qualification','No.of flying hours','Health Status','Experince:Aircraft kind']
    print('    ')
    print('THE ASSIGNED PILOTS ARE:')
    f.write('Pilot details:'+'\n')
    p1=random.choice(pilot)
    x.add_row(p1)
    f.write(str(p1)+'\n')
    while True:
        p2=random.choice(pilot)
        if p2!=p1:
            x.add_row(p2)
            f.write(str(p2)+'\n')
            break
    print(x)
    print('   ')
    f.write('---------------------------------------------------------------------------------------'+'\n')
#crew_members selection
    mycursor.execute("select * from crewmember_details where age<30 and healthrate>3 and travelhours>12")
    cm=mycursor.fetchall()
#no of flight attendants
    y=PrettyTable()
    y.field_names=['ID','Name','Age','Qualification','Experience','Travel hours','Health status','Contact','Gender']
    print("THE ASSIGNED ATTENDANTS ARE:")
    f.write("THE ASSIGNED ATTENDANTS ARE:"+'\n')
    if pass_count<9:
        a=random.sample(cm,k=3)
        for i in a:
            y.add_row(i)
            f.write(str(i)+'\n')
    elif 9<pass_count<15:
        a1=random.sample(cm,k=8)
        for i in a1:
            y.add_row(i)
            f.write(str(i)+'\n')
    elif 15<pass_count<21:
        a2=random.sample(cm,k=13)
        for i in a2:
            y.add_row(i)
            f.write(str(i)+'\n')
    elif 21<pass_count<60:
        a3=random.sample(cm,k=25)
        for i in a3:
            y.add_row(i)
            f.write(str(i)+'\n')
    print(y)
    f.write('---------------------------------------------------------------------------------------'+'\n')
    f.close()
while True:
    print('---------------------------------------------------------------------------------------------')
    print("    MAIN MENU   ")
    print('---------------------------------------------------------------------------------------------')
    print("1.PASSENGER_DETAILS")
    print("2.PILOT_DETAILS   ")
    print("3.CREW MEMBER_DETAILS")
    print("4.FLIGHT SUMMARY")
    print("5. EXIT          ")
    choice=int(input("enter your choice:"))
    if choice==1:
        passenger()
    elif choice==2:
        pilot()
    elif choice==3:
        aircrew()
    elif choice==4:
        selection()
    elif choice==5:
        break
    else:
        print("invalid choice")

