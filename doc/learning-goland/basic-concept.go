
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

                   
                   
类对象/数据对象/接口定义 
struct ／interface 

type Piggie struct{
   ...
  CallFunc() int
}
                   
对象成员函数定义
func (pig *Piggie)CallFunc() int{
  // pig 代表 Piggie实例对象，同java/c++的this
}

                   
                   
                   
                   
                   
                   
                   
