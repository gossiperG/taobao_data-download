"""青木日常数据下载"""
import os
import datetime
import re
import time
import requests.cookies
import json
import xlwt
from urllib.parse import urlencode
import math
from support_fun import Rewrite_ziprelease,timemark,intturn,floatturn,presfloatturn,divisionprotect3,divisionprotect2,divisionprotect1
import  execjs






#直通车
class Subway():
    def __init__(self,sdate,edate,datediff=1):
        self.filepathdir1 = 'C:\\Users\\DELL\\Desktop\\data_file_competiter\\pay\\subway\\'
        self.datediff=datediff
        self.daten=datetime.datetime.now()
        self.sdate=sdate
        self.edate=edate

    @timemark
    def download_subway(self,cookies,type="all"):
        token_url='https://subway.simba.taobao.com/bpenv/getLoginUserInfo.htm'
        create_url = "https://subway.simba.taobao.com/reportdownload/addMultiTask.htm"
        downloadindex_url="https://subway.simba.taobao.com/reportdownload/getdownloadTasks.htm"
        download_url='https://download-subway.simba.taobao.com/download.do?'
        deltask_url='https://subway.simba.taobao.com/reportdownload/deltask.htm'

        header= {'Referer': 'https://subway.simba.taobao.com/',
                   'Accept-Encoding': 'gzip,deflate,br',
                   'Accept-Language': 'zh-CN,zh;q=0.9',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
                   'Origin': 'https://subway.simba.taobao.com',
                   'Accept': 'application/json, text/javascript, */*; q=0.01',
                   'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                   'X-Requested-With': 'XMLHttpRequest',
                   'Host': 'subway.simba.taobao.com',
                    'cookie':cookies,
                   }
        header_download = {'Sec-Fetch-Mode': 'navigate',
                           'Sec-Fetch-Dest': 'document',
                           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                           'Accept-Encoding': 'gzip,deflate,br',
                           'Accept-Language': 'zh-CN,zh;q=0.9',
                           'Upgrade-Insecure-Requests': '1',
                           'Host': 'download-subway.simba.taobao.com',
                           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
                           'cookie': cookies
                           }

        session_id="BCE65990"
        token=json.loads(requests.post(token_url,headers=header).content.decode('utf-8'))['result']['token']
        pagenum=1
        filename=time.strftime("%Y%m%d%H%M%S")

        params_create = {
            'startDate':self.sdate,
            'endDate':self.edate,
            'transactionCycle':-1,
            'aggregationMode':2,
            'sla':'json',
            'isAjaxRequest':'true',
            '_referer':'/report/bpreport/campaign/index',
            'sessionId':session_id,
            'token':token,
            'fileName':filename
        }
        params_index={
            'pageSize':'20',
            'pageNumber':pagenum,
            'sla': 'json',
            'sessionId': session_id,
            'token': token,
            'isAjaxRequest': 'true',
            '_referer':'/report/bpreport/download-list?rows=20&page=1'
        }
        params_download={
            'spm':'a2e2i.23211836.ce272de26.d5325113b.7f3368f815YMsW',
            'custId':'1104204309',
            'token':token,
        }
        params_del={
            'sla':'json',
            'isAjaxRequest':'true',
            'sessionId': session_id,
            'token': token,
        }
        re_filename=re.compile(".*%s_(.*)" % (filename))

        if type=="account":
            params_create["dimension"]="[101]"
        if type=="keyword":
            params_create["dimension"]="[104]"
        if type=="orient":
            params_create["dimension"]="[105]"
        if type=="cell":
            params_create["dimension"]="[103]"
        if type == "region":
            params_create["dimension"] = "[108]"
        if type == "all":
            params_create["dimension"] = "[101,103,104,105,108]"

        requests.post(create_url,headers=header,data=params_create) #request_create=
        time.sleep(2.5)
        request_downloadindex_init=requests.post(downloadindex_url,headers=header,data=params_index)
        pagenum=math.ceil(int(request_downloadindex_init.json()["result"]['totalItem'])/20)
        for num in range(pagenum-1,pagenum+1):
            params_index['pageNumber'] = num
            request_downloadindex = requests.post(downloadindex_url, headers=header, data=params_index)
            dlist = request_downloadindex.json()["result"]["items"]
            for di in range(len(dlist)):
                filetype=re.findall(re_filename, dlist[di]['fileName'])
                if filetype:  #注意Python不支持dict的key为list或dict类型，因为list和dict类型是unhashable（不可哈希）
                    params_download['taskId']=dlist[di]['id']
                    download_get= download_url+ urlencode(params_download)
                    file_f=requests.get(download_get,headers=header_download)  #单文件下载header一定要对，不然会报错，文件下下来也是错的；文件太大就用stream设置为false用chunk-size去下载;需要验证的网站，不能禁止重定向

                    _path=r'./数据源/报表/直通车'
                    if not os.path.exists(_path):
                        os.makedirs(_path)
                    download_path=os.path.join(_path,r'%s_%s.zip'%(filename,filetype[0]))
                    with open(download_path,'wb') as fg:
                        fg.write(file_f.content)
                    try:
                        _rel=Rewrite_ziprelease(download_path,_path)
                        _rel.ziprelease()
                    except Exception as ec:
                        # print('err:',ec)
                        continue
                    print('直通车_%s下载完成！'%(type))

                    params_del['taskId']=dlist[di]['id']
                    params_del['_referer']='/report/bpreport/download-list?rows=20&page=%s'%(num)
                    requests.post(deltask_url,params=params_del,headers=header)

