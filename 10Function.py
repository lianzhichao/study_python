#def 函数名（参数列表）:
#    函数体
#函数体第一行可以选择性使用文档字符串 用以存放函数说明

def hello():
	'我的第一个自定义函数'
	print("Hello World!")
hello()


def area(width, height):
	return width*height
print(area(20,10))


# 传递的是引用
def change(mylist):
	mylist.append([1,2,3,4])
mylist = ["aa",21]
print(mylist)
change(mylist)
print(mylist)

# 可变对象传递到函数中,被改变的话 , 对象本身也发生变化 , 作用到函数体之外
# 此变化不包括重新赋值
print("------")
def change2(list):
	list = [1,2,3,4]
mylist = ["aa",21]
print(mylist)
change2(mylist)
print(mylist)

# 不可变对象 , 比如 Str , 在函数中重新赋值的话 , 不会影响到函数体之外的对象
def changestr (str):
	str = "inside" 
	print("这是function中 , 值为:",str)
mystr = "outside"
changestr(mystr)
print("这是函数外边 , 值为:",mystr)

def changetuple (tuple):
	tuple = (1,25,2)
	print("这是function中:",tuple)
mytuple = ("12",21,4.4)
changetuple(mytuple)
print("这是函数外边:",mytuple)	


# 必须参数 : 以上正常的写法 , 参数都是必须参数 , 如果不传参的话 ,会报错
print("")
# 一下为传参关键字用法 , 传入参数可以不按照方法参数  , 顺序也可以不一样,  
#但是必须与方法体参数名字对应 , 且如果使用关键字传参 , 必须所有参数都使用这种方法
print("--------------关键字参数-------------")
def printinfo(job , age):
	print("工作:" , job)
	print("年龄:" , age)
printinfo(age = 25 ,job = ["java","python"] )


print("")
print('----------------不定长参数---------------')
# 语法 :def functionname([formal_args,] *var_args_tuple):
# 固定的参数要放在前面 , 不定长的放在后边
def mychangefunc(noneed , *vartuple ):
	"打印任何传入的参数"
	print("输出:")
	for x in vartuple:
		print(x)
	return
mychangefunc(12)
mychangefunc("lian", "python")
mychangefunc("121", "python" , "C++" , "C")


print("")
print("-------------------匿名函数(lambda)----------------------")
# 语法 :lambda [arg1 [,arg2,.....argn]]:expression
sum = lambda arg1 , arg2 : arg1+arg2
print(sum(12,13))

print("")
print("-------------return-------------------")
# return不写的时候 , 或者单独一个return的时候 , 返回值为None
def myreturnfun(arg1 , arg2):
	return arg1+arg2
def myreturnfun2(arg1 , arg2):
	arg1 + arg2
def myreturnfun3(arg1 , arg2):
	arg1 + arg2
	return
print(myreturnfun(4,11))
print(myreturnfun2(4,11))
print(myreturnfun3(4,11))



print(id("aa") , id("aa"))
print(id(12) , id(12))
print(id((1,"a")) , id((1,"a")))