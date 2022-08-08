try :
    #ป้อนคะแนน
    fw =open("Score.txt","w",encoding="utf-8")
    print("สร้างไฟล์เรียบร้อย")
    while True : 
        studentid=input("ป้อนรหัสนักเรียน:")
        if studentid == "exit" :
            break
        score = input("ป้อนคะแนนสอบ:")
        fw.writelines(studentid+"\t"+score+"\n")
    fw.close()

    fr=open("Score.txt","r",encoding="utf-8")
    fw=open("Grade.txt","w",encoding="utf-8")
    grade = None
    for line in fr.readlines():
        score=line[-4:-1].strip() #เอาช่วงที่เป็นตัวเลข และลบช่องว่างด้วย strip
        studentid=line[0:5].strip() #เอาช่วงที่เป็นไอดี
       
        score=int(score)
        if score >= 80 :
            grade="A"
        elif score >=70:
            grade="B"
        elif score >=60:
            grade="C"
        elif score >=50:
            grade="D"
        elif score >0 or score<50 :
            grade="F"
        print("รหัสนักเรียน:",studentid," คะแนน:",score,"เกรด",grade)
        fw.writelines("รหัสนักเรียน:"+studentid+"\t"+"คะแนน:"+str(score)+"\t"+"เกรด:"+grade+"\n")
    fw.close()
except Exception as e:
    print(e)