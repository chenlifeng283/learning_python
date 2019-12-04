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
