"""执行文件相关操作_qingmu"""
import os

from Qingmu import GOODs, GOODs_id, Subway, Super_r, Newsuper_r, monitor_import, competiter_import, Store_data, \
    Reference, Drill, Flow_data, timemark, import_new,Aipush,Taoke,Reportbyday,Shengyicanmou
import datetime
import time

dates = '2022-02-10'
daten = datetime.datetime.now().strftime('%Y-%m-%d')


# datem=datetime.datetime.now()
# daten='2021-12-15'
# 全量商品效果表
def goods_download():
    goods = GOODs(dates, daten)
    goods.download()
    time.sleep(10)
    goods.indexm()
    time.sleep(4)
    goods.importdb()


#商品下载
goods_download()

# goods = GOODs(dates,daten)
# goods.importdb()



# sku=['13143','149463','99999863']
# id=['585395538992','651906665545','610646114785']

d_sku = {"88888008": "610139576448", "66666078": "574850052768", "896045": "659826227485", "167338": "654528663210",
         "144271": "651049048097", "144004": "624281919528", "32782": "572819137868",
         "11977": "562098732351", "13143": "585395538992", "99999863": "610646114785", "11959": "623730975672",
         "88888250": "636047745663", "896002": "656976640322", "117003": "612308733402", "896020": "637649369020",
         "15600": "637860339836", "66666281": "612463186205", "100022": "612308577232", "31963": "586894075879",
         "L122W140": "668084007686", "149238": "622417341946", "12241": "574848208083", "149463": "651906665545",
         "66666292": "612150257480", "896026": "642105974374", "33492": "611356042758", "L122W143": "666448736505",
         "L122W160": "667824698166",
         }


# d_sku={"896002":"638571579777","15600":"637860339836","100022":"612308577232"}

# 单品商品下载：
def monitor_goods(dated):
    # for i,j in zip(range(len(sku)),range(len(id))):
    for k, v in d_sku.items():
        goods_id = GOODs_id(dates, k, v, dated)
        goods_id.download()
        time.sleep(10)
        goods_id.indexm()
        time.sleep(5)
        goods_id.importdb()
        time.sleep(2)


# monitor_goods(2)
# id商品下载
# monitor_goods(2)
# for k,v in d_sku.items():
#     goods=GOODs_id(dates,k,v,200)
#     goods.importdb()
#
#


# 导入竞店
# competiter_import(dates,daten)

# #导入监控店铺
# monitor_import(dates,daten)


# #导入直通车
subway = Subway(dates,daten,1)
# subway.importdb_cell()
# subway.importdb_keyword()
# subway.importdb_orient()
# subway.importdb_region()

#
#
# #导入超推
super_r = Super_r(1)
# super_r.importdb_position()
# super_r.importdb_orient()
# super_r.importdb_cell()

# 导入引力魔方
newsuper_r = Newsuper_r(dates,daten,1)
# newsuper_r.importdb_cell()
# newsuper_r.importdb_position()
# newsuper_r.importdb_orient()


# 导入钻展
drill = Drill()
# drill.importdb_plan()


# 店铺核心指标数据
sd = Store_data(1)
# sd.di_storedata()
# sd.importdb_storedata()


# 参考表导入
reference = Reference()
# reference.importdb_pice()
# reference.importdb_rings()
# reference.importdb_dimension()


# 店铺流量地图下载
flow_data = Flow_data(dates, daten)
# flow_data.download()
# flow_data.importdb()


# 市场排行导入
# import_new(conn_name="skecherswoman_industry",t_name="industry_rank",header=0,filepath=r"C:\Users\DELL\Desktop\data_file_competiter\industry_rank",sheet=1,modetype="replace",file_type="xlsx",if_tmp=True,"ALTER TABLE industry_rank ADD 年 VARCHAR(10) AFTER `日期`,ADD 月 VARCHAR(10) AFTER `日期`;","UPDATE industry_rank SET 年=YEAR(`日期`),月=MONTH(`日期`);")


# 新新表导入
# import_new("skecherswoman_reference","pice",0,r"C:\Users\DELL\Desktop\data_file_competiter\reference\id-货号-主图-标题",if_tmp=False)
# import_new("skecherswoman_reference","dimension",0,r"C:\Users\DELL\Desktop\data_file_competiter\reference\货号-故事线",if_tmp=True)

import requests

