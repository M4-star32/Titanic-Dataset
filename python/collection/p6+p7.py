#
# # print括号内不加引号输出变量值，如果是字符串必须加引号，否则会报错
# a = 6
# a = 9
# print(a)
# a = 0
# # 代码是从上到下运行的，输出9
#
# # 标识符由字母数字和下划线组成（不推荐使用中文） 不能以数字开头且不能使用关键字
# 数量 = 7
# print(数量)
#
# # 数值类型
# # 1.int整数型  任意大小的整数
# num = 1
# print(type(num))
#
# # 2.浮点型float  小数
# num1 = 1.2
# print(type(num1))
#
# # 3.布尔型bool  有固定写法，一个为True（真），一个为False（假）  通常用于判断
# # 布尔值可以当作整型对待，True=1，False=0
# print(True + False)
# print(True + True)
#
# # 4.复数型
# z1 = 1+2j;z2 = 2+3j;
# print(type(z1))
# print(type(z2))
# print(z1+z2)
#
# #5.字符串str 使用单引号或多引号，若包含多行内容，也可使用三引号
# name = 'Mario'
# print(type(name))
#
# name2='''
# 111
# 222
# '''
# print('name2')
# print(name2)
# # 注意name2已经赋值，print输出name2加上引号则输出name2此时他为字符串，不加引号则输出数值
#
# name = 'Mario'
# print('我的名字：%s'%name)
#
# name = 'jason'
# age = 18
# print('我的名字:%s,年龄:%d'%(name,age))
#
#
# # p7
# n1 = 100;
# n2 = 69;
# n1 = n1 + n2
# n1 += n2
# print(n1)
#
# # input输入函数   是字符串类型
# age = input('请输入年龄:')
# print(age)
#
# # 转义字符  \t制表符缩进四位  \n是换行符
# print('pass\nword')

# score = input('请输入成绩:')
# if score == '100':
#     print('great')
# if score == '60':
#     print('struggle')

a = 1
b = 2
if a == 1 and b == 2:
    print("a and b are equal")