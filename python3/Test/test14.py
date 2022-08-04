#โปรแกรมวาดสี่เหลี่ยม จตุรัส
'''
4*4
xxxx
xxxx
xxxx

5*5
xxxxx
xxxxx
xxxxx
xxxxx
xxxxx
'''
number = int(input("ป้อนขนาด = ")) # 5 => 0,1,2,3,4
for row in range(number):
    for column in range(number):
        print("x",end="")
    print("") #จบ 1 รอบใน loop column แล้วขึ้นบรรทัดใหม่ใน Loop Row
   
