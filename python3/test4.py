# โปรแกรมแลกเงินและหาจำนวนแบงค์
number = int(input("ป้อนจำนวนเงินของคุณ"))
if number >= 1000:
    # หารปัดเศษออกไปเพื่อหาจำนวนแบงค์
    print("ได้ 1000 บาท", number//1000, "ใบ")
    # ทำการ mod เพื่อหาเศษเงินที่เหลือจากนั้นนำเอาไปเช็คเงื่อนไขต่อไปว่าตรงกับข้อใด
    number = number % 1000
if number >= 500:
    print("ได้ 500 บาท", number//500, "ใบ")
    number = number % 500
if number >= 100:
    print("ได้ 100 บาท", number//100, "ใบ")
    number = number % 100 
if number >= 50:
    print("ได้ 50 บาท", number//50, "ใบ")
    number = number % 50
if number >= 20:
    print("ได้ 20 บาท", number//20, "ใบ")
    number = number % 20
