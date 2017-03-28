#python变量不需要声明  每个变量在使用前必须赋值,赋值之后才会被创建
#python中变量没有类型,此处的类型指的是存储到内存中的对象类型
counter = 10 		#整型变量
miles = 1000.0		#浮点型变量
name = "runoob"	#字符型变量
print(counter)
print(miles)
print(name)
#python中可以同时创建多个变量
a = b = c = 1			#三个变量被分配到 相同的内存空间上
a , b , c  = 1 , 2 ,"runoob"	#同时赋值三个变量
#python中有六个标准数据类型
#Number 数字 
#String 字符
#List 列表
#Tuple 元组
#Sets集合
#Dictionary字典
#Number
#python3中 支持int  float bool complex(复数)
# type() 可以返回该变量的类型
print("\n\n\n--------数值型---------")
a, b, c, d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d))
#也可以用 isinstance(param,type)
a=11
print(isinstance(a,int))
#区别 :
# type 不认为子类是一种父类的类型 
# instance 认为 子类是一种父类的类型
class A:
	pass
class B(A):
	pass
print(type(A()) == A)
print(isinstance(A(),A))
print(type(B()) == A)
print(isinstance(B(),A))

#在Python2中没有布尔型  用数字0代表False 1代表True
#Python3中 True和False 是关键字  但是他们的值还是1 和0 ,可以进行数字相加
print("\n\n\n---------bool 运算---------")
a = True
b = False
print(a)
print(b)
print(a +b)
print(a - b)
print(a * b)
print(b / a)

#当指定一个值时 Nbmber对象就会被创建
print("\n\n\n---------删除元素---------")
var1 = 1
var2 = 10
print(var1)
print(var2)
# del 可以用来删除对象引用 , 可以删除一个或者多个,删除之后,这个变量将不存在 not defined
del var1,var2

#1、Python可以同时为多个变量赋值，如a, b = 1, 2。
#2、一个变量可以通过赋值指向不同类型的对象。
#3、数值的除法（/）总是返回一个浮点数，要获取整数使用//操作符。
#4、在混合计算时，Python会把整型转换成为浮点数。
# 运算
print("\n\n\n---------运算---------")
print(5+4)
print(4.3-2)
print(3*7)
print(2/4)
print(2//4)	# //除法 得到一个整数
print(17%3)	#取余
print(2 ** 5)	#乘方



#String类型
print("\n\n\n---------字符串---------")
# 字符串可以用 单引号 ' ' 也可以用 双引号" "
# 字符串截取语法  变量[头下标:尾下标]  	不包含尾下标
# 索引为从0 开始, 负数索引为从最后开始计算 -1开始
str  = "runoob"
print(str[0])	#返回第一个字符
print(str[1:3])	#第二个字符到第四个字符
print(str[1:-1])	#第二个字符到倒数第二个字符
print(str[1:])	#第二个字符到最后
print(str * 2)	#输出两遍字符
print(str + "Test")
#python字符串不可改变 ,如果赋值 str[0]="m" 会报错
#strutf = "廉志超工程师"
#print(strutf[1:-1])


#List 列表
print("\n\n\n---------List列表---------")
#列表中元素类型可以不相同
list = ["abcd", 22, 2.33, True, 123, 22]
print(list)
#列表的截取方式和string类型一样, 变量[头下标:尾下标] 
tinylist = [123, "runoob"]
print(list[0])
print(list[2:3])
print(list[1:-1])
print(list[1:])
print(tinylist * 2)
print(list + tinylist)
#不同的是列表中的元素值可以改变
print("------")
a = [1,2,3,4,5,6]
print(a)
a[0] = 12
print(a)
a[1:3] = [7,6,8]
print(a)
a[1:4] = [3,3]
print(a)
a[2:4] = []	#删除
print(a)


#Tuple 元组
print("\n\n\n---------Tuple 元组---------")
# 和列表类似  不同的是元组的元素不能修改  写在() 中, 类型也可以不同
tuple = (12, "aa", True, 12.12, 'runoob')
print(tuple)
tup1 = ()    # 空元组
print(tup1)
tup2 = (20,) # 一个元素，需要在元素后添加逗号
print(tup2)
tinyTyple = (True, "呵呵")
print(tuple[0])
print(tuple[1:3])
print(tuple[2:])
print(tinyTyple * 2)
print(tuple + tinyTyple)
tuple  = tuple + (["bb", 13 , False],)
print(tuple)
tuple[5][1] = "cc"
print(tuple)

#Set 集合
print("\n\n\n---------Set 集合---------")
# set是一个无序不重复的集合
# 可以用 ({}) 或者set() 创建新的set集合  但是空集合 只能用set()
# set() 参数为单个, 一个字符串或者另外一个set集合、list列表、tuple 元组 , 不可以是number 和 对象
setTemp =  ({"Tom", "Jim", "Mary", "Tom", "Jack", "Rose"})
print(setTemp)
if("Rose" in setTemp):
	print("Rose is in")
else :
	print("Rose is not in")
a = setTemp
b = {"Tom", "Lian", "Jack", "Chan", "Lee"}
print(a - b)
print(a | b)
print(a & b)
print(a ^ b)
c = set('asdkfjskd')
print(c)
d = set(b)
print(d)
e = set([1,"dd"])
print(e)
f = set((2,))
print(f)


# Dictionary 字典
print("\n\n\n---------Dictionary 字典---------")
""" Dictionary 是无序的对象集合 , 和list不同 , 它通过键(key) 来存取,而不是list那样偏移存取 
用{} 表示 key必须是不可变类型  元组可以 , 字符串 , Number , 对象也可以  
但是list不可以作为key , set也不可以 , dict字典本身也不可以
dist.keys()   dist.values() 可以获取dict字典的键列表  和值列表   """
dict = {}
dict['one'] = "1-菜鸟教程"
dict[2] = "2 - 菜鸟工具"
print(dict)
class B:
	lst = 1
	ll = "ll"
tinyDict = {"name":"lianzc", "age":25, "3": [1], 4:("data",), ("nimei",):23, "name": "deng",B():2}
print(tinyDict)
print(tinyDict["name"])
print(tinyDict[("nimei",)])
print(tinyDict.keys())
print(tinyDict.values())

'''dict()是Python的一个函数，但之前将dict自定义为一个python字典，
在之后想调用dict()函数是会报出“TypeError: 'dict' object is not callable”的错误，
只需将之前自定义的变量delete掉即可。'''
del(dict)
#dict 可以直接用dict() 构建字典
oneDict = dict([("runoob",1), ("菜鸟教程","2"), (3,"呵呵")])
print(oneDict)
towDict = {x : x * 2 for x  in ("2","呵呵",6)}
print(towDict)
threeDict = dict(Runoob=1,Google=2,cc=3)
print(threeDict)
# clear() 可以清空dict
threeDict.clear()
print(threeDict)


# 元素类型之间转换
print("\n\n\n---------元素类型之间转换---------")
print(int(4.65))
print(float(12))
print(complex(2,3.4))
del str
print(str({"12",12}))
print(repr({"12",12}))
print(chr(97))
print(ord("z"))
print(hex(1337))
print(oct(1633))
