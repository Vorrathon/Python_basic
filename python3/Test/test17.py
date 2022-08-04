# เกมส์ทายลูกเต๋า
# ลูกเต๋ามี 1,2,3,4,5,6
import random  # คือการนำfuntion randam มาทำงาน
myRandom = random.randrange(1, 7)  # ทำการ randomเลขในช่วง 1-6
# print(myRandom)
# สุ่มตัวเลขลูกเต๋า

i=1
while True:
    number = int(input("ป้อนตัวเลข"))
    correct = number == myRandom
    wrong = number < 1 or number > 6
    miss = number != myRandom 
    if correct :
        print("ถูกต้องนะครับ เฉลย",myRandom)
        break
    elif wrong :
        print("ใส่ตัวเลขให้ถูกต้อง")
    if miss != wrong :
        if number > myRandom:
            print("น้อยกว่า")
        elif number < myRandom :
            print("มากกว่า")
    if i == 3 :
        print("เสียใจด้วย") 
        break
    i=i+1


        
   
     
       
