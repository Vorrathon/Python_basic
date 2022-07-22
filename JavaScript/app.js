//แสดงข้อความบน browser หรือ console
// document.write("<h1>สวัสดีนายวรธน</h1>"); //การเขียน javascipt แบบ external เขียนภายนอกแล้วเรียกใช้ไฟล์
// document.write("<p>Vorrathon</p>");
// alert("เตือนนะ วรธน"); //การแจ้งเตือนใน browser
// console.log("hello javascript"); //การแสดงข้อความผ่าน tab console ไม่แสดงผลหน้าเว็บ
// console.error("virus");
// console.warn("mistake");
alert("สวัสดี");
console.log("หน้าหมี")


//การสร้างตัวแปร
// let Name = 200; //สร้างตัวแปรสามารถเปลี่ยนค่าตัวแปรทีหลังได้
// let a=1,b=2,c=3 ;
// let d=a+b+c;
// let _Name = "Vorrathon";
// const vat= 0.07; // ค่า constant ค่าคงที่ไม่สามารถเปลียนค่าทีหลังได้
// console.log(Name);
// console.log("ผลรวมเท่ากับ",d);
// console.log("before",_Name);
// _Name = "Kedpratoom";
// console.log("after",_Name);
// console.log(vat*b);
// console.log(vat*c);
// document.write("<h1>name</h1>");
// document.write("ผลรวมเท่ากับ&nbsp&nbsp",d);
// let money = 500+500 ; //ตัวแปรแบบ interger เป็นตัวเลขแบบจำนวนเต็ม
// let price = 99.99 ;
// let message = "Vorrathon";
// let message2 = 'Kedpratoom';
// let checkname = false;
// let age = "20"+money ;

//การตรวจสอบชนิดข้อมูล
// console.log(typeof(money)); //typeof เป็นคำสั่งเช็คชนิดข้อมูล
// console.log(typeof(price));
// console.log(typeof(message),typeof(message2));
// console.log(typeof(checkname));
// console.log(age);
// let age = +"20.54" ; //ใส่คำสั่ง parseInt parseFloat และเครื่องหมาย+ไว้หน้า string จะทำการแปลง string เป็นตัวเลข
// console.log(age);
// let price = 30+"" ; //ใส่เครื่องหมาย +"" หลังค่าชนิดข้อมูล Number เพื่อแปลงค่าจาก Number เป็น string
// console.log(typeof(price));

//สร้าง arrayแบบที่หนึ่ง
// let number =Array(1,2,3,4,5,6,true,"Vorrathon"); //สร้างตัวแปรเดียวแต่เก็บค่าได้หลายค่า เรียกว่า Array
// console.log(number);//แสดงค่าใน array ทั้งหมด
// console.log(number[7]);//แสดงค่าในarray แบบเจาะจงที่อยู่โดยใส่เลขลำดับหรือ INDEX โดยเริ่มด้วยเลข 0 จะแสดงค่าในลำดับนั้นออกมา

// //สร้าง arrayแบบที่สอง
// let colors =["แดง","น้ำเงิน","ขาว","เขียว"];
// colors[1] = "เหลือง"; // สามารถเปลี่ยนค่าตัวแปรในarrayได้
// console.log(colors);
// console.log(colors[1]);
// let days =["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"];
// console.log(days);
// console.log(days[0]);

//ตัวดำเนินการของ Javascript
// let result =[2,4];
// let a=10 ,b=30 ;
// console.log("ผลบวกของ",5+10);
// console.log("ผลลบของ",5-5);
// console.log("ผลคูณของ",10*8);
// console.log("ผลหารของ",10/2);
// console.log("ผลของMod",10%3);
// console.log(result[0]+result[1]);
// console.log(a-b);
// console.log("ยกกำลัง",5**2); // ** ดอกจัน2ตัวคือการยกกำลัง

//ตัวดำเนินการเปรียบเทียบของJavascipt
// let a=10 ,b=10 ;
// let check = true;
// console.log("เท่ากันหรือไม่",a==b);
// console.log("ไม่เท่ากันหรือไม่",a!=b);
// console.log("มากกว่าหรือไม่",a>b);
// console.log("น้อยกว่าหรือไม่",a<b);
// console.log("มากกว่าหรือเท่ากับหรือไม่",a>=b);
// console.log("น้อยกว่าหรือเท่ากับหรือไม่",a<=b);
// console.log(!check);

