#Attibute and Method
class Employee:  
    #สร้าง Method พฤติกรรม
    def detail(self,name,salary,department):
        #สร้าง attibute
        self.name= name
        self.salary=salary
        self.departmnet=department
        # print("กำหนด attibute เรียบร้อย")
    def showdata(self):
        print("ชื่อพนักงาน = {}".format(self.name))#เรียกใช้ attibute
        print("เงินเดือน = {}".format(self.salary))
        print("แผนก = {}".format(self.departmnet))


obj1 = Employee()
obj1.detail("Vorrathon",15000,"โปรแกรมเมอร์") #เรียกใช้ method

obj2 = Employee()
obj2.detail("Amonteap",3000,"Grabfood")

obj3 = Employee()
obj3.detail("Panyapon",50000,"PHP Deverloper")

obj1.showdata() #แสดงข้อมูลคนที่หนึ่ง


