#Constructor และ Destructor

#การสร้าง Constructor

class Employee:

    def __init__(self,fname,lname,carrier):  #เป็นคำสั่งเมื่อเราสร้างวัตถุแล้วมันจะ default 
        self.fname = fname
        self.lname = lname
        self.carrier = carrier
    

    def showdata(self):
        print("ชื่อ:{}".format(self.fname))
        print("นามสกุล:{}".format(self.lname))
        print("อาชีพ:{}".format(self.carrier))

    def __del__(self):
        print("Call Destructor")  #เรียกใช้เพื่อคืนค่าให้คืนความจำหลังใช้งานวัตถุ

#สร้าง วัตถุ
obj2 = Employee("Vorrathon","Kedpratoom","Programmer") #=>construc สามารถใส่ค่าในวงเล็บได้เลย
obj2.lname = "AloneManZ" #ปรับเปลี่ยนค่าได้
obj2.showdata()

