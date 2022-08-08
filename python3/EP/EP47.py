#ลบ text 
import os #จัดการเกี่ยวกับไฟล์ที่อยู่
try:
    if os.path.exists("student.txt"): #ถ้าเจอไฟล์นี้
        os.remove("student.txt")
        print("ลบข้อมูลเรียบร้อย")
    else :
        print("ไม่พบไฟล์")
except Exception as e:
    print(e)