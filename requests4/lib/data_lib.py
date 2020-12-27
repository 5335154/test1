'''
读取文件
'''
import xlrd    #需要下载,pycharm里直接下载

#读取Excel文件
def read_excel(file):
    data = xlrd.open_workbook(file,"r+")    #打开文件
    table = data.sheet_by_name("XB")    #通过表格名读取表格
    # table = data.sheet_by_index(0)        #通过索引读取表格
    lst = []                                #创建个空列表来接遍历的数据
    for i in range(1,table.nrows):          #从第二行开始遍历所有行
        lst.append(table.row_values(i))     #返回遍历的行中所有单元格的数据组成的列表，并添加到空列表lst中
#    print(lst)
    return lst                              #返回列表lst
#read_excel(r"../data/case1.xlsx")
