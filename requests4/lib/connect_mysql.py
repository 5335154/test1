'''连接数据库'''
import pymysql

def mysql_connect():
    #建立连接
    config = {
        'host':'localhost',       #地址
        'port':3306,              #端口
        'user':'root',            #数据库用户名
        'passwd':'',              #数据库密码
        'db':'wanghui',           #数据库名
        'charset':'utf8'          #编码方式utf-8
    }
    db = pymysql.connect(**config)  #链接数据库
    #创建游标
    cursor = db.cursor()
    #操作
    sql = "select * from xb_user;"
    cursor.execute(sql)        #执行数据库的操作
    data = cursor.fetchall()   #以元组形式返回所有数据
    #关闭
    cursor.close()             #关闭游标
    db.close()                 #关闭数据库
    return data
