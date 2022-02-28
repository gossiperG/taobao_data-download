"""this file is served as frame attach"""





import json
import tkinter
from tkinter import *
import time
from tkinter.ttk import *
from tkinter.messagebox import*
from tkinter.simpledialog import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from Qingmu import Subway,Newsuper_r,Aipush,Taoke,timemark,Reportbyday
import subprocess
import traceback
from io import StringIO
import sys
import brower_request
import datetime
from support_fun import Rethread
from user_data_manger import Timejudge,User_account
from PIL import Image,ImageTk
import os
from icon import img_navi,img_top,img_icon,js_tk
import base64
import xlwt










class Date_frame():
	def __init__(self,mywindow):
		self.window=mywindow
		#为什么封装在函数中调用则textvarible无效？，因为没有使用变量再赋值-sd=sd.set()
		self.sd = ttk.StringVar()
		self.ed = ttk.StringVar()
		self.ed.set(time.strftime("%Y-%m-%d"))
		self.sd.set((datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d'))
		self.datediff = ttk.IntVar()
		self.datediff.set(2)
		self.username=ttk.StringVar()
		self.password=ttk.StringVar()

		self.ua=User_account()
		self.acc_dict=self.ua.user_retrieve()
		self.username.set(self.acc_dict['username'])
		self.password.set(self.acc_dict['password'])

		self.init_frame = ttk.Frame(self.window, style="secondary",)

		self.start_date = ttk.Entry(self.init_frame, textvariable=self.sd,style="light", width=12,)
		self.end_date = ttk.Entry(self.init_frame, textvariable=self.ed,style="light", width=12)
		dated = ttk.Entry(self.init_frame, style="light", textvariable=self.datediff, width=4)
		l_sd = ttk.Label(self.init_frame, text="起始日期： ", style="secondary", foreground="#ADB5BD", background="#444444",font=('微软雅黑',9))
		l_ed = ttk.Label(self.init_frame, text="结束日期： ", style="secondary", foreground="#ADB5BD", background="#444444",font=('微软雅黑',9))

		kval=45
		jval=2
		ttk.Label(self.init_frame,style="secondary", foreground="#ADB5BD", background="#444444",width=6).grid(row=1, rowspan=2, column=32, columnspan=3, padx=(30, 5))

		l_sd.grid(row=jval,column=kval,padx=(30,5),pady=(0))
		self.start_date.grid(row=jval,column=kval+3,columnspan=5)
		l_ed.grid(row=jval+1,column=kval,padx=(30,5),pady=(0))
		self.end_date.grid(row=jval+1,column=kval+3,columnspan=5)

		# l_dd = ttk.Label(init_frame, text="导入周期",font=("微软雅黑",9),  style="secondary", foreground="#ADB5BD", background="#444444")
		# l_dd.grid(row=1,column=12,padx=(45,5),pady=(0))
		# dated.grid(row=2,column=12,columnspan=5,padx=(45,5),pady=(0))

		_username=ttk.Entry(self.init_frame,style="light", textvariable=str(self.username), width=23)
		_password=ttk.Entry(self.init_frame,style="light", textvariable=str(self.password),show="*", width=23)
		l_un= ttk.Label(self.init_frame, text="账户名： ", style="secondary", foreground="#ADB5BD", background="#444444",font=('微软雅黑',9))
		l_pw= ttk.Label(self.init_frame, text="密  码： ", style="secondary", foreground="#ADB5BD", background="#444444",font=('微软雅黑',9))
		l_un.grid(row=jval,column=kval+20,padx=(45,5),pady=(15,5))
		_username.grid(row=jval,column=kval+24,columnspan=5)
		l_pw.grid(row=jval+1,column=kval+20,padx=(45,5),pady=(5,15))
		_password.grid(row=jval+1,column=kval+24,columnspan=5)

		signin_butt=ttk.Button(self.init_frame,text="登 录", bootstyle="success",width=12,command=lambda :Rethread(self._login))
		signin_butt.grid(row=jval,rowspan=2,column=kval+32,columnspan=3,padx=(30,5))

		self.cookdict={}
		self.path=r'.\user_data\request_data'
		if not os.path.exists(self.path):
			os.makedirs(self.path)
		self.file = os.path.join(self.path, r'%s_cookies.json' % (time.strftime('%Y-%m-%d')))
		try:
			with open(self.file,'r') as cookjson:
				for line in cookjson.readlines():
					line=line.strip()
					l=json.loads(line)
			self.cookdict=l
		except Exception:
			pass

	def _login(self):
		tarwin=brower_request.Browser_login(self.sd.get(),self.ed.get())
		tarwin.login(self.username.get(),self.password.get())
		self.ua.user_dict={'username':self.username.get(), 'password':self.password.get()}
		self.ua.user_save()

		self.cookdict=tarwin.cookdir
		self.save()
		print('登录成功!!!')

	def save(self):
		with open(self.file,'w') as cookiejson:
				json.dump(self.cookdict,fp=cookiejson,ensure_ascii=False)


class Dataview(Reportbyday):
	def __init__(self,frame,dfcookdir):
		super().__init__(dfcookdir)
		self.function_frame=ttk.Frame(frame)
		self.view_frame=ttk.Frame(frame)

		self.dfcookdir = dfcookdir
		m = Timejudge()
		if m.request_j():
			pass
		else:
			showinfo(title='登录提示', message='请检查登录状态！')

		col=list(self.reportdata.keys())

		self.button_output = ttk.Button(self.function_frame, text="报数导出", bootstyle="info", width=10, style='info.TButton',command=lambda: Rethread(self.outport))
		self.button_request = ttk.Button(self.function_frame, text="请求数据", bootstyle="info", width=10, style='primary.TButton',command=lambda: Rethread(self.data_request))

		self.datatree=ttk.Treeview(self.view_frame,columns=col,displaycolumns=col[3:],selectmode=tkinter.BROWSE,style='secondary')
		for i in range(len(col)):
			self.datatree.column(col[i],anchor=CENTER,width=70)
			self.datatree.heading(col[i],text=col[i])
		self.hbar = ttk.Scrollbar(self.view_frame, orient=HORIZONTAL, command=self.datatree.xview,style='light')
		self.datatree.configure(xscrollcommand=self.hbar.set)

		self.path=r'.\user_data\report_data'
		if not os.path.exists(self.path):
			os.makedirs(self.path)
		self.file = os.path.join(self.path, r'%s_report.json' % (time.strftime('%Y-%m-%d')))

		if m.report_j():
			self.reportdata = m.report_j()
			self.datawrite()


	def load_frame(self):
		self.button_output.pack(side=RIGHT,)
		self.button_request.pack(side=RIGHT,)

		self.datatree.pack(side=TOP,fill=X,pady=(5,0))
		self.hbar.pack(side=TOP,fill=X)

		self.function_frame.pack(side=TOP,fill=X, pady=(12, 10),padx=(7,8))
		self.view_frame.pack(side=TOP,padx=(7,8))

	def datawrite(self):
		subway = self.datatree.insert('', 0, 'subway', text='直通车', open=True)
		super_r = self.datatree.insert('', 1, 'super', text='引力魔方', open=True)
		aipush=self.datatree.insert('', 2, 'aipush', text='万相台', open=True)
		for i in range(len(self.reportdata['日期'])):
			if self.reportdata['日期'][i]==self.edate:
				rowdata = []
				if self.reportdata['渠道'][i]=='直通车':
					if self.reportdata['细分'][i]=='all':
						for k, v in self.reportdata.items():
							rowdata.append(v[i])
						self.datatree.insert(subway,2, '直通车', text='直通车-汇总', values=(rowdata),open=False)
					if self.reportdata['细分'][i]=='standard':
						for k, v in self.reportdata.items():
							rowdata.append(v[i])
						self.datatree.insert(subway,0,'standard',text='直通车-标准计划',values=(rowdata),open=False)
					if self.reportdata['细分'][i]=='ai':
						for k, v in self.reportdata.items():
							rowdata.append(v[i])
						self.datatree.insert(subway,1,'ai',text='直通车-智能计划',values=(rowdata),open=False)

				if self.reportdata['渠道'][i]=='引力魔方':
					if self.reportdata['细分'][i]=='all':
						for k, v in self.reportdata.items():
							rowdata.append(v[i])
						self.datatree.insert(super_r,END, '引力魔方', text='引力魔方-汇总', values=(rowdata),open=False)  #第三参数iid不能与所有层集中的任何一个子集重复，否则报错

				if self.reportdata['渠道'][i]=='万相台':
					if self.reportdata['细分'][i]=='all':
						for k, v in self.reportdata.items():
							rowdata.append(v[i])
						self.datatree.insert(aipush,END, '万相台', text='万相台-汇总', values=(rowdata),open=False)  #第三参数iid不能与所有层集中的任何一个子集重复，否则报错


	def data_request(self):
		if self.dfcookdir:
			self.deldata()  #注意使用并发线程之后造成的错误,但这里是由于在一个实例类report下多个方法多次写入造成键值重复
			self.subway_report()
			self.super_report()
			self.aipush_report()
			self.datawrite()
			self.save()
			self.view_frame.update()
		else:
			showinfo(title='登录提示', message='请检查登录状态！')

	def deldata(self):
		self.reportdata={'日期':[],'渠道':[],'细分':[],'花费':[],"展现":[],"点击":[],"点击率":[],'点击成本':[],"加购":[],"加购率":[],"加购成本":[],"成交金额":[],'成交笔数':[],"ROI":[],"转化率":[]}
		items=self.datatree.get_children()
		[self.datatree.delete(item) for item in items]  #这种写法emmm，就是列表迭代器吧

	def outport(self):
		if self.reportdata:
			datareport_file = xlwt.Workbook(encoding='utf-8', style_compression=0)
			datasheet = datareport_file.add_sheet('taokedata', cell_overwrite_ok=False)
			len_dic = list(self.reportdata.keys())
			for w in range(len(len_dic)):
				datasheet.write(0, w, len_dic[w])
			for y in range(len(self.reportdata['日期'])):
				for r in range(len(len_dic)):
					datasheet.write(y + 1, r, self.reportdata[len_dic[r]][y])
			if not os.path.exists(r'.\数据源\报数'):
				os.makedirs(r'.\数据源\报数')
			datareport_file.save(os.path.join(r'.\数据源\报数', '报数导出.xls'))

	def save(self):
		with open(self.file,'w') as reportjson:
				json.dump(self.reportdata,fp=reportjson,ensure_ascii=False)


class TextRedirector(object):
	def __init__(self, widget, tag="stdout"):
		self.widget = widget
		self.tag = tag


	def write(self, str):
		self.widget.configure(state="normal")
		self.widget.insert(INSERT, str, (self.tag,))
		self.widget.configure(state="disabled")

class Item_checkb:
	def __init__(self,mywindow):
		self.lf=ttk.Labelframe(mywindow,padding=10,text=" 选 项 ")
		self.account_value = ttk.IntVar()
		self.keyword_value=ttk.IntVar()
		self.region_value=ttk.IntVar()
		self.cell_value =ttk.IntVar()
		self.orient_value=ttk.IntVar()
		self.position_value=ttk.IntVar()
		self.ai_creative_value = ttk.IntVar()
		self.taoke_value = ttk.IntVar()

	def _item(self):
		account_b = ttk.Checkbutton(self.lf, text='账户', variable=self.account_value, onvalue=1, offvalue=0)
		keyword_b=ttk.Checkbutton(self.lf,text='关键词',variable=self.keyword_value,onvalue=1,offvalue=0)
		region_b = ttk.Checkbutton(self.lf, text='地域', variable=self.region_value, onvalue=1, offvalue=0)
		cell_b = ttk.Checkbutton(self.lf, text='单元', variable=self.cell_value, onvalue=1, offvalue=0)
		orient_b = ttk.Checkbutton(self.lf, text='人群', variable=self.orient_value, onvalue=1, offvalue=0)
		position_b = ttk.Checkbutton(self.lf, text='资源位', variable=self.position_value, onvalue=1, offvalue=0)
		ai_creative_b=ttk.Checkbutton(self.lf, text='万-创意', variable=self.ai_creative_value, onvalue=1, offvalue=0)
		taoke_b=ttk.Checkbutton(self.lf, text='淘-团长', variable=self.taoke_value, onvalue=1, offvalue=0)
		account_b.pack(side=LEFT,padx=10,pady=6)
		keyword_b.pack(side=LEFT,padx=10,pady=6)
		region_b.pack(side=LEFT,padx=10,pady=6)
		cell_b.pack(side=LEFT,padx=10,pady=6)
		orient_b.pack(side=LEFT,padx=10,pady=6)
		position_b.pack(side=LEFT,padx=10,pady=6)
		ai_creative_b.pack(side=LEFT,padx=10,pady=6)
		taoke_b.pack(side=LEFT,padx=10,pady=6)
		return self.lf
