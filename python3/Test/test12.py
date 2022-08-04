#โปรแกรมค้นหาตัวเลขมากสุดน้อยสุด
max,min = 0,999
while True :
    number = int(input("ป้อนตัวเลขของคุณ "))
    if number < 0:
        break
    if number > max :
       max = number
    if number < min :
       min = number
print("ค่าสูงสุด ",max)
print("ค่าต่ำสุด ",min)
