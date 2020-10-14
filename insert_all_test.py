#!C:\Program Files\Python38\python.exe
# -*- coding: utf-8 -*-
import cgi, cgitb, pymongo
import sys, io, pip

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["LabEquipmentRentalDB"]
mycol = mydb["LoanRecord"]

mylist = [
  { "狀態" : "租借中",
    "借用人" : "Yanhow",
    "財物編號" : "1014",
    "財物名稱" : "測試物件",
    "廠牌" : "none",
    "型式" : "none",
    "財物條碼" : "999999991014"},
  { "狀態" : "租借中",
    "借用人" : "Yanhow",
    "財物編號" : "1014-2",
    "財物名稱" : "測試物件-2",
    "廠牌" : "none",
    "型式" : "none",
    "財物條碼" : "999999991014"}
]

x = mycol.insert_many(mylist)

print(x.inserted_ids)
