#!C:\Program Files\Python38\python.exe
import cgi, cgitb, pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["LabEquipmentRentalDB"]
mycol = mydb["LoanRecord"]

print("Content-type:text/html\r\n")

form = cgi.FieldStorage()
name2 = form.getvalue('name2')

mydict = { 
    "狀態" : "租借中",
    "借用人" : name2,
    "財物編號" : "1015",
    "財物名稱" : "測試物件-2",
    "廠牌" : "none",
    "型式" : "none",
    "財物條碼" : "999999991015" 
}


x = mycol.insert_one(mydict)
print(x.inserted_id)
