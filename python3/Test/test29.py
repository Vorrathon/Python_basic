#ฟีโบนัสชี คือ 0,1,1,2,3,5,8,13
#เอาเลขหน้าสองตัวบวก กันแล้วจับคู่บวกกันต่อไปเรื่อยๆ
def fibo(number):
    if number <= 1:
        return number
    else:
       return fibo(number-1)+fibo(number-2)

for i in range(5) :#0-4
    print(fibo(i))

'''
number = 0 =>0
number = 1 =>1
number = 2 ตำแหน่ง fibo(2-1)+fibo(2-2) =>1
number = 3 ตำแหน่ง fibo(3-1)+fibo(3-2) =>2
number = 4 ตำแหน่ง fibo(4-1)+fibo(4-2) =>3

ค่า 0,1,1,2,3
'''