//ตัวดำเนินการทางตรรกศาสตร์ของJavascipt
//ตัดเกรด
//and && ,or ||
//>=80 =>A
//70-79 =>B
//60-69 =>C
//50-59 =>D
// let score =80 ;
// console.log(score>=80,"A");
// console.log(score>=70 && score<79,"B");
// console.log(score>=60 && score <70,"C");
// console.log(score>=50 && score<60,"D");

//ตัวดำเนินการเพิ่มค่าลดค่าใน Javascript

// let a = 5 ,b=10 ;
// //เพิ่มค่าแบบ prefix
// console.log("ค่าเริ่มต้น",a);
// console.log("ค่าprefix",++a); //เพิ่มค่าไปแล้ว1 คือ 5+1 =6
// console.log("ค่าปัจจุบัน",a); //ค่าปัจจุบันคือ 6 

// //เพิ่มค่าแบบ postfix
// a= 5 ;
// console.log("ค่าเริ่มต้น",a);
// console.log("ค่าprefix",a++); 
// console.log("ค่าปัจจุบัน",a); 

// //ลดค่าแบบ prefix
// console.log("ค่าเริ่มต้น",b);
// console.log("ค่าprefix",--b); 
// console.log("ค่าปัจจุบัน",b);

// b=10;
// //ลดค่าแบบ postfix
// console.log("ค่าเริ่มต้น",b);
// console.log("ค่าprefix",b--); 
// console.log("ค่าปัจจุบัน",b);

//Compound assignment คือการลดรูปสมการโดยใช้เท่ากับ =
// let a =50 , b=30 ;
// console.log("ก่อน",a);
// a+=b //ความหมายคือ a=a+b
// console.log("หลัง",a);
// a = 50 ;
// console.log("ก่อน",a);
// a-=b; //ความหมายคือ a=a-b
// console.log("หลัง",a);
// a = 50 ;
// console.log("ก่อน",a);
// a*=b //ความหมายคือ a=a*b
// console.log("หลัง",a);

//ลำดับความสำคัญของตัวดำเนินการ 
// console.log(5+8*9); //แนะนำเปิดตารางความสำคัญ
// console.log(10-4+2);
// console.log(10-(2+1));
// console.log(5*2-40/5);
// console.log(7+8/2+25);

//โครงสร้างแบบมีเงื่อนไข(if)
// let a = 2 , b=2 ;
// let result = a+b;
// if(result == 5)
// {
//     console.log("ถูกต้อง") ;
//     alert("ถูกต้อง");
// }
// else
// {
//     alert("ผิด");
// }
// let balance = 1000;
// let withdraw = 400 ;
// if(withdraw<=balance){
//     document.write("สามารถถอนเงินได้");
//     balance -=withdraw;
//     document.write("<p>ยอดเงินคงเหลือ<p>",balance);
// }
// else{
//     document.write("ยอดเงินไม่เพียงพอ");
// }
// let score = 50;
// if(score>=80){
//     console.log("เกรดที่ได้ A")
// }else if(score>=70){
//     console.log("เกรดที่ได้ B")
// }
// else if(score>=60){
//     console.log("เกรดที่ได้ C")
// }
// else if(score>=50){
//     console.log("เกรดที่ได้ D")
// }
// else{
//     console.log("เกรดที่ได้ F")
// }

//Ternary operater คำสั่ง if else แบบลดรูป
// let score = 48 ;
// let pass ;
// // if(score>=50){
// //     pass = "ผ่านเกณฑ์" ;
// // }else{
// //     pass = "ไม่ผ่านเกณฑ์" ;
// // }
// // console.log(pass);

// //แบบลดรูป
// pass = score >=50 ? "ผ่านเกณฑ์": "ไม่ผ่านเกณฑ์"
// console.log(pass);

//การเขียนเงือนไข ซ้อนเงื่อนไข if ซ้อน if
// let age = 14 ;

// if(age<=15){
//     if(age == 15){
//         console.log("ม.3");
//     }
//     else if (age == 14){
//         console.log("ม.2");
//     }
//     else if(age == 13){
//         console.log("ม.1");
//     }
//     else if(age<13){
//         console.log("ประถม");
//     }
// }else{
//     console.log("ม.ปลาย,ปริญญา");
// }

