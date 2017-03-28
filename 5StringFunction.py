#字符串 
print("-aaa\b`bbb")
print("--aaa\000`bbb")
print("---aaa\v`bbb")
print("----aaa\t`bbb")
print("-----aaa\r`bbb")
print("------aaa\n`bbb")
print("------aaa\f`bbb")
print("------aaa\032`bbb")
print("------aaa\x32`bbb")

print(r"-aaa\b`bbb")
print(R"-aaa\b`bbb")


# % 为字符串格式化   可以将值插入到字符串中
print("我叫%s今年%d岁" % ("廉志超",25))
print("我叫%s今年25岁%s" % ("廉志超"," , the end"))

print("我叫%c今年%d岁" % (97,25.1))

print("wojiao%d今年")


print('-----------字符串内建函数----------------')
a = "nishiwodexiaoya"
print(a)
print("str.capitalize() 将字符串首个字母大写",a.capitalize())

print("")
b = "zhichao.lian@lrlz.com"
print(b)
print("str.center(width,fillchar) 将指定字符按照规定长度居中,width小于字符串长度等同无效")
print("width大于字符串长度,不够的以fillchar填空,默认空格:",b.center(28,"*"))

print("")
print("ljust(width,fillchar) 将字符串左对齐 , 不够的以fillchar填充 , 默认空格")
print(b.ljust(28,"*"))


print("")
print("rjust(width,fillchar) 将字符串右对齐 , 不够的以fillchar填充 , 默认空格")
print(b.rjust(28))
print(b.rjust(28,"&"))


print("")
print("zfill(width) 返回指定长度字符串,不够的右移,前面补0 ")
print("this is string example from runoob....wow!!!".zfill(20))
print("this is string example from runoob....wow!!!".zfill(50))



print("")
print("count(sub,start,end) 返回sub在字符串中出现的次数 , start,end可选")
print(b.count("i"))
print(b.count("i",3))
print(b.count("hehe"))

print("")
print("encode(encoding , error) 编码 ; decode(encoding , error) 解码")
str = "廉志超"
str_utf8 = str.encode("UTF-8")
str_gbk = str.encode("GBK")
print("原始:",str)
print("utf-8编码:",str_utf8)
print("gbk编码:",str_gbk)
print("uft-8 解码:",str_utf8.decode("utf-8"))
print("gbk 解码:",str_gbk.decode("gbk","strict"))

print("")
print("endswith(suffix ,beg,end) 检查字符串是否以suffix结尾 , beg和end存在则指定范围")
del str
strS = "nishiwodexiaoyaxiaopingguo"
print("strS:",strS)
print("strS是否以 guo 结尾:", strS.endswith("guo"))
print("strS(3:)是否以 guo 结尾:", strS.endswith("guo",3))
print("strS(:10)是否以 guo 结尾:", strS.endswith("guo",0,10))

print("")
print("startswith(prefix,beg,end) 检查字符串是否以prefix开头, beg和end存在则指定范围")
strS = "nishiniswodexiaoyaxiaopingguo"
print("strS:",strS)
print("strS是否以 nis 开头:", strS.startswith("nis"))
print("strS(5:)是否以 nis 开头:", strS.startswith("nis",5))
print("strS(:10)是否以 nis 开头:", strS.startswith("nis",0,10))


print("")
print("expandtabs(tabsize=8) 把字符串中的tab转成指定数量的空格")
strS = "nishi\twode"
print("strS:",strS)
print("strS.expandtabs():",strS.expandtabs())
print("strS.expandtabs(0):",strS.expandtabs(0))
print("strS.expandtabs(1):",strS.expandtabs(1))
print("strS.expandtabs(16):",strS.expandtabs(16))

print("")
print("find(str,beg,end) 检索str在字符串中的索引位置 ,如果没有则返回-1")
strS = "nishide"
print("strS",strS)
print("strS.find('ni'):",strS.find("ni"))
print("strS.find('aa'):",strS.find("aa"))
print("strS.find('i'):",strS.find("i"))
print("strS.find('i',2):",strS.find("i",2))


print("")
print("rfind()  与find()相同 不过是从右侧开始检索")
print("strS",strS)
print("strS.rfind('ni'):",strS.rfind("ni"))
print("strS.rfind('aa'):",strS.rfind("aa"))
print("strS.rfind('i'):",strS.rfind("i"))
print("strS.rfind('i',0,-3):",strS.rfind("i",0,-3))

print("")
print("index(str, beg, end) 同find方法 ,不同的是如果str不存在,则抛出异常")
print("strS",strS)
print("strS.index('ni'):",strS.index("ni"))
print("strS.index('i'):",strS.index("i"))
print("strS.index('i',0,4):",strS.index("i",0,4))
#print("strS.find('aa'):",strS.index("aa"))


