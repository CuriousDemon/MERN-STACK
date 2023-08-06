from django.shortcuts import render,redirect
from django.http import HttpResponse
import mysql.connector as sql
from django.contrib import messages

# Create your views here.

def signup_page(request):
    if request.method == 'POST':
        mySql = sql.connect(host = 'localhost',user = 'root',password = '1234',database = 'website')
        cur = mySql.cursor()
        uname = request.POST.get('username')
        emailId = request.POST.get('emailId')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        # print(uname,emailId,pass1,pass2)
        if pass1 == pass2:
            quary = '''insert into user (username,emailId,password) values ('%s','%s','%s');'''%(uname,emailId,pass1)
            cur.execute(quary)
            mySql.commit()
            return redirect("/")
        else:
            messages.warning(request, "Your Username and Password is wrong")
            return redirect("/")
    return render(request,'Sign_Up.html')

name = ''
email = ''
id = 0
def signin_page(request):
    if request.method == 'POST':
        mySql = sql.connect(host = 'localhost',user = 'root',password = '1234',database = 'website')
        cur = mySql.cursor()
        uname = request.POST.get('username')
        password = request.POST.get('password')
        quary = '''select * from user where username = '%s' and password = '%s';'''%(uname,password)
        cur.execute(quary)
        msg = cur.fetchall()
        if msg != []:
            global name,email,id
            for value in msg:
                for index,val in enumerate(value):
                    if index == 0:
                        id = val
                    if index == 1:
                        name = val
                    if index == 2:
                        email = val
        #     return render(request,'dashboard.html', {
        #     'name': name,
        #     'email': email,
        # })   
            return redirect("/signin/dashboard/")  
        else:
            messages.warning(request, "Your Username and Password is wrong")
            return redirect("/signin/")
    return render(request,'Sign_In.html')

def dashboard(request):
    if request.method == 'POST':
        global id
        mySql = sql.connect(host = 'localhost',user = 'root',password = '1234',database = 'website')
        cur = mySql.cursor()
        sname = request.POST.get('sitename')
        password = request.POST.get('password')
        open = request.POST.get('open')
        quary = '''insert into passmanager (site_name,password,Id) values ('%s','%s',%d);'''%(sname,password,id)
        cur.execute(quary)
        mySql.commit()
        return redirect("/signin/dashboard/")
    return render(request,'dashboard.html', {
            'name': name,
            'email': email,
        })


def manager(request):
    global id
    print(id)
    mySql = sql.connect(host = 'localhost',user = 'root',password = '1234',database = 'website')
    cur = mySql.cursor()
    quary = '''select site_name,passmanager.password from user right join passmanager on user.id = passmanager.Id where user.id = %d;'''%(id)
    cur.execute(quary)
    msg = cur.fetchall()
    print(msg)
    return render(request,'notemanager.html', {
        'list':msg
    })