//String
//สัญลักษณ์ patic หรือ ` มีไว้สำหรับการพิมพ์ string แบบยาวๆแบบขึ้นบรรทัดใหม่ได้ โดยไม่เกิด ERROR 
//keyshort เปลี่ยนภาษาเป็น Eng แล้วกด [window+`] ประมาณ 1 วิ
/*
const cusTomer = `ชื่อลูกค้า: ปัญญาพล นัวสาวมา3ทุ่ม ที่อยู่ 1234/56 ถนนสายนัว อำเภอหญิงเยอะ 
จังหวัดนัดเย เบอร์โทร:090-111-1234`

console.log(cusTomer)
*/ 

//interporation การแทรกตัวแปร
// การแทรกตัวแปรใน string `${ตัวแปร}` อยู่ภายใต้สัญลักษณ์patic
let Name = "Vorrathon Kedpratoom"
let age=26
let address = "82/4"
let person = `ชื่อ:${Name}
อายุ :${age}
อาชีพ:นักศึกษา
ที่อยู่:${address}`

console.log(person)