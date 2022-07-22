#แปลงชนิดข้อมูล

x = 10 ; y=20 ; z="50"
result = x+y
result1 = x+int(z)  #การแปลงชนิดข้อมูลจาก string ไปเป็น 
result2 = str(x)+z #การแปลงชนิดข้อมูลจาก ing เป็น string
result3 = y + float(z) #แปลง string เป็น float
result4 = float(x)+y #แปลง int เป็น float แปลง float เป็น int
print(result)
print(result1)
print(result2) 
print(type(result2))
print(result3)
print(result4)