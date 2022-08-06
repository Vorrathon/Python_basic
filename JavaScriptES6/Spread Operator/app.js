//Spread Operator ใช้ในการกระจายสมาชิกใน Array
/*
let newArr =[100,200,400]
let Data =[10,20]

// โจทย์นำเอา newArr ยัดไปใน Data
let newData = [...Data,...newArr] //... หน้าอาเรย์จะเป็นการกระจายสมาชิกใน Array
console.log(newData)


let color =["red","green","blue"]
let newcolor =["black","purple"]
let  allcolor=[...newcolor,...color]
console.log("สีทั้งหมดคือ",allcolor)
*/

//function push

let color =["red","green","blue"]
let newcolor =["black","purple"]

let allcolor =["grey","pink"]
allcolor.push(...color,...newcolor) //แยกข้อมูลใน array แล้ว push ลงไปใน array allcolor
console.log(allcolor)