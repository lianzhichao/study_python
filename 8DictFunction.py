#字典函数
_dict_1 = {1:"heh","la":"lla",("12",1,"lain"):"sd"}
print(_dict_1)

print("dictionary 键是唯一的  且只能用不可变型类型数据 , Number Str tuple ")

print("set 和 list 不能作为字典的key")
#_dict_2 = {1:2,["hehe",11]:12}
#print(_dict_2)

#_dict_3 = {{"as",12}:12}
#print(_dict_3)

print("")
print("len(dict) 返回字典元素个数")
print(len(_dict_1))

print(str(_dict_1))

print("")
print("type(obj) 返回输入变量的类型,如果是字典就返回 dict")
print(type(_dict_1))	#<class 'dict'>
print(type(12))		#<class 'int'>
print(type("hehe"))	#<class 'str'>
print(type(["12",""]))	#<class 'list'>
print(type({"sd ",12}))	#<class 'set'>
print(type(("12",12)))	#<class 'tuple'>


print("")
print("dict.clear() 清空字典")
_dict_a = {"id":1,"name":"lian","age":25}
print(_dict_a)
_dict_a.clear()
print(_dict_a)


print("")
print("dict.copy() 复制一个新的字典  并返回")
_dict_a = {"id":1,"name":"lian","age":25,"job":["java","python","c++"]}
print(_dict_a)
_dict_b = _dict_a.copy()
print(_dict_b)
_dict_c = _dict_a
_dict_a['id'] = 3
print(_dict_a)
print(_dict_b)
print(_dict_c)

print("直接将一个对象赋予给另外一个对象,则两个对象指向相同的内存, 所以修改也会一样")
print("copy()方法则只是复制了对象的内容 , 但是子对象是浅copy")
print("如果字典中有可变的值, 比如列表 ,则copy的对象的列表元素值和原字典指向相同的列表")

_dict_a['job'][1] = "python3"
print(_dict_a)
print(_dict_b)
print(_dict_c)



print("")
print("ditc.fromkeys(seq[,value]) 创建一个新的字典 , 使用seq的元素作为字典的键 , value为所有元素的默认值")
print(_dict_b)
_seq = ("_newid","_newname","_newage")
print(_dict_b.fromkeys(_seq))
print(_dict_b.fromkeys(_seq,1))
print(_dict_b)


print("")
print("dict.get(key,default) 获取指定key元素 , 如果没有,则返回默认值 , 不写则为None")
print("与直接用dict['key'] 获取不同, dict[key] 如果key不存在, 则会报错")
print(_dict_b)
print(_dict_b.get("id"))
print(_dict_b.get("idi"))
print(_dict_b.get("idi","呵呵"))
print(_dict_b['id'])
#print(_dict_b['idi'])


print("")
print("dict.setdefault(key,default) 如果键不存在,设置默认值 , 存在则不改变")
print(_dict_b)
_dict_b.setdefault("id" , 12)
_dict_b.setdefault("soso")
_dict_b.setdefault("heh","non")
print(_dict_b)


del _dict_b['soso']
del _dict_b['heh']

print("")
print("key in dict 判断key是否在dict中")
print("id" in _dict_b)
print("idi" in _dict_b)


print("")
print("dict.keys() 会返回字典的所有key")
print(_dict_b)
print(_dict_b.keys())
for x in _dict_b.keys():
	print(x)

print("")
print("dict.values() 会返回字典的所有value")
print(_dict_b.values())
for x in _dict_b.values():
	print(x)


print("")
print("dict.items() 返回字典键值组成的可遍历的元组数组")
print(_dict_b.items())
for x in _dict_b.items():
	print(x)


print("")
print("dict.update(dict2) 把字典2 里边的元素更新到字典1 中")
_aa = {"id":12 , "name":"chao"}
_bb = {"id": 13 , "age":25}
_aa.update(_bb)
print(_aa)


