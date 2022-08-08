#Utility Module ที่มีใน python
#ตัวแรก Date and time วันและเวลา
import datetime
from time import strftime

'''
datenow=datetime.datetime.now() #ดึงวันเวลาปัจจุบัน
print(datenow) #ปี/เดือน/วัน เวลา 
print(datenow.year) #ปี
formatdate=datetime.datetime(2022,8,8,1) #วัน/เดือน/ปี เวลา
print(formatdate)
'''

#จัดรูปแบบการแสดงผล
date=datetime.datetime.now()
print(date)
print(strftime("%x")) #"%x" คือ mm/dd/yy
print(strftime("%X")) #"%X" คือ time 20:58:00
print(strftime("%c")) #"%c" คือ Mon Aug (day) 20:59:09 2022
print(strftime("%A:%B:%Y")) #วัน/เดือน/ปี ***

#ทำงานวันที่เท่าไรของปี
print(strftime("%j"))

#date
print(strftime("%a"))#Mon แบบสั้น
print(strftime("%A"))#Monday แบบยาว
print(strftime("%b")) #เดือน แบบสั้น

