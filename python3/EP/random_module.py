import random #ฟังก์ชั่นสุ่ม
x = random.random() #สุ่ม 0.0-1.0
data =["Vorathon","kong","not","alonemanz"]
'''
for i in range(15):
    x = random.uniform(5,10)  #สุ่ม 10 รอบในช่วง 5 - 10
    y = random.randrange(1,10,1) #สุ่มตัวเลขแบบจำนวนเต็ม 1 ก่อนถึง 10 เพิ่มที่ละ1
    z = random.randint(1,15) #สุ่มตัวเลขแบบจำนวนเต็ม 1 ถึง 10 เพิ่มที่ละ1
    print(z)
'''
for i in range(3):
    # data = random.choice(data) #สุ่มใน list
    random.shuffle(data) #สุ่มสลับที่ใน list
    print(data)