#引力魔方
class Newsuper_r():
    def __init__(self,sdate,edate,datediff=1):
        self.filepathdir1 = 'C:\\Users\\DELL\Desktop\\data_file_competiter\\pay\\new recomemend\\'
        self.datediff=datediff
        self.daten=datetime.datetime.now()
        self.dtjs_path=r".\token_dymatic"
        self.sdate=sdate
        self.edate=edate

    @timemark
    def download_newsuper(self,cookies,type="all"):
        token_url = 'https://tuijian.taobao.com/api2/member/getInfo.json?'
        export_url='https://tuijian.taobao.com/api2/report/export.json?'

        cookies=cookies.replace(',',';').rstrip(';')
        header_init= {'Referer': 'https://tuijian.taobao.com/indexbp-display.html',
                   'Accept-Encoding': 'gzip,deflate,br',
                   'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
                   'X-Requested-With': 'XMLHttpRequest',
                   'Host': 'tuijian.taobao.com',
                   'cookie':cookies,
                   'sec-fetch-mode':'cors',
                   'sec-ch-ua':'Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97',
                   'sec-fetch-dest':'empty',
                   'Sec-Fetch-Site':'same-origin'
                   }
        header_export={
            'Upgrade-Insecure-Requests':'1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Sec-Fetch-Dest':'document',
            'sec-fetch-mode':'navigate',
            'Referer': 'https://tuijian.taobao.com/indexbp-display.html',
            'Accept-Encoding': 'gzip,deflate,br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'cookie':cookies
        }
        params_tokenquery={
            "r":"mx_14",
            'callback':'jQuery',
            'bizCode':'display',
            'invitationCode':'',
            'csrfID':'',
        }
        params_export={
            'alias':'def',
            'bizCode':'displayDefault',
            'componentTemplateId':'',
            'creativeId':'',
            'privateMiniId':'',
            'startTime':self.sdate,
            'componentCode':'reportFiledTemplate',
            'curComponentTemplateId':'undefined',
            'effect':'15',
            'endTime':self.edate,
            'effectType':'click',
            'baseDomainOptionList':'["needCampaignGroup","needCampaign","needPromotion"]',
            'campaignIdList':'',
            'materialIdList':'',
            'campaignGroupIdList':'',
            'creativeIdList':'',
            'subPromotionTypeList':'',
            'targetTypeList':'',
            'creativeFormIdList':'',
            'adzoneIdList':'',
            'offset':'',
            'pageSize':'100',
            'orderField':'',
            'orderBy':'',
            'exportSummary':'',
        }

        init_time = int(time.time())*1000
        with open(r'.\js_refile\jstk.js', "r", encoding="utf-8") as file1:
            jk = file1.read()
        dytoken_init = execjs.compile(jk).call('get_token', init_time)
        params_tokenquery['dynamicToken']=dytoken_init
        params_tokenquery['timeStr']=init_time
        params_tokenquery['_']=str(init_time+100)
        init_request=requests.get(token_url,headers=header_init,params=params_tokenquery)
        # print(json.loads(init_request.text[7:-1]))


        csrfID=json.loads(init_request.text[7:-1])['data']['csrfID']
        seedToken=json.loads(init_request.text[7:-1])['data']['seedToken']
        pin=int(json.loads(init_request.text[7:-1])['data']['pin'])
        params_export['timeStr']=init_time+3000
        params_export['dynamicToken']=execjs.compile(jk).call('get_token', init_time+3000,seedToken,pin)
        params_export['csrfID']=csrfID

        filename = type + '_' + str(self.sdate) + '_' + str(self.edate)
        params_export['excelName'] = filename

        if type!='all':
            if type=="orient":
                params_export["advancedDomainOptionList"]='["needTargeting"]'
                params_export['rptDomainOption']= '{"needCampaignGroup":true,"needCampaign":true,"needPromotion":true,"needTargeting":true}'
            if type=="cell":
                params_export["advancedDomainOptionList"]='[]'
                params_export['rptDomainOption'] = '{"needCampaignGroup":true,"needCampaign":true,"needPromotion":true}'
            if type=="position":
                params_export["advancedDomainOptionList"]='["needAdzone"]'
                params_export['rptDomainOption'] = '{"needCampaignGroup":true,"needCampaign":true,"needPromotion":true,"needAdzone":true}'
            exportcontent = requests.get(export_url, headers=header_export, params=params_export)
            # if exportcontent.content.decode('utf-8').json()[]
            savepath = r'.\数据源\报表\超级推荐'
            if not os.path.exists(savepath):
                os.makedirs(savepath)
            try:
                with open(os.path.join(savepath,r'%s.xls' % (filename)), 'wb') as fl:
                    fl.write(exportcontent.content)
                    print('超推%s报表下载完成！'%(type))
            except Exception as file_state:
                print('Error:\n请检查文件状态：\n',file_state)
        elif type=="all":
            for i in ['orient','cell','position']:
                self.download_newsuper(cookies,i)
                time.sleep(2)