//Switch case 
// let status = 1 ;
// let light ;
// if(status == 0){
//     light="ปิดไฟ";
//     console.log(light) ;
// } else if(status == 1){
//     light = "เปิดไฟ" ;
//     console.log(light);
// }
// let month = 4 ;
// let $name ;
// switch(month){
//     case 1 : $name = "มกราคม" 
//     break ;
//     case 2 : $name = "กุมภาพันธ์"
//     break ;
//     case 3 : $name = "มีนาคม"
//     break ;
//     default : $name = "ไม่พบข้อมูล"
// }
//     console.log($name);

//โปรแกรมเช็คเลขคู่หรือเลขคี่
// let x = 44;

// if(x%2==0){
//     console.log("เป็นเลขคู่");
// }else
// {
//     console.log("เป็นเลขคี่");
// }

//โปรแกรมเปรียบเทียบค่าตัวเลข
// let x = 10 , y=10;
// if(x>y){
//     console.log("x มีค่ามากกว่า y") ;
// }else if(x<y){
//     console.log("x มีค่าน้อยกว่า y") ;
// }
// else{
//     console.log("x มีค่าเท่ากับ y") ;
// }

//การทำซ้ำ Loop
//while Loop ถ้าเงื่อนไขเป็นจริงจะทำในลูปจนกว่าเงื่อนไขจะเป็นเท็จ
// let count = 1 ; //ตัวแปร count คือตัวแปรที่ใช้นับ
// while(count<=10){
//     if(count >= 11){
//         break ;
//     }
//    console.log("สั่งสินค้าชิ้นที่ ",count);
//    count++ ;
// }

//for Loop
// for(let i =8 ;i<=10; i++){    //for(ตัวแปรนับ; เงื่อนไขเป็นจริงทำซ้ำ ;เพิ่มทีละ1){ให้ทำอะไร}
//     console.log("สั่งสินค้าชิ้นที่ ",i)
// }
// for (let i = 10 ; i >= 1 ;i--){ //นับเลขลดลงทีละ 1  ถ้าจะเพิ่มที่ละ 2 i+=2
//     console.log(i);
// }

// let i = 1
// do{
// console.log(i); //แสดงค่า i ก่อนแล้วเช็คเงื่อนไข ถ้าจริงก็ทำซ้ำ ถ้าเท็จก็หยุดทำ
// i++ ;
// }while(i<=5);
 
//คำสั่งbreak ในกระโดดออกจาก loop for 
/* for(let i = 1 ; i<=10 ;i++){
//     if(i==5)break;
//     console.log(i);
// }
// console.log("จบโปรแกรม");

// //คำสั่ง continue 
// for(let i =1 ; i<=10; i++){
//     if(i==5)continue; //continue คือการข้าม loop นั้นที่ระบุไว้
//     console.log(i);
// }
console.log("จบโปรแกรม"); */

//ค่า null ,undefined และ NaN
//null คือค่าว่างไม่มีค่าอะไร มี boolean เป็น false
//uidefined เป็นตัวแปรที่ไม่กำหนดค่าเอาไว้
//NaN not a number คือตัวแปรที่ไม่ใช่ตัวเลข

//function ใน Javascipt เป็นชุดคำสั่งย่อยของโปรแกรมที่สร้างขึ้นมาเพื่อใช้งานในกรณีที่มีการใช้คำสั่งซ้ำ การใช้ function จะช่วยลดความยุ่งยากตรงนี้
//function แบบไม่มีการรับค่าส่งค่า
// let i ;
// function text(){            //รูปแบบการสร้าง function
//     console.log("Hello World",i);
// }
// for(i=1 ; i<=3 ;i++){
//     text(); //การเรียกใช้ function
// }
// function message1(){
//     alert("แจ้งเตือน")
// }
// function DisplayName(){
//     document.write("Vorrathon")
// }

//fucntion แบบรับส่งค่า
// function plus(x){ //x คือตัวแปร(parameter)ในfunction ไว้สำหรับรับค่า จาก agument
//     console.log("เลขที่ส่งมาคือ ",x);
// }
// plus(5); //ส่งค่าตัวเลขไปไว้ที่ตัวแปรใน function
// plus(6);

// let Num = 350 ; //ส่งค่าตัวแปรไปไว้ที่ function
// plus(Num); 

