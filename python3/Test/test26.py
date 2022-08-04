#โปรแกรมค้นหาจำนวนตัวอักษรในสมาชิกของ list
msg= ["AA","AB","CDA","ACB","CBA","AAA","BBC"]
result=[]
for item in msg :
  result.append(item.count("A"))
  
print(msg)
print(result)