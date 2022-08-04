#โปแกรมจับคู่คำ /บุคคล
'''
บาส,แพร
ครับ,ค่ะ

บาสครับ,แพรค่ะ,บาสค่ะ,แพรครับ
'''
person=["บาส","แพร"]
word=["ครับ","ค่ะ"]

result=[]
for x in person:
    for y in word:
       
        result.append(x+y)
print(result)

#ลดรูป
result=[x+y for x in person for y in word] 
print(result)

    