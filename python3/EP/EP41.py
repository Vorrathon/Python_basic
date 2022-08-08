#EXceotion การดักจับข้อผิดพลาด

'''
tyy: 
    รันคำสั่งปกติ
except
    คำสั่งที่ทำงานตอนรันมีข้อผิดพลาด

'''
'''
try:
    number1 = int(input("ป้อนตัวเลข:"))
    number2 = int(input("ป้อนตัวเลข:"))
    sum = number1/number2
    print(sum)
except:
    print("โปรแกรมมีข้อผิดพลาด")
'''
#Exception หลายเหตุการณ์
#valueError
#Zerodivision error 

'''
try:
    number1 = int(input("ป้อนตัวเลข:"))
    number2 = int(input("ป้อนตัวเลข:"))
    sum = number1/number2
    print(sum)
except ValueError:
    print("ERROR !! ป้อนตัวเลขจำนวนเต็มเท่านั้น")
except ZeroDivisionError:
    print("ERROR !! ตัวหารต้องไม่ใช้ 0")
'''


#Exception กรณีไม่รู้ชนิด error

try:
    number1 = int(input("ป้อนตัวเลข:"))
    number2 = int(input("ป้อนตัวเลข:"))
    sum = number1/number2
    print(sum)
    print("โอนเงิน")
except Exception as e :  #จะมี object ของ error เก็บไว้ที่ตัวแปร e
    print(e)
else:
    print("โอนเงินสำเร็จ")

 