# oop

class MyClass:
	'''一个简单的类实例'''
	i = 1234
	def f(self):
		return 'hello world'

#类实例化
x = MyClass()
#访问
print(x.i)
print(x.f())
MyClass.i = "a"
print(x.i)



# self 代表实例 , 而不是类
print("-----------------------------")
class Complx:
	def __init__(self , realpart , imagpart):
		self.r = realpart
		self.i = imagpart

x = Complx(1.2 , "aa")
print(x.r , x.i)
Complx.r = 1
Complx.i = "b"
print(x.r , x.i)
x.r = "1.1"
x.i = 2
print(x.r , x.i)




print("===================")
#类的方法与普通的函数只有一个特别的区别
#——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是 self
class Test:
	def prt(self):
		print(self)
		print(self.__class__)
t = Test()
t.prt()

Test.prt(1)
Test.prt(Test)
Test.prt(Test())


#self并不是python关键字 , 把self换成其他也是可以正常执行的 , 但是必须有一个代表自身的参数
class Test:
    def prt(runoob):
        print(runoob)
        print(runoob.__class__)
 
t = Test()
t.prt()


print("")
print("============")
print("")
# 类的方法
class Peopel:
	# 直接写在类中的属性 , 可以直接使用类来访问 
	# 写在构造方法中的 , 只能用对象访问 , 用类访问不到
	# 用对象访问属性 , 是访问构造方法中的 , 如果构造方法中没有
	# 再访问类中的公共属性
	aa = "aa"
	name = ' '
	age =  0
	# 私有化属性 , 类外部无法直接访问 双 "_"下划线
	__weight = 0
	# 定义构造方法
	def __init__(self , n , a , w):
		self.name = n
		self.age = a
		self.__weight = w
	def speak(self):
		print("%s 说: 我%d岁了 , 体重 %dkg" % (self.name , self.age , self.__weight))
		print("--")
		self.__talk()
	# 私有化方法
	def __talk(self):
		print("%s%d岁了,重 %dkg" % (self.name , self.age , self.__weight))

p = Peopel('小明' , 11 , 30)
p.speak()
print(p.name)
print(p.age)
#print(p.__weight)
#p.__talk()
print(Peopel.age)
Peopel.age = 12
print(p.age)



#继承
class student(Peopel):
	grade = ' '
	def __init__(self , n , a , w , g):
		#调用父类构造器
		Peopel.__init__(self , n , a , w)
		self.grade = g
	#复写父类的方法
	def speak(self):
		print("%s 说: 我 %d 岁了，我在读 %d 年级"%(self.name,self.age,self.grade))

s = student('ken',12 , 60 , 3)
s.speak()
print(s.grade)
print(student.grade)


#另一个类，多重继承之前的准备
class speaker():
    topic = ''
    name = ''
    def __init__(self,n,t):
        self.name = n
        self.topic = t
    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s"%(self.name,self.topic))

#多重继承
class sample(speaker,student):
    a =''
    def __init__(self,n,a,w,g,t):
        student.__init__(self,n,a,w,g)
        speaker.__init__(self,n,t)

test = sample("Tim",25,80,4,"Python")
test.speak()   #方法名同，默认调用的是在括号中排前地父类的方法
print(test.topic)


#复写 -- 参照student



'''类的私有属性
__private_attrs：两个下划线开头，声明该属性为私有，不能在类地外部被使用或直接访问。
在类内部的方法中使用时 self.__private_attrs。
类的方法
在类地内部，使用def关键字可以为类定义一个方法，与一般函数定义不同，
类方法必须包含参数self,且为第一个参数
类的私有方法
__private_method：两个下划线开头，声明该方法为私有方法，不能在类地外部调用。
在类的内部调用 self.__private_methods。'''


'''类的专有方法：
__init__ : 构造函数，在生成对象时调用
__del__ : 析构函数，释放对象时使用
__repr__ : 打印，转换
__setitem__ : 按照索引赋值
__getitem__: 按照索引获取值
__len__: 获得长度
__cmp__: 比较运算
__call__: 函数调用
__add__: 加运算
__sub__: 减运算
__mul__: 乘运算
__div__: 除运算
__mod__: 求余运算
__pow__: 称方'''

#运算符重载(相当于java 对象重写equles() 方法)

class Vector:
   def __init__(self, a, b):
      self.a = a
      self.b = b

   def __str__(self):
      return 'Vector (%d, %d)' % (self.a, self.b)
   
   def __add__(self,other):
      return Vector(self.a + other.a, self.b + other.b)

v1 = Vector(2,10)
v2 = Vector(5,-2)
print (v1 + v2)


