#lambda function
#โครงสร้าง
'''
lambda argument : expression
'''
'''
x=lambda name:name  #xก็คือ ชื่อ funtion
print(x("vorrathon"))

sum =lambda x,y: x+y 
print(sum(1,2))

mutiply=lambda a,b: a*b
print(mutiply(5,3))

def myPower(p):
    return p*p
result=myPower(5)
print(result)

'''

def Power(x): #ตัวเลข
    return lambda a : x**a # aคือเลขชี้กำลัง
y = Power(5) #ตัวเลข
result=y(2)  #คือเลขชี้กำลัง
print(result)


