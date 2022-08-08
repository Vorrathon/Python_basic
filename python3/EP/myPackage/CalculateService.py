#กลุ่มคำสั่งสำหรับคำนวณ
#ให้บริการคำนวณและค่าคง
PI = 3.14 
def addition(*args):
    total = 0
    for i in range(len(args)): #เก็บลำดับ
        total+=args[i] #เก็บค่า
    print("ผลบวกเท่ากับ:",total)

def minus(x,y):
    print("ผลลบคือ:",x-y)

def Power(number,n):
    print("ผลการยกกำลัง:",number**n)
