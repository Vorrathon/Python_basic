#try exception with while\
while True:
    try :
        Number1=int(input("ป้อนเลข1: "))
        Number2=int(input("ป้อนเลข2: "))
        if Number1 ==0 and Number2 == 0 :
            break
        result = Number1/Number2
        print("ผลลัพธ์คือ",result)
    except ZeroDivisionError:
        print("ตัวหารห้ามเป็นเลข 0")
    except ValueError:
        print("กรุณาป้อนตัวเลข")
    finally:
        print("ทำงานต่อ...")
