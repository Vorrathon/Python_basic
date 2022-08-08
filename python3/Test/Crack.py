#รหัส ATM = 132
import random
ATM_PASS = "130739"
result ="" #เก็บผมลัพธ์
while result!=ATM_PASS:
    result=""
    for letter in range(len(ATM_PASS)):
        listNum=random.choice("0123456789")
        result="".join(listNum)+str(result)
        print("SEARCH...",result)
print("CRACK PASSWORD IS :",result)