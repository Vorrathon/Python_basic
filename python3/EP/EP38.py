#Recursive Function เรียกใช้ function ตัวเอง
# def addNum(number):
    
#     if number == 5 :
#         return
#     print(number+1)
#     number+=1
#     addNum(number)
# addNum(0)

def sum(Num):
    if Num == 1:
        return Num
    else:
        return Num+sum(Num-1)

x=sum(5) #5+4+3+2+1
print(x)



