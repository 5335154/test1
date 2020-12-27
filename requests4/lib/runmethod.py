import requests
from lib.hash_pwd import hash_pwd


def run_post(url,data,hash):
    if hash == "y":  # 如果hash=y，密码需要加密，则进行下面的操作
        data['password'] = hash_pwd(str(data['password']))  # data是个字典格式，里面的password需要加密，所以把password通过切片取出来并给他赋值为加密后的值，这里调用了lib里面data_lib.py文件里的hash_pwd()加密的方法
        res = requests.post(url=url, data=data)  # 发起post请求，并将返回的值赋给res，用于后面断言的使用，需要的url,data参数来自于上面取到的数据
    else:  # 如果不需要加密
        res = requests.post(url=url, data=data)
    return res

def run_get(url,data,hash):
    if hash == "y":
        data['password'] = hash_pwd(str(data['password']))
        res = requests.get(url=url, params=data)
    else:
        res = requests.get(url=url, params=data)
    return res