# def log(func):
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper
#
# @log
# def now():
#     print('2017-1-1')
#
# now()

# def log(text):
#     def decorator(func):
#         def wrapper(*args, **kw):
#             print('%s %s():' % (text, func.__name__))
#             return func
#         return wrapper
#     return decorator
#
# @log('excute')
# def now():
#     print('2017-1-1')
#
#
# now()
# print(now.__name__)

def log(func):
    def wrapper(*args, **kw):
        print('begin call %s()' % func.__name__)
        func()
        print('end call %s()' % func.__name__)
    return wrapper

@log
def now():
    print('2017-1-1')

now()



