# 函数 -------------------
# 1. 参数定义的顺序必须是：位置参数、默认参数、可变参数（包裹）、命名关键字参数和关键字参数(包裹)。最好不要都用上；
# 2. 没有return默认返回None；return None可以简写为return
# 3. 可以return多个值，其实是组成一个tuple返回，可以发现所有没有括号的，都默认为tuple类型；
# 4. *表示标识后面为命名关键字参数，而*s表示s是可变参数，可以接受值；
# 5. 对于位置参数和命名关键字参数，调用时个数必须相等（除非默认值），且前者靠前，或者参数名必须带上且不能错；
def func1():
    print('hello python')
    pass
a = func1()  # 一定要有(); print(a)->None；

def func2(a, b):
    tmp1 = a + b
    tmp2 = a - b
    return tmp1, tmp2
print(func2(8.3, 4))  # 函数参数个数或类型不对，都会报错；
print(func2(b=4,a=8))  # >>> (12, 4), 位置参数也可通过命名关键字参数的方式来传递，顺序不限；

def func3(name, school):
    return name - school
print(func3(3, 8))
print(func3(school=8, name=3))  # 与上列效果相同,这种也是关键参数方式，**那种方式叫包裹关键字参数；
# print(func3(name=8, 3))  # 出错，位置参数在前，关键字参数在后；

def func4(a, b=3, city='beijing'):
    return a - b, city
print(func4(5, city='university'))  # 位置参数在前，默认参数在后；

def func5(a, b, *c):  # 参数位置：位置参数，默认参数，可变参数；
    return c
print(func5(2, 3, *(9, 8)))  # 加*，输出(9, 8)；不加，输出((9, 8),)
print(func5(2, 3, 9, 8, 'liu'))  # >>> (9, 8, 'liu')，可变参数在调用时自动组装为tuple；
print(func5(2, 3))  # >>> (), 可变参数可以是0个；


def func6(a, b, **kwords):  # 关键字参数可以传入任意不受限制的关键字参数，且没有顺序之分；**可称为包裹关键字参数；
    return a + b, kwords
print(func6(2, 3))  # >>>(5, {})  # 可接受0-N个关键字参数，并自动组装为dict；位置参数始终不能省；
print(func6(2, 3, name='liu', num=5))  # >>> (5, {'name': 'liu', 'num': 5})
# print(func6(2,3,name='liu',num=5,45))  #45会被认为是位置参数，其不能在关键字参数后面，会出错，因此必须带上参数名；
dict1 = {'name': 'liu', 'num': 5}
print(func6(2, 3, num=dict1['num'], name=dict1['name']))  # 如已经是dict了，可通过这种方式输入关键字参数；
print(func6(2, 3, **dict1))  # 更简单的方法，*和**称为解包裹。

def func7(a, b, *, name, num):  # 命名关键字参数可限制参数的名字；如果没有可变参数，必须加一个*，*后的参数被视为命名关键字参数；
    return a + b, name, num
print(func7(2, 3, name='liu', num=5))  # 命名关键字参数必须传入参数名，且不能像关键字那样多传几个；
# 这里只能输入2个位置参数，func7(2,3,'liu',5)会被认为是4个位置参数，因为没有可变参数接收值，出错；

def func8(a, b, *s, name='liu', num):  # 命名可以带默认参数，且不用放在最右边，因为必须传入参数名；
    return a + b, s, name, num
print(func8(2, 3, 4, 8, num=9))  # >>> (5, (4, 8), 'liu', 9); 默认值不同才需要传入；
# 对比func7和func8，单纯*号只起标识作用，而*s则表示可变参数，是可以接受参数的；

def func_comb1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
func_comb1(1, 2)  # >>> a = 1 b = 2 c = 0 args = () kw = {}
func_comb1(1, 2, 3, 'a', 'b')  # >>> a = 1 b = 2 c = 3 args = ('a', 'b') kw = {}
func_comb1(1, 2, 3, 'a', 'b', x=99)  # >>> a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'x': 99}

def func_comb2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
func_comb2(1, 2, 3, d=99, ext=None)  # >>> a = 1 b = 2 c = 0 d = 99 kw = {'ext': None}
# func_comb2(1, 2, 3, 4, d=99, ext=None) # 出错，这里*表示标识作用，不能接受多余的4；

def func_comb3(a, b, c=0, *args, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'd =', d, 'kw =', kw)
func_comb3(1, 2, 3, 4, 'm', d=6, x=7, y='n')  # >>> 这里args是可变参数，可以接收值；

args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
func_comb1(*args, **kw)  # >>> a = 1 b = 2 c = 3 args = (4,) kw = {'d': 99, 'x': '#'}
args = (1, 2, 3)  # 从func_comb2的定义看，不能传入4个数；
kw = {'d': 88, 'x': '#'}
func_comb2(*args, **kw)  # >>> a = 1 b = 2 c = 3 d = 88 kw = {'x': '#'}
# 对于任意函数，都可以通过类似func(*args, **kw)的形式（即解散后重组）调用它，无论它的参数是如何定义的。

