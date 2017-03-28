from collections import deque
queue = deque(["java","python","C++"])
queue.append("C")
queue.append("C#")
print(queue.popleft())
print(queue.popleft())
print(queue.pop())
print(queue)


print("")
vec = [2,4,6]
vec_new = [x*3 for x in vec]
print(vec_new)

vec = [2,4,6]
vec_new = [x*3 for x in vec if x >2]
print(vec_new)

vec = [2,4,6]
vec_new = [[x , x**2] for x in vec]
print(vec_new)

vec = ["2","4","6"]
vec_new = [x*3 for x in vec]
print(vec_new)

vec = ["2","4","6"]
vec_new = [(x,x*2) for x in vec]
print(vec_new)


freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
freshfruit_new = [x.strip() for x in freshfruit]
print(freshfruit_new)

def doublev(num):
	return num*2
vec = ["2","4","6"]
vec_new = [doublev(x) for x in vec]
print(vec_new)


print("")
vec1 = [2,4,6]
vec2 = [1,3,5]
vec_1 = [x*y for x in vec1 for y in vec2]
print(vec_1)


vec1 = [2,4,6]
vec2 = [1,3,5]
vec_1 = [x+y for x in vec1 for y in vec2]
print(vec_1)

vec1 = [2,4,6]
vec2 = [1,3,5]
vec_1 = [vec1[i]*vec2[i] for i in range(len(vec1))]
print(vec_1)


vec_1 = [str(round(355/113, i)) for i in range(1, 6)]
print(vec_1)







print("-----------------------------------------------------")

set_1 = set("asddgfghdsa")
set_2 = set('qwresdfgui')
print( set_1 & set_2)
print( set_1 | set_2)
print( set_1 ^ set_2)
print( set_1 - set_2)
print(set_1 and set_2)
print(set_1 or set_2)
print( not set_2)
# set不支持 + / * 操作
# string/list / tuple 支持 + 操作 ,但是不支持以上四种操作 和 * (支持* 整型)
# dictonary 以上六种操作都不支持
# Number 支持所有以上六种操作
# 都支持 and or  not 操作
# set可以用 比较符号  但是除了完全相同 == 返回True 其他情况无论大于小于还是等于 都是False
#  list/tuple 可以用大小号比较  ,从第一个元素开始比较 , 需要保证相同下标的元素类型一样 
#  比较出一个大小即返回 , 不管后边有多少个元素
# dictonary 只能用 == 和!= 其他比较符都不能用

print({x for x in set_1})
print({x for x in set_1 if x not in 'abc'})


