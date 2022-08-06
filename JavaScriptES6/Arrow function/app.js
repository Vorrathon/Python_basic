// Arrow funcion
/*  function แบบเดิม function fullname(fname,lname){
    return fname+lname
    } */
// แบบใหม่ arrow function
// fullname=(fname,lame)=>fname+lname 
/* 
//ex ตัวอย่างการสร้าง function แบบเดิม
function fullname(fname,lname){
    return fname+lname
}
//เรียกใช้งานฟังก์ชั่น
console.log(fullname("vorrathon ","kedpratoom"))
*/

//ex ตัวอย่างการใช้ arrow fuction แบบใหม่
//สร้าง function 
fullname=(fname,lname)=>fname+lname
setAge=(age)=>"อายุ= "+age
proDuct=(Name,price,amount)=>"ชื่อสินค้า "+Name+" ราคา "+price+" จำนวน "+amount+" ชิ้น"

//เรียกใช้function
console.log(fullname("Panyapon ","Putachart")) 
console.log(setAge(20))
console.log(proDuct("CPU",12000,1))