# cookie= 'JSESSIONID=717BEFCF9632D238BA41345204B793BA,l=eBrf0CQnLjMaWbdLKOfwourza77OSIRAguPzaNbMiOCPOJdM5zKRW6cTDT_HC3GchshpR3XK4ADbBeYBqSqSmA7IK6Po_fkmn,cna=C1aPGlhekmACAXFt6HkNQsGG,cancelledSubSites=empty,isg=BDMzoR-dVdIZNBkGvQ3fO6cxwjddaMcqYEbzoOXQj9KJ5FOGbThXepH2mhUKxB8i,xlly_s=1,sn=skechers%E5%AE%98%E6%96%B9%E6%97%97%E8%88%B0%E5%BA%97%3A%E6%8E%A8%E5%B9%BF01,_cc_=W5iHLLyFfA%3D%3D,tfstk=cRzOB_Xue9XMOBGLalI3cVtRq5wNZq6xdCMDk65pLwudGxYAiL4uyCOhfjMrB6C..,csg=6df2cd50,unb=2210639251036,skt=752f24aecbca8343,cookie2=16de6d01a89fa32c588a08733f26f322,sgcookie=E100ATLtzcFhzuHH0eYlwawg15E27QyTtVMbWL5PZCJoLADOkXa6S5ytu7VJM3KH%2FGyP6MLie507CFLymLW8eKPDMd9oyRDU5FjrLDRRfQIacMA%3D,uc1=cookie21=U%2BGCWk%2F7oPIg&cookie14=UoewBGChU3To7A%3D%3D,__wpkreporterwid_=84fb7e7c-5fab-4db6-22fa-b606ac884a2f,t=03e5f584ce5761e07f7fc087eb0bdfbc,_tb_token_=e7799f87997a5,_samesite_flag_=true,'
#
# cd={'subway_cook': 'JSESSIONID=717BEFCF9632D238BA41345204B793BA,l=eBrf0CQnLjMaWbdLKOfwourza77OSIRAguPzaNbMiOCPOJdM5zKRW6cTDT_HC3GchshpR3XK4ADbBeYBqSqSmA7IK6Po_fkmn,cna=C1aPGlhekmACAXFt6HkNQsGG,cancelledSubSites=empty,isg=BDMzoR-dVdIZNBkGvQ3fO6cxwjddaMcqYEbzoOXQj9KJ5FOGbThXepH2mhUKxB8i,xlly_s=1,sn=skechers%E5%AE%98%E6%96%B9%E6%97%97%E8%88%B0%E5%BA%97%3A%E6%8E%A8%E5%B9%BF01,_cc_=W5iHLLyFfA%3D%3D,tfstk=cRzOB_Xue9XMOBGLalI3cVtRq5wNZq6xdCMDk65pLwudGxYAiL4uyCOhfjMrB6C..,csg=6df2cd50,unb=2210639251036,skt=752f24aecbca8343,cookie2=16de6d01a89fa32c588a08733f26f322,sgcookie=E100ATLtzcFhzuHH0eYlwawg15E27QyTtVMbWL5PZCJoLADOkXa6S5ytu7VJM3KH%2FGyP6MLie507CFLymLW8eKPDMd9oyRDU5FjrLDRRfQIacMA%3D,uc1=cookie21=U%2BGCWk%2F7oPIg&cookie14=UoewBGChU3To7A%3D%3D,__wpkreporterwid_=84fb7e7c-5fab-4db6-22fa-b606ac884a2f,t=03e5f584ce5761e07f7fc087eb0bdfbc,_tb_token_=e7799f87997a5,_samesite_flag_=true,', 'newsuper_cook': 'c_csrf=7dcf917f-e429-4801-b234-3a2ac8be8ce8,l=eBrf0CQnLjMaWUiEKOfwnurza77tIIRAguPzaNbMiOCPOHXw5yX1W6cTDT-eCnGch6o9R3XK4ADbBeYBqSqSmA7BtTJ6NQMmn,cna=C1aPGlhekmACAXFt6HkNQsGG,cancelledSubSites=empty,isg=BC8v6q1Xka5lQ5WSWeEbd0vlvkM51IP2_JJ_FEG8zR6lkE-SSadGRhHCFoGu6Ftu,xlly_s=1,sn=skechers%E5%AE%98%E6%96%B9%E6%97%97%E8%88%B0%E5%BA%97%3A%E6%8E%A8%E5%B9%BF01,_cc_=W5iHLLyFfA%3D%3D,tfstk=cUtPB0stm0nyidIIWgsER169mk25ZU9kKoW1rUiueCQIB9blipVdn_6R39w4taf..,csg=6df2cd50,unb=2210639251036,skt=752f24aecbca8343,cookie2=16de6d01a89fa32c588a08733f26f322,sgcookie=E100ATLtzcFhzuHH0eYlwawg15E27QyTtVMbWL5PZCJoLADOkXa6S5ytu7VJM3KH%2FGyP6MLie507CFLymLW8eKPDMd9oyRDU5FjrLDRRfQIacMA%3D,uc1=cookie21=U%2BGCWk%2F7oPIg&cookie14=UoewBGChU3To7A%3D%3D,t=03e5f584ce5761e07f7fc087eb0bdfbc,_tb_token_=e7799f87997a5,_samesite_flag_=true,', 'aipush_cook': 'l=eBrf0CQnLjMaWZLbBOfwourza77OSIRAguPzaNbMiOCP9aQy5o0cW6cTDMA2C3Gch6WXR3XK4ADbBeYBqSvp0_Q6bgiplEMmn,cna=C1aPGlhekmACAXFt6HkNQsGG,cancelledSubSites=empty,isg=BNHRN6mrV-g3QLv8Sxud8fkv4N1rPkWwDggROrNmzRi3WvGs-45VgH84-C-80t3o,xlly_s=1,sn=skechers%E5%AE%98%E6%96%B9%E6%97%97%E8%88%B0%E5%BA%97%3A%E6%8E%A8%E5%B9%BF01,_cc_=W5iHLLyFfA%3D%3D,tfstk=caxNB7s-xcnZsssjyGsql_68ZEhhZtvMnkW5SFigBp2jS6bGiNVAK16OLtwUiNf..,csg=6df2cd50,unb=2210639251036,skt=752f24aecbca8343,cookie2=16de6d01a89fa32c588a08733f26f322,sgcookie=E100ATLtzcFhzuHH0eYlwawg15E27QyTtVMbWL5PZCJoLADOkXa6S5ytu7VJM3KH%2FGyP6MLie507CFLymLW8eKPDMd9oyRDU5FjrLDRRfQIacMA%3D,uc1=cookie21=U%2BGCWk%2F7oPIg&cookie14=UoewBGChU3To7A%3D%3D,t=03e5f584ce5761e07f7fc087eb0bdfbc,_tb_token_=e7799f87997a5,c_csrf=201eeded-e8c5-43f8-a463-ff4dbedbcc39,_samesite_flag_=true,', 'taoke_cook': 'isg=BNDQluAlhlvuS1pfEp2BhT1soR4imbTjN8fwGcqhnCv-BXCvcqmEcya32czl1Wy7,_ga=GA1.1.694558927.1644718097,login=U%2BGCWk%2F75gdr5Q%3D%3D,taokeIsBoutiqueSeller=eQ%3D%3D,alimamapw=Q1pTBgtQQBJBdQ4WJVgcdlMQcnUTJlUQdyJBdXMWIFMcdlEQdXA%2FVVZRBlcFAAADA1QODVZWVgFV%0AVlQGAQNVAAZVVVBdUQY%3D,_ga_Q39CBKW296=GS1.1.1644718097.1.0.1644718097.0,cookie31=Mjk5NzYxMjYsc2tlY2hlcnMlRTUlQUUlOTglRTYlOTYlQjklRTYlOTclOTclRTglODglQjAlRTUlQkElOTcsc2tlY2hlcnNfdGFvYmFvQDE2My5jb20sVEI%3D,cookie32=e2d7e6bf6aec9c0f178b71095b131f82,tfstk=c9qGBjD1hPu1we33PGi_KK8SdjhGZJ-qZorQYuOMH14i9bEFifYezDGAKff5_E1..,alimamapwag=TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzk3LjAuNDY5Mi43MSBTYWZhcmkvNTM3LjM2,l=eB_WqdqPLjMalqtBBOfwourza77OSIRAguPzaNbMiOCPO6Xe5KjFW6cTDGxwC3GchseyR3XK4ADbBeYBqS0T84PRPpboSVDmn,xlly_s=1,_tb_token_=ee0738e5e39e0,v=0,cna=C1aPGlhekmACAXFt6HkNQsGG,cookie2=115d0a3afa06cbb0e9f6c7c4fe9ae55f,rurl=aHR0cHM6Ly93d3cuYWxpbWFtYS5jb20vaW5kZXguaHRt,taokeisb2c=,t=9c25b55ff8dd4d1dcf7922c6879f4cdf,'}
#
#
# # subway.download_subway(cookie,'keyword')
# reby=Reportbyday(cd)
# reby.subway_report()