// let Name = "Vorrathon";
// plus(Name);
// //5 6 Num Name คือ agument สำหรับส่งค่าไปให้ตัวแปร parameter

// function fullname(fname,lname,city){ //กรณีมี parameter 2 ตัว
//     console.log("ชื่อ",fname,"นามสกุล",lname,"ที่อยู่",city);
// }
// fullname("Vorrathon","Kedpratoom","กำแพงเพชร"); //มี agument 2 ตัว
// fullname("oooo","sss","กรุงเทพ");

// function SuM9(x,y){
//     let total = x+y ;
//     console.log("ผลรวมคือ",total);
// }
// SuM9(1,2);
// SuM9(5,2);

// function Return

// function getIP(){
//     return "192.168.1.2" ;
// }
// let myIP = getIP(); //สร้างตัวแปรไว้รับค่าจาก return
// console.log("ไอพี",myIP);

// function GetNum(){
//     return 10*2 ;
// }
// function GetAddress(){
// let Address = "กรุงเทพ"
// return Address 
// }

// let total = GetNum();
// console.log(total);
// console.log(GetAddress()); //เรียกใช้ชื่อ function

//function รับค่าแล้วส่งออกไป
// function  setSalary(salary){
//     let bonus = 1000 ;
//     return salary+bonus;
// }
//  let a = setSalary(15000);
//  a-=5000 //นำค่าที่ได้มาคำนวณต่อ
// console.log("เงินเดือนรวม",a);

// let b = setSalary(20000);
// b-=5000 ;
// console.log("เงินเดือนรวม",b);

// function Sum(x,y){
//     return x+y
// }
// let total2=Sum(10,45);
// console.log(total2);

// function getName(Name,city){
// return Name+city
// }
// let history = getName("Vorrathon ","กำแพงเพชร")
// console.log(history);

//function ที่มีการใส่ค่าเริ่มต้น คือกรณีมีข้อมูลไม่ครบจะมีการกำหนดชื่อเริ่มต้นให้กับ parameter
// function fullname(fname="ไม่ทราบ",lname="ไม่ทราบ",city="ไม่ทราบ"){ 
//     console.log("ชื่อ",fname,"นามสกุล",lname,"จังหวัด",city)
// }
// fullname("vorrathon","kedpratoom","Bangkok");
// fullname("sommar","ssss","Pijit");
// fullname("chakit","wongkomta");
// fullname("GORR");

//ขอบเขตของตัวแปร
// let a = 100 ; // ทำงานแบบ goalbal ทำงานได้ทั้งหมด
// function Display(){
//     let b = 50 ; // ทำงานแบบ local ตัวแปรทำงานภายใต้ปีกกา
//     let a =50 ;
//     console.log("a ในฟังก์ชั่น ",a);
//     // console.log("bในฟังก์ชั่น ",b);
// }
// Display();
// console.log("aนอกฟังก์ชั้น",a);
// //  console.log("bนอกฟังก์ชั้น",b);

//Array properties & function

// let colors = ["แดง","ขาว","ฟ้า","เหลือง"] ;
// // let i = colors.length ; //หาความยาวArray
// // console.log(i);
// console.log("Before ",colors);
// let result = colors.sort() ; //เรียงลำดับ Array 
// console.log("After ",result) ;

// let fruits = ["แอปเปิ้ล","มะม่วง","ทุเรียน","ส้ม","องุ่น"];
// console.log("Before",fruits);
// let fruitssort = fruits.sort();
// console.log("After",fruitssort);

// let fruits = ["แอปเปิ้ล","มะม่วง","ทุเรียน","ส้ม","องุ่น"];
// fruits.push("มังคุด","มะละกอ"); //เพิ่มสมาชิกใน array
// console.log("Before",fruits);
// console.log(fruits[0]); //หา index array เริ่มต้น
// console.log(fruits[fruits.length-1]); //หา array ตัวสุดท้าย

// let fruitssort = fruits.reverse(); // เรียงลำดับจากมากไปน้อย
// console.log("After",fruitssort);

//การเข้าถึงสมาชิกด้วย for loop

// let colors = ["แดง","ขาว","น้ำเงิน","ส้ม","เหลือง","เขียว","น้ำตาล","เทา"];
// let i = 0
// let count = colors.length;
// console.log(colors);
// for(i; i < count; i++){
//     console.log("ลำดับที่",i+1 ,colors[i]);
// }

