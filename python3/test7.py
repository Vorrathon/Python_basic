#โปรแกรมแปลงอุณภูมิ
temp = input("ป้อนอุณภูมิ(องศา)")
degree = int(temp[:-1]) #เป็นค่าตัวเลข
unit = temp[-1].upper() #เป็นหน่วยองศา
if unit == "C":
    result=((9/5)*degree)+32
    unit_result = "ฟาเรนไฮล์"
    print("แปลงจาก ",degree,"องศาเซลเซียส","เป็น",format(result,'.2f'),unit_result) #format(result,'.2f') คือการแปลงผลลัพธ์ให้เป็นทศนิยม 2 ตำแหน่ง
elif unit == "F":
    result=5/9*(degree-32)
    unit_result= "เซลเซียส"
    print("แปลงจาก ",degree,"องศาฟาเรนไฮน์","เป็น",format(result,'.2f'),unit_result) 
elif unit != "C" and unit !="F":
    print("กรุณาใส่หน่วยให้ถูกต้อง")