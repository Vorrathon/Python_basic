# Dictinary
# ex list and tuple ต้องอ้างอิงจาก index
# lis =["สีแดง","เขียว","เหลือง"]
# tup =("สีแดง","เขียว","เหลือง")

# dictionary => key กับ value อ้างอิงผ่าน key
# สร้าง dictionary
#ชื่อตัวแปร ={key:value,key:value}

# แบบแรก
'''
color = {'red': "สีแดง",
         'blue': "น้ำเงิน",
         'green': "สีเขียว",
         'address': "บ้านเลขที่ 82/4",
         'provice': "กำแพงเพชร"}
student = {"น็อต": f'{100}{" คะแนน"}', "บาส": f'{80}{" คะแนน"}',"โอ๊ต": f'{0}{" คะแนน"}'}

print(color["provice"])
print(student["บาส"])
'''

# แบบสอง constructor
'''
life = dict(cat="แมว",dog="หมา",human="คน")
print(life["cat"],life["dog"])
print(life.get("human")) #เรียกโดยใช้ get.(key)
'''
# การแก้ไขข้อมูลใน dict
'''
life = dict(cat="แมว",dog="หมา",human="คน")
print("ก่อนเปลี่ยน",life.get("cat"))
life["cat"] = "เจ้าเหมียว"
print("หลังเปลี่ยน",life.get("cat"))
'''
'''
#การเพิ่มข้อมูลใน dict
life.update({"bird":"นก","tiger":"เสือ"})
#ถ้าเจอ key ซ้ำมันจะทำการ update ถ้าไม่ซ้ำจะทำการเพิ่ม
print(life)
'''
# #การวนลูป dict
'''
for i in life:
    print(i) #มันแสดง key ไม่ใช่ value

for x in life.values():
    print(x) #แสดง value
for item in life.items():
    print(item) #แสดง key กับ value

#หรือการเลือกแสดง
for k,v in life.items():
    print("แสดง key:",k,"แสดง value:",v)
 '''
# การลบข้อมูลใน dict
'''
life = dict(cat="แมว",dog="หมา",human="คน",duck="เป็ด",snack="งู",lion="สิงโต")
print("ข้อมูลก่อนลบ",life)
life.pop("cat") #ลบแบบกำหนด key
print("ข้อมูลหลังลบ",life)
life.popitem() #ลบข้อมูลท้ายสุด
print("ข้อมูลลบแบบpop",life)
life.update({"lion":"สิงโต"})
print(life)
life.clear() #ล้างข้อมูลใน dict
print(life)
del life #ลบตัวแปร
print(life)
'''
# การ copy dict
'''
life = dict(cat="แมว",dog="หมา",human="คน",duck="เป็ด",snack="งู",lion="สิงโต")
lifecopy=life.copy()
print(lifecopy)
'''

# การซ้อน dict
# แบบไม่ซ้อน
'''
market = {"ร้านสาหร่าย": "อาหารตามสั่ง",
          "ร้านเจ๊ฝน": "ขายน้ำปั่น",
          "ร้านชาใจ": "ขายกาแฟ"
          }
'''
# แบบซ้อน หรือ dict ย่อย
market = {
    "ร้านสาหร่าย": {
        "name": "ป้าสี",
        "menu": ["กระเพราไก่", "กระเพราเนื้อ", "ข้าวผัดต้มยำ"],
        "zone": "KPRU"
    },
    "้ร้านเจ๊ฝน": {
        "name": "เจ๊ฝน",
        "menu": ["กาแฟ", "โกโก้ปั่น", "นมปั่น"],
        "zone": "หลัง KPRU"
    },
    "ร้านชาใจ": {
        "name": "นายชา",
        "menu": ["เอสเพรสโซ่", "คาปูชิโน", "ลาเต้"],
        "zone": "ซอย KPRU หลังมอ"
    }

}
print(market["ร้านชาใจ"]["zone"]) #แสดง dict หลัก และ dict ย่อย


if "กาแฟ" in market["้ร้านเจ๊ฝน"]["menu"]:
    print("เป็นสมาชิก")
else :
    print("ไม่เป็น")