# cookie='c_csrf=d63d8c23-6cf0-4d40-8cee-b301caecc5d0,l=eBgdKThrgQqYPja2BOfwourza77OSIRAguPzaNbMiOCPOHBM5poAW6L3-axHC3GVh6vWR3WK4ADbBeYBqQAonxv9tTJ6NQMmn,cna=xmiGGgenaxECAXQW0MdFIYGV,cancelledSubSites=empty,isg=BLCw-URrpUzm93lIID9dJyyxgX4C-ZRDV2cQuaoBfIveZVAPUglk0wZXuW0FdUwb,xlly_s=1,sn=skechers%E5%AE%98%E6%96%B9%E6%97%97%E8%88%B0%E5%BA%97%3A%E6%8E%A8%E5%B9%BF01,_cc_=U%2BGCWk%2F7og%3D%3D,tfstk=cmnGB726hVzsqiUnPhZsKMEDdKycZ2S4ZmoIY0_7_Fc_8zoFifbFzkNvK5AW_Z1..,csg=0470f55b,unb=2210639251036,skt=ef9dfaa44744a719,sgcookie=E100P8s2TtHlj9yMD4Ps4%2BPCKeYUsQX0wXgZ%2B6HMoRqrbYbg0mywhU%2F1OIvqc7wxUBU8mOur60q31qcfAK1nGMUIKUGT1yqTgRdG%2FnfbCPXK%2F9c%3D,cookie2=11d2761b2019c6a118c6be32e06f6591,_tb_token_=fee3d6e41ee53,_samesite_flag_=true,uc1=cookie21=VT5L2FSpdiBh&cookie14=UoewBGb611IlNg%3D%3D,t=ac8f3a808ea5b3f7549da4c210f68b32,'
#
# newsuper_r.download_newsuper(cookie,'position')

