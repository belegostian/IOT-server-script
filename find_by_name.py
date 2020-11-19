#!C:\Program Files\Python38\python.exe
import cgi, cgitb, pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["LabEquipmentRentalDB"]
mycol = mydb["LoanRecord"]


print("Content-type:text/html\r\n")
print("Charset:UTF-8\r\n")

form = cgi.FieldStorage()
name = form.getvalue('name')

myquery = { "借用人" : name }
mydoc = mycol.find(myquery)

for x in mydoc:
      print("<p>")
      print(x)
      print("</p>")