#ฟังก์ชั่นหาผลรวม และ ค่าเฉลี่ย
def sum(number):
    total=0
    avg = 0
    for i in number :
        total=total+i 
    avg =total/len(number)
    return total,avg

x =[1,2,3,4,5,6,7,8,9]
y,z=sum(x)

print(y)
print(z)