print("")
print("rindex() 同index() 方法,从右侧索引开始检索")
print("strS",strS)
print("strS.rindex('ni'):",strS.rindex("ni"))
print("strS.rindex('i'):",strS.rindex("i"))
print("strS.rindex('i',2):",strS.rindex("i",2))

print("")
print("isalnum() 字符串至少有一个字符,且全部为数字或者字母组成,返回True,否则返回False")
print('"nishiwo".isalnum() :' , "nishiwo".isalnum())
print('"1234".isalnum() :' , "1234".isalnum())
print('"12nishiwo34".isalnum() :' , "12nishiwo34".isalnum())
print('"12nishi wo34".isalnum() :' , "12nishi wo34".isalnum())
print('"".isalnum() :' , "".isalnum())

print("")
print("isalpha() 字符串至少有一个字符,且全部为字母  返回True  否则返回False")
print('"".isalpha() :', "".isalpha())
print('"abcsd".isalpha() :', "abcsd".isalpha())
print('"abcs12d".isalpha() :', "abcs12d".isalpha())
print('"123".isalpha() :', "123".isalpha())


print("")
print("isdigit() 字符串至少有一个字符 ,且全部为数字 ,返回True 否则返回False")
print('"".isdigit() :' , "".isdigit())
print('"24112".isdigit() : ', "24112".isdigit())
print('"24sd12".isdigit() : ' , "24sd12".isdigit())
print('"sdsfd".isdigit() : ' , "sdsfd".isdigit())


print("")
print("isdecimal() 查询字符串是否只包含十进制字符")
print('"232343389067".isdecimal() :' , "232343389067".isdecimal())
print('"".isdecimal(): ' ,"".isdecimal())
print('"645a23".isdecimal() :' ,"645a23".isdecimal())
print('"343%453".isdecimal():' ,"343%453".isdecimal())
print('"43\\012".isdecimal():',"43\012".isdecimal())
print('"43\\x12".isdecimal():' ,"43\x12".isdecimal())

print("")
print("islower() 至少包含一个有大小写区别的字符 , 并且是小写 返回True  否则为False")
print('"".islower():',"".islower())
print('"sdDsd".islower():',"sdDsd".islower())
print('"sddsd".islower():',"sddsd".islower())
print('"sdfsd!~sdd123".islower():', "sdfsd!~sdd123".islower())
print('"2234@#^%#".islower():' ,"2234@#^%#".islower())

print("")
print("isupper() 至少包含一个区分大小写的字符 , 并且是大写 ")
print('"".isupper():' ,"".isupper())
print('"sdDsd".isupper():',"sdDsd".isupper())
print('"GFSR".isupper():',"GFSR".isupper())
print('"SDF!~FDS123".isupper():',"SDF!~FDS123".isupper())
print('"2234@#^%#".isupper():',"2234@#^%#".isupper())

print("")
print("lower() 将字符串中所有大写转换成小写")
print('"dDk~#2D3sd".lower() :' , "dDk~#2D3sd".lower())
print('"sdf45#$%^%".lower() :' , "sdf45#$%^%".lower())

print("")
print("upper() 将字符串中所有小写转换成大写")
print('"dDk~#2D3sd".upper() :' ,"dDk~#2D3sd".upper())
print('"sd45#$%^%".upper() :' , "sd45#$%^%".upper())

print("")
print("swapcase() 将字符串中大小写字母转换为小大写")
print('"dDk~#2D3sd".swapcase() :' ,"dDk~#2D3sd".swapcase())
print('"sd45#$%^%".swapcase() :' , "sd45#$%^%".swapcase())
print('"".swapcase():',"".swapcase())

print("")
print("isnumeric() 包含全部为数字则返回True  只支持unicode对象")	
print("1234354".isnumeric())
print("123ssd4354".isnumeric())
print("121`34354".isnumeric())

print("四".isnumeric())
print("四".isdigit())
print("IV".isnumeric())
print("IV".isdigit())
print(b"1".isdigit())



print("")
print("isspace() 字符串是否全部由空格组成")
print(' "".isspace() :' , "".isspace())
print(' "  ".isspace() :' , "  ".isspace())
print(' "\\t".isspace() :' , "\t".isspace())
print(' "\\v".isspace() :' , "\v".isspace() )
print(' "\\n".isspace() :' , "\n".isspace() )
print(' "\\r".isspace() :' , "\r".isspace() )
print(' "\\f".isspace() :' , "\f".isspace() )
print(' "\\000".isspace() :' , "\000".isspace() )


