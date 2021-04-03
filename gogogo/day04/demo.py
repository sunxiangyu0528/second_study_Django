# 常用的内置函数
# filter:接收两个参数，第一个是函数，第二个是可迭代对象，可以在函数里面对可迭代对象进行过滤
# def fun(n):
#     return n > 5
#
#
# li = [1, 3, 2, 4, 6, 7]
# res = filter(fun, li)
# print(list(res))
# ==>[6, 7]
# map函数接收两个参数，第一个是函数，第二个是可迭代对象，将可迭代对象中的数据迭代出来，一个一个传到函数中去调用，将返回结果反倒到新的对象中
def fun(n):
    return n * 5


li = [1, 3, 2, 4, 6, 7]

res = map(fun, li)
print(list(res))
