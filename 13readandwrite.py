s = "Hello World!"
# str(): 函数返回一个用户易读的表达形式
print(str(s))
# repr()：产生一个解释器易读的表达形式。
print(repr(s))
print(str((12,2.2,"aa")))
print(repr((12,2.2,"aa")))


# format()字符串的参数使用{NUM}进行表示,0, 表示第一个参数,1, 表示第二个参数, 以后顺次递加
# 括号及其里面的字符 (称作格式化字段) 将会被 format() 中的参数替换
#可选项 ':' 和格式标识符可以跟着字段名。 这就允许对值进行更好的格式化
#在 ':' 后传入一个整数, 可以保证该域至少有这么多的宽度
# 2d表示两个10进制数的宽度 
for x in range(1, 11):
	print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x),",",'{0:2} {1:3} {2:4}'.format(x, x*x, x*x*x))

print('{1} 和 {0}'.format('Google', 'Runoob'))
print('{name} 的工作是 {job}'.format(name='lian' , job='engineer'))
# 位置以及关键字可以随意组合,  但是关键字参数要放在位置参数后边
print('{0}要努力{done} ,争取{1}'.format('wo','财务自由' ,done='工作'))


#'!a' (使用 ascii()), '!s' (使用 str()) 和 '!r' (使用 repr()) 可以用于在格式化某个值之前对其进行转化:
import math
print('常量 PI 的值近似为： {!r}。'.format(math.pi))
print('heh{}'.format('a'))
print('heh{!r}'.format('a'))
print('heh{!s}'.format('a'))
print('heh{!a}'.format('a'))
# ascii() 功能和 repr() 类似 , 如果输入的字符是非ascii字符 , 会转化
print(ascii("廉"))


table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
print('Runoob: {0[Runoob]:d};Google: {0[Google]:d};Taobao: {0[Taobao]:d}'.format(table))

print('Runoob: {Runoob:d}; Google: {Google:d}; Taobao: {Taobao:d}'.format(**table))



#m.n.	m 是显示的最小总宽度,n 是小数点后的位数(如果可用的话)
# 0	显示的数字前面填充'0'而不是默认的空格
# +	在正数前面显示加号( + )
# %	'%%'输出一个单一的'%'
print('常量 PI 的值近似为：%+09.3f%%。' % 23.32)


#in_str = input("请输入")
#print("你输入的内容是: " , in_str)


print("")
# 打开一个文件
f = open("C:/Users/dell/Desktop/pythontest.txt" , "w")
print(f)
# write() 往文件写入文字, 返回返回写入的字符数
aa = f.write("我叫廉志超 , 我是java程序员 ,我在学习python\n")
bb = f.write("我叫廉志超 , 我是java程序员 ,我在学习python\n")
# 如何要写入非字符串对象 , 需要先转换为字符串
cc = f.write(str(("www.runoob.com" , 14 )))
# 关闭打开的文件
f.close()
print(aa ," " , bb , " " ,cc )

f = open("C:/Users/dell/Desktop/pythontest.txt" , "r")
# read([size]) 读取 , 读取大小可选
print(f.read())
f.close()
f = open("C:/Users/dell/Desktop/pythontest.txt" , "r")
print("1",f.read(20))
print("2",f.read(20))
print("3",f.read(20))
print("4",f.read(10))

f.close()

#readline() 按照行读取 , 如果返回为空字符 , 说明读到头了
f = open("C:/Users/dell/Desktop/pythontest.txt" , "r")
print("l1",f.readline() , end="")
print("l2",f.readline() , end="")
print(" =1=")
print(f.readline())
f.close()


#readlines() 读取所有行 , 参数size可选 , 指定读取几行
f = open("C:/Users/dell/Desktop/pythontest.txt" , "r")
print(f.readlines())
f.close()

#也可以迭代读取
f = open("C:/Users/dell/Desktop/pythontest.txt" , "r")
for line in f:
	print(line , end=",")
print()
f.close()


f = open("C:/Users/dell/Desktop/pythontest.txt" , "rb")
# tell() 返回当前文件指针所在的位置
print(f.tell())
f.readline()
print(f.tell())
# f.seek(offset,from_what) 改变当前文件指针的位置 , offset是要移动的字符数,
#from_what 有三个值 , 0 文件起始位置往后移 , 1表示从当前位置往后移 , 2表示从文件结尾往前移动
# from_what 默认为0 , 返回当前指针位置 
# !!!!!!! 需要以二进制方式打开文件才能进行1 和2 两种操作 , 以文本方式打开 , 只能从文件开头移动
print(f.seek(10))
print(f.tell())
print(f.seek(12,0))
print(f.read(2))
print(f.seek(11,1))
print(f.seek(14,2))

f.close()


f = open("C:/Users/dell/Desktop/pythontest.txt" , "rb")
f.seek(5)
print(f.read(2))
f.close()

# 使用seek方法  , 如果用文本方式打开文件,  重新定位之后 , 读取可能会报错, 
# 因为一个汉字是两个字符 , seek() 可能从一个汉字中分开, 读取就会发生错误
f = open("C:/Users/dell/Desktop/pythontest.txt" , "r")
f.seek(10)
print(f.read(2))
#f.seek(3)
#print(f.read(2))


f = open("C:/Users/dell/Desktop/11.png" , "rb")
print(f.read(20))


print("====================")
#序列化和发序列化
#pickle.dump(obj, file, [,protocol]) 接口可以将对象序列化到文本中
output = open("C:/Users/dell/Desktop/seria.pkl" , "wb")
ser_list = ["A",12, 3-4j]
ser_list.append(["A" , 3.3 , 4+2j , (1,2)])

ser_dict = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}
import pickle
# Pickle dictionary using protocol 0.
pickle.dump(ser_dict , output )
# Pickle the list using the highest protocol available.
pickle.dump(ser_list , output )
output.close()


#pickle.load(file)  可以从文本中读取对象
output = open("C:/Users/dell/Desktop/seria.pkl" , "rb")
data_1 = pickle.load(output)
print(data_1)
data_2 = pickle.load(output)
print(data_2)
print(len(data_2))
print(data_2[3][3])
output.close()



print("---------------")
f = open("C:/Users/dell/Desktop/pythontest.txt" , "r")
print(f.fileno())
f.close()

f = open("C:/Users/dell/Desktop/11.png" , "rb")
print(f.fileno())
print(f.name)
print(f.isatty())
print(next(f))
print(next(f))
f.close()

print("---------------")
# writelines() 可以输入一个序列  但是必须是字符串
f = open("C:/Users/dell/Desktop/pythontest.txt" , "a+")
seq_1 = ("you are the one\n" , "12121212\n" , "我们")
f.writelines(seq_1)
f.close()


#runcate() 方法用于截断文件，如果指定了可选参数 size,则表示截断文件为 size 个字符 
#close()后文件只保留阶段的字符
#如果没有指定 size，则重置到当前位置。
f = open("C:/Users/dell/Desktop/pythontest.txt" , "r+")
print(f.read(3))
print("----")
f.truncate()
print(f.read())
f.close()


