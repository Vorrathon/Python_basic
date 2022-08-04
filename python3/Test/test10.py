#โปรแกรมป้อนข้อมูลหาผลรวมตัวเลข และ ค่าเฉลี่ย
'''
start = 1 
stop = 5
sum = 0 
while start <= stop:
    number = int(input("ป้อนตัวเลข"))
    sum= sum+number #บวกเลขที่ป้อนแต่ละรอบ
    start =start+1
print("หาผลรวม ",sum)
print("ค่าเฉลี่ยคือ ",sum/stop)
'''
sum = 0
for i in range(1,6):
    number = int(input("ป้อนตัวเลข"))
    sum=sum+number
    avg = sum/5
print("ผลรวมคือ ",sum)
print("ค่าเฉลี่ยคือ ",format(avg,'.2f'))
