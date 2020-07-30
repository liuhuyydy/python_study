###数据类型

##整数:
#包括任意正整数和负整数，也包括16进制的：十六进制用 0x前缀 和0-9、a-f表示
data_int = 1
print(data_int)
#输出：1

data_int = -1
print(data_int)
#输出：-1

data_int = 0x9f
print(data_int)
#输出：159


##浮点数:
#浮点数也就是我们常说的小数，计算机里之所以称之为浮点数，因为按照科学计数法计算时小数点是变化的。比如1.83乘以10的9次方，和18.3乘以10的8次方是相等的。
#浮点数可以用数学写法：-1.23、1.56 、8.90,但是当浮点数很大或者很小的时候就必须用科学计数法表示，把10用e代替，1.83乘以10的9次方可以用1.83e9来表示。
data_float = 1.83
print(data_float)
#输出:1.83

data_float = -1.83
print(data_float)
#输出:-1.83

data_float = 1.83e9
print(data_float)
#输出:1830000000.0


##字符串
#字符串是用单引号''或者双引号""括起来的任意文本。比如:'abc123',"d1.2{}_+"。注意单引号和双引号只是一种表示方式，不是字符串的一部分。
data_str = 'abc123'
print(data_str)
#输出:abc123

data_str = "d1.2{}_+"
print(data_str)
#输出:d1.2{}_+

#转移字符用\符号来表示，如果字符串中本身包含单引号或者双引号就使用转义符来转移。如：'I\'m OK!'
data_str = 'I\'m OK!'
print(data_str)
#输出：I'm OK!


#转移字符\可以转移很多字符，比如\n表示换行，\t表示制表符
data_str = "\tI'm OK!\nAre You OK?"
print(data_str)
#输出：    
#	I'm OK! 
#Are You OK?


#多行字符串'''.......'''，如果一段多行的字符串中一直都有\n来换行，则不好阅读。python为了简化可以用'''......'''表示
print('''我在学习python，希望能学友所用，
	学完python我想对系统的统计功能做个升级，
	另外我还可以学习做点自动化运维的脚本''')
#输出：
#我在学习python，希望能学友所用，
#	学完python我想对系统的统计功能做个升级，
#	另外我还可以学习做点自动化运维的脚本


##布尔值：
#布尔值只有True和False两个值（注意大小写），用来表示真和假。
print(True)
#输出：True

print(False)
#输出：False

print(1==2)
#输出：False

print(1==1)
#输出：True


##空值：空值是 Python 里一个特殊的值，用 None 表示。None 不能理解为 0，因为 0 是有意义的，而 None 是一个特殊的空值。
print(None)
#输出：None

print(None == 0)
#输出：False