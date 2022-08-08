#การสร้างไฟล์ text
'''
fw=open("score.txt","w",encoding="utf-8") #สร้างไฟล์พร้อมให้เขียน
print(fw.read())
fw.write("Hello World\n")
fw.writelines("สวัสดีชาวโลก") #เขียนต่อในบรรทัดเดียวกัน
fw.close()
'''
# try:

#     # fr=open("score.txt","r",encoding="utf-8")
#     # line= fr.readlines() #readlines อ่านไฟล์ทีละบรรทัด #readline อ่านทีละตัวอักษร
#     # for i in line:
#     #     print(i)
#     # fa=open("score.txt","a",encoding="utf-8")
#     # fa.writelines("สวัสดีวันสงกรานต์\n") #"a"หรือ append เขียนข้อความใหม่ทับไฟล์เดิม"
#     # fr.close()
#     # fa.close()
# except FileNotFoundError :
#     print("หาไฟล์ไม่เจอ")


try:
    # fw=open("Data.txt","w",encoding="utf-8") คำสั่งสร้างไฟล์แล้วเขียน
    # fw.write("The voice")
    # fw.close()
    fw=open("Data.txt","a",encoding="utf-8") #เขียนข้อความต่อจากไฟล์เดิม apend ,(a)
    for i in range(5) :  #ป้อน 5รอบ
        name=input("ป้อนชื่อ: ") 
        fw.writelines(name+"\n") #เขียนข้อ
    fw.close()
except FileNotFoundError :
    print("หาไฟล์ไม่เจอ")