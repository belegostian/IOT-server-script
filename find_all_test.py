#!C:\Program Files\Python38\python.exe
import cgi, cgitb, pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["LabEquipmentRentalDB"]
mycol = mydb["LoanRecord"]

print("Content-type:text/html\r\n")

mydoc = mycol.find()
for x in mydoc:
      print("<p>")
      print(x)
      print("</p>")
