import sys
print(sys.path)

# 每个模块都有自己独立的符号表 , 模块内的全局变量不会影响到其他模块
# 也可以引入其他模块 , 将其他模块的名称放在该模块的符号表中
import modulesys
modulesys.print_func("A")

# 在python中 如果module被当做一个整体执行时,即直接执行该py文件 , __name__ 是"__main__"
# 如果该module被其他module调用时 , module.__name__ 则是该module的名字
print(__name__)
print(modulesys.__name__)
print(modulesys.job)
print(modulesys._job)

#如果多次使用module中的函数 , 可以将其赋予给本地的一个函数
modulesys.fib(100)
fib = modulesys.fib
fib(1000)

del modulesys
del fib

# 也可以用from .. import ..引用某个moudle中的方法(可以多个) , 但是这样并不会引入该module
from modulesys import fib
fib(1000)
# print(modulesys.__name__)
# modulesys.print_func("x")

# 或者引用该module的全部函数和变量 ,但是下划线( _ ) 开头的变量不会被应用
# 尽量少用 , 可能覆盖该模块已有的定义
from modulesys import * 
print_func("aa")
print(job)
#print(_job)


#内置的函数 dir() 可以找到模块内定义的所有名称。以一个字符串列表的形式返回:
import modulesys
print(dir(modulesys))
print(dir(sys))
#如果没有给定参数 dir() 会罗列当前module定义的所有函数和变量
print("")
print(dir())
a = 10
print(dir())
del a
print(dir())

import mine.modulesys
print(dir(mine.modulesys))
del mine.modulesys

from mine import modulesys
modulesys.print_func("x")
del modulesys

from mine.modulesys import print_func
print_func("y")

del print_func

from mine import *
print(dir(mine.minetest))