print("")
print("istitle() 字符串所有字符首字母是否大写")
print('"".istitle() :' , "".istitle())
print(' "This Is 1 Lee! ~".istitle() : ', "This Is 1 Lee! ~".istitle())
print(' "This Is 1Lee! ~".istitle() : ', "This Is 1Lee! ~".istitle())
print(' "This Is 1lee! ~".istitle() : ', "This Is 1lee! ~".istitle())
print(' "123".istitle() : ', "123".istitle())

print("")
print("title() 将字符串标题化 即所有单词首字母大写")
print('"".title():' ,"".title())
print("i am 25 year old !".title())
print("I am 25year old !".title())
print("i am 25~year Old !".title())

print("")
print("join(seq) 将seq中的所有元素,按照指定的分隔符链接起来,合并为新字符串")
print("seq中必须全部为字符串")
print(' "-".join(seq) :' , "-".join(["1","zz","4.4","hehe"]))
print(' "".join(seq) : ' , "".join(["1","zz","4.4","hehe"]))
print("-".join(("2" ,"lee" , "qq")))
print("-".join({"lian","zhi","chao"}))
print("-".join("asdfghjkl"))
print("-".join("我的heart"))


print("")
print(" len(str) 返回字符串长度")
print(' len("") :' ,  len(""))
print(' len("2sd") :' ,  len("2sd"))
print(' len("~12$s1") : ',len("~12$s1") )
print(' len("\\d"):' , len("\d"))
print(' len("\\t"):' , len("\t"))
print(' len("\\v"):' , len("\v"))
print(' len("\\r"):' , len("\r"))
print(' len("\\n"):' , len("\n"))
print(' len("我是chan"):' , len("我是chan"))

print("")
print(" lstrip() 截掉字符串左端的空格")
print( '"  ad12  12 ".lstrip():',"  ad12  12 ".lstrip() , "---")
print( '"ad12  12 ".lstrip():',"ad12  12 ".lstrip() , "---")
print( '"\tad12  12 ".lstrip():',"\tad12  12\t".lstrip() , "---")

print("")
print("rstrip() 截掉字符串右边的空格")
print( '"  ad12  12 ":',"  ad12  12 ", "2---")
print( '"  ad12  12 ".rstrip():',"  ad12  12 ".rstrip() , "---")
print( '"ad12  12 ".rstrip():',"  ad12  12".rstrip() , "---")
print( '"\tad12  12 ".rstrip():',"\tad12  12\t".rstrip() , "---")

print("")
print("strip() 同时截取字符串两端的空格,执行 lstrip() 和 rstrip()")
print( '"  ad12  12 ".strip():',"  ad12  12 ".strip() , "---")
print( '"ad12  12 ".strip():',"  ad12  12".strip() , "---")
print( '"\tad12  12 ".strip():',"\tad12  12\t".strip() , "---")

print("")
print("str.maketrans(intab , outtab) 创建字符映射转换表")
print("intab为需要转换的字符, outtab为转换后的字符 , 两者长度必须相等 ,一一对应")
print(" string.translate(str.maketrans(intab,outtab)) 将string字符串转换")
intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab,outtab)
strS = "this is a string example...wow!"
print(trantab)
print(strS.translate(trantab))
print(strS.translate(str.maketrans(intab,outtab)))

print("")
print("max(str) 返回字符串中最大的字母 , 可以是列表 集合  元组 但是其中元素必须都是字符串")
print('max("aAGg") :' , max("aAGg"))
print('max("aA~^&*") :' , max("aA~^&*"))
#print('max("") :' , max(""))
print(max(["a","v","A"]))
print(max(("ab","Ab","~b")))
print(max({"a","A","C","a%"}))

print("")
print("min(str) 返回字符串中最小的字母")
print('min("aAGg") :' , min("aAGg"))
print('min("aA~^&*") :' , min("aA~^&*"))
#print('min("") :' , min(""))
print(min(["a","v","A"]))
print(min(("ab","Ab","~b")))
print(min({"a","A","C","a%"}))


print("")
print("replace(old,new,times) 将字符串中的old 替换成new ,最多替换times次")
print("ni shi wo bu ni shi".replace("ni","wo"))
print("ni shi wo bu ni shi".replace(" ","&",2))


print("")
print("split(str , num) 以str为分隔截取字符串 , 最多截取num次")
print("niabiaklakjkda".split("a"))
print("niabiaklakjkda".split("a",2))


print("")
print("str.splitlines([keepends]) 按照行 '\\r' '\\n' '\\r\\n' 分隔")
print("keepends 为True保留换行符  为False , 不保留 , 默认False")
print("ab c\nda\rdsd\r\nsaa".splitlines())
print("ab c\nda\rdsd\r\nsaa".splitlines(True))
print("ab c\nda\rdsd\r\nsaa".splitlines(False))
print("ab c\nda\rdsd\r\nsa\fas\vsd".splitlines(True))