'''python中参数传递分为传不可变对象和传可变对象，效果分别和C++的值传递（不会被修改）和引用传递一样'''

# lambda匿名函数 ---------------
c = 3.5
sum1 = lambda a, b=9: a + b + c  # 用法为： lambda arg1, arg2, ...: expression， 可带默认参数；
print(sum1(3))  # >>>15.5
print(sum1(b=3, a=5))  # >>>11.5 ，也可用关键字参数进行传递,且顺序不限；
# lambda 函数有自己的命名空间，除自己参数列表和全局命名空间里的参数，均不能访问；


# 函数名作为参数 ---------------
def sayhello():
    print('hello')
def execute(f):
    f()
execute(sayhello)  # >>> hello


# 函数内变量的作用域  -------------------
# 1. 以 L –> E –> G –>B 的规则查找，即：在局部找不到，便会去局部外的局部找（例如闭包），再找不到就会去全局找，再者去内建中找；
# 2. Python 中只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，其它的代码块（如 if/elif/else/、
#    try/except、for/while等）是不会引入新的作用域的，也就是说这些语句内定义的变量，外部也可以访问;

x = 1.0
def outer():
    x = 2.0
    def inner():
        i = 1.0
        print(x)
    inner()  # 这行不能少，表示执行inner()；可以再函数内定义某函数，并立即执行；
outer()  # >>> 2.0

if True:
    a = 'liu'
print(a)  # >>> liu, 外部也可以访问；


# global 和 nonlocal关键字 -------------------
# 1. 内部函数，不修改全局变量可以访问全局变量；内部函数，修改同名全局变量，则python会认为它是一个局部变量；
# 2. 当内部作用域想修改修改全局变量，需要使用 global 关键字声明；
# 3. 如果要修改闭包作用域（即嵌套作用域或外层非全局作用域）中的变量则需要 nonlocal 关键字声明；
# 4. 注意函数内部出现先应用后赋值的错误；

total = 0  # 这是一个全局变量
def sum(arg1, arg2):
    total = arg1 + arg2  # total在这里是局部变量.
    print("函数内是局部变量 : ", total)
    return total
sum(10, 20)  # >>> 30
print("函数外是全局变量 : ", total)  # >>> 0， 并没有修改全局变量total值；

num = 1
def fun1():
    global num   # 修改全局变量，需要使用 global 关键字声明
    print(num)   # 注释global这行，则num为局部变量，虽然可以往外找值，但若后面有对他的赋值，则会出现引用后才赋值的错误：local variable 'num' referenced before assignment；
    num = 123    # 若注释上面两行，则num被修改，是局部变量；
    print(num)
fun1()  # >>> 1, 123
print(num)  # >>> 123，依然是123

a = 10
def test():
    b = a + 1  # 若b改为a, 则a有被修改，被认为是局部变量，就出现了引用后才赋值的错误: local variable 'a' referenced before assignment。
    print(a, b)
test()
a = a + 1  # >>> 11, 上述问题只会出现在函数内部，函数外部没关系；

# 如果要修改闭包作用域（即嵌套作用域或外层非全局作用域）中的变量则需要 nonlocal 关键字；
def outer():
    num_t = 10
    def inner():
        nonlocal num_t  # nonlocal关键字声明
        num_t = 100
        print(num_t)
    inner()
    print(num_t)
outer()  # >>> 100, 100， 如果把nonlocal那行注释，则输出100,10，因为内部函数要修改num_t的话，会被认为是局部变量；
# print(num_t)  >>> 函数内变量，外部不能引用；NameError: name 'num_t' is not defined


## 高阶函数 -------------------
'''
1. 函数名作为函数入参或出参的称为高级函数；
   1） 函数名其实就是指向函数的变量！
   2） 函数的参数能接收变量，因此函数名可作为入参和出参；
   3)  map/reduce/filter/sorted
'''

f1 = abs
print(f1(-4.3))  # 通过变量调用

def abs_sum(x, y, f):
    print(f(x) + f(y))
abs_sum(3, -4.5, f1)  # >>> 7.5;

# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素。
map1 = map(f1, [1, 3, -4.5, -8])
print(type(map1))  # <class 'map'>，需要list/tuple才可显示出来，分别输出为list/tuple类型;
print(tuple(map1))  # >>> [1, 3, 4.5, 8]

# reduce()把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和
# 序列的下一个元素做累积计算，其效果就是：reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
from functools import reduce  # 需要import
def add1(x, y):
    return x + y
reduce1 = reduce(add1, [1, 3, 5])
print(reduce1, type(reduce1))  # 9 <class 'int'>，int类型，无需用list/tuple显示；

# filter()把传入的函数依次作用于序列的每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
def is_odd(n):
    return n % 2 == 1
filter1 = filter(is_odd, [1, 2, 3, 4])
print(tuple(filter1), type(filter1))  # (1, 3) <class 'filter'>  # 需用list/tuple显示

