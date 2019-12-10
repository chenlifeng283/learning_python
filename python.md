1. 输入输出示例,获得用户输入的一个整数N，计算N的平方值;
结果采用宽度20字符方式居中输出，空余字符采用减号(-)填充。如果结果超过20个字符，则以结果宽度为准。
```python
n = eval(input()) #eval()可以用来计算字符串表达示，如eval('2+2')==4
m = power(n,2)
if len('m') < 20:
    print("{:-*20}".format(m)) #格式化字符串功能str.format(), 用法如"{}".format()
else:
    print(m)
```
---
2. 同符号数学运算
```python
n = eval(input())
a = abs(n)
b = a + 10
c = a - 10
d = a * 10
if n >= 0:
    print(a,abs(b),abs(c),abs(d))
else:
    print(a,-abs(b),-abs(c),-abs(d))
```
---
3. 天天向上的力量
```python
a = eval(input())
b = pow(1 + a * 0.001,365)
c = pow(1 - a * 0.001,365)
d = int(b/c)
print("{:.2f},{:.2f},{}".format(b,c,d)) #{:.2f}保留两位小数
```
---
4. 读入一个整数N，N是奇数，输出由星号字符组成的等边三角形，要求：第1行1个星号，第2行3个星号，第3行5个星号，依次类推，最后一行共N的星号。
```python
a = eval(input())
n = int(a/2) + 1
m = 1
for i in range(n):
    print((' '*((a-m)//2))+('*'*m)+(' '*((a-m)//2)))
    m += 2
```
---
5. 解方程
```python
from sympy import *
x = symbol('x') # 设未知数
y= symbol('y')
a = solve([2*x-y-3,3*x+y-7],[x,y]) #输入方程体，等号右边转左边，不带等号
print(a)
```
---
6. 类（class)和实例(instance):类是创建实例的模板，而实例则是一个一个具体的对象，各个实例拥有的数据都互相独立，互不影响
```python
class Student(object):     #定义类

    def __init__(self,name,score):    #类由模板作用，初使化时可以设置属性，在创建实例的时候就必须强制填写这些属性了，通过__inin__方法。
        self.__name=name              #在属性前面加两条下划下__,表明为私有变量，可以保护数据，不被外部引用。
        self.__score=score

    def print_score(self):   #方法一，各个实例都能调用，结果不一样。方法实际上是在类内部定义的函数，这样就把数据封装起来了，这些封装数据的函数和类本身是关联起来的。
        print('%s:%s' %(self.__name,self.__score))
        
    def get_grade(self):          #方法二。
        if self.__score>=90:
            return 'A'
        elif self.__score>=60:
            return 'B'
        else:
            return 'C'

     def get_name(self):          #访问限制后，如果外部真的要使用name等，如最后一行是要打印名字+等级的，名字不能直接bart.name，而需要在这里创建方法，包括要允许修改也要创建方法来实限。
         return self.__name
        
bart=Student('bart',85)  #根据定义好的类，创建实例，有了__init__里规定的属性，在创建实例时必须传入与__init__方法匹配的参数，
bart.print_score()  #实例调用方法一，输出结果为bart:85
print(bart.get_name(),bart.get_grade())  
```
---
7.
