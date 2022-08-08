#Finally ทำงานต่อแบบไม่สนแม้มี error
try:
    number1 = int(input("ป้อนตัวเลข:"))
    number2 = int(input("ป้อนตัวเลข:"))
    sum = number1/number2
    print(sum)
    print("โอนเงิน")
except Exception as e :  #จะมี object ของ error เก็บไว้ที่ตัวแปร e
    print(e)
finally :
    print("ไม่สนทำงานต่อ")