// let Name = ["ชาคริต","สรศักดิ์","วรธน","ปัญญาพล","นิธิพล","นพดล","วีระ"] ;
// let i = 0; 
// let count = Name.length;
// for(i;i<count;i++){
//     console.log(Name[i]);
// }

//เข้าถึงสมาชิกใน array ด้วย foreach

//  let colors = ["แดง","ขาว","น้ำเงิน","ส้ม","เหลือง","เขียว","น้ำตาล","เทา"];
 
//  colors.forEach(getColors); //ดึงข้อมูลใน array มาแสดง
 
//  function getColors(item){ 
//     console.log(item);
//  }

//แปลง Array เป็น String
// let colors = ["แดง","ขาว","น้ำเงิน","ส้ม","เหลือง","เขียว","น้ำตาล","เทา"];
// let x = colors.toString();//แปลงข้อมูล array เป็นข้อมูล string
// console.log(x); 
// let y = colors.join(" "); //การแปลง , เป็นตัวอื่นตามที่เรากำหนดใน วงเว็บ
// console.log(y);

//การรวม Array 
// let vegetables =["ผักกาด","ผักชี","คะน้า","พริก","มะนาว"];
// let hardwares = ["เม้าส์","คีบอร์ด","หูฟัง","ซีพียู"] ;
// let books = ["Harry Potter","Elder ring"];

// let cart = vegetables.concat(hardwares,books); //รวม array แต่ละชุดเข้าเป็นอันเดียว
// let x = cart.toString();
// x = cart.join(" ");
// console.log(cart);
// console.log(x);

// // let i = 0 
// // let count = cart.length;
// // for(i;i<count;i++){
// //     console.log(cart[i]);

// // }
// cart.forEach(myCart);
// function myCart(item){
//     console.log(item);
// }

//การเรียงลำดับมน Array 
// let Num = [1,2,-44,4,45];
// console.log(Num);
// let point= Num.sort(function(a,b){ 
//     return a-b // เรียงลำดับตัวเลขจากน้อยไปมาก
// })
// console.log("เรียงลำดับจากน้อยไปมาก",point);
// let ponint2 = Num.sort(function(a,b){
//     return b-a //เรียงลำดับจากมากไปน้อย
// })
// console.log("เรียงลำดับจากมากไปน้อย",ponint2);

// ๋Javascript Object

// let products = {name:"mic",price:200,color:"white",category:"Hardware"}; //การสร้าง Object
// console.log("ชื่อสินค้า",products.name,"หมวดหมู่",products.category); //เข้าถึง Object

//การสร้าง function ใน object
// let products = {name:"CPU",price:15000,spec:"corei7",category:"Hardware",
// displayproduct:function(){
//     return "ชื่อสินค้า "+this.name+" ราคา "+this.price+" หมวดหมู่ "+this.category
// },discount:function(){
//     return this.price-1000
// }};
// //เรียกใช้ method
// let x = products.displayproduct();
// let y = products.discount();
// console.log(x,"ส่วนลด 1000 บาท",y);

//การยืนยันด้วย confirm
// function deleteData(){
//  let result = confirm("คุณต้องการลบข้อมูลหรือไม่?") ;
//   if(result == true){
//   alert("ลบข้อมูลเรียบร้อย") ;
//   console.log(result);
//   }
//   else{
//     console.log(result);
//   }
// }

//html DOM เข้าถึง element ผ่าน id,tag,class
// let a = document.getElementsByTagName('p'); //อ้างอิงผ่านtag
// console.log(a);
// let b = document.getElementById('demo'); //อ้างอิงผ่าน id
// console.log(b);
//    const x = document.getElementById('demo2');
//    const e = document.querySelector('.myjs'); //อ้างอิงผ่าน class หรือ id ก็ได้ .คือ class #คือไอดี 
//    const f = document.querySelectorAll('p');

//    x.innerText="ไม่สอนแล้ว"; //เปลี่ยนแปลงข้อความผ่าน id โดยใช้ javascript
//    console.log(x);

