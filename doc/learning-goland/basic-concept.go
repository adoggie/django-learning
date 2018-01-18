参考：
https://gobyexample.com


变量定义
var a int = 100 显示声明类型
a:=100 编译器自动推导 

循环
for init;loop;post{   注意: { 必须同 for 在一行
}


字典map
// 查找键值是否存在
if v, ok := m1["a"]; ok {
	fmt.Println(v)
} else {
	fmt.Println("Key Not Found")
}

// 遍历map
for k, v := range m1 {
	fmt.Println(k, v)
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

对象创建 
                   p1:= Number{}  生成对象
                   p2:= new(Number) 返回对象指针
                   但访问内部变量均使用 '.' , p1.value,p2.value 
                   
type 使用
                   定义结构:   type xxx struct {}
                   重命名 :   type namestr string  
                   为新类型增加方法: 
                   func (name namestr) len() int {}  定义 len()成员函数
                   
类对象/数据对象/接口定义 
struct ／interface 

type Piggie struct{
   ...
  CallFunc() int
}
                   
对象成员函数定义
func (pig Piggie)CallFunc() int{
  // pig 代表 Piggie实例对象，同java/c++的this
}

接口查询 

if file5,ok := file1.(two.IStream);ok {
...
}
                   
                   
                   
                   
                   
                   
                   
