# ค้นหาเบอร์โทร
data = {"191":"เหตุด่วน","1669":"โรงบาล","1001":"ดับเพลิง"}
def searchNum(message):
    for key, value in data.items():
        if value == message:
            print("เบอร์ติดต่อ=",key)
      
message=input("ป้อนข้อมูล ")
searchNum(message)
