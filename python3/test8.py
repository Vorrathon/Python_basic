#โปรแกรมหาผลรวมตัวเลข
i = 1
sum = 0 #เก็บผลบวกตัวเลขตามจำนวนรอบ
#1+2+3+4+5
while i<= 3 :
    sum = sum+i 
    print("ค่าsumรอบที่ ",i,"คือ",sum)
    avg = sum/i #หาค่าเฉลี่ย
    i=i+1
    
print("ผลลัพธ์คือ ",sum)
print("avgคือ ",format(avg,'.2f'))