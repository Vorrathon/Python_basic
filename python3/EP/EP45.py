import os
#จัดการ ไฟล์ ในภาษา Python
#อ่าน text file
#open("ชื่อไฟล์","โหมด","เข้ารหัส")   **โหมด read,write,read and write  
os.chdir(r"C:\Users\AloneManZ\Desktop\Trainprogrammer\python3")
try:
    fr=open("student.txt","r",encoding="utf-8")   #encoding="utf-8" คือการเข้ารหัสให้อ่านภาษาไทยได้
    print(fr.read()) #.read(5) อ่านข้อความใน fr  พร้อมระบุตัวอักษรที่จะอ่าน
except FileNotFoundError:
    print("หาไฟล์ไม่เจอ")
