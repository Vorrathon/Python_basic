#โปรแกรมหาผลรวมตัวเลขค่าเฉลี่ยแบบปรับเงื่อนไข
sum = 0
while sum < 100:
    number=int(input("ป้อนตัวเลข"))
    sum=number+sum
    print("ผลรวมเท่ากับ ",sum)
