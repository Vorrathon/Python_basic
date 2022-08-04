#Loop for
#for in range(start,stop,step) #range เป็นการกำหนดรอบ
'''
for i in range(1,6,2): #ค่า range จะเริ่มต้นที่ 0 1 2  (ค่าเริ่มต้น,ค่าสุดท้าย-1,บวกเพิ่มจำนวนรอบ)
'''
#ผลรวมตัวตัวเลข และ หาค่าเฉลี่ย
'''
sum = 0
for i in range(11): #0+1+2+3+4+5+6+7+8+9+10 
    sum = (i)+ sum
    print("รอบที่ ",i,"ผลรวม ",sum)

avg = sum/i
print(sum)
print("ค่าเฉลี่ยคือ ",format(avg,'.2f'))


for i in range(-10,1): #เริ่มค่าติดลบได้
    print(i)
'''
for i in range(10,0,-1): #ลดค่าตรง step ได้ตามที่กำหนด
    print(i)