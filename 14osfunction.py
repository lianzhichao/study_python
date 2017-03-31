import sys , os
# 假定文件存在，并有读写权限
#os.F_OK: 作为access()的mode参数，测试path是否存在。
#os.R_OK: 包含在access()的mode参数中 ， 测试path是否可读。
#os.W_OK 包含在access()的mode参数中 ， 测试path是否可写。
#os.X_OK 包含在access()的mode参数中 ，测试path是否可执行
ret = os.access("C:/Users/dell/Desktop/pythontest.txt", os.F_OK)
print ("F_OK - 返回值 %s"% ret)
ret = os.access("C:/Users/dell/Desktop/pythontest.txt", os.R_OK)
print ("R_OK - 返回值 %s"% ret)
ret = os.access("C:/Users/dell/Desktop/pythontest.txt", os.W_OK)
print ("W_OK - 返回值 %s"% ret)
ret = os.access("C:/Users/dell/Desktop/pythontest.txt", os.X_OK)
print ("X_OK - 返回值 %s"% ret)


# 查看当前工作目录
retval = os.getcwd()
print ("当前工作目录为 %s" % retval)
# 修改当前工作目录
os.chdir( "E:/python/project" )s
# 查看修改后的工作目录
retval = os.getcwd()
print(retval)

