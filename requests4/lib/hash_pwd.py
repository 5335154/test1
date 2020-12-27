'''加密'''
import hashlib

def hash_pwd(pwd):
    md5 = hashlib.md5()        #调用hashlib的md5加密方法
    md5.update(pwd.encode("utf-8"))  # 加密
    return md5.hexdigest()     #返回十六进制的加密密码
