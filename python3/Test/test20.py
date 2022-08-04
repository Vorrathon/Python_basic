#โปรแกรมหากลุ่มเลขคี่เลขคู่
number=[]
odd=[] #เลขคี่
even=[] #เลขคู่
while True:
    x=int(input("ป้อนตัวเลข"))
    if x < 0 :
        break
    number.append(x)
    if x % 2 == 0:
        even.append(x)
    if x % 2 != 0:
        odd.append(x)
print("แสดงทั้งหมด",number)
print("เลขคี่",odd)
print("เลขคู่",even)