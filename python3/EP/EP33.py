#list parameter

def displayfriut(item):
    for i in range(len(item)):
        print("ผลไม้ชิ้นที่",i+1,"คือ",item[i])

fruit=["apple","banana","pieapple","orange","strawberry","mango"] #list
displayfriut(fruit)

def COM(item):
    for i in range(len(item)):
            print("สินค้าชิ้นที่",i+1,"คือ",item[i])

product = ("CPU","GPU","RAM","SSD")    #tuple
COM(product) 

def animal(pett):
    for i in range(len(pett)):
        print("สัตว์เลี้ยงตัวที่",i+1,"คือ",pett[i])

pet=["dog","cat","bird","hamter","fish"]
animal(pet)