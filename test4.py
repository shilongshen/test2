"""
说明：利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
"""
#n=len(name)
def normalize(name):
    return name[0].upper() + name[1:].lower()#
        #for k in n[1:i]:


# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)