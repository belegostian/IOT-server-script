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
account = form.getvalue('account')
password = form.getvalue('password')

myquery = { "帳戶名稱" : account, "密碼" : password }
mydoc = mycol.find_one(myquery)
print(mydoc['聯絡人'])