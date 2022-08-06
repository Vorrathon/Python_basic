#การสร้าง function แบบ return ค่า
'''
มีสามแบบ
1.ไม่มีการรับค่าและส่งค่า
def name():
2.มีการรับค่าเข้าไปทำงาน
def name(a,b):

3.รับค่าเข้าไปทำงานและ ส่งออกมา
def name(a,b):
    return  a+b

4.ไม่มีการรับค่าแต่ส่งค่าไป
def name()
    return value
'''
'''
def add(a,b):
   return a+b #ส่งค่าไปใช้ด้านนอกfunction
x=(add(10,20)) #return กลับมาเก็บที่ตัวแปร x
print(x)

def showNumber():
    return 500
x=showNumber()
print(x)
'''
def randomNum(x):
    if x == '100':
        print("ถูกหวย")
        return 1000
    else :
        print("ไม่ถูกหวย")
        return 0

money=randomNum("100") 
y = 300
result=money-y
print("เงินรางวัล",money,"บาท") 
print("เงินเหลือ",result,"บาท")
