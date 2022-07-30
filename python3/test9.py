#โปรแกรมแม่สูตรคูณ
'''
x = int(input("ใส่แม่สูตรคูณ "))
for i in range(1,13):
    result = x*i
    print("ผลคูณแม่",x,"x",i,"คือ",result)
'''
start = int(input("ใส่แม่สูตรคูณเริ่มต้น"))
end = int(input("ใส่แม่สูตรคูณตัวท้าย"))
for x in range(start,end+1):
    print("แม่สูตรคูณแม่",x)
    for y in range(1,13):
        print(x,"x",y,"=",x*y)