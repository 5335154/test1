'''testcase'''
import os            #使用到os库的定位，所以引入os库
import unittest      #使用到unittest组织用例
import ddt           #使用到ddt数据驱动
from lib.rely import is_rely
from lib.runmethod import run_post, run_get
from setting import DATA_PATH     #引入setting.py文件对于DATA_PATH路径的确定

@ddt.ddt   #类前
class LoginCase(unittest.TestCase):
    @ddt.file_data(os.path.join(DATA_PATH,'login.yaml'))  #ddt数据驱动，导入data目录里的login.yaml，这里的参数是导入文件的绝对路径，os.path.join类似于字符串拼接，DATA_PATH是setting.py文件里面定义的路径变量，这里引入调用，然后和login.yaml拼接。
    def test_login(self,**userdata):  #userdata来自于data里的login.yaml,yaml文件设计到几种数据类型的表述（这里自行百度）,我们这里的userdata是字典格式的数据类型，所以我们需要用关键字参数的解析方法——**获得多个键值对的数据。如果是可变参数(列表、元组），则使用*解析
        id = userdata['id']     #将取出来的数据通过字典的键获得值，切片的方法
        name = userdata['name']  #获取接口名称
        rely = userdata['rely']  #确定是否有依赖
        hash = userdata['hash']  #确定是否加密
        method = userdata['method'] #获取请求方法
        url = userdata['url']    #获取请求URL
        data = userdata['data']  #获取请求的参数
        result = userdata['assert'] #获取期望结果

        if rely == "y":           #判断是否有依赖
            data = is_rely(data)  #如果有，则执行获取依赖需要的参数的方法,is_rely()方法在lib目录的rely.py内
            if method == "post":  #如果method是post请求，则进行下述的操作
                res = run_post(url,data,hash)  #发起请求的方法在lib目录的runmethod.py内

            elif method == "get":  #又如果method是get请求，则进行下述的操作
                res =run_get(url,data,hash)    #发起请求的方法在lib目录的runmethod.py内

        else:
            if method == "post":  #如果method是post请求，则进行下述的操作
                res = run_post(url,data,hash)  #发起请求的方法在lib目录的runmethod.py内

            elif method == "get":  #又如果method是get请求，则进行下述的操作
                res = run_get(url,data,hash)  #发起请求的方法在lib目录的runmethod.py内

        print(id,name,method,res.json())  #打印 id(编号),name(接口名称),method(请求方法),res.json()——将上面requests请求响应的结果res以json格式展示
        resu = res.text.replace('":','=') #因为res.text打印出来是键值对的字符串格式,eg:'ret':200,'data':{'err_code':0,...}，而yaml文件断言里是ret=200,err_code=0这种，我要设置断言，两个数据得一样，所以这里用到了字符串的替换方法replace，将":替换成=
        for i in result:   #遍历上面取到的result的值，result写在yaml文件里是用的数组（也就是列表）的方式，所以遍历出来的i，第一次是ret=200,第二次err_code=0这种，然后依次和实际结果resu比对。
            self.assertIn(i,resu)

if __name__ == '__main__':
    unittest.main()
