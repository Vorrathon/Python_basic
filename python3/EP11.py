# โครงสร้างควบคุม (control structure)
'''
1.แบบลำดับ => ทำงานตามลำดับจากบนลงล่าง
2.แบบเลือก
3.แบบทำซ้ำ

#คำสั่ง if else
if boolean expreesion:
    statement

'''
'''
age = int(input("กรุณาป้อนอายุ:"))
if age >= 18:
    print("คุณบรรลุนิติภาวะแล้ว")
    print("จบโปรแกรม")
'''
# ตรวจคะแนน
'''
point = int(input("กรอกคะแนนของคุณ:"))
if point >= 50 :
    print("คุณสอบผ่าน")
else:
    print("คุณไม่ผ่าน")
print("จบโปรแกรม")
'''
# ดูเกรด if หลายอัน มันเช็คทุกเงื่อนไข
Grade = int(input("กรอกคะแนนของคุณ:"))
if Grade >79 and Grade <=100:
    print("คุณได้เกรด A")
elif Grade >=70:
    print("คุณได้เกรด B")
elif Grade >=60:
    print("คุณได้เกรด C")
elif Grade >=50:
    print("คุณได้เกรด D")
elif Grade < 50 and Grade >= 0 :
    print("คุณได้เกรด F")
else:
    print("กรอกข้อมูลให้ถูกต้อง")
print("จบโปรแกรม")
