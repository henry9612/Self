# import --------
# import tensorflow as tf
# from math import *  # 最好不用这种方式，如果导入的有同名，会覆盖现有的对象。
# 自定义模块的导入：模块不能带.py，导入的函数不能带();
from function_class_python import func1, func2
func1(), print(func2(3,8))

# type和size ------------
# list, tuple, dict, str等类型用len查看元素个数，用type查看类型；

# 字典dict ---------
dict1 = {'liu': 42, 'heng': [3, 5], 6: 90}  # strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。
dict1[12] = 'hengjin'  # 可以直接通过可以增加元素；
print(dict1, dir(dict1), type(dict1), sep='\n', end='#')  # end是关键字参数，后面不能再输入字符串等
# 脚本中dir()和type()等，需要print()才能显示出来
del dict1['liu'], dict1[6]
print(dict1.keys(), dict1.values())  # 输出所有键和值；
for k, v in dict1.items():  # 输出键值对，前者表示键；
    print(k, v)
dict([('a', 3), [3, 'b']])  # 可以直接从键值对创建dict； 不要用dict(a=3, b=3)方式；

# list ----------
list1 = [1, 2, 3, 4, 5]
for x in list1:
    print(x + 2)
list2 = [1, 'liu', 5]
list3 = [2, (2, 3)]  # list和tuple可以互相嵌套；
print(list2 + list3, list2 * 2)  # >>> [1, 'liu', 5, 2, (2, 3)] [1, 'liu', 5, 1, 'liu', 5]
g = [0] * 3 + [1] * 4 + [2] * 2  # >>>
print(g)  # >>> [0, 0, 0, 1, 1, 1, 1, 2, 2]
g[2:5] = [9, 2, 3]  # >>> 赋值也可以按照一段来;
list4 = [1, 2, 3, 4, 5]
print(type(list4))  # >>> list4如果没有中括号，则为tuple
# print(list4 + 4)  # >>> list和tuple不能和数字相加，也不可互加，只能同类相加，表示串联。
print(list4 * 2)  # 不是list或tuple中的每个数字乘以2，而是复制2倍. >>>[1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
del list1, list2, list4[4]
for i, v in enumerate([1, 2, 3]):  # i为序号，从0开始；tuple也可以.
    print(i, v)
# 一般来讲，tuple/list/dict/set/str/number等类型是一个整体（容器），一般是作为“一个”参数，因此该括号必须加括号。

# tuple ------------
tuple1 = (1, 'ad', [24, 32])  # tuple也可以是不同类型，可以嵌套。
tuple2 = 'a', 3, 8, [1, 2]  # 不带括号默认表示tuple；
print(type(tuple2))
tuple3 = (32,)  # 当tuple只有一个元素时，一定要加上逗号。
del tuple2  # 不允许删除tuple中的元素，可以删除整个tuple；
print(tuple([1, 2]))  # tuple只能有一个参数且iterable，tuple(1,3)都是错的，tuple(3)也是，因为3不是iterable；
print(list((1, 3)))  # list与tuple规则一样；()改成[]也可以，仍然满足条件；
print((1, 2, 3, 4, 5)[2:4])  # >>> (3,4)
# tuple不可变，只有len,max,min等操作，而没有append, pop等操作，而list都有；dict没有append操作；
# int(x)，float(x)，complex(real [,imag])，str(x)，tuple(s)，list(s)，set(s)，dict(d)都是类型转换函数；


# set -----------
A = set([1, 2, 3, 4])
B = {3, 4, 5, 6}
C = set([1, 1, 2, 2, 2, 3, 3, 3, 3])
print(C)  # 集合的去重效果，set([1, 2, 3])
print(A | B)  # 求并集，set([1, 2, 3, 4, 5, 6])
print(A & B)  # 求交集，set([3, 4])
print(A - B)  # 求差集，属于A但不属于B的，set([1, 2])

# 变量赋值 ---------
a, b, c = 1, 2, 3
a = b = c = 5
d = None
print('the number are:', a, b, c, type(d))  # >>> <class 'NoneType'>, 在很多API中，如果执行失败就会返回None
a = 1
b = a
c = 1
print(id(a), id(b), id(c))  # >>> id相同，
b = 1.0
print(a is b)  # False，这个语句等效于 id(a) == id(b)；==和!=比较引用指向的内存中的内容，而is判断两个变量是否指向一个地址；
# 变量其实是个引用

