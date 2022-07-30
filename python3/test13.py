#โปรแกรมตัวเลขแบบขั้นบรรได
last = int(input("ป้อนตัวเลข "))
for row in range(1,last+1):
    for column in range(1,row+1):
        print(column,end="") #end = การแสดงผลแนวรอบ
    print("")