# sorted()可以接收一个key函数来实现自定义的排序；
print(sorted([1, 9, 3, -8, -5]))  # >>> [-8, -5, 1, 3, 9]
print(sorted([1, 9, 3, -8, -5], key=abs))  # >>> [1, 3, -5, -8, 9]


# 函数作为结果返回 ----------------
# 1） 例子：可变参数求和；如果不需要立即求和，可以不立即返回求和结果，而是返回求和的函数；
# 2） 内部函数sum可以引用外部函数lazy_sum的参数和局部变量；
# 3） 当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力；
# 4） 每次调用都会返回一个新的函数，即使每次输入的参数完全一样；
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
f = lazy_sum(1, 2, 3, 4)  # >>> 注：不能是list，即加[]，否则ax=ax+n会出现int和list相加的错误；
print(f)  # >>> <function lazy_sum.<locals>.sum at 0x0000000002877488>
print(f())  # >>> 10，调用f时才真正执行计算；

# 装饰器 -----------------
# 参考：看完这篇文章还会不懂Python装饰器？掐死小编吧
# 功能：本质就是函数，功能是装饰其他函数，其实就是给其他函数添加附加功能；高阶函数+嵌套函数===装饰器
# 原则：1）不能修改被装饰的函数的源代码；2）不能修改被装饰的函数的调用方式；
## 1. @w1作用：
#    1）执行w1函数，并将@w1下面的函数f1作为w1的参数，即@w1 等价于 w1(f1)；
#    2）将执行完的 w1 函数返回值赋值给@w1下面的函数的函数名；
#    3）先执行新f1函数，在新f1函数内部先执行验证，再执行原来的f1函数，然后将原来f1函数的返回值返回给了业务调用者。
def w1(func):
    def inner(x, y):  # 注意：inner才是新的f1，因此参数是放在这里；其实就是将原来的 f1 函数塞进另外一个函数中
        print('checking...')
        print('验证完毕')
        return func(x, y) # 如改为 return func(x, y) ,999； 则>>> (3, 999)
        # 将原来f1函数的返回值return给了业务调用者，逻辑上不能return其他东西，否则会影响调用者的输出结果;
    return inner
@w1   # 可以用此装饰多个函数；
def f1(a, b):
    print('print f1')
    return a + b
print(f1(1,2))

# 让装饰器带参数：和上一示例相比在外层多了一层包装,内层没变；
def w0(para):
    def w1(func):
        def inner(x, y):
            print(para)
            print('checking...')
            print('验证完毕')
            return func(x, y)
        return inner  # 其实就是将原来的 f1 函数塞进另外一个函数中
    return w1
@w0('----liuhengjin----')   # 这里是w0;
def f2(a, b):
    print('print f1')
    return a + b
print(f2(1,2))

# 可以装饰具有处理n个参数的函数的装饰器
'''
def w1(func):
    def inner(*args,**kwargs):
        # 验证1
        # 验证2
        # 验证3
        return func(*args,**kwargs)
    return inner
@w1
def f1(arg1,arg2,arg3):
    print('f1')
'''
# 一个函数可以被多个装饰器装饰
def w1(func):
    def inner(*args,**kwargs):
        # 验证1
        print('装饰器w1')
        return func(*args,**kwargs)
    return inner
def w2(func):
    def inner(*args,**kwargs):
        # 验证1
        print('装饰器w2')
        return func(*args,**kwargs)
    return inner
@w1
@w2
def f1(arg1,arg2,arg3):
    print('f1...')
    return arg1 + arg2 + arg3
print(f1(1,2,3))  # 需要print;



# 类 ---------------
# 1. 类的定义
class Hotel(object):  # 如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类;
    def __init__(self, room, cf=1.0, br=15):
        self.room = room
        self.cf = cf
        self.br = br

    def cacl_all(self, days=1):
        return (self.room * self.cf + self.br) * days

if __name__ == '__main__':
    stdroom = Hotel(200)    # 先初始化，后调用类中方法；
    big_room = Hotel(230, 0.9)
    print(stdroom.cacl_all(), stdroom.cacl_all(2), big_room.cacl_all(), big_room.cacl_all(3))  # >>> 215.0 430.0 222.0 666.0

# 2. 类的继承: 子类可以继承父类的所有方法和属性，也可以重载父类的成员函数及属性
class CAnimal(object):
    def __init__(self, voice1='hello'):  # voice初始化默认为hello
        self.voice = voice1
    def Say(self):
        print(self.voice)
    def Run(self):
        pass  # 空操作语句（不做任何操作）
t = CAnimal()
t.Say()
dog = CAnimal('wow')  # 类定义时不需要携带参数列表，初始化时才需要；
dog.Say()

class CDog(CAnimal):  # 继承类CAnimal
    def SetVoice(self, voice):  # 子类增加函数SetVoice
        self.voice = voice
    def Run(self):  # 子类重载函数Run
        print('Running')
bobo = CDog()
bobo.SetVoice('My Name is BoBo!')  # 设置child.data为hello
bobo.Say()  # My Name is BoBo!
bobo.Run()  # Running  # 重载了；
