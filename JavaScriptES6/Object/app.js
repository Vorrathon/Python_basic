//Object
//สร้าง object
/*
const customer ={
    custName : "Vorrathon",
    age: 26,
    tel: "084-xxxx",
    address: "KampheagePhet"
}
//แสดง Object
console.log(customer)
*/

//การแสดง Object สมัยใหม่
//สร้างตัวแปร
const Name = 'vorrathon'
const age = 26
const tel = '084-382-3028'
const address = 'bangkok'

//สร้าง Object
//กรณีชื่อPropertyกับตัวแปรเหมือนกัน เขียนแค่ตัวเดียวได้
const cusTomer = {
  showData() {
    console.log('ชื่อลูกค้า ' + Name)
  },
  อายุ: age,
  เบอร์โทร: tel,
  ที่อยู่: address,
}
const customersmall = { Name, age, tel, address } //เขียน object แบบย่อกรณี property กับ ชื่อตัวแปรเหมือนกัน

console.log(customersmall)

//เรียกใช้ function ใน object
cusTomer.showData()
