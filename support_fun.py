"""support fun which are rewrited and used"""


from threading import Thread
from zipfile import ZipFile
import os
import time
import datetime
import pandas as pd
import threading
import json


class Rewrite_ziprelease():
    def __init__(self, filepath, releasedir):
        self.filepath = filepath
        self.releasedir = releasedir

    def ziprelease(self):
        file_zip = ZipFile(self.filepath)
        if not os.path.exists(self.releasedir):
            os.makedirs(self.releasedir)
        for file_item in file_zip.namelist():
            file_zip.extract(file_item, path=self.releasedir)
        file_zip.close()
        self._rename()
        os.remove(self.filepath)

    def _rename(self):
        for i in os.listdir(self.releasedir):
            old_path = os.path.join(self.releasedir, i)
            try:
                i = i.encode('cp437').decode('gbk')
                newpath = os.path.join(self.releasedir, i)
                os.rename(old_path, newpath)
            except Exception as ecd:
                print(ecd)




#杂项定义#
#索引文件夹
# esspath='C:\\Users\\DELL\\Desktop\\女鞋-竞店\\数据源\\竞店数据2'
# edate='2021-08-18'
# filepathlist=os.listdir(esspath)
# for each in filepathlist:
#     filedirpath=esspath+'\\'+each
#     filepath=glob.glob(filedirpath+'\\'+r'竞店分析-入店来源_无线端_二级来源*'+edate+'.xlsx')#索引文件夹或者文件
#     print(filepath[0])

# 定义类型
# dc = tuple(df_goods_effect.columns)
# dt_goods = {'统计日期': Date()}  # 指定日期列
# for di in range(len(dc)):
#     if di > 0:
#         if di < 6:
#             dt_goods[dc[di]] = TEXT()
#         else:
#             dt_goods[dc[di]] = TEXT()


#日期变量
#常量


# #时间装饰器-类
# class Timemark():
def timemark(fun):
    def inner(self,*args,**kwargs):
        start=time.time()
        fun(self,*args,**kwargs)
        end=time.time()
        f_time=str(round(start-end,1))+"s"
        print('%s 程序运行完成,累计耗时%ss' % (fun.__name__,f_time))
        pd_logs=pd.DataFrame(data=None,columns={"function_name","final_time","date"},index=[1])
        pd_logs["function_name"]=fun.__name__
        pd_logs["final_time"]=f_time
        pd_logs["date"]=datetime.datetime.now().strftime('%Y-%m-%d')
        # pd_logs.to_sql("mylogs",con=conn_reference,if_exists="append",index=False)
        print(pd_logs)
        return pd_logs

    return inner


class Rethread(threading.Thread):
    def __init__(self, func, *args):
        super().__init__()

        self.func = func
        self.args = args

        self.setDaemon(True)
        self.start()  # 在这里开始

    def run(self):
        self.func(*self.args)







def intturn(num):
    try:
        num=int(num)
    except Exception:
        num=0
    return num

def floatturn(num):
    try:
        num=round(float(num),2)
    except Exception:
        num=0
    return num

def presfloatturn(num):
    try:
        num=format(round(float(num),3)/100,'.2%')
    except Exception:
        num=0
    return num

def divisionprotect3(numup,numdown):
    num=0
    try:
        num=presfloatturn(float(numup)/float(numdown))
    except Exception:
        pass
    return num

def divisionprotect2(numup,numdown):
    num=0
    try:
        num=floatturn(float(numup)/float(numdown))
    except Exception:
        pass
    return num

def divisionprotect1(numup,numdown):
    num=0
    try:
        num=format(round(float(numup)/float(numdown),3),'.2%')
    except Exception:
        pass
    return num