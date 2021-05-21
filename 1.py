# 开发人员： 曾祥茂
# 日期： 2021/03/31


#位置参数 传参数有顺序
#func1(1,2,3)
def func1(a,b,c):
    """
    函数func1的作用
    :param a:
    :return:
    """
    # print("这是一个函数")
    # print("这是一个参数a",a)
    # print("这是一个参数a",b)
    # print("这是一个参数a",c)
    #不带表达式的return相当于none
    return

#函数的调用
func1(1,2,3)

#默认蚕食
def func2(a=1):
    print("参数值为",a)

func2(2)

#关键字参数调用/定义  必须跟随在位置参数的后面
def func2(a,b,c,d):
    print("参数值为", a)
    print("参数值为", b)
    print("参数值为", c)
    print("参数值为", d)


func2(a=1,b=2,c=4,d=4)


#特殊参数
def func2(a,b,c,*,d):
    print("参数值为", a)
    print("参数值为", b)
    print("参数值为", c)
    print("参数值为", d)


func2(1,2,4,d=4)


#Lambda表达式
func2 = lambda x: x*2

print(func2(3))
