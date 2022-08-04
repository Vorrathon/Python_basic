#โปรแกรมจับคู่สินค้าและราคา
product = ["CPU","RAM","GPU"]
price =[15000,3000,25000]
for x,y in zip(product,price): #คำสั่ง zip คือการจับคู่ list แบบ 1ต่อ1
    print("สินค้า",x,"มีราคา",y)

    
'''
for x,y in zip(product,price[::-1]):
     print("สินค้า",x,"มีราคา",y)

'''
