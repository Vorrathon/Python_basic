#โปรแกรมบัญชีธนาคาร
#data 

account ={"นายA":5000,"นายB":0} 

def getBalance():#fucntion ดูยอดเงิน
    print("ยอดเงินคงเหลือ: ",account)   

def deposit(money):  #fucntion ฝากเงิน
    if money <= 0  or type(money) is float:
        raise Exception ("ป้อนตัวเลขเป็นบวกเท่านั้น")
    print("ฝากเงินเข้าบัญชี นาย A",money)
    account["นายA"]+=money

def withdraw(money): #fucntion ถอดเงิน
    if money > account["นายA"] :
        raise Exception ("ยอดเงินไม่เพียงพอ")
    if money <= 0 or type(money) is float :
        raise Exception ("ป้อนตัวเลขเป็นบวกเท่านั้น")
    print("ถอดเงินจากบัญชี A",money)
    account["นายA"]-=money

def transferAtoB(money): #fucntion โอนเงิน
    if money > account["นายA"]:
        raise Exception ("ยอดเงินไม่เพียงพอ")
    if money <= 0 :
        raise Exception ("ป้อนตัวเลขเป็นบวกเท่านั้น")
    print("โอนเงินเข้าบัญชีนาย B",money)
    account["นายA"]-=money
    account["นายB"]+=money

try:
    getBalance() #ดูยอดเงินใน account รอบ1
    deposit(500) #ฝากเงิน 500
    getBalance() #ดูยอดเงินรอบ 2 
    withdraw(50)#ถอดเงินรอบ
    getBalance()#ดูยอดเงินรอบ 3 
    transferAtoB(1) #Aโอนเงินให้ B
    getBalance()#ดูยอดเงินรอบ 4
except Exception as e: #แสดงกฏที่เขียนไว้ใน เงื่อนไข
    print(e)