# import execjs
# init_time=int(time.time())*1000
# with open(r'.\token_dymatic\dynamicToken.js', "r", encoding="utf-8") as file1:
#     jk = file1.read()
# dytoken_init = execjs.compile(jk).call('get_token', init_time)
# print(dytoken_init,init_time)


# cookie='l=eBgdKThrgQqYP7xDBOfwourza77OSIRAguPzaNbMiOCPO97J5QzhW6LhiHdvC3GVhsTwR3WK4ADbBeYBq7Vonxv9bgiplEMmn,cna=xmiGGgenaxECAXQW0MdFIYGV,cancelledSubSites=empty,isg=BC0twUmjMHMnD9SfpSyoqAFyPMmnimFcCgQ9zm8yaUQz5k2YN9pxLHs01LoA5nkU,xlly_s=1,sn=skechers%E5%AE%98%E6%96%B9%E6%97%97%E8%88%B0%E5%BA%97%3A%E6%8E%A8%E5%B9%BF01,_cc_=VFC%2FuZ9ajQ%3D%3D,tfstk=ctkCBvM7hwbC-_RPLDtN4ccK0nrCZdSbVBanAb212C9O3umCioW4le-mZaez2l1..,csg=120b9b9d,unb=2210639251036,skt=c278849c5732965d,sgcookie=E100bkgnwYrZvjwnanEd9Ry031Dh71C%2FhloELjxEn3LXTuDE4DDss2J1EFE49ke%2FPs062uALdgUMVNqEkHXKAd7aglxfEi%2FLDR2TlfskGy8P6mI%3D,cookie2=1f1193aaff0da75763b087f12c3fc1f5,_tb_token_=3eb865be694e5,c_csrf=27c34694-f1e9-4b32-84e6-6704835f54c4,_samesite_flag_=true,uc1=cookie21=WqG3DMC9Eman&cookie14=UoewBGb60GWXlA%3D%3D,t=ac8f3a808ea5b3f7549da4c210f68b32,'
#
# aipush=Aipush(dates,daten)
# aipush.download_aipush(cookie,)


