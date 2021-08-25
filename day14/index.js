// test.js
//
//function test(name){
//    alert("恭喜你中了一等奖，200W！")
function test(number) {
   console.log("!!!", number)
   name = "abc"
   var age = "18"
   var msg = "2"
   let msg2 = "sdd"
   const addr = "北京" //常量
   let sex = "女"
   // if (age===18 && sex=="nv "){
   //    console.log("成年人")
   // }else if(add=="beijing"){
   //    console.log("xx")
   // }else {
   //
   // }

   // for while

   // for (var i= 0;i<5;i++){
   //    console.log(i)
   // }
   //
   // var j = 0
   // while (j<5){
   //    j=j+1
   // }
   var l = [1, 2, 3, 4]
   l.push("aaa")
   console.log(l.indexOf(1))
   l[0]
   l[0] = "xx"

   console.log(l)
   var tag = true
   var tag2 = false
   var tag3 = null


   var l2 = {"name": "哈哈哈哈", "b": 2}
   console.log(l2.name)
   var l3 = "abc"
   l3.toUpperCase()
   l3.toLowerCase()
   var names = ["xiaohei", "xiaobai"]
   var names2 = {"name": "xxx", "sex": "22"}  //对象 object
   // for (var names2Element of names2) {
   //    console.log(names2Element)
   //
   // }


   // for (var i= 0;i<names.length;i++){
   //    console.log(i)
   // }
   // for (var index in names2) {
   //    console.log(index)
   //    names2[index]
   //
   // }
   var names = [1, 2, 3, 4, 5]

   // names.forEach(function(item,index){
   //    if (item==3){
   //       return false //如果写了return，那么就和continue是一样的
   //    }
   //    console.log(item,index)
   //
   // }) //不能用break和continue

   names.some(function (item, index) {
      if (item == 3) {
         return true
         //如果写了return false，那么就和continue是一样的
         //如果写了return true，那么就和break是一样的
      }
      console.log(item, index)

   })

   var response = JSON.parse('{"code":0,"msg":"注册成功"}')
   var s = JSON.stringify({"code": 0, "msg": "注册成功"})
   console.log(response.msg)
   console.log(typeof s)

   let sex_name = 1 > 2 ? "男" : "女"


   function test2() {
      console.log(name)
   }

}
//判断
//循环、定义变量、list、字典、字符串
评论 ( 0 )

