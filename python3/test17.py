# เกมส์ทายลูกเต๋า
# ลูกเต๋ามี 1,2,3,4,5,6
from bdb import Breakpoint
import random  # คือการนำfuntion randam มาทำงาน
myRandom = random.randrange(1, 7)  # ทำการ randomเลขในช่วง 1-6
# print(myRandom)
# สุ่มตัวเลขลูกเต๋า
i=1
while True:
    number = int(input("ป้อนตัวเลข"))
    if number == myRandom:
        print("คุณคือผู้โชคดี")
        print("จบโปรแกรม")
        break
    if  i==3:
        number == myRandom
        break
    elif number != myRandom or i==3:
        print("เสียใจด้วย")
        print("เฉลย", myRandom)

    
       
