#break and continue
'''
i = 0
while i <= 10 :
    i=i+1
    if i == 9 :
        continue  #ข้ามรอบที่ 9
    print("รอบที่",i)
''' 
#แสดงเลขคี่ 
'''
i = 0
while i<20 :
    i=i+1
    if i%2 == 0 :
        continue
    print(i)
'''
#แสดงเลขคู่
'''
i = 0
while i < 20 :
    i=i+1
    if i%2 != 0 :
        continue
    print(i)
print("จบโปรแกรม")
'''

#loop for
'''
for i in range(0,21):
    if i%2 == 0 :
        continue
    print("แสดงเลขคี่ ",i)
'''
#break
'''
i = 1
while i <= 10 :
    print("รอบที่ ",i)
    if i == 5 :
        break # หยุดการทำงานแล้วออกนอกลูป
    i=i+1 
print("จบโปรแกรม")
'''
for i in range(1,6):
    print("รอบที่",i)
    if i == 5 :
        break
print("จบโปรแกรม")
