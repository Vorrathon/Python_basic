#**Kwargs


# *args

def add(*number): #รับค่าจาก  argument ได้แบบไม่จำกัด
    sum=0
    for i in range(len(number)):
        sum=sum+number[i]
    print(sum)       


# **kwargs
def displayData(**kwargs): #รับค่า arument แบบที่ต้องการได้ทีหลัง โดยข้อมูลจะแสดงแบบ dict
    print(kwargs["fname"]) #ระบุ key เพื่อเจาะจงส่งที่แสดง
displayData(fname="Vorrathob",lname="Kedpratoom")
displayData(fname="Panyapon",lname="Putachar",age="24")
displayData(fname="Chakirt",lname="Wongkomta",age="24",status="มีลูก")