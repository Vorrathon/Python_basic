# Set คือ ข้อมูลในสมาชิกจะไม่ซ้ำกัน แก้ไขไม่ได้ถ้าสร้างไปแล้วไม่มี index ใช้สัญลักษณ์ {} ลำดับไม่แน่นอน
'''
# แบบปกติ
friut = {"มะม่วง", "มะขาม", "มะยม"}
# print(friut) #เรียงลำดับไม่ชัดเจน เข้าถึงแบบindex ไม่ได้

# สร้างแบบ constructor
# กรณีข้อมูลซ้ำจะแสดงข้อมูลแค่ตัวเดียว
fish = set(["ปลาดุก", "ปลานิล", "ปลานิล"])
'''
'''
#การเพิ่มข้อมูลใน set
myPC ={"CPU","RAM","GPU"}
myPC.add("SSD")
myPC.add("HDD") #เพิ่ม HDD SSD ลงใน myPC5555555าสดเสดาเดสาเสดาเสาสวกด
'''

#การเพิ่มสมาชิกใน set แบบหลายตัว
#เพิ่มแบบที่สอง
'''
lisPC = {"CASE","FAN","Mainbroad"} 
myPC.update(lisPC) 
#แบบสอง
myPC.update({"Mouse","Keybroad"}) 
'''

'''
#แสดงข้อมูลแบบ loop
for i in myPC:
    print("แสดงข้อมูล=>",i)
'''
#การนับจำนวนสมาชิก
'''
myPC ={"CPU","RAM","GPU","CASE","FAN","Mainbroad"}
#len คือการนับจำนวนสมาชิก
print(len(myPC)) 

#การ Check ค่าในสมาชิก
if "CP" in myPC:
    print("มีของ")
else:
    print("ไม่มีของ")
'''
#การลบข้อมูลใน set 






myPC ={"CPU","RAM","GPU","CASE","FAN","Mainbroad"}

print("ก่อนลบ",myPC)
#remove ลบข้อมูลใน set
myPC.remove("CPU") 
print("หลังลบ",myPC)

#Discard เป็นคำสั่งลบก็ต่อเมื่อไม่เจอข้อมูลใน set ก็จะไม่ ERROR
myPC.discard("GPU")
myPC.add("GPU 2060")
print("หลัง discard",myPC)

#หลบข้อมูลใน set ทั้งหมด 
myPC.clear()
print("หลังclear",myPC)

#คำสั่ง del ลบตัวแปรทิ้งเลย
del myPC 
print(myPC)

