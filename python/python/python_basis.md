# python基础学习

## 1. python基础语法

- python中注释使用#来表示
- 由于python为unicode字符串，所以可以用中文作为标识符(变量名是表示符的子集，函数名类名之类的都为标识符)
- python的特色之一是以缩进表示代码块，相同缩进的代码为同一代码块
- python中有复数类型
- python中的单引号和双引号的意义相同
- python中的import表示导入一个模块的所有函数，from xxx import aaa表示导入aaa模块中的xxx库

## 2. python基本数据类型
python中的变量不需要声明

- 可变类型:数据可以改变，如list,dictionary,set
- 不可变类型:数据不可以改变，如Number,String,Tuple

**注**：
```
下面的a发生变化的原因不是把11给a，而是创建了11，把a指向新对象
a = 10
a = a + 1
```

### 2.1 string