//    function displayText(){
//     x.innerText="กลับมาสอนแล้ว";
//     console.log(x);
//    }
//    function displayText2(){
//     x.innerHTML="<strong>แสดงตัวหนา</strong>" ;
//     console.log("แสดงแบบตัวหนา",x);
//    }
//    function displayText3(){
//     let c = 20,d=30 ;
//     x.innerHTML="ผลรวมคือ "+(c+d) ;
//    }
//    console.log(e);
//    console.log(f);
//การเปลี่ยน class ไอดี tag ผ่าน Javascript
// const titleEL =document.querySelector('#title');
// const contentEL =document.querySelector('.content');



// function display(){
//     titleEL.setAttribute('id','not1')
//     contentEL.setAttribute('class','not') ;
// }
// const mode1=document.querySelector('.defalt1');
// const mode2=document.querySelector('.defalt2');

// function displaylight(){
//     mode1.setAttribute('class','light');
//     mode2.setAttribute('class','light');
// }
// function displaydark(){
//     mode1.setAttribute('class','dark');
//     mode2.setAttribute('class','dark');
// }

//DOM NODE
// const textall =document.querySelectorAll('p') ;
// let message = textall[2].innerHTML;
// console.log(textall);;
// console.log(textall[0]);
// console.log(textall[1].innerHTML);
// console.log(message);
// const menu = document.querySelector('#menu'); //เข้าถึง ul id menu
// const item = document.createElement('li'); //สร้าง element li ใน HTML ผ่าน Javascript
// item.innerText = "item" ; //เขียนข้อความ HTML ผ่าน javascript
// menu.appendChild(item); // add โหนดลูกเข้าไปต่อจากโหนด แม่
// let conut = 1 ;

// function additem(){
//     const item = document.createElement('li') ;
//     item.innerText = "item "+(conut++) ;
//     menu.appendChild(item);
// }

//ลบโหนด

// const menu = document.querySelector('#menu'); //เข้าถึงไอดี menu
// const item = document.getElementById('item-2');
// // menu.removeChild(item);

// function deletechild(){
//     menu.removeChild(item); //ลบelement ของโหนดลูก
// }
// const menu = document.getElementById('menu');
// const itemB = document.getElementById('item-2');
// const newItem = document.createElement('li');
// newItem.innerText = "Panyapon ชอบพาสาวไปกินข้าว";


// function replace(){
//     menu.replaceChild(newItem,itemB); //การแทนที่ element
// }

// DOM CSS add และ Remove Class
// const box = document.getElementById('box');
// let status1;

// function addDarkMode(){
//     box.classList.add('darkMode'); //เพิ่ม style darkMode ลงใน fucntion

// }
// function removeDarkMode(){
//     box.classList.remove('darkMode'); //ลบ style darkMode ใน fucntion
// }
// function switchMode(){
//     box.classList.toggle('darkMode'); //สลับ style ใน fucntion
//     status1 = box.classList.contains('darkMode'); //เช็คสถานะ style ว่ามี class หรือป่าว ถ้ามี จะ ขึ้นว่า true ใน console
//     console.log(status1);
//     if(status1){
//         box.style.color="blue" ;

//     }else{
//         box.style.color="red" ;
//     }
// }
//การเกิด Event 
// function welcome(){
//     alert("ยินดีต้อนรับ") ;  //Event onload ใช้กับ tag body ใน HTML
// }
// function hightlight(obj){ //Event onfocus ใช้กับ object tag input type "text" เมื่อนำเคอเซอร์เม้าไปวางจะให้ทำอะไร
//     obj.style.background ="red";

// }
// function nofocus(obj1){
//     obj1.style.background= "white"; //Event onblur ใช้กับ object tag input type "text" เมื่อนำเคอเซอร์เม้าออกไปจะให้ทำอะไร
// }
// function getmenu(){
//     const menu =document.getElementById('menu');
//     const display =document.getElementById('display'); // Event เลือกเมนูแล้วแสดงผล option นั้น
//     display.innerText = menu.value;
//     console.log(menu.value);
// }

//Event listener //เขียน Event ใน javascript เพียวๆ

// const menu =document.getElementById('menu');
// const display=document.getElementById('display');
// const remove=document.getElementById('remove');

// menu.addEventListener('change',getmenu);
// remove.addEventListener('click',showalert);

// function getmenu(){
//     display.innerText = menu.value;
//     console.log(menu.value);
// }
// function showalert(){
//   confirm("แน่ใจนะว่าจะลบ");
// }
