#factorial
#5! = 5*4*3*2*1
def fact(number):
    if number == 1:
        return number
    else:
        return number*fact(number-1)
result = fact(5)
print(result) 


#ขั้นตอนการทำงานย 
'''
#fact(3) 
   ขั้นแรก 5*(5-1) = 5*4 returnไป number *fact(4)  =>20
   สอง   4*(4-1) = 4*3 returnไป number *fact(3) =>20*3=>60
   สาม   3*(3-1) = 3*2 returnไป number *fact(2) =>60*2=>120
   สี่     2*(2-1) = 2*1 returnไป number *fact(1)  =>120*1 =120 หยุด
   
'''
