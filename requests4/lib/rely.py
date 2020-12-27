from requests4.lib.base import get_login


def is_rely(data):
    uuid = get_login()['data']['uuid']   #调用lib目录下的base.py文件的get_login()的方法，获取uuid的值
    token = get_login()['data']['token'] #调用lib目录下的base.py文件的get_login()的方法，获取token的值
    data.setdefault("uuid", uuid)        #字典的操作，data是一个字典，这里的意思是data字典里有无uuid这个键，有则改变uuid键的值，无则添加uuid这个键值对
    data.setdefault("token", token)      #字典的操作，data是一个字典，这里的意思是data字典里有无token这个键，有则改变token键的值，无则添加token这个键值对
    return data                          #返回data的值
