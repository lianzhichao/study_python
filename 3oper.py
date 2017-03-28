#python运算符
print("--------算数运算符--------")
a = 10
b = 5
print( a + b)
print(a - b )
print(a * b)
print( a ** b)
print(a / b)
print(a // b)
print(a % b)

# 比较运算符
print("----------比较运算符-----------")
print( a == b)
print( a != b)
print( a > b)
print( a >= b)
print( a < b)
print( a <= b )

#赋值运算符
print("-----------赋值运算符------------")
c = a +b
c += a
c -+ a
c *= a
c /= a
c %= a
c **= a
c //= a
print(c)

#位运算符
print("-----------------位运算符------------")
a = 60		# 60 = 0011 1100 
b = 13		# 13 = 0000 1101 
print(a & b)
print(a | b)
print(a ^ b)
print( ~a)
print( a << 2)
print( a >> 2)


#逻辑运算符
print("--------------逻辑运算符--------------")
# python中 数字 0 位False  非0 为True
a = 10
b = -10
if(a and b):
	print("and : 两个都为True则为True")
else:
	print("and : 其中有一个为False 则为False")
b = 0
if(a and b):
	print("and : 两个都为True则为True")
else:
	print("and : 其中有一个为False 则为False")
if(a or b):
	print("or : 其中一个为True则为True")
else:
	print("or : 两个都为False 则为False")
a = 0
if(a or b):
	print("or : 其中一个为True则为True")
else:
	print("or : 两个都为False 则为False")
if ( not a):
	print("not : 取反1")
else:
	print("not : 取反2")
c = 1
if(a and c and b):
	print("aa")
if(a or c or b):
	print("bb")
if(c or (a and b)):
	print("cc")

#成员运算符 in 和 not  in 支持 字符串 列表 集合 元组
print("---------------成员运算符-------------")
aaList = ["aa","vb","runoob"]
if("aa" in aaList):
	print("aa 在list中")
else:
	print("aa 不在list中")
bbSet = ({"你是",2,"hhh"})
if("bb" not in bbSet):
	print("bb 不在set中")
else:
	print("bb在set中")

strStr = "aadsjfksj"
if("aa" in strStr):
	print("aa 在字符中")

#身份运算符
print("------------身份运算符---------------")
abc = "vvv"
print(id(abc))
abc = "aaa"
print(id(abc))
cba = "aaa"
print(id(cba))
bac = "ddd"
if(bac is cba):
	print("hehe")
else:
	print("nini")	
if(cba is abc):
	print("ksks")
if( bac is not cba):
	print("sd")


ablist = ["2",2,"lian"]
bclist = ["2",2,"lian"]
print(id(ablist))
print(id(bclist))
ablist[2] = "lee"
print(id(ablist))