print("Number型")
aa = 3
bb = 2
# 算数运算符
print(aa + bb )
print(aa - bb )
print(aa * bb )
print(aa / bb )
print(aa % bb )
print(aa ** bb )
print(aa // bb )
# 比较运算符
print(aa  == bb)
print(aa != bb)
print(aa > bb)
print(aa < bb)
print(aa >= bb)
print(aa <= bb)
#位运算符
print(aa & bb)
print(aa | bb)
print(aa ^ bb)
print(aa >> bb)
print(aa << bb)
print(~aa)
#成员运算符 , 不支持!!!
#print(2 in 22)
#print(3 not in 22)

print("String型")
str_1 = "aaa"
str_2 = "aab"
# 算数运算符
print(str_1 + str_2 )	#字符串拼接
#print(str_1 - str_2 )
print(str_1 * 2 )		#相当于多个字符串相加
#print(str_1 * str_2 )
#print(str_1 / str_2 )
#print(str_1 % str_2 )
#print(str_1 ** str_2 )
#print(str_1 // str_2 )
# 比较运算符
print(str_1  == str_2)
print(str_1 != str_2)
print(str_1 > str_2)	#大小比较是按照字符从前到后
print(str_1 < str_2)	#一个一个比较转化为ascii的大小
print(str_1 >= str_2)	#如果第一个就比较出来大小 , 后边不再比较
print(str_1 <= str_2)
#位运算符
#print(str_1 & str_2)
#print(str_1 | str_2)
#print(str_1 ^ str_2)
#print(str_1 >> str_2)
#print(str_1 << str_2)
#print(~str_1)
#成员运算符
print("a" in str_1)
print("a" not in str_1)



print("元组型")
tuple_1 = (1 , (3 , "3") , "aa" , 1)
tuple_2 = (1 , (3 , "2") , "bb" )
# 算数运算符
print(tuple_1 + tuple_2 )	#两个元组组合在一起的新元组
#print(tuple_1 - tuple_2 )
print(tuple_1 * 2 )		#相当于多个元组相加
#print(tuple_1 * tuple_2 )
#print(tuple_1 / tuple_2 )
#print(tuple_1 % tuple_2 )
#print(tuple_1 ** tuple_2 )
#print(tuple_1 // tuple_2 )
# 比较运算符
print(tuple_1  == tuple_2)
print(tuple_1 != tuple_2)
print(tuple_1 > tuple_2)		#大小比较 , 索引位置相同的元素做比较
print(tuple_1 < tuple_2)		#在比较出来结果之前的所有元素,必须同为Number或者同为String
print(tuple_1 >= tuple_2)	#比如例子中 ,如果吧tuple_2 的 元素3改为"3" ,则报错
print(tuple_1 <= tuple_2)	#直到某一个索引位置的两个元素比较出大小 ,之后的元素没有类型要求

#位运算符
#print(tuple_1 & tuple_2)
#print(tuple_1 | tuple_2)
#print(tuple_1 ^ tuple_2)
#print(tuple_1 >> tuple_2)
#print(tuple_1 << tuple_2)
#print(~tuple_1)
#成员运算符
print("aa" in tuple_1)
print("aa" not in tuple_1)


print("集合型")
set_1 = {1 , 2 , "aa" ,4}
set_2 = {1 , 3 , "aa" }
# 算数运算符
#print(set_1 + set_2 )
print(set_1 - set_2 )	# 差集 1中有 2中没有的元素组成的新集合
#print(set_1 * 2 )
#print(set_1 * set_2 )
#print(set_1 / set_2 )
#print(set_1 % set_2 )
#print(set_1 ** set_2 )
#print(set_1 // set_2 )
# 比较运算符
print(set_1  == set_2)
print(set_1 != set_2)
print(set_1 > set_2)		# 如果两个集合不相同, 除了 != 其他比较符都为False
print(set_1 < set_2)		# 如果两个集合相同 , == 和 >= <= 都为True
print(set_1 >= set_2)		# > 和< 对于集合没有意义 
print(set_1 <= set_2)

#位运算符
print(set_1 & set_2)	#逻辑与为交集组成的集合
print(set_1 | set_2)	#逻辑或为并集组成的集合
print(set_1 ^ set_2)	#逻辑异或为两集合中不相同的元素组成的集合
#print(set_1 >> set_2)
#print(set_1 << set_2)
#print(~set_1)
#成员运算符
print("aa" in set_1)
print("aa" not in set_1)


print("字典型")
dict_1 = {"id" : 1 , "name" : "lzc"}
dict_2 = {"id":  2 , "job" : "java" }
# 算数运算符
#print(dict_1 + dict_2 )
#print(dict_1 - dict_2 )
#print(dict_1 * 2 )
#print(dict_1 * dict_2 )
#print(dict_1 / dict_2 )
#print(dict_1 % dict_2 )
#print(dict_1 ** dict_2 )
#print(dict_1 // dict_2 )
# 比较运算符
print(dict_1  == dict_2)
print(dict_1 != dict_2)
#print(dict_1 > dict_2)
#print(dict_1 < dict_2)		
#print(dict_1 >= dict_2)		 
#print(dict_1 <= dict_2)

#位运算符
#print(dict_1 & dict_2)	
#print(dict_1 | dict_2)	
#print(dict_1 ^ dict_2)
#print(dict_1 >> dict_2)
#print(dict_1 << dict_2)
#print(~dict_1)
#成员运算符
print("id" in dict_1)	#字典的in 和 not in 判断的是键
print("id" not in dict_1)




print("列表型")
list_1 = [1 , [3 , "a"] , "aa" , 1]
list_2 = [1 , [3 , "a"] , "bb" ]
# 算数运算符
print(list_1 + list_2 )	#两个列表组合在一起的新列表
#print(list_1 - list_2 )
print(list_1 * 2 )		#相当于多个列表相加
#print(list_1 * list_2 )
#print(list_1 / list_2 )
#print(list_1 % list_2 )
#print(list_1 ** list_2 )
#print(list_1 // list_2 )
# 比较运算符
print(list_1  == list_2)
print(list_1 != list_2)
print(list_1 > list_2)		#大小比较 , 索引位置相同的元素做比较
print(list_1 < list_2)		#在比较出来结果之前的所有元素,必须为相同类型
print(list_1 >= list_2)	#比如例子中 ,如果吧list_2 的 元素3改为"3" ,则报错
print(list_1 <= list_2)	#直到某一个索引位置的两个元素比较出大小 ,之后的元素没有类型要求

#位运算符
#print(list_1 & list_2)
#print(list_1 | list_2)
#print(list_1 ^ list_2)
#print(list_1 >> list_2)
#print(list_1 << list_2)
#print(~list_1)
#成员运算符
print("aa" in list_1)
print("aa" not in list_1)
