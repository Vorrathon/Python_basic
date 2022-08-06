#function
#สาเหตุที่ต้องเขียน function คือการทำงานคำสั่งซ้ำๆ ให้อยู่ในกลุ่มๆเดียว
'''
a,b,c = 10,23,40 
if a%2==0:
    print("เลขคู่")
else :
    print("เลขคี่")
if b%2==0:
    print("เลขคู่")
else :
    print("เลขคี่")
if c%2 == 0:
    print("เลขคู่")
else:
    print("เลขคี่")
'''
#การสร้าง function และ เรียกใช้งาน function
'''
def ชื่อfunction():
    statement (คำสั่ง)
'''
def sayhi():
    print("Hello function")

def saygoodbye():
    print("Bye")

def name():
    print("vorrathon")

#ฟังก์ชั่น บวกเลข
def add1():
   num1=int(input("ป้อนตัวเลข1 ")); num2=int(input("ป้อนตัวเลข2 "))
   result = num1+num2
   print("คำตอบคือ",result)
    
#เรียกใช้งาน function
# add1()
for i in range(2):
    name()
 
    