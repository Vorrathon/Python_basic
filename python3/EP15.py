#เจาะลึก string
'''
name ="Vorrathon Kedpratoon 56"
print(name)
print(name[0]) #แสดงข้อความ string ใน arrayในลำดับที่ต้องการ
print(name[0:3])#แสดงก่อนถึงลำดับที่3
print(name[5:])#แสดงเริ่มต้นที่ 5 ถึงลำดับสุดท้าย
print(name[5:6])#แสดงลำดับที่5ก่อนถึงลำดับที่6
print(name[-1])#แสดงลำดับสุดท้ายคือใช้ -1 แสดงเลข 6
print(name[-2:])#แสดง 2 ตัวสุดท้ายคือ 56
print(name[-7:])

'''
#len fuction
'''
x = " Amonteap "
print(len(x)) #แสดงจำนวน string
print(x)
#strip คือการลบ ช่องว่าง string ซ้ายขวา
x.strip()
x=x.strip()
print(x)

y = " START "
print(len(y))
y=y.rstrip() #ลบช่องว่างทางขวา rstrip,lstrip ลบช่องว่าทางซ้าย
print(y)
'''

#แปลง case ของ string
'''
name = "vorrathon"
lname = "KEDPRATOOM"
print(name.upper()) #คำสั่งแปลง string เป็นตัวพิมพ์ใหญ่
print(lname.lower()) #คำสั่งแปลง string เป็นตัวพิมพ์เล็ก
print(name.capitalize())#แปลงตัวแรกสุดของ string เป็นตัวพิมพ์ใหญ่

'''
#คำสั่งแทนที่
'''
name = "Vorrathon"
grade = "Vorrathon เกรด 2 ชั้น ป.2 ชั้น 2"
print(name.replace("Vor","Thunder")) #คำสั่งแทนที่ข้อความเปลี่ยนจาก Vor เป็น Thunder
print(grade.replace("2","4",1)) #เพิ่ม parameter count(1) เพื่อ เปลี่ยนแค่จุดที่ต้องการในที่นี้เปลี่ยนตำแหน่งแรกสุด
'''
#คำสั่ง Check ข้อความ true or false
'''
name ="บาสไปหาสาวทุกวันตอนเย็น"
x = "บาส" in name  #คำสั่งเช็คว่า "บาส" มีอยู่ในตัวแปร name หรือป่าว
print(x)
if x :
    print(name.replace("บาส","โอ๊ต"))
'''
#การต่อ string (Concatinate)
'''
fname = "Vorrathon "
lname = "Kedpratoom"
age = " 26"
fullname = fname+lname+age #คำสั่งบวก คือคำสั่งที่ใช้ในการต่อ string แต่ถ้าเป็น int จะ Error
print(fullname)
print("ชื่อต้น "+fname+"นามสกุล "+lname+" อายุ"+age)
'''
#การจัดรูปแบบการแสดงผล {}
'''
fname = " Vorrathon "
lname = " Kedpratoom "
age = " 26 "
career = " Programmer "
salary = 15000.0035
text = "ชื่อ{1}นามสกุล{0}อายุ{2}อาชีพ{3}ที่อยู่{4}เงินเดือน {5:.2f}" #สามารถระบุตำแหน่งที่จะแทรกได้ {0} ตำแหน่งแรก #.2f คือแปลงตัวเลขเป็น float ทศนิยม 2 ตำแหน่ง
print(text.format(fname,lname,age,career," 82/4 ",salary)) #คำสั่ง format เป็นการนำค่าไป แทรกใน {} 
'''
#การนับจำนวน(count) คำ ใน ประโยค
'''
color = "ฉันชอบ สีน้ำเงิน ดำ เทา และ อารมณ์เทาๆ"
print(color.count("เทา")) #คำสั่ง count เป็นคำสั่งที่ใช้นับ
'''
#เช็คค่า ขึ้นต้น
'''
name ="นาย ปัญญาพล ชอบพาสาวกินข้าว"
text ="ปัญญาพล ไปแหละ"
print(name.startswith("นาย")) #คำสั่ง startswith เป็นคำสั่งที่ใช้ check ว่ามีคำขึ้นต้นที่เขียนไว้ใน function หรือป่าว แสดงผลเป็น boolean
if text.startswith("ปัญ") :
    print("ไปหาสาว")
else:
    print("ก็ไปหาสาวเหมือนกัน")
'''

#เช็คค่าลงท้าย
tabean = "กยค 204"
if tabean.endswith("204"): #คำสั่ง endswith เป็นคำสั่งที่ใช้ check ว่ามีคำขึ้นต้นที่เขียนไว้ใน function หรือป่าว แสดงผลเป็น boolean
    print("รถโดนขโมย")
else :
    print("รถอยู่ดี")