# 数学运算 ---------
print(9 // 2, 9.0 // 2, 9.0 / 2.0)  # >>> 4, 4.0, 4.5
print(type(9 // 2), type(9.0 // 2))  # int, float
num1 = 3.68
import math
print(abs(num1), math.ceil(num1), math.floor(num1), math.exp(num1), math.sqrt(num1), math.pow(3, 2))
# math模块有很多函数： sin, cos, exp, sqrt, pow, log等
# python内置函数：
# 1. 数学运算类：abs, complex, float, int, pow, range, bool, round, sum等, 还有+-*/;
print(abs(-1), complex(2, 3), int(4.2), pow(2, 3), range(0, 3), bool('liu'), sum([1, 2, 3]))
# >>> 1 (2+3j) 4 8 range(0, 3) True 6
tmp1 = 2 + 3j  # 不是3*j, 等价于tmp1 = complex(2, 3)
# 2. 集合类操作： iter, max, min, dict, list, tuple, set, str, sorted.
# 3. 逻辑判断类：all, any
# 4. 其他：type, dir, help, len, id, isinstance, len, map, next, zip.
# 5. IO类：input, open, print.
add_test = [1, 2] + [[3, 4]]  # >>> [1,2,[3,4]]  必须是同类型(同list)相加；
mul_test = [1, 3] * 3  # >> [1,3,1,3,1,3]
# +,-,x,/,**适用于number类型数据，因为sequence，dict可以包含不同的数据类型，没法数学运算；+，x在序列中表示叠加和复制；


# 字符串 -------------
str1 = 'Liuhengjin'  # 单字符也是字符串
print(str1.upper(), str1.lower())  # 大小写；
str2 = "hengjin"  # 单双引号都可以
str3 = '''liu
jin'''  # 多行字符串，且所见即所得，三个双引号也可；
'''
三（双）引号也可以用于多行注释
单行注释用#
'''
print(str1, str2, str3, type(str3))
str4 = r"hi, \n liuhengjin"  # 单双引号均可，r/R均可， 则\n均是字符串的一部分。
print(str4)
print(str4 + 'name', 'name' * 3, str4[3:8])  # +表示拼接，*表示复制
print('NaMe', len(str4), 'NaMe'.upper(), 'NaMe'.lower())  # 注意upper，lower的用法。


# 输入input ----------
# a = input('\nplease enter an number:')  # input也可以加提示语；任何内容都会被转为字符串，存放在a中；一次只能得到一个字符串；
# b = int(a)  # int()的参数必须只有一个，且必须是纯数字的字符串；如果要和数字比大小，则要转成对应类型；


# 格式化输出: % 和 str.format() ---------------
print('liu, %s' % 'hengjin', 'hello')  
print('hi, %s have $%d' % ('you', 1000000))
print('%.4f' % 3.1415926)
print('{}, {}'.format('hello', 'world'))  # 不设置指定位置，按默认顺序
print("{1} {0} {1}".format("hello", "world"))  # 设置指定位置
print("网站名：{name}, 地址: {url}".format(name="菜鸟教程", url="www.runoob.com"))
site = {"name": "菜鸟教程", "url": "www.runoob.com"}
print("网站名：{name}, 地址 {url}".format(**site))  # 通过字典设置参数
print('\n\n')
str1 = '{0} need {1}, {1} need {0}'
print(str1.format('i', 'you'))  # >>> i need you, you need i
str2 = '{name} is {age} years old.'
c = str2.format(name='Tom', age=8)  # Tom is 8 years old.
d = str2.format(age=7, name='Jerry')  # Jerry is 7 years old.
print(c, d)

# 控制语句: 有if,for,while,else,elif这几个； -------------
# Python的条件控制主要是三个关键字：if-elif-else，其中elif就是else if的意思;
age = 3
if age > 3:
    print('age<3')
elif age == 3:
    print('age=3')
else:
    print('age>3')
# 都有冒号；可以简写为“if x：”，只要x为非零数值，非空list/tuple/str,就为True，0和null为False;
if age > 2:
    pass  # 啥都不写会出错，可以pass占位。for/while中均可用；同一语句块保持缩进相同即可；
if -3 < age < 3:  # if链式用法，等价于if x > -3 and x < 3
    print('age =', age)
if age in [1, 6, 3]:  # 判断一个值是不是等于多个可能性中的一个
    print('age is in the list')

n = 3
while n > 0:  # 也可以像if那样，写成 while x：的形式。
    print(n)
    n = n - 1  # python中没有++，--运算符；
else:
    print('当条件为False时，执行else语句')
'''循环语句可以有 else 子句，它在穷尽列表(以for循环)或条件变为 false (以while循环)导致循
环终止时被执行,但循环被break终止时不执行'''

for x in range(11):  # range可以换成list， tuple， list(range(11)), tuple(range(11))等
    print(x)
else:
    print('循环终止')
for x in 1, 2, 3:  # 可以没有括号，表示tuple；
    print(x + 1)
# for可以遍历任何任何序列，如list/tuple/str，就是把每个元素带入x,然后执行缩进语句；
print(range(11), type(range(11)))  # >>> 输出range(0, 11), <class 'range'>
print(list(range(3)), tuple(range(3)))  # >>> [0, 1, 2] (0, 1, 2)

for i in ['liu', 12, 'jin']:  # 遍历元素，不一定是数字；
    print(i)
for i in 'Python': print(i)  # 遍历字符串，如果只有一个语句，可以写成一行， if/while也是；

for m, n in zip([1, 2, 3], ('a', 'b', 'c')):  # 任一个都可是tuple/list，不用类型一致；
    pass  # 起占位作用；
    print(m, n)  # 输出1，a, 2, b, 3, c,可以加括号形成list/tuple;


# 高级特性  -----------------
# - 列表生成式：用于生成list；
list_gen1 = [x * x for x in range(11)]  # 没有冒号了；
list_gen2 = [[x, x * x] for x in range(11) if x % 2 == 0]  # 2个表达式
print(list_gen1, '\n', list_gen2)
list_gen3 = [x * y for x in range(5) if x > 3 for y in range(4) if y < 2]
print(list_gen3)  # >>> [0, 4], 执行顺序如下：
'''
for x in range(5):
    if x > 3:
        for y in range(4):
            if y < 2:
                x*y
'''
list_gen4 = [m + n for m in 'ABC' for n in 'XYZ']
print(list_gen4)  # >>> ['AX','AY', ...] , 使用两层循环生成全排列

dict1 = {x: x**2 for x in range(5)}  # 也可以生成dict;
print(dict1)  # >>> {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}


# - 生成器 -----------------
'''
1. 在 Python 中，使用了yield的函数被称为生成器（generator）。跟普通函数不同的是，生成器是一个返回迭代器的函数；
1) 在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回 yield 的值, 并在下一次执行 next() 方法时从当前位置继续运行
2) 直接把列表生成式中的[]改为()就可产生一个生成器；
'''
gen1 = (x * x for x in range(11))  # 没有冒号了；
print(type(gen1), next(gen1), next(gen1))  # >>> <class 'generator'> 0 1

# generator非常强大。如果推算的算法比较复杂，用类似列表生成式的for循环无法实现的时候，还可以用函数来实现;
def fib(max):  # 上述for循环没法穷尽，可用函数来代替；
    n, a, b = 0, 0, 1
    while n < max:
        yield b  # 这是生成generator的另一种方式，即带yield的函数；
        a, b = b, a + b  # 等价于t=(b, a+b), a = t[0], b = t[1], 而绝非 a = b, b = a + b;
        n = n + 1
    return 'done'
f1 = fib(6)
print(type(f1), next(f1), next(f1), next(f1))  # >>> <class 'generator'> 1 1 2

# 简单generator
def odd():
    yield 1
    yield 2
    yield (3)
o = odd()  # 一定要有这一行；而不是直接next(odd),fib那个也是一样；
print(next(o), next(o), next(o))  # >>> 1,2,3

# - 可迭代对象Iterable和迭代器Iterator
'''
1. 可用于for in的是可迭代对象，如list,tuple,dict,set,str，range(),generator等；
2. 迭代器有iter(),next()两个基本用法，可用iter()将list等iterable变成iterator；
3. 已验证，generator既是iterable也是iterator，即都用于for in和next();
'''
# Python的for循环本质上就是通过不断调用next()函数实现的
from collections import Iterable, Iterator

print(isinstance(f1, Iterable), isinstance(f1, Iterator))  # >>> True True
iter1 = iter([1, 6, 3])
print(next(iter1), next(iter1), next(iter1))  # >>> 1 6 3


# 错误、异常处理机制 ----------
# 1） 由try, except, else, finally模块组成；


# 文件读写 ------------
f = open('./tmp/liu.txt', 'w')  # tmp为当前文件夹的子文件夹，必须要有点号，且tmp必须已存在，liu.txt则可有可无；这行代码会清空liu.txt内容;
f.write('my name is liuhengjin, I love wangling\n')
s1 = str([1, 2, 3, 4])
f.write(s1)
f.close()
f = open('./tmp/liu.txt', 'r')
s2 = f.read()
print(s2)

# 计时模块 ----------------
import time
tick = time.time()
print('当前时间戳为：', tick)
delay = 1.2
time.sleep(delay)  # 单位为秒
toc = time.time()
print('%.3f' % (toc - tick), '秒')  # 一定要带上()；

localtime = time.asctime(time.localtime(time.time()))
print(localtime)

# 多进程 --------------




# **************** the end of general python *********************