#万象台
class Aipush():
    def __init__(self,sdate,edate,datediff=1):
        self.sdate=sdate
        self.edate=edate
        self.download_path=r'./数据源/报表/万相台'

    @timemark
    def download_aipush(self,cookies,type="all"):
        token_url = 'https://adbrain.taobao.com/api/member/getInfo.json?'
        export_url='https://adbrain.taobao.com/api/export/report/exportOverProductReportList.json?'

        cookies = cookies.replace(',', ';').rstrip(';')
        header_init= {'Referer': 'https://adbrain.taobao.com/indexbp.html',
                   'Accept-Encoding': 'gzip,deflate,br',
                   'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                   'Accept':'application/json, text/javascript, */*; q=0.01',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
                   'X-Requested-With': 'XMLHttpRequest',
                   'host': 'adbrain.taobao.com',
                   'cookie':cookies,
                   'sec-fetch-mode':'cors',
                   'sec-fetch-dest':'empty',
                   'Sec-Fetch-Site':'same-origin',
                   }
        header_export={
            'Upgrade-Insecure-Requests':'1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Sec-Fetch-Dest':'document',
            'sec-fetch-mode':'navigate',
            'Referer': 'https://adbrain.taobao.com/indexbp.html',
            'Accept-Encoding': 'gzip,deflate,br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'cookie':cookies
        }
        params_tokenquery = {
            "r": "mx_14",
            'bizCode':'adStrategy',
        }
        params_export = {
            'rptDataContentType':'creative',
            'startTime': self.sdate,
            'effects': '15',
            'endTime': self.edate,
            'effectType': 'click',
            'groupByDate':'day',
            'unifyType':'zhai',
        }
        init_time = int(time.time()) * 1000
        with open(r'.\js_refile\jstk.js', "r", encoding="utf-8") as file1:
            jk = file1.read()
        dytoken_init = execjs.compile(jk).call('get_token', init_time)
        params_tokenquery['dynamicToken'] = dytoken_init
        params_tokenquery['timeStr'] = init_time
        url=token_url+urlencode(params_tokenquery)
        init_request = requests.get(url, headers=header_init,)
        csrfID = init_request.json()['data']['csrfID']
        seedToken = init_request.json()['data']['seedToken']
        pin = init_request.json()['data']['pin']
        params_export['timeStr']=init_time+3000
        params_export['dynamicToken']=execjs.compile(jk).call('get_token', init_time+3000,seedToken,pin)
        params_export['csrfID']=csrfID

        params_account=params_export.copy()
        params_account['bizCode']='dkx'
        params_account['rptDataContentType']='adv'

        if not os.path.exists(self.download_path):
            os.makedirs(self.download_path)
        stragecode_dic={"拉新快":"Dkx","上新快":"ShangXin","会员快":"RuHui","货品加速":"ProductSpeed","活动加速":"YuRe","爆发收割":"BaoFa","测款快":"CeKuan",}
        if type == 'all':
            for k,v in stragecode_dic.items():
                params_export['bizCode']='adStrategy'+v
                export_content=requests.get(export_url,params=params_export,headers=header_export).content
                with open(os.path.join(self.download_path,r'创意数据_%s_%s-%s.xls'%(k,self.sdate,self.edate)),'wb') as savedile:
                    savedile.write(export_content)
            print('万相台创意报表数据下载完成')

        if type=='account':
            export_content=requests.get(export_url,params=params_account,headers=header_export).content
            with open(os.path.join(self.download_path,r'账户数据_%s-%s.xls'%(self.sdate,self.edate)),'wb') as savedile:
                savedile.write(export_content)
            print('万相台账户报表数据下载完成')


#淘客
class Taoke():
    def __init__(self,sdate,edate,datediff=1):
        self.sdate=sdate
        self.edate=edate
        self.download_path=r'./数据源/报表/淘宝客'

    @timemark
    def download_taoke(self,cookies,type='account'):
        campaign_url='https://ad.alimama.com/openapi/param2/1/gateway.unionadv/mkt.rpt.lens.data.campaign_present_list.json?'
        taokedata_url='https://ad.alimama.com/openapi/param2/1/gateway.unionadv/mkt.rpt.lens.data.item_effect.json?'
        cprequest_url='https://ad.alimama.com/cp/event/joined.json?'

        tb_token=''
        for i in range(len(cookies.split(','))):
            m=cookies.split(',')[i].split('=')
            if m[0]=='_tb_token_':
                tb_token=m[1]

        headers={
        	'host':'ad.alimama.com',
        	'cookie': cookies,
        	'accept-encoding': 'gzip, deflate, br',
        	'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36',
        	'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        	'accept': '*/*',
        	'x-requested-with': 'XMLHttpRequest',
        	'referer': 'https://ad.alimama.com/fifth/report/item/list.htm'
        }
        params_cpname = {
            "t": int(time.time() * 1000),
            '_tb_token_': tb_token,
            'sceneId': '6',
            'status': '',
            'keyword': '',
            'pageNo': '1',
            'pageSize': '5000',
        }
        coldict = {"日期": "thedate", "商品id": "itemId", "商品名称": "itemTitle", "图片链接": "itemUrl", "计划类型": "campaignName",
                   "计划名称": "campaignTitle", "团长名称": "tkCpPubName", "商品链接": "auctionUrl", "平均优惠券面额": "avgCouponAmount",
                   "支付金额": "alipayAmt", "预售定金金额": "alipayAmtDepositPresale", "支付件数": "alipayByrCnt",
                   "支付笔数": "alipayNum", "预估预售付尾款数量": "alipayNumDepositCpaSubsidyPresale",
                   "预售定金笔数": "alipayNumDepositPresale", "支付人数": "alipayQuantity", "加购宝贝量": "cartAddItmCnt",
                   "收藏宝贝量": "cltAddItmCnt", "结算佣金支出": "cmCommissionFee", "结算佣金率": "cmCommissionRate",
                   "结算服务支出": "cmServiceFee", "结算服务费率": "cmServiceRate", "结算支出费用": "cmTotalFee",
                   "商品折扣率": "couponDisRate", "结算金额": "cpsSettleAmt", "结算件数": "cpsSettleByrCnt", "结算笔数": "cpsSettleNum",
                   "结算人数": "cpsSettleQuantity", "转化率": "cvr", "预售金额": "depPreAlipayAmt",
                   "预估预售整单金额": "depPreAlipayAmtCpaSubsidyPresale", "预估预售佣金费": "depPreCommissionFee",
                   "预估预售佣金率": "depPreCommissionRate", "预估预售整单佣金": "depPreFeeCpaSubsidyPresale",
                   "预估预售尾款支付金额": "depPreRestAmt", "预估预售服务费": "depPreServiceFee", "预估预售服务费率": "depPreServiceRate",
                   "预估预售支付金额": "depSerPreAlipayAmt", "进店量": "enterShopPvTk", "进店访客数": "enterShopUvTk",
                   "付款佣金支出": "preCommissionFee", "付款佣金率": "preCommissionRate", "单件商品付款支出费用": "preGPP",
                   "付款服务费支出": "preServiceFee", "付款服务费率": "preServiceRate", "付款支出费用": "preTotalFee",
                   "确认收货金额": "tkSuccAmt", "确认收货笔数": "tkSuccByrCnt", "确认收货人数": "tkSuccCnt", }

        if type=='all':
            filename=r'%s-%s_淘客分日明细数据.xls'%(self.sdate,self.edate)
        else:
            filename = r'%s-%s_淘客分日账户数据.xls' % (self.sdate, self.edate)
        sheetdict = {}
        for key in coldict.keys():
            sheetdict[key] = []

        cplist = requests.get(cprequest_url, headers=headers, params=params_cpname).json()['data']['result']
        cpdict = {}
        for q in cplist:
            cpdict[q['groupId']] = q['cpName']

        try:
            while self.sdate < self.edate:
                print(self.sdate)
                params_precampaign = {
                    "t": int(time.time() * 1000),
                    '_tb_token_': tb_token,
                    'startDate': self.sdate,
                    'endDate': self.sdate,
                }

                params_goods = {
                    "t": int(time.time() * 1000),
                    '_tb_token_': tb_token,
                    'startDate': self.sdate,
                    'endDate': self.sdate,
                    'q': "",
                    'pageNo': '1',
                    'pageSize': 1000000,
                    'period': '1d',
                    'totalpage': '1'
                }

                campaignlist = requests.get(campaign_url, headers=headers, params=params_precampaign).json()['data']
                for i in range(len(campaignlist)):  # 类型遍历；dict的has_key方法在python3中已被淘汰
                    params_goods['rateSource'] = campaignlist[i]['rateSource']
                    campaigntype = campaignlist[i]['campaignName']

                    if type=='account':
                        params_goods['campaignId'] = ''
                        response_taoke = requests.get(taokedata_url, headers=headers, params=params_goods)
                        pagegoodlist = response_taoke.json()['data']['list']
                        if pagegoodlist:
                            for p in pagegoodlist:  # 商品列表循环
                                if 'auctionUrl' in p:
                                    for key, value in coldict.items():
                                        try:
                                            if key == '计划类型':
                                                sheetdict[key].append(campaigntype)
                                            elif key == '计划名称':
                                                sheetdict[key].append('-')
                                            elif key == '团长名称':
                                                sheetdict[key].append('-')
                                            else:
                                                sheetdict[key].append(p[value])
                                        except Exception:
                                            pass
                                else:
                                    print(campaigntype, ":", p['itemId'])

                    if type=='all':

                            if 'campaignIds' in campaignlist[i] and campaigntype=='营销计划':
                                for j in campaignlist[i]['campaignIds']: #计划遍历
                                    campaignId=j['campaignId']
                                    params_goods['campaignId']=campaignId
                                    response_taoke=requests.get(taokedata_url,headers=headers,params=params_goods)
                                    pagegoodlist = response_taoke.json()['data']['list']

                                    if pagegoodlist:
                                        for p in pagegoodlist:
                                            if 'auctionUrl' in p:
                                                for key, value in coldict.items():
                                                    if key=='计划类型':
                                                        sheetdict[key].append(campaigntype)
                                                    elif key=='计划名称':
                                                        sheetdict[key].append(j['campaignTitle'])
                                                    elif key == '团长名称':
                                                        sheetdict[key].append(cpdict[campaignId])
                                                    else:
                                                        sheetdict[key].append(p[value])
                                            else:
                                                print(campaigntype,'-',campaignId,":",p['itemId'])
                            else:
                                params_goods['campaignId']=''
                                response_taoke = requests.get(taokedata_url, headers=headers, params=params_goods)
                                pagegoodlist = response_taoke.json()['data']['list']
                                if pagegoodlist:
                                    for p in pagegoodlist:  # 商品列表循环
                                        if 'auctionUrl' in p:
                                            for key, value in coldict.items():
                                                try:
                                                    if key == '计划类型':
                                                        sheetdict[key].append(campaigntype)
                                                    elif key == '计划名称':
                                                        sheetdict[key].append('-')
                                                    elif key == '团长名称':
                                                        sheetdict[key].append('-')
                                                    else:
                                                        sheetdict[key].append(p[value])
                                                except Exception:
                                                    pass
                                        else:
                                            print(campaigntype,":",p['itemId'])

                    self.sdate=(datetime.datetime.strptime(self.sdate,'%Y-%m-%d')+datetime.timedelta(days=1)).strftime('%Y-%m-%d')

            taoke_file=xlwt.Workbook(encoding='utf-8',style_compression=0)
            datasheet=taoke_file.add_sheet('taokedata',cell_overwrite_ok=False)
            len_dic=list(sheetdict.keys())
            for w in range(len(len_dic)):
                datasheet.write(0,w,len_dic[w])
            for y in range(len(sheetdict['日期'])):
                for r in range(len(len_dic)):
                    datasheet.write(y+1,r,sheetdict[len_dic[r]][y])

            if not os.path.exists(self.download_path):
                os.makedirs(self.download_path)
            taoke_file.save(os.path.join(self.download_path,filename))
            print('淘客下载成功！')

        except Exception:
            print('请检查登录状态！')




