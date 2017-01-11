#根据用户输入习惯计算一个更安全的口令
import hashlib

db = {}
def get_md5(pwd):
    md5 = hashlib.md5()
    md5.update(pwd.encode('utf-8'))
    return md5.hexdigest()

#根据用户输入的登录名和口令模拟用户注册,计算更安全的MD5

def register(user, pwd):
    db[user] = get_md5(pwd + user + 'the-salt')

def login(user,pwd):
    p = get_md5(pwd + user + 'the-salt')
    if db[user] == p:
        print('True')
        return True
    else:
        print('False')
        return False

if __name__ == '__main__':
    register('lxl', '123456')
    register('lyl', 'lxllyllzl')
    register('lzl', 'hahahaha')
    print(db)
    login('lxl', '123456')


