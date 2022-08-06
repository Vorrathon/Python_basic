#Non-Primitive Tuple
#แตกต่างจาก list คือ Tuple ข้อมูลในสมาชิกไม่สามารถเปลี่ยนแปลงได้
'''
tup=tuple((1,2,3,4,"Vorrathon",True)) #tuple
list=list([1,2,3,4,"Kedpratoom",False]) #list
tup1=(55,3.14,"มะนาว","Valorant")

list[0]="กำแพงเพชร"
#tup ไม่สามารถแก้ไขได้
print(tup)
print(list)

'''

#การเข้าถึงข้อมูลใน tuple
'''
print(tup1[3])
print(tup1[-3])
'''
#การเข้าถึงข้อมูลแบบกำหนดช่วง

'''
tup=(55,3.14,"มะนาว","Valorant")
print(tup[1:])
'''
#การแก้ไขข้อมูล tuple
'''
tup=(55,3.14,"มะนาว","Valorant")
print("ก่อนเแก้ไข",tup)
lis=list(tup) #แปลง tuple เป็น list

lis[0]="alonemanz"
print("หลังแก้ไข",lis)

tup=tuple(lis) #นำค่าที่เปลี่ยนแปลงกลับมาเป็น tuple
print("แปลงกลับเป็นtuple",tup)
'''
#การ loop ข้อมูลแบบ tuple
'''
tup=(55,3.14,"มะนาว","Valorant")
for item in tup:
    print("สมาชิก",item)
'''
#การตรวจสอบ tuple
'''
tup=(55,3.14,"มะนาว","Valorant")
if "มะนำ" in  tup:
    print("เป็นสมาชิก")
else:
    print("ไม่เป็นสมาชิก")
'''
#การนับสมาชิกใน tuple
'''
tup=(55,3.14,"มะนาว","Valorant")
print(len(tup))
'''

#การใช้ len ร่วมกับ loop for
'''
tup=(55,3.14,"มะนาว","Valorant")
for item in range(len(tup)):
    print(tup[item])
'''
#การสร้างสมาชิกใน tuple
'''
tup=(55,3.14,"มะนาว","Valorant")
x=("Vorrathon",)
y=tuple("Vorrathon")
print(type(x))
print(type(y))
'''

#การเพิ่มข้อมูล หรือ join แบบ tuple
'''
name =("alonemanz","freedom")
lname =("captain",) #แปลง lname เป็น tuple
group_name=name+lname
print(group_name)
'''

#การแก้ไขข้อมูล tuple
'''
name =("alonemanz","freedom")
name=list(name)
name[1]="sunshine"
name=tuple(name)
print(type(name))
'''

#นำเอา list ไปรวมกับ tuple
'''
name =("alonemanz","freedom")
city=["bangkok","kampheagephet"]
city=tuple(city) #แปลง list เป็น tuple
data=name+city
print(data)
'''
#การลบข้อมูลใน tuple
'''
name =("alonemanz","freedom","captain","ShinV")
city=("bangkok","kampheagephet")
del(city) #คำสั่งลบ ตัวแปร หรือเคลีย memery


#คำสั่ง remove กับ pop

lis=list(name) #แปลง tuple เป็น list
lis.pop() #ลบตัวสุดท้ายออก
print(lis)
lis.remove("alonemanz") #ลบ alonemanz ออก
print(lis)
lis.clear()#clearข้อมูลทั้งหมดใน สมาชิกใน tuple
print(lis)
lis=tuple(lis) #แปลงกลับเป็น tuple
print(type(lis))
print(lis)
'''


#การ sort ข้อมูล
'''
tup=(100,43,434,553,53,12,2,7,8,77,6,98)
lis=list(tup)#แปลงะtuple เป็น list
lis.sort()
print(lis)
lis=tuple(lis) #แปลงกลับเป็นtuple
print(lis)
lis=list(lis)
lis.reverse()
print(lis)
tup=tuple(lis)
print(type(tup))
'''

#นำค่า tuple เก็บไว้ในตัวแปร
'''
tup=("Vorrathon","alonemanz","shinV")
a,b,c=tup #ตัวแปร a b c เก็บ tup ไว้
print(a+" "+b+" "+c)

#การสลับ tuple
x=(50,60)
y=(88,99)
x,y=y,x
print(x,y)
'''
#แปลงtuple เป็นสตริง 
charecter=("V","o","r","r","a","t","h","o","n")
x="".join(charecter)
print("ก่อนแปลง",charecter)
print("หลังแปลง",x)
 







