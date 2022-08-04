#โปรแกรมหาค่ามากที่สุด น้อยสุด ผลรวม และค่าเฉลี่ย
from audioop import avg
from tkinter import N


number=[]
i=0
while True :
    x=int(input("ป้อนตัวเลข"))
    if x < 0 :
        break
    i=i+1
    print("รอบที่",i)
    number.append(x)

print(number)
print("ตัวเลขที่น้อยที่สุด",min(number)) #หาตัวเลขที่น้อยที่สุด
print("ตัวเลขที่มากที่สุด",max(number)) #หาตัวเลขที่มีค่ามากที่สุด
print("ผลรวมคือ",sum(number)) #หาผลรวม
avg = sum(number)/i
print("ค่าเฉลี่ยคือ",avg)#หาค่าเฉลี่ย
print("จบโปรแกรม")
    