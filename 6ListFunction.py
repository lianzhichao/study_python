#列表
print("len(seq) 返回列表的元素个数")
childL = ["廉"]
listL = ["1",2,"aa",childL]
print(len(listL))
print("str in list  in返回字符是否在列表中")
print("1" in listL)
print("廉" in listL)
child2L = ["廉"]
print(childL in listL)
print(child2L in listL)
print(id(child2L) == id(childL))

print("for x in list  遍历列表元素")
for x in listL:
	print(x)

print("")
print("max(seq)  列表中最大的值,元素类型必须一致 ,都给Number 或者String")
print(max([1,23,5,77]))
print(max(["a","df","5","廉"]))
#print(max(["a","df",5,"廉"]))

print("")
print("min(seq)  列表中最小的值,元素类型必须一致 ,都给Number 或者String")
print(min([1,23,5,77]))
#print(min(["a","df",5,"廉"]))


print("")
print("list(seq) 将元组转换为list列表,集合和字典也可以 , 字典默认是将keys()转成列表")
tupleT = (1,4.5,"sdf","里")
print("tupleT:" , tupleT)
print("list(tupleT):",list(tupleT))

set_t = {"12",2,"kluan"}
print(list(set_t))

dit_t = {"id":1,"name":"lian"}
print(list(dit_t))
print(list(dit_t.keys()))
print(list(dit_t.values()))

print("")
print("list.append(obj) 在列表末尾添加对象")
aList = ["A",1,"lia","呵呵"]
print(aList)
aList.append(12)
aList.append("你的")
print(aList)

print("")
print("list.count(obj) 统计元素在list中出现的次数")
print(aList.count(12))
print(aList.count("12"))
aList.append(12)
print(aList.count(12))


print("")
print("list.index(obj) 查询元素在list中第一次出现的位置 , 索引,如果没有,则抛出异常")
print(aList)
print(aList.index(12))


print("")
print("list.insert(index.obj) 将对象插入到列表中,指定的索引位置")
print(aList)
aList.insert(2,"插入")
print(aList)


print("")
print("list.pop(index) 移除列表中一个元素, 默认为-1,即最后一个元素 , 并返回该元素")
print(aList)
a1 = aList.pop()
print(a1)
print(aList)
a2 = aList.pop(3)
print(a2)
print(aList)



print("")
print("list.remove(obj) 移除某一个元素的第一个匹配项 , 如果元素不存在, 报错")
print(aList)
aList.remove("A")
print(aList)
aList.append(["B","zhi",22])
print(aList)
aList.remove(["B","zhi",22])
print(aList)
aList.append("呵呵")
print(aList)
aList.remove("呵呵")
print(aList)



print("")
print("list.reverse() 翻转列表中的元素顺序")
print(aList)
aList.reverse()
print(aList);


print("")
print("list.sort(fun) 对元素进行排序 , 可以指定方法 , 或者使用默认 , 元素类型必须一样")
#print(aList);
#aList.sort();
#print(aList);
bList = [45,12311,31,244,2]
bList.sort()
print(bList)


cList = ["heh","sdfj","廉","431"]
cList.sort()
print(cList)


cList = ["heh","sdfj","廉","431"]
cList.sort(key = len)
print(cList);

cList = ["heh","sdfj","廉","431"]
cList.sort(reverse = False)
print(cList);


aL = [[1,2],[2,1],[1,1],[2,2]]  
print(aL)  
aL.sort(key=lambda x:(-x[0],x[1]))  
print(aL)  



print("")
print("list.clear()清空列表")
print(cList)
cList.clear()
print(cList)


print("")
print("list.copy() 复制列表,相当于 list[:]")
list1 = ['Google', 'Runoob', 'Taobao', 'Baidu']
list2 = list1.copy()
print ("list2 列表: ", list2)
list3 = list2[:]
print("list3列表:",list3)

list2.clear()
print(list1,list2,list3)



