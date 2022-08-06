#default parameter การกำหนดค่าเริ่มต้นให้กับ parameter ที่ไม่ทราบ

def appData(fname,lname,age,city="ไม่ทราบ"): #city="ไม่ทราบ" กรณีไม่ได้ระบุ argument city จะกำหนดให้เป็น ไม่ทราบ
    print("ชื่อ",fname)
    print("นามสกุล",lname)
    print("อายุ",age)
    print("จังหวัด",city)

appData("vorathon","kedpratoom",26,"กรุงเทพ")
