#Number 类型的 函数
print("-----------------数学函数----------------")
print("abs(x) ,  绝对值:" , abs(-10.1))
import math
print("math.fabs(x) , 绝对值:", math.fabs(-10.1))
"""abs 和math.fabs的区别   前者是内置函数 , 后者在math模块中
fabs只对整型和浮点型有效  对复数型数字无效"""

print("math.ceil(x) 向上取整:" , math.ceil(2.6))
print("math.floor(x) 向下取整:",math.floor(2.6))
print("round(x[n]) 四舍五入, 默认取整数" , round(12.5254))
print("round(x[n]) 四舍五入 , 可以选择保留小数位数" , round(12.5254,2))
print("math.exp(x) e的x次幂", math.exp(3))
print("max(v1,v2) 返回参数的最大值:" , max(1,3,12,55,2,132))
print("min(v1,v2) 返回参数的最大值:" , min(1,3,12,55,2,132))
print("math.modf(x) 返回x的整数部分和小数部分",math.modf(-12.34))
print("pow(x, y) 返回x**y:",pow(12,3))
print("math.sqrt(x) 返回x的平方根:",math.sqrt(9))


print("----------------数字常量------------------")
print("math.e :",math.e)
print("math.pi:" , math.pi)


print("-----------------随机数函数-----------------")
import random
print("random.choice(seq) 从序列中随机挑选一个元素:",random.choice(range(10)))
print("random.choice(seq) 从序列中随机挑选一个元素:",random.choice([12,"lian","志"]))
print("random.choice(seq) 从序列中随机挑选一个元素:",random.choice((3.3,"heh")))
print("random.choice(seq) 从序列中随机挑选一个元素:","set不支持索引")
print("random.randrange ([start,] stop [,step]) 指定范围返回随机数",random.randrange (1,100,3))
print("ramdom.random() 生成一个随机数,范围[0,1)",random.random())
print("random.seed(x)  指定x为random() 的随机数种子")
random.seed(47)
print(random.random())
print(random.random())
random.seed("hello",3)
print(random.random())
print(random.random())
print("random.shuffle(list) 将序列或者元组打乱排序")
aa = ["lian",2,4.1,"hi",3+2j , -20 , "chao"]
print("aa : " , aa)
random.shuffle(aa)
print("aa : ", aa)

print("random.uniform(x,y)  随机在x到y的范围内生成一个实数" , random.uniform(1,10))

print("---------------三角函数-----------------")

