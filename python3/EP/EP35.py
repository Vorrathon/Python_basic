#return
def randomNum(x):
    if len(x) < 3 : 
        print("กรุณาใส่ตัวเลขสามหลัก")
        return   #คำสั่งกระโดดออกจาก function
    if x =="100":
        print("ถูกรางวัล")
        return 2000
    else:   
        print("เสียใจด้วย")
        return 0
money=randomNum("22")
print("เงินรางวัล",money)

