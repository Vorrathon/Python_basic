#โปรแกรมหลัก เตรียมใช้ module
#Package คือการนำ package วิธีเรียกใช้
#Package.module.function
from myPackage.CalculateService  import addition #as cal  #ดึงไฟล์ module ที่สร้างไว้จากข้างนอก  *as การตั้งชื่อเล่นให้กับ Module
from myPackage.weather import city

print(city)
addition(4,5)
# CalculateService.addition(5,6,7) #เรียกใช้module.ฟังก์ชั่นที่สร้างไว้()
# CalculateService.minus(5,2)
# CalculateService.PI #เรียกตัวแปร
# print(CalculateService.PI)
# print(weather.city["กำแพงเพชร"]) #เรียกใช้ keyของกำแพงเพชรจาก module weather.py
# weather.getweather() #แสดง dict ของ weather ทั้งหมด
# cCalculateServiceal.Power(5,2)

# #ดึง fuction ใน module แบบเจาะจง
# from CalculateService import addition
# from CalculateService import PI
# from weather import city
# from CalculateService import *  #นำ ทั้ง function และ ตัวแปรมาทั้งหมด
# #เรียกใช้ function ได้เลย ไม่ต้องพิมพ์ module.fucntion
# addition(5,6)
# print(PI)
# print(city["ชลบุรี"])