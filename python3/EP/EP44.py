
# try exception ด้วย raise
# กำหนดกฏ ที่จะทำให้เกิดข้อผิดพลาดด้วยตนเอง
while True:
    try:
        name=input("ป้อนชื่อผู้ใช้โปแกรม: ")
        if name =="Vorrathon":
            raise Exception("มีชื่อนี้ในระบบแล้ว")
        Number1 = int(input("ป้อนเลข1: "))
        Number2 = int(input("ป้อนเลข2: "))
        if Number1 == 0 and Number2 == 0:
            break
        if Number1 < 0 or Number2 < 0:
            raise Exception("ห้ามป้อนตัวเลขติดลบ") #เขียนกฏดักจับข้อผิดพลาดขึ้นเอง
       
        result = Number1/Number2
        print("ผลลัพธ์คือ", result)
    except ZeroDivisionError:
        print("ตัวหารห้ามเป็นเลข 0")
    except ValueError:
        print("กรุณาป้อนตัวเลข")
    finally:
        print("ทำงานต่อ...")
