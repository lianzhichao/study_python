# 异常处理
"""while True:
	try:
		x = int(input("please input a number:"))
		print("your number is : " , x)
		break
	except ValueError:
		print("Oops! That was no valid number .Try again : ")
	print("function end")	
print("out of while")"""



"""import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
print("this block is out of try")"""


# raise可以抛出一个异常
'''raise NameError('HiThere')
print("a")'''


'''try:
        raise NameError('HiThere')
except NameError:
        print('An exception flew by!')
        raise'''


#可以自己创建异常
'''class myError(Exception):
	def __init__(self , value):
		self.value = value
	def __str__(self):
		return repr(self.value)

try:
	raise myError(2*2)
except myError as e:
	print(e.value)'''


'''try:
        raise KeyboardInterrupt
finally:
        print('Goodbye, world!')'''

"""def divide(x, y):
        try:
            result = x / y
        except ZeroDivisionError:
            print("division by zero!")
        else:
            print("result is", result)
        finally:
            print("executing finally clause")

divide(12 , 6)
divide(1 , 0)
divide('a' , 1)"""


# with 关键字 可以保证文件之类的对象 , 在使用完成之后 , 一定会正确地执行清理
with open("C:/Users/dell/Desktop/pythontest.txt") as f:
    for line in f:
        print(line, end="")

