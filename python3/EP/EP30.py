#argument

def add(x,y,z):
    print(x+y+z)


#กรณีส่ง argument หลายตัวแต่ parameter มีจำกัด
def addnew(*agrs):
    print("ผลรวมคือ",agrs[0]+agrs[1]) #เป็น tuple ระบุindex
addnew(0,4)

#กรณีบวกหลายตัว
def addloop(*agrs): #agrs เปลี่ยนชื่อได้
    sum=0
    for item in agrs:
        sum+=item
    print("ผลรวมคือ",sum)


addloop(5,6,7,9)
addloop(44,33)

