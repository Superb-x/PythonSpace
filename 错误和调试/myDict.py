#单元测试时用来对一个模块、一个函数或者一个类进行正确性的检测工作
#比如对函数abs()，我们可以编写以下几个测试用例：
# 输入正数，比如1、1.2、0.99，期待返回值与输入相同；
#
# 输入负数，比如-1、-1.2、-0.99，期待返回值与输入相反；
#
# 输入0，期待返回0；
#
# 输入非数值类型，比如None、[]、{}，期待抛出TypeError。

class Dict(dict):
    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s' " % key)

    def __setattr__(self, key, value):
        self[key] = value

#为了编写单元测试模块我们需要引入Python的unittest模块