#!C:\Program Files\Python38\python.exe
#-*- coding: utf-8 -*-
import cgi, cgitb
import pymongo, json
import codecs, sys 
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["LabEquipmentRentalDB"]
mycol = mydb["LoanRecord"]

print("Content-type:text/html\r\n")

mydoc = mycol.find()
for x in mydoc:
      print("<p>")
      print(x)
      print("</p>")