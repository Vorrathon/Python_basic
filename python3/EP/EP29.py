#argument and parameter
#อาส่ง-พารับ

#argument คือ ค่าที่เราส่งไปใน function
#parameter คือ ตัวแปรที่รับมาเพื่อทำงานใน function ที่รับมาจาก argument

def myData(a,b,c): #=> เรียกว่า parameter ตัวแปรที่รอรับค่า มี 3 ค่า a,b,c
    print("สวัสดี",a,b,"อายุ",c) #=>แสดงค่า parameter ที่ได้รับจาก argument
fname= "vorrathon"
lname="kedpratoom"
age = 26 

myData(fname,lname,age) #คือ argument ที่ส่งค่าไปให้ parameter รับค่าในฟังก์ชั่น 

def addition(a,b):
    print("ผลลัพธ์คือ",a+b)
x=50
y=50
addition(5,9)
addition(x,y)
