#Non-Primitive 
#list สามารถเก็บชนิดข้อมูลได้หลายชนิด

'''
fill=[] #list ว่าง
number=[1,2,3,4,5,6] #list number มีสมาชิกสองตัว คือ 1กับ2
name=["Mr.Vorrathon","Mr.Charkirt","Mr.Panyapon"] #เก็บ string
all=[10,"นาง",4.66,-70,False]#เก็บ type
alldata=list([10,"นาย",3.14,-50,True])
'''
#construtor คือการประกาศ รูปแบบ list
'''
print(name)
print(alldata)
print(all)
print(type(alldata))
print(type(all))
'''

#การเข้าถึงข้อมูลสมาชิกแต่ละตัวใน list
'''
print(name[0]) #เข้าถึงสมาชิกตัวแรกของ list
print(all[1])
print(alldata[3])
print(name[-1]) #เข้าถึงสมาชิกตัวหลังสุดของ list
'''
#การเข้าถึงข้อมูลแบบกำหนดช่วง
'''
print(name[0:2]) #ตัวแรกถึงตัวสอง
print(all[-2:-1]) 
print(name[1:]) #เข้าถึงข้อมูลตำแหน่งที่ 1 และที่เหลือต่อไปทั้งหมด
'''

#การแก้ไข้ข้อมูลใน list
#ชื่อตัวแปร[index] = "ข้อมูลที่ต้องการแก้ไข"
'''
number = [1,2,3,4,5,6]
print(number) # แสดงข้อมูลก่อนแก้ไข้
number[2] = 111
print(number) #แสดงหลังแก้ไข้ list
number[-1] = "Vorrathon"
print(number)
'''

#การแสดงผลข้อมูลใน list ด้วย loop
'''
number = [0,1,2,3,4,5]
sum = 0
for x in number :
    sum=sum+x
    print("สมาชิก=> ",x)  
print("ผลรวมของสมาชิกคือ",sum)
'''

#การตรวจสอบข้อมูลใน list
'''
friut = ["มะม่วง","มะพร้าว","ทุเรียน"]
if "มะม่ว" in friut :
    print("มีสมาชิก")
else :
    print("ไม่มีสมาชิก")
'''
#การนับจำนวนสมาชิกใน list
'''
friut = ["มะม่วง","มะพร้าว","ทุเรียน","แอปเปิ้ล"]
myPC = ["CPU","RAM","Mainborad"]

print(len(friut))
print(len(myPC)) #แสดงจำนวนสมาชิกในตัวแปร myPC
'''

#การใช้ len ทำงานร่วมกับ loop
'''
friut = ["มะม่วง","มะพร้าว","ทุเรียน","แอปเปิ้ล","ส้ม"]
myPC = ["CPU","RAM","Mainborad","HDD","SSD"]

for i in range(len(myPC)):
    # print(i) #แสดงจำนวนสมัครใน myPC
    print(myPC[i])  #แสดงลูปรายชื่อข้อมูลใน myPC ตามจำนวนสมาชิก

#แสดงข้อมูลใน firut โดยใช้ for loop
for item in friut:
    print(item,end=" "); 

'''
#การเพิ่มข้อมูลใน list
'''
friut = ["มะม่วง","มะพร้าว","ทุเรียน","แอปเปิ้ล","ส้ม"]
print("ก่อนเพิ่มสมาชิกในlistคือ",friut)

#append คือการนำสมาชิกมาต่อท้าย
friut.append("มังคุด")
print("หลังเพิ่มข้อมูลในlistคือ",friut)

#insert คือการเพิ่มข้อมูลในตำแหน่งที่ต้องการ
friut.insert(0,"สตอเบอรี่") #ระบุตำแหน่งที่จะแทรก และ ข้อมูลที่จะแทรก
print("แทรกข้อมูล",friut)
'''
#การลบข้อมูลใน list
'''
myPC = ["CPU","RAM","Mainborad","HDD","SSD","FAN","GPU"]

#การ remove
print("ก่อนremove",myPC)
myPC.remove("SSD")
print("หลังremove",myPC)

#การ pop ลบสมาชิกตัวล่าสุดออก
myPC.pop()
print("หลังpop",myPC)

#การ del การลบข้อมูลโดยระบุหมายเลข index
del myPC[0]
print("หลังdel",myPC)

#การล้างข้อมูลใน สมาชิก
myPC.clear()
print("หลัง clear",myPC) #จะไม่มีสมาชิกในlist

del myPC #ล้างข้อมูล หรือลบตัวแปร
'''

#การคัดลอกข้อมูลในlist
'''
myPC = ["CPU","RAM","Mainborad","HDD","SSD","FAN","GPU"]
myPCcopy =[]
print(myPCcopy)
myPCcopy=myPC.copy()
print("คัดลอกข้อมูลของตัวแปรmyPC",myPCcopy)
'''
#การรวมข้อมูลในแต่ละ list
'''
myPC = ["CPU","RAM","Mainborad","HDD","SSD","FAN","GPU"]
friut = ["มะม่วง","มะพร้าว","ทุเรียน","แอปเปิ้ล","ส้ม"]
allData= myPC+friut
print("รวมข้อมูลในlist",allData)
'''

#การนับข้อมูลในสมาชิก
'''
number=[1,2,4,5,5,44,5,2,44]
myPC = ["CPU","RAM","Mainborad","HDD","SSD","FAN","GPU"]
item = myPC.count("CPU")
count=number.count(2) #นับจำนวนข้อมูลที่อยู่ใน list และเก็บไว้ในตัวแปร
print(count)
print(item)
'''

#การรวมข้อมูลโดยใช้ extend การรวมข้อมูลไว้ใน list ใด list หนึ่งโดยไม่ต้องสร้างตัวแปรใหม่number=[1,2,4,5,5,44,5,2,44]
myPC = ["CPU","RAM","Mainborad","HDD","SSD","FAN","GPU"]
friut = ["มะม่วง","มะพร้าว","ทุเรียน","แอปเปิ้ล","ส้ม"]

print("ก่อนextend",myPC)
myPC.extend(friut) #การนำเอา firut ไปรวมในlist myPC
print("หลังextend",myPC)