#keyword agrument
def displayData(fname,lname,city):
    print("ชื่อ",fname)
    print("นามสกุล",lname)
    print("จังหวัด",city)
displayData("alonemanz","solo","กำแพงเพชร") #การแสดงผลจะเรียงลำดับตาม parameter

#กรณีที่กรอกข้อมูลไม่เรียงลำดับ แต่การแสดงผลนั้นต้องทำให้ถูกต้อง ต้องระบุ parameter ="argument" 
displayData(city="กรุงเทพ",lname="Kedpratoom",fname="Vorrathon")