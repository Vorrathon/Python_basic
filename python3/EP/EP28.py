#การส่ง-รับค่าเข้ามาที่ function
'''
def myData(name): #nameเรียกว่า parameter รับ
    print("Hello",name) #แสดง
myData("Vorrathon") #=> จะส่งVorrathon ไปที่ตัวแปร name
myData("Chakrit")
myData(5)
'''
def fullname(fname,lname,age):
    print("สวัสดี",fname,"นามสกุล",lname,age)

fullname("Vorraton","Kedpratoom",26)
fullname("Panyapon","Puttachat",24)

fname = "alonemanz"
lname = "captain"
age = 32
fullname(fname,lname,age)