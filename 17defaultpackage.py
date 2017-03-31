'''from urllib.request import urlopen
for line in urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl'):
	line = line.decode('utf-8')  # Decoding the binary data to text.
	if 'EST' in line or 'EDT' in line:  # look for Eastern Time
		print(line)
'''


#for line in urlopen('http://172.21.1.96:8080/'):
#	line = line.decode('utf-8')  # Decoding the binary data to text.
#	print(line , end= "")


'''import smtplib
server = smtplib.SMTP('localhost')
server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
	"""To: jcaesar@example.org
	From: soothsayer@example.org
	Beware the Ides of March.
	""")
server.quit()'''

#时间类库
from datetime import date
now  = date.today()
print(now)
birthday = date(1991 , 6 ,  13)
age = now - birthday
print(age.days//365)


#数据压缩 必须为byte
print("")
import zlib
s = b'witch which has which witches wrist watch'
print(len(s))
print(s)
t = zlib.compress(s)
print(len(t))
print(t)
ns = zlib.decompress(t)
print(len(ns))
print(ns)
print(zlib.crc32(s))
print(zlib.crc32(t))
print(zlib.crc32(ns))


#性能度量
print("")
from timeit import Timer
print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())
print(Timer('a,b = b,a', 'a=1; b=2').timeit())


# 测试模块
print("")
import doctest
def average(values):
	"""Computes the arithmetic mean of a list of numbers.
    	
    	>>> print(average([20, 30, 70]))
    	40.0
    	"""
	return sum(values)/len(values)
#print(average([1 , 3 , 6 , 10]))
doctest.testmod()

print("")
import unittest

#unittest模块不像 doctest模块那么容易使用，不过它可以在一个独立的文件里提供一个更全面的测试集:
class TestStatisticalFunctions(unittest.TestCase):
    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        self.assertRaises(ZeroDivisionError, average, [])
        self.assertRaises(TypeError, average, 20, 30, 70)
unittest.main() # Calling from the command line invokes all tests

print("test end")