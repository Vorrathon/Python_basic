#if ซ้อน if
#เช็คระดับนักเรียน
age = int(input("ป้อนอายุ"))
if age < 16 and age >= 13 :
    print("อายุ",age,"อยู่มัธยมต้น")
    if age == 15 :
        print("ม.3")
    elif age == 14 :
        print("ม.2")
    elif age == 13 :
        print("ม.1")
elif age > 15 and age<=18 :
    print("มัธยมปลาย")
    if age == 16 :
        print("ม.4")
    elif age == 17 :
        print("ม.5")
    elif age == 18 :
        print("ม.6")
elif age < 13 :
    print("ประถม")
else :
    print("ผู้ใหญ่")
print("จบโปรแกรม")
