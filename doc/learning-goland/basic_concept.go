
变量定义
var a int = 100 显示声明类型
a:=100 编译器自动推导 

循环
for init;loop;post{   注意: { 必须同 for 在一行
}


import (
  _ "fmt"   
)

函数参数

func cook(recipe string) string{
}

//参数为函数类型
func setBack( action (event string) int){
}

&变量地址 ，例如： &x ， 但无法获得函数地址 ，例如: &cook 报错
