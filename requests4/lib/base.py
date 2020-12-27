import requests


def get_logining(): #已登录
    url = "http://hn216.api.yesapi.cn/?s=App.User.LoginExt"
    data= {"app_key":"53407A38CCBA92F10BC8A11E529D5134","username":"wbx001","password":"zx5335154"}
    res = requests.post(url=url,data=data)
    return res.json()

def get_login(): #未登录
    url = "http://hn216.api.yesapi.cn/?s=App.User.LoginExt"
    data= {"app_key":"53407A38CCBA92F10BC8A11E529D5134","username":"王辉1","password":"banxian123"}
    res = requests.post(url=url,data=data)
    return res.json()

