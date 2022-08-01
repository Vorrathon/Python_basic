#โปรแกรมตารางหมาก
"""
ตารางหมาก คือ 8*8
"""
for row in range(8):
    for column in range(8):
        if (row+column)%2 == 0:
            print("x",end="")
        elif (row+column)%2 != 0:
            print("o",end="")
    print("")
