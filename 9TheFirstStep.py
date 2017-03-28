print("斐波那契:")
a , b = 0,1
while b < 1000:
	print(b , end=",")
	a , b = b , a+b

'''
print("--------------------------")
age = int(input("请输入你家狗狗的年龄: "))
print("")
if age < 0:
	print("你是在逗我吧!")
elif age == 1:
	print("相当于 14 岁的人。")
elif age == 2:
	print("相当于 22 岁的人。")
elif age > 2:
	human = 22 + (age -2)*5
	print("对应人类年龄: ", human)
### 退出提示
input("点击 enter 键退出")
'''

"""
print("")
number = int(input("请输入你的底牌数字:"))
guess = -1
while number != guess:
	guess = int(input("请输入你猜的数字:"))
	if guess == number:
		print("恭喜你猜对了")
	elif guess > number:
		print("你猜的数字太大了")
	else:
		print("你猜的数字太小了")	
"""


print("")
count = 0 
while count < 5:
	print(count, "小于5")
	count = count+1
else:
	print(count , "大于等于5")


print("")
language = ["java","C","C++","Python"]
cc = 0;
for x in language: 
	cc = cc +1
	print(x)
else:
	print(cc)

print("")
for x in "abcdefghijklmnopqrstuvwxyz":
	print("当前字母:" , x)
	if ord(x) > ord("d"):
		break
else:
	print("没走到最后?")

print("")
for x in "abcdefghijklmnopqrstuvwxyz":
	print("当前字母:" , x)
	if ord(x) > ord("d"):
		continue
else:
	print("没走到最后?")

print("")
for x in "asdfg":
	pass
	print(x , end=",")


print("")
for x in range(10):
	print(x , end=",")

print("")
for x in range(11,22):
	print(x,end=",")

print("")
print("range() 参数写成单个负数无效")
for x in range(-5):
	print(x , end=",")

print("")
print("range() 参数第二个参数比第一个参数小 , 无效")
for x in range(10,5):
	print(x,end=",")

print("")
for x in range(-25 , -15 ):
	print(x , end=",")

print("")
for x in range(-5 , -15 , -3):
	print(x , end=",")

print("")
for x in range(22 , 10 , -4):
	print(x , end= ",")



print("----------------------------")
for i, j in enumerate("asdfgh"):
	print(i , j)



print("-----------迭代器---------")
_list = [12,"test","和" , "qq" , "python"]
_it = iter(_list)
print(next(_it))
print(next(_it))
for x in _it :
	print(x)
try:
    next(_it)
except StopIteration:
    print("exception done")

print("")
print("-------生成器(generator)------")
#生成器函数(generator)
def fibonacci(n):
	a  , b , count  = 0 , 1 ,0
	while True:
		if(count > n ):
			return
		yield a
		print(count , end= " →   ")
		a , b = b , a + b
		count += 1
# 如果注释掉yield 则调用该函数 , 会将打印信息全部打印出来
# 但是使用yield 会在第一次循环的时候就暂停,  在迭代器迭代的时候才会继续往下执行
# yield 只能放在function中
b = fibonacci(10)
while True:
	try:
		print(next(b) , end = '| ')
	except StopIteration:
		break


