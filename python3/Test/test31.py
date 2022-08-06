#fucntion หาตัวพิมพ์เล็ก พิมใหญ่กี่ตัว
def checkString(msg):
    result={"UPPER":0,"LOWER":0}
    for char in msg:
        if char.isupper():
            result["UPPER"]=result["UPPER"]+1
        elif char.islower():
            result["LOWER"]=result["LOWER"]+1
        else:
            pass
    return result
msg = input("ป้อนข้อความ")
x=checkString(msg)
print(x)