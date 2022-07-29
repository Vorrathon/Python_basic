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
'''
y = " START "
print(len(y))
y=y.rstrip() #ลบช่องว่างทางขวา rstrip,lstrip ลบช่องว่าทางซ้าย
print(y)
