def print_func(x):
	print(x)

def fib(n):    # 定义到 n 的斐波那契数列
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()

job = ["java","python"]
_job = ["c++"]


if __name__ == '__main__':
	print("本module自身在运行")
else:
	print("我是来自其他module的引用")