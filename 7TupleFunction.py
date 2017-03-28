# 元组函数
print("len(tuple) 计算元组元素个数")
tup = ('physics', 'chemistry', 1997, 2000);
print(len(tup))

print("")
_tup = (12,3,5,13,344,3)
print("max(tuple) 返回元组中最大值 元素类型必须一致")
print(max(_tup))
print("min(tuple) 返回元组中最小值 , 元素类型必须一致")
print(min(_tup))

_tup = ('23','lian','郑州','121')
print(max(_tup))
print(min(_tup))


print("")
print("tuple(seq) 将列表转换成元组,集合和字典也可以,字典默认是keys()")
_list = ["12",1,"zhi","炒"]
print(tuple(_list))

_set = {"skdjlf",12,"谁得好"}
print(tuple(_set))

_dit = {"id":12,"name":"呵呵"}
print(tuple(_dit))
print(tuple(_dit.keys()))
print(tuple(_dit.values()))
print(_dit)


