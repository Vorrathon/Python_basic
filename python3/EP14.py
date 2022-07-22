#คำสั่ง pass คือ การผ่านสิ่งที่ต้องทำไปก่อนไม่ต้องระบุ
wallet = 10000 
money = int(input("กรุณากดเงินที่ต้องการ"))
if money <= wallet:
    print("สามารถกดเงินได้")
    tatol = wallet - money
    print("ยอดเงินคงเหลือ",tatol)
elif money > wallet :
    pass
else:
    print("กรอกข้อมูลให้ถูกต้อง")
print("จบโปรแกรม")


