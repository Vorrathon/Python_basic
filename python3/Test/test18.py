#โปรแกรมเรียงรับลำดับตัวเลข
number=[]
while True:
    x= int(input("ป้อนตัวเลขของคุณ"))
    if x < 0 :
        break 
    number.append(x);
print("ก่อนเรียง",number);
number.sort() #ทำการเรียงลำดับจาก น้อยไปมาก
print("เรียงน้อยไปมาก",number)
number.reverse()
print("เรียงมากไปน้อย",number) #ทำการเรียงลำดับจาก มากไปน้อย
print("จบโปรแกรม")
    