"""
说明：
把一个list中所有的字符串变成小写（list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错）

"""
L1 = ['Hello', 'World', 18, 'Apple', None]
for i in L1:
    if isinstance(i,str)==True:#使用内建的isinstance函数可以判断一个变量是不是字符串
        i=i
    else:
        L1.remove(i)#删除list中的元素

L2=[s.lower() for s in L1]

print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')

"""
简便方法：
L1=['Hello','World',18,'Apple',None]

L2=[s.lower() for s in L1 if isinstance(s,str)]
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')
"""