# cookie='isg=BOvrqPhRDTPcYVIZN1U7OJy9eg_VAP-CmK47yF1oxyqB_Ate5dCP0oleUjySXFd6,rurl=aHR0cHM6Ly93d3cuYWxpbWFtYS5jb20vaW5kZXguaHRt,taokeIsBoutiqueSeller=eQ%3D%3D,alimamapw=Q1pTBgtQQBJBdQ4WJVgcdlMQcnUTJlUQdyJBdXMWIFMcdlEQdXA%2FVVZRBlcFAAADA1QODVZWVgFV%0AVlQGAQNVAAZVVVBdUQY%3D,_ga_Q39CBKW296=GS1.1.1644279057.7.0.1644279057.0,cookie31=Mjk5NzYxMjYsc2tlY2hlcnMlRTUlQUUlOTglRTYlOTYlQjklRTYlOTclOTclRTglODglQjAlRTUlQkElOTcsc2tlY2hlcnNfdGFvYmFvQDE2My5jb20sVEI%3D,cookie32=e2d7e6bf6aec9c0f178b71095b131f82,_tb_token_=f5113ee911707,v=0,tfstk=cnuhBFNBNDrBH_qiceaIsiUNIO4lZwQzn4us7q_65OOxA0gNibjN0PwJsJvXLg1..,alimamapwag=TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzk3LjAuNDY5Mi43MSBTYWZhcmkvNTM3LjM2,l=eBanQ507gQqYlw5yBOfwourza77OSIRAguPzaNbMiOCP_uBB5ysAW6cfyGK6C3GVhsZ6R3WK4ADbBeYBqIbT84PRPpboSVDmn,xlly_s=1,login=VFC%2FuZ9ayeYq2g%3D%3D,new-entrance-guide=true,cna=xmiGGgenaxECAXQW0MdFIYGV,cookie2=13a0cfa97724fa8fb2cd422e8dd60abd,_ga=GA1.1.232577869.1644133093,taokeisb2c=,t=8bcf207108c2e5a30b2b02a1108996ec,'
# taoke=Taoke(dates,daten)
# taoke.download_taoke(cookie)


# cookie='everywhere_tool_welcome=true; thw=cn; t=3e13bc200d9ddfea2196cb06d9633f9c; enc=bNWRZpsMUNiVzlBkGnK%2BmqjaRiYyg%2BkFCDXu%2BnpkP03oVjziANqn8cZ%2Bs%2B5EXztsou7XEzFvUkv6Zl0ZGlJcNBtf6pKuhoKoRDO%2FLFNfvxE%3D; cc_gray=1; cookie2=10b2d929c5f7ae2f8f91200756c3cd53; _tb_token_=ed573e0707ee7; xlly_s=1; _samesite_flag_=true; sgcookie=E100%2FDyh7pnbVk7rQhbydl7LpH7yBKydiqyhwaLhRv1fzDSlg5ee8mlsF1h6X1ewSxEIA01iXep0oVL6xWLh4HbI1E0%2Fq%2BbhpoP619%2BFA9sn9jM%3D; unb=2210639251036; sn=skechers%E5%AE%98%E6%96%B9%E6%97%97%E8%88%B0%E5%BA%97%3A%E6%8E%A8%E5%B9%BF01; uc1=cookie14=UoewBG5Px6ODqA%3D%3D&cookie21=UIHiLt3xSalX; csg=cb9ee820; cancelledSubSites=empty; skt=c3b0b2b087ff8921; _cc_=UtASsssmfA%3D%3D; cna=+TtKGTmEi0gCAXeDdyWdHVdu; _euacm_ac_l_uid_=2210639251036; 2210639251036_euacm_ac_c_uid_=783329018; 2210639251036_euacm_ac_rs_uid_=783329018; _portal_version_=new; v=0; XSRF-TOKEN=56c80e16-b333-495a-af79-afaee3870d00; _m_h5_tk=47f40faf00c49c72127d7f0a07a34192_1644970345295; _m_h5_tk_enc=6ccf161642b2d8d2b8d61ed4044f5b98; _euacm_ac_rs_sid_=null; JSESSIONID=1882F6A1C749DB06452866684265E0B8; isg=BMDAtrPmto_TwUhyduY1rmB_kU6SSaQTCQeaPjpTLVthtWXf4l8ho2DNyRV1BVzr; l=fBxmohD4jdYza732BO5Zlurza779NQRfCsPzaNbMiIeca6dlwFGbTNCn9cwXkdtj_T548etruAU7_dnwlxULRxijiQtA6Vm5_bv6JeM3N7AN.; tfstk=ccUVBo0drZQ2hXu1vqgNfTMjq-QAZTN0sUlImo_LV5P5QlicixvtZxGxafOyImf..'
#
# s=Shengyicanmou()
# s.store_review(cookie,'2022-02-15')