#渠道实时报数
class Reportbyday():
    def __init__(self,cookdir):
        self.edate=datetime.datetime.now().strftime('%Y-%m-%d')
        self.sdate=(datetime.datetime.strptime(self.edate,'%Y-%m-%d')-datetime.timedelta(days=1)).strftime('%Y-%m-%d')
        self.filepath=r'./数据源/报数'
        self.reportdata={'日期':[],'渠道':[],'细分':[],'花费':[],"展现":[],"点击":[],"点击率":[],'点击成本':[],"加购":[],"加购率":[],"加购成本":[],"成交金额":[],'成交笔数':[],"ROI":[],"转化率":[]}
        self.cookdir=cookdir


    def subway_report(self):
        token_url='https://subway.simba.taobao.com/bpenv/getLoginUserInfo.htm'
        campaign_url='https://subway.simba.taobao.com/openapi/param2/1/gateway.subway/common/campaign/list$?'
        report_url='https://subway.simba.taobao.com/openapi/param2/1/gateway.subway/common/rtreport/data/get$'

        session_id = "BCE65970"
        header= {'Referer': 'https://subway.simba.taobao.com/',
                   'Accept-Encoding': 'gzip,deflate,br',
                   'Accept-Language': 'zh-CN,zh;q=0.9',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
                   'Origin': 'https://subway.simba.taobao.com',
                   'Accept': 'application/json, text/javascript, */*; q=0.01',
                   'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                   'X-Requested-With': 'XMLHttpRequest',
                   'Host': 'subway.simba.taobao.com',
                    'cookie':self.cookdir['subway_cook'],
                   }

        params_list={
            'sla':'json',
            'isAjaxRequest':'true',
            'sessionId':session_id,
        }
        params_report={
            'templateId':'rtRptCampaign',
            'trafficType':'[1,4,2,5,6]',
            'mechanism':'[0,2]',
            'group':'custId',
            '_referer':'/manage/campaign/index?selectedCampaignType=8&page=1'
        }

        c_list={'standard':[],'ai':[],'all':[]}
        token=json.loads(requests.post(token_url,headers=header).content.decode('utf-8'))['result']['token']
        params_list['token']=token
        list_request=requests.get(campaign_url,headers=header,params=params_list).json()['result']
        for i in list_request:
            if i['status']!='0':
                c_list['all'].append(int(i['campaignId']))
                if i['type']=='0':
                    c_list['standard'].append(int(i['campaignId']))
                if i['type']=='8':
                    c_list['ai'].append(int(i['campaignId']))

        params_report.update(params_list)
        for d in [self.edate,self.sdate]:
                params_report['theDate']=d
                for k in c_list.keys():
                    params_report['campaignIds']=c_list.get(k)
                    data_up=urlencode(params_report)
                    query_subway=requests.post(report_url,headers=header,data=data_up).json()['result'][0]
                    self.reportdata['日期'].append(d)
                    self.reportdata['渠道'].append('直通车')
                    self.reportdata['细分'].append(k)
                    self.reportdata['花费'].append(floatturn(query_subway['cost'])/100)
                    self.reportdata['展现'].append(intturn(query_subway['impression']))
                    self.reportdata['点击'].append(intturn(query_subway['click']))
                    self.reportdata['点击率'].append(format(float(query_subway['ctr'])/100,'.2%'))
                    self.reportdata['点击成本'].append(floatturn(float(query_subway['cpc'])/100))
                    self.reportdata['加购'].append(intturn(query_subway['cartTotal']))
                    self.reportdata['加购率'].append(divisionprotect1(query_subway['cartTotal'],query_subway['click']))
                    self.reportdata['加购成本'].append(divisionprotect2(floatturn(query_subway['cost'])/100,intturn(query_subway['cartTotal'])))
                    self.reportdata['成交金额'].append(floatturn(query_subway['transactionTotal'])/100)
                    self.reportdata['成交笔数'].append(intturn(query_subway['transactionShippingTotal']))
                    self.reportdata['ROI'].append(floatturn(query_subway['roi']))
                    self.reportdata['转化率'].append(presfloatturn(query_subway['coverage']))


    def super_report(self):
        token_url = 'https://tuijian.taobao.com/api2/member/getInfo.json?'
        get_url='https://tuijian.taobao.com/api2/report/promote/findSum.json?'
        cookies=self.cookdir["newsuper_cook"].replace(',',';').rstrip(';')

        header_init= {'Referer': 'https://tuijian.taobao.com/indexbp-display.html',
                   'Accept-Encoding': 'gzip,deflate,br',
                   'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
                   'X-Requested-With': 'XMLHttpRequest',
                   'Host': 'tuijian.taobao.com',
                   'cookie':cookies,
                   'sec-fetch-mode':'cors',
                   'sec-ch-ua':'Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97',
                   'sec-fetch-dest':'empty',
                   'Sec-Fetch-Site':'same-origin'
                   }

        params_tokenquery={
            "r":"mx_14",
            'callback':'jQuery',
            'bizCode':'display',
            'invitationCode':'',
            'csrfID':'',
        }
        params_get={
            'r':'mx_204'
        }
        data_post={
            'alias':'def',
            'bizCode':'displayDefault',
            'campaignId':'',
            'campaignGroupId':'',
            'creativeId':'',
            'today':self.edate,
            'perspective':'manage',
            'queryTimeDim':'hour',
            'queryDomain':'account',
            'tab':'campaign',
        }

        init_time = int(time.time()* 1000)
        with open(r'.\js_refile\jstk.js', "r", encoding="utf-8") as file1:
            jk = file1.read()
        dytoken_init = execjs.compile(jk).call('get_token', init_time)
        params_tokenquery['dynamicToken'] = dytoken_init
        params_tokenquery['timeStr'] = init_time
        params_tokenquery['_'] = str(init_time + 100)
        init_request = requests.get(token_url, headers=header_init, params=params_tokenquery).text[7:-1]

        csrfID = json.loads(init_request)['data']['csrfID']
        seedToken = json.loads(init_request)['data']['seedToken']
        pin = int(json.loads(init_request)['data']['pin'])

        data_post['timeStr']=init_time
        data_post['dynamicToken'] =execjs.compile(jk).call('get_token', init_time,seedToken,pin)
        data_post['csrfID']=csrfID
        header_get=header_init.copy()

        header_get['content-type']='application/x-www-form-urlencoded; charset=UTF-8'
        header_get['Accept']='application/json, text/javascript, */*; q=0.01'
        header_get['Origin'] ='https://tuijian.taobao.com'

        for i in [self.sdate,self.edate]:
            data_post['startTime']=i
            data_post['endTime']=i

            data_up=urlencode(data_post)
            data_request = requests.post(get_url,params=params_get,data=data_up,headers=header_get)

            if data_request.status_code==200:
                data_list=data_request.json()['data']['list'][0]
                self.reportdata['日期'].append(i)
                self.reportdata['渠道'].append('引力魔方')
                self.reportdata['细分'].append('all')
                self.reportdata['花费'].append(floatturn(data_list['charge']))
                self.reportdata['展现'].append(intturn(data_list['impression']))
                self.reportdata['点击'].append(intturn(data_list['click']))
                self.reportdata['点击率'].append(format(float(data_list['ctr']),'.2%'))
                self.reportdata['点击成本'].append(floatturn(data_list['cpc']))
                self.reportdata['加购'].append(intturn(data_list['cartNum']))
                self.reportdata['加购率'].append(divisionprotect1(data_list['cartNum'],data_list['click']))
                self.reportdata['加购成本'].append(divisionprotect2(data_list['charge'],data_list['cartNum']))
                self.reportdata['成交金额'].append(floatturn(data_list['alipayInshopAmt']))
                self.reportdata['成交笔数'].append(intturn(data_list['alipayInshopNum']))
                self.reportdata['ROI'].append(floatturn(data_list['roi']))
                self.reportdata['转化率'].append(format(float(data_list['cvr']),'.2%'))


    def aipush_report(self):
        token_url = 'https://adbrain.taobao.com/api/member/getInfo.json?'
        camlist_url='https://adbrain.taobao.com/api/account/report/findOverProductAccountRealTime.json?'

        cookies=self.cookdir["aipush_cook"].replace(',',';').rstrip(';')
        init_time = int(time.time() * 1000)
        stragecode_dic={"拉新快":"Dkx","上新快":"ShangXin","会员快":"RuHui","货品加速":"ProductSpeed","活动加速":"YuRe","爆发收割":"BaoFa","测款快":"CeKuan",}

        header= {
                'Referer': 'https://adbrain.taobao.com/indexbp.html',
                'Accept-Encoding': 'gzip,deflate,br',
                'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
                'X-Requested-With': 'XMLHttpRequest',
                'Host': 'adbrain.taobao.com',
                'cookie':cookies,
                'accept':'application/json, text/javascript, */*; q=0.01'
                }


        params_campaign={
            'r':'mx_259',
            'bizCode':'dkx',
            'unifyType':'zhai',
            'timeStr':init_time,
        }

        params_tokenquery = {
            "r": "mx_14",
            'bizCode':'adStrategy',
        }
        with open(r'.\js_refile\jstk.js', "r", encoding="utf-8") as file1:
            jk = file1.read()
        dytoken_init = execjs.compile(jk).call('get_token', init_time)
        params_tokenquery['dynamicToken'] = dytoken_init
        params_tokenquery['timeStr'] = init_time
        url=token_url+urlencode(params_tokenquery)
        init_request = requests.get(url, headers=header,)
        csrfID = init_request.json()['data']['csrfID']
        seedToken = init_request.json()['data']['seedToken']
        pin = init_request.json()['data']['pin']

        params_campaign['dynamicToken']=execjs.compile(jk).call('get_token', init_time,seedToken,pin)
        params_campaign['csrfID']=csrfID

        for d in [self.edate,self.sdate]:
            params_campaign['logDateList']=[d]
            campaignreq=requests.get(camlist_url,headers=header,params=params_campaign)
            if campaignreq.json()['data']['list']:
                result=campaignreq.json()['data']['list'][0]
                # if campaignreq==200:
                self.reportdata['日期'].append(d)
                self.reportdata['渠道'].append('万相台')
                self.reportdata['细分'].append('all')
                self.reportdata['花费'].append(floatturn(result['charge']))
                self.reportdata['展现'].append(intturn(result['adPv']))
                self.reportdata['点击'].append(intturn(result['click']))
                self.reportdata['点击率'].append(presfloatturn(['ctr']))
                self.reportdata['点击成本'].append(floatturn(result['ecpc']))
                self.reportdata['加购'].append(intturn(result['cartNum']))
                self.reportdata['加购率'].append(
                    divisionprotect1(result['cartNum'],result['click']))
                self.reportdata['加购成本'].append(divisionprotect2(result['charge'],result['cartNum']))
                self.reportdata['成交金额'].append(floatturn(result['alipayInshopAmt']))
                self.reportdata['成交笔数'].append(intturn(result['alipayInShopNum']))
                self.reportdata['ROI'].append(floatturn(result['roi']))
                self.reportdata['转化率'].append(presfloatturn(result['cvr']))



#市场排行导入

