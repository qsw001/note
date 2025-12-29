# go的基本语法

## 1. go的最小运行程序

```
package main

import "fmt"

func main(){
    fmt.Println("Hello world")
}
```

## 2. go的变量声明

- 显式声明:var a int = 10
- 类型推到:var a = 10
- 短变量声明:a:=10(函数内常用)

## 3. if用法

```
if a > 10 {
    ...
}
```

```
if a:=10; a > 5 {
    ...
}
```

## 4. for用法

```
for i:=1;i<10;i++{
    fmt.Println(i)
}
```
类似while
```
for a>10{

}
```
如果用的是switch则不需要加break

for循环的range形式可以遍历数组或切片，遍历时返回两个数据一个是元素的下标，另一个是元素的副本

```
这里面的a为对应的索引，b为副本，挡不需要时可以用_代替
for a,b := range pow {

}
```

## 5. 函数

最简单的格式如下
```
func add(a, b int) (int, int){
    return a,b
}
```

在go中，函数的“地位”会高一些，例如它可以直接赋值给其他变量，例如：
```
写一个函数
func add(a, b int) int {
    return a+b
}

然后我们可以直接将函数当作一个变量一样
a := add

这里的a就是add了
res := a(3,4)
```
go中函数“地位”的体现主要在callback上面，我们假设一个函数在某个特定的地方需要干一件事(函数)，而这件事又是不确定的，那么我们需要自己去定义这件事，于是我们可以一个未知函数作为变量传入这个函数中
```
此时done函数是外部定义的
func process(a,b int, done func(...) ...) int {

} 
```

方法：方法是一类带特殊接收者的函数

```
这里Abs就是Vertex的一个方法
func (v Vertex) Abs() float64 {
	return math.Sqrt(v.X*v.X + v.Y*v.Y)
}
```

## 6. 数组和切片
数组(array):数组是值类型，定义方式如下
```
var a [5]int
或
a := [3]int{1,2,3}
```
其中长度是类型的一部分，由于他的长度不能发生变化，拷贝起来不方便，所以用的少。

切片:数组的大小是固定的，但是切片大小并不是如此，实际中，切片比数组更加常用。通常，我们将[]T称为T类型的切片
```
a := []int{1,2,3,4,5,6}
此时a[1:4]表示的是下标从一到三的东西
```
切片像是数组的引用，他本身不存储任何东西，当修改切片时，其对应的数组也发生改变
```
names := [4]string{
		"John",
		"Paul",
		"George",
		"Ringo",
	}
当我们定义一个切片时
a:=names[1:3]
a[1] = "XXX"
此时names里的东西也发生改变
```
切片是有其长度和容量的，分别通过len和cap来表示，通常我们也可以通过make来创建切片
```
使用make创建切片的方法为make([]int, 4, 5)类型，长度，容量
```

