#เขียนโปรแกรมเปรียบเทียบตัวเลขมากหรือน้อย
a = int(input("ป้อนตัวเลขตัวที่1:"))
b = int(input("ป้อนตัวเลขตัวที่2:"))
if a > b :
    print("ตัวเลข",a,"มีค่ามากกว่า",b)
elif b>a :
    print("ตัวเลข",a,"มีค่าน้อยกว่า",b)
else:
    print("ตัวเลขทั้งสองเท่ากัน")
print("END PROGRAM")