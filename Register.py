#!C:\Program Files\Python38\python.exe
#-*- coding: utf-8 -*-
import cgi, cgitb
import pymongo, json
import codecs, sys 
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["LabEquipmentRentalDB"]
mycol = mydb["UserList"]


print("Content-type:text/html\r\n")

form = cgi.FieldStorage()
name = form.getvalue('name')
affiliatedUnit = form.getvalue('affiliatedUnit')
email = form.getvalue('email')
phoneNum = form.getvalue('phoneNum')
account = form.getvalue('account')
password = form.getvalue('password')
password2 = form.getvalue('password2')

if (password != password2):
    print(0)
else:
    mydict = { 
    "聯絡人" : name,
    "所屬單位" : affiliatedUnit,
    "聯絡信箱" : email,
    "聯絡電話" : phoneNum,
    "帳戶名稱" : account,
    "密碼" : password,
    "身份" : "user" 
    }
    x = mycol.insert_one(mydict)
    print(x.inserted_id)