# -*- coding:utf-8 -*-
#JSON表示对象就是标准的JavaScript对象
#   JSON类型         Python类型
#   {}               dict
#   []               list
#   'string'         str
#   123.456          int float
#   true/false       True/False
#   null             None
#Python内置的json模块提供了非常完善的Python对象到JSON格式的转换
import json
d = dict(name = 'LXL', age = 22, score = 99)
print(json.dumps(d))
#JSON反序列化为Python对象
json_str = '{"age": 20, "name": "LXL", "score":98}'
print(json.loads(json_str))

#JSON进阶
#Python的dict对象可以直接序列化为JSON{}，不多，很多时候，我们更喜欢用class表示对象，比如定义student类，然后序列化
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('LXL', 20, 87)
#print(json.dumps(s))  像这样是会报错的，因为读，dumps()方法不知道如何将Student实例编程一个JSON的{}对象

def student2str(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }

#print(json.dumps(s, default=student2str))

#这样确实能实现将dict类型序列化成JSON的对象，但是当我还有一个Teacher类的实例或者其他的实例，照样无法无法序列化成JSON对象
print(json.dumps(s, default=lambda obj: obj.__dict__, sort_keys=True, indent=4))
#方然我们也可以反序列化一个Student对象实例，loads()方法首先转换出一个dict对象，然后，传入的object_hook函数负责把dict转换成Student实例：
def dict2Student(d):
    return Student(d['name'], d['age'], d['score'])

print(json.loads(json_str, object_hook=dict2Student))