#fucntion เรียก fucntion

def compareMax(x,y):
    if x>y:
        return x 
    else:
        return y 
def TreeNum(x,y,z):
    # a=compareMax(x,y) #เรียกใช้ function compairMax เพื่อเปรียบเทียบเลข 2 ตัว
    # b=compareMax(a,z) #เรียกใช้function compairMax อีกรอบเพื่อเปรียบเทียบกับตัวที่ 3
    # return b
    #ลดรูป
    return compareMax(compareMax(x,y),z)

max=TreeNum(20,3,50)
# print("ค่าทีมากสุดคือ",max)




def displayFood():
    print("หูฉลาม")
def displayCity():
    print("สวัสดีกรุงเทพ")
def Data():
    displayCity()
    displayFood()

Data()







