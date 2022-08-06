# operater ของ set หรือตัวดำเนินการ

from traceback import print_tb


ani = {"dog", "cat", "rat", "fish", "bird"}
wild = {"tiger", "lion", "wolf", "bird"}

'''
#การยูเนียนการนำเอาสมาชิกของแต่ละsetมารวมกัน
ani.update(wild) #การอัปเดตไม่ต้องสร้างตัวแปรใหม่
world = ani.union(wild) 
print(world)
print(ani)

#คำสัง copy 
animal = ani.copy() #copy ตัวแปร ani
print(animal)
'''
# differnce เอา a ไม่เอา b
# a-b หรือ b-a
'''
world = ani.difference(wild)
print(world)  #เอา ani แต่ไม่ เอา wild

world2 = wild.difference(ani)
print(world2)  #เอา  wild แต่ไม่ เอา ani

#intersection เอาตัวที่เหมือนกัน
sameworld = ani.intersection(wild)
print(sameworld)

#diff update เพิ่มข้อมูลที่ต่างกันไว้ที่ตัวแปรเดิม
ani.difference_update(wild)
print(ani)


#intersec update การนำข้อมูลที่เหมือนกัน มาอัปเดตที่ตัวแปรเดิม
ani.intersection_update(wild)
print(ani)
'''
# subset
'''
fish = {"ปลาดุก", "ฉลาม", "วาฬ", "กระเบน", "แซลม่อน", 1}  # superset
x = {"วาฬ"}  # subset
y = {2}
# check ว่า x อยู่ใน subset ของ fish หรือป่าว ? ส่งค่าเป็น boolean
print((x and y).issubset(fish))

# check ว่า fish คือ superset ของ x หรือป่าว ? ส่งค่าเป็น boolean
print(fish.issuperset(x))
'''
#min - max-averge
Num = {1,2,3,4,5,6,7}
Minn=min(Num) #หาค่าต่ำสุดใน set
Maxx=max(Num) #หาค่าสูงสุดใน set 
Summ=sum(Num) #หาผลรวมของ set 
i=len(Num)

print("ค่าที่น้อยที่สุดคือ",Minn)
print("ค่าที่มากที่สุดคือ",Maxx)
print("ผลรวมคือ",Summ)
print("ค่าเฉลี่ยของ set คือ",int(Summ/i))
