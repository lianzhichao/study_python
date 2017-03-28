# python 不需要{} () 来实现代码块 直接用同行缩进表示 , 如果同一代码块缩进不同 就会报错
if True:
   print('True')
   print("question")
else:
   print('False')	
   print("answer")
#一行放不下时 , 可以用可以用反斜杠 \ 实现多行
total =  "item_one"  +\
	"item_two"  +\
	"item_three"
print(total)
total = ["total_one","total_two","total_three"]
print(total)
#复数运算
a = 1.1+2.2j
b = 1+2j
print(a+b)
print(a-b)
print(a*b)
print(a/b)
#python中单引号和双引号完全相同 """ '''可以指定一个多行字符串
word = '字符串'
sentence = "这是一个句子."
paragraph = """这是一个段落,
可以由多行组成"""
print(word)
print(sentence)
print(paragraph)
# 在字符串前面加上r或者R 表示自然字符串
print("this is a line with\nreturn")
print(r"this is a line with\n return but have r")
print(R"this is a line with\n return but have R")
# 用前缀u或者U表示unicode string
print("this is an unicode string")
print(u"this is an unicode string")
print(U"this is an unicode string")
# python按照字面意义级联字符串 如下边不需要加号也可以
print("this ""is ""string")
#input  等待用户输入
#x = input("\n按下enter键后退出\n")
#print(x)
#python同一行可以写多条语句,用;分开
import sys; x='runoob'; sys.stdout.write(x+'\n')
#缩进
if 1==2 :
	"tt"
elif 2==2 :
	"ee"
else :
	"ss"
#print 默认输出是换行的,如果不想要换行,要在变量末端加上end=""
a="aa"
b="bb"
print(a)
print(b)
print(a,end=" ")
print(b,end="")
