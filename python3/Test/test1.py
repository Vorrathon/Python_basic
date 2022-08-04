# โปรแกรมคำนวณ BMI (ดัชนีมวลกาย)
# BMI = น้ำหนัก(kg)/ส่วนสูง*ส่วนสูง(m)

# inputข้อมูล
weight = int(input("กรุณาป้อนน้ำหนักของคุณ(kg):"))
high = int(input("กรุณาป้อนส่วนสูงของคุณ(cm):"))/100  # cm=m แปลงจาก cm เป็น m
# process
bmi = weight/(high**2)  # สูตรหาค่า bmi
# output
print("BMI =", bmi)
