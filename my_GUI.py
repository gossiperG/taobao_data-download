"""日用GUI工具"""
import json
import tkinter
from tkinter import *
import time
from tkinter.simpledialog import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from Qingmu import Newsuper_r,Aipush,Taoke,timemark,Reportbyday,Subway
import sys
from support_fun import Rethread
from PIL import Image,ImageTk
import os
from icon import img_navi,img_top,img_icon,js_tk
import base64
from attach_frame import Date_frame,TextRedirector,Item_checkb,Dataview


#window—initial
# window=Tk()




window=ttk.Window(themename="darkly")
# r_info = subprocess.Popen('cmd', stdout=subprocess.PIPE).communicate()[0]


for p in [r'.\asset',r'.\js_refile']:
	if not os.path.exists(p):
		os.makedirs(p)


def write_file(name,bstr):
	if name=='jstk.js':
		file_tmp=open(os.path.join(r'.\js_refile',name),'wb+')
	else:
		file_tmp=open(os.path.join(r'.\asset',name),'wb+')
	file_tmp.write(base64.b64decode(bstr))
	file_tmp.close()

pic_dict={'icon.ico':img_icon,'icon_top.png':img_top,'icoc_navi.png':img_navi,'jstk.js':js_tk}
for k,v in pic_dict.items():
	write_file(k,v)

icon=Image.open(r'.\asset\icoc_navi.png')  #一定要放在win窗体里面才行，不然报错
icon_load = ImageTk.PhotoImage(image=icon.resize((12,12)))

icon_top = Image.open(r'.\asset\icon_top.png')
itop_load = ImageTk.PhotoImage(image=icon_top.resize((35,35)))

window.iconbitmap(r'.\asset\icon.ico')

class App():
	def __init__(self,mywindow:Tk):
		self.mywindow = mywindow
		self.mywindow.geometry("800x700")
		self.mywindow.title("日用工具箱")
		self.df=Date_frame(self.mywindow)
		self.download_frame = ttk.Frame(self.mywindow)
		self.todo_frame = ttk.Frame(self.mywindow)
		self.viewframe=ttk.Frame(self.mywindow)
		self.statement_frame=ttk.Frame(self.mywindow)

		self.booljudge = {'boolm':False,'boold':False,'boola':False,'boolv':False}


	def load_frame(self):
		self.frame_top().pack(fill=BOTH,side=TOP)
		self.df.init_frame.pack(fill=BOTH, pady=(15, 12), padx=(20, 20),ipady=2)
		self.tab_frame = self.tabframe(self.booljudge)
		self.tab_frame.pack(side=LEFT,fill=Y,expand=NO,pady=(3,40),padx=(20,7))


	def frame_top(self):
		top_f=ttk.Frame(self.mywindow,style="light",height=40)
		var_time = StringVar()
		def time_set():
			var_time.set(time.strftime("%H:%M:%S"))
			top_f.after(1000, time_set)
		l_time = ttk.Label(top_f, textvariable=var_time,font=("微软雅黑",10,'bold'),background="#ADB5BD",foreground="#2f2f2f")
		time_set()
		self.datecal = ttk.DateEntry(top_f,bootstyle='secondary',width=10)

		top_icon = ttk.Label(top_f, image=itop_load, background="#ADB5BD")
		l_toptitle=ttk.Label(top_f,text="自用工具箱",font=("微软雅黑",14,"bold"),background="#ADB5BD",foreground="#2f2f2f")

		l_time.pack(side=RIGHT, padx=(0,30))
		self.datecal.pack(side=RIGHT ,padx=(0,8))
		top_icon.pack(side=LEFT, padx=(28, 15))
		l_toptitle.pack(side=LEFT,padx=(0,15),pady=18,ipady=5)
		return top_f


	def tabframe(self,booljudge={'boolm':False,'boold':False,'boola':False,'boolv':False}):
		tabmenu=ttk.Frame(self.mywindow,bootstyle="secondary")
		navigation=ttk.Frame(tabmenu,bootstyle='light')
		iconbutton=ttk.Label(navigation,image=icon_load,background="#ADB5BD")
		navi_label=ttk.Label(navigation,text='功能导航',font=("微软雅黑",10,'bold'),background="#ADB5BD",foreground="#2f2f2f")
		iconbutton.pack(side=LEFT,padx=(14,4))
		navi_label.pack(side=LEFT,padx=(0,8))

		if booljudge['boold'] == False:
			button_download = ttk.Button(tabmenu, text="数据下载", style='dark.TButton',command=lambda:Rethread(self.download_tabchange))  # outline 设置当失去焦点时转变格式为outline
		else:
			button_download = ttk.Button(tabmenu, text=">>  数 据 下 载", style='secondary.TButton',command=lambda: Rethread(self.download_tabchange),)

		if booljudge['boola'] == False:
			button_arrangement=ttk.Button(tabmenu,text="今日待办",style='dark.TButton',command=lambda :Rethread(self.todo_tabchange))
		else:
			button_arrangement = ttk.Button(tabmenu, text=">>  今 日 待 办", style='secondary.TButton',command=lambda: Rethread(self.todo_tabchange))

		if booljudge['boolv'] == False:
			button_view=ttk.Button(tabmenu,text="数据速览",style='dark.TButton',command=lambda :Rethread(self.view_tabchange))
		else:
			button_view = ttk.Button(tabmenu, text=">>  数 据 速 览", style='secondary.TButton',command=lambda: Rethread(self.view_tabchange))
		if booljudge['boolm'] == False:
			button_statement=ttk.Button(tabmenu,text="使用说明",style='dark.TButton',command=lambda :Rethread(self.statement_tabchange))
		else:
			button_statement = ttk.Button(tabmenu, text=">>  使 用 说 明", style='secondary.TButton',command=lambda: Rethread(self.statement_tabchange))


		kval=12
		navigation.pack(fill=X,padx=0,pady=(0,0),ipady=20)
		button_download.pack(fill=X,padx=0,pady=(0,0),ipady=kval)
		button_arrangement.pack(fill=X,padx=0,pady=(0,0),ipady=kval)
		button_view.pack(fill=X, padx=0, pady=(0, 0), ipady=kval)
		button_statement.pack(fill=X, padx=0, pady=(0, 20), ipady=kval)
		return tabmenu

	def data_download(self,frame,df,item):
		download_frame=ttk.Frame(frame)
		item._item().pack(fill=X,padx=(7,15),pady=5)

		datam_frame1=ttk.Frame(download_frame,bootstyle="secondary")
		button_subwayd=ttk.Button(datam_frame1,text="直通车",bootstyle="light",command=lambda :Rethread(Func(frame,df.start_date,df.end_date).subway_d,item,df.cookdict['subway_cook']))  #一定要注意实例化赋值传参以及lambda写法两个要点
		button_newrecommandd=ttk.Button(datam_frame1,text="引力魔方",bootstyle="light",command=lambda :Rethread(Func(frame,df.start_date,df.end_date).super_d,item,df.cookdict['newsuper_cook']))
		button_aipushd = ttk.Button(datam_frame1, text="万象台", bootstyle="light",
		                                  command=lambda: Rethread(Func(frame, df.start_date, df.end_date).aipush_d,
		                                                           item, df.cookdict['aipush_cook']))
		button_taoked = ttk.Button(datam_frame1, text="淘宝客", bootstyle="light",
		                                  command=lambda: Rethread(Func(frame, df.start_date, df.end_date).taoke_d,
		                                                           item, df.cookdict['taoke_cook']))
		button_subwayd.pack(side=LEFT,padx=20,pady=17)
		button_newrecommandd.pack(side=LEFT,padx=20,pady=17)
		button_aipushd.pack(side=LEFT,padx=20,pady=17)
		button_taoked.pack(side=LEFT,padx=20,pady=17)
		datam_frame1.pack(fill=BOTH,pady=(15,15),padx=(7,15))
		return download_frame


	def info_output(self,frame):
		info_frame =ttk.Frame(frame)
		info_lf=ttk.Frame(frame)
		info_label=ttk.Label(info_lf,text="运行日志",style="light",font=("微软雅黑",10,"bold"))
		info_text=ttk.Text(info_frame)
		# info_clear=ttk.Button(info_lf,text="clear",bootstyle="light",command=lambda : self._clear())
		info_label.pack(side=LEFT,fill=X)
		# info_clear.pack(side=LEFT)
		info_text.pack(fill=X)
		sys.stdout = TextRedirector(info_text, "stdout")
		sys.stderr = TextRedirector(info_text, "stderr")
		return info_lf,info_frame,info_text

	def todaytodo(self):
		self.todo_frame=ttk.Frame(self.mywindow)
		todo_tar=Todo(self.todo_frame)
		todo_tar.todo_load()
		return self.todo_frame

	def viewdata(self):
		self.viewframe=ttk.Frame(self.mywindow)
		viewtree=Dataview(self.viewframe,self.df.cookdict)
		viewtree.load_frame()
		self.info_output(self.viewframe)[0].pack(fill=X,padx=(7,15),pady=2)
		self.info_output(self.viewframe)[1].pack(fill=BOTH,padx=(7,10))
		return self.viewframe

	def statement(self):
		self.statement_frame=ttk.Frame(self.mywindow)
		statement='	本工具主要用于推广数据下载和实时监控，目前估计存在的bug不少，如有问题和建议\n可联系韭乌！\n' \
				  '其余注意事项包括：\n' \
				  '1、使用前请注意登录，一般登录有效期为15min，不同后台具体不同，操作失效可重新登录尝试；\n' \
				  '2、短时间内（3min内）不要频繁登录（>3），否则会触发进一步反爬，导致十几分钟的锁ip\n（一般不至于会登来登去的吧？？？）\n' \
				  '3、数据速览也需要登录，也即所有的功能都需要登录本店账号进行统一登录\n' \
				  '4、很重要！！！请自行务必安装node.js[百度搜官网下]\n' \
				  '5、各渠道下载周期均为15天转化'
		statement_l=ttk.Label(self.statement_frame,text=statement,bootstyle="light",font=('微软雅黑',10),width=70,justify=LEFT)
		statement_l.pack(side=TOP,padx=(7,15),pady=(60,40),fill=BOTH)
		return self.statement_frame

	def download_col(self):
		self.download_frame = ttk.Frame(self.mywindow)

		itemcheck=Item_checkb(self.download_frame)
		self.data_download(self.download_frame,self.df,itemcheck).pack(fill=X)

		self.info_output(self.download_frame)[0].pack(fill=X,padx=(7,15),pady=2)
		self.info_output(self.download_frame)[1].pack(fill=BOTH,padx=(7,15),pady=(5,40))

		return self.download_frame


	def download_tabchange(self):
		self.forget()
		self.booljudge['boold'] = True
		self.tab_frame = self.tabframe(self.booljudge)
		self.tab_frame.pack(side=LEFT, fill=Y, expand=NO, pady=(15, 40), padx=(20, 7))
		self.download_col().pack()

	def statement_tabchange(self):
		self.forget()
		self.booljudge['boolm'] = True
		self.tab_frame = self.tabframe(self.booljudge)
		self.tab_frame.pack(side=LEFT, fill=Y, expand=NO, pady=(15, 40), padx=(20, 7))
		self.statement().pack()

	def todo_tabchange(self):
		self.forget()
		self.booljudge['boola'] = True
		self.tab_frame = self.tabframe(self.booljudge)
		self.tab_frame.pack(side=LEFT, fill=Y, expand=NO, pady=(15, 40), padx=(20, 7))
		self.todaytodo().pack(pady=(5,40),padx=(7,15),expand=True,fill=BOTH)

	def view_tabchange(self):
		self.forget()
		self.booljudge['boolv'] = True
		self.tab_frame = self.tabframe(self.booljudge)
		self.tab_frame.pack(side=LEFT, fill=Y, expand=NO, pady=(15, 40), padx=(20, 7))
		self.viewdata().pack(pady=(5,40),padx=(7,15),expand=True,fill=BOTH)

	def forget(self):
		self.booljudge={'boolm':False,'boold':False,'boola':False,'boolv':False}
		self.statement_frame.pack_forget()
		self.tab_frame.pack_forget()
		self.download_frame.pack_forget()
		self.todo_frame.pack_forget()
		self.viewframe.pack_forget()



class Todo():
	def __init__(self,frame):
		self.dict={}

		self.inputv = StringVar(value='在此添加一条待办吧！')
		self.todoframe = ttk.Frame(frame)
		self.doneframe = ttk.Frame(frame)
		self.menuframe = ttk.Frame(frame)

		self.todo_label = ttk.Label(self.todoframe, text="今日待办", foreground="#ADB5BD", background="#222222",font=('微软雅黑',11,'bold'),)
		self.list_todo=Listbox(self.todoframe,foreground="#ADB5BD", background="#444444",height=50,width=27)
		self.done_label = ttk.Label(self.doneframe, text="完结撒花", foreground="#ADB5BD", background="#222222",font=('微软雅黑',11,'bold'))
		self.done_list = Listbox(self.doneframe,foreground="#ADB5BD", background="#444444",height=50,width=27)

		self.entry=ttk.Entry(self.menuframe,foreground="#ADB5BD", background="#444444",textvariable=self.inputv)
		self.button_insert = ttk.Button(self.menuframe,text='插入',bootstyle="primary",command=lambda :self.insert())
		self.button_done = ttk.Button(self.menuframe,text='完成',bootstyle="success",command=lambda :self.done())
		self.button_update = ttk.Button(self.menuframe,text='修改', bootstyle="warning", command=lambda: self.update())
		self.button_remove = ttk.Button(self.menuframe,text='删除', bootstyle="danger", command=lambda: self.remov())
		self.button_clear = ttk.Button(self.menuframe,text='清空', bootstyle="danger", command=lambda: self.clear())

	def todo_load(self):
		self.ini()
		self.todo_label.pack(side=TOP,padx=(3),pady=10,fill=X)
		self.list_todo.pack(side=TOP,padx=(3),fill=BOTH)

		self.entry.pack(side=TOP, padx=(10), pady=(43,15), fill=X)
		self.button_insert.pack(padx=(10),fill=X,pady=(5))
		self.button_done.pack(padx=(10),fill=X,pady=5)
		self.button_update.pack(padx=(10), fill=X,pady=5)
		self.button_remove.pack(padx=(10),pady=5, fill=X)
		self.button_clear.pack(padx=(10),pady=5, fill=X)

		self.done_label.pack(side=TOP,padx=(3),pady=10,fill=X)
		self.done_list.pack(side=TOP,padx=(3),fill=BOTH)


		self.todoframe.pack(side=LEFT,pady=(15,0),padx=5,fill=BOTH,expand=True)
		self.menuframe.pack(side=LEFT, pady=(15,0),padx=5,fill=BOTH)
		self.doneframe.pack(side=LEFT, pady=(15,0),padx=5,fill=BOTH,expand=True)

		self.save()

	def ini(self):
		loaddata={}
		try:
			if not os.path.exists(r'.\user_data\todo_data'):
				os.makedirs(r'.\user_data\todo_data')
			with open(r'.\user_data\todo_data\%s_tododata.json'%(time.strftime('%Y-%m-%d')),'r') as todojson:
				for line in todojson.readlines():
					line=line.strip()
					l=json.loads(line)
			loaddata=l
		except Exception:
			pass

		if loaddata:
			for i in loaddata['todo']:
				self.list_todo.insert(END,i)
			for j in loaddata['done']:
				self.done_list.insert(END,j)

	def done(self):
		if self.list_todo.curselection() == ():
			pass
		else:
			self.done_list.insert(END,self.list_todo.get(self.list_todo.curselection()[0]))
			self.list_todo.delete(self.list_todo.curselection()[0])

	def insert(self):
		if self.entry.get()!="":
			if self.list_todo.curselection()==():
				self.list_todo.insert(self.list_todo.size(),self.entry.get())
			else:
				self.list_todo.insert(self.list_todo.curselection(),self.entry.get())

	def update(self):
		if self.entry.get()!="" and self.list_todo.curselection()!=(): #!=()代表选定了某些项
			selecd_item=self.list_todo.curselection()[0]
			self.list_todo.delete(selecd_item)
			self.list_todo.insert(selecd_item,self.entry.get())

		if self.entry.get()!="" and self.done_list.curselection()!=(): #!=()代表选定了某些项
			selecd_item=self.done_list.curselection()[0]
			self.done_list.delete(selecd_item)
			self.done_list.insert(selecd_item,self.entry.get())

	def remov(self):
		if self.list_todo.curselection()!=():
			self.list_todo.delete(self.list_todo.curselection())
		if self.done_list.curselection()!=():
			self.done_list.delete(self.done_list.curselection())

	def clear(self):
		self.list_todo.delete(0,END)
		self.done_list.delete(0,END)

	def save(self):
		self.dict['todo']= self.list_todo.get(0,END)
		self.dict['done'] = self.done_list.get(0,END)
		with open(r'.\user_data\todo_data\%s_tododata.json'%(time.strftime('%Y-%m-%d')),'w') as todojson:
				json.dump(self.dict,fp=todojson,ensure_ascii=False)
		self.menuframe.after(1200,self.save)



class Func():
	def __init__(self,mywindow:Tk,sd,ed):
		# super().__init__(mywindow)
		self.sdate=str(sd.get())
		self.edate=str(ed.get())
		# self.dd=int(self.target[3].get())

	def subway_d(self,item,cookies):
		subway = Subway(self.sdate, self.edate)
		if item.account_value==0 and item.cell_value==0 and item.keyword_value==0 and item.orient_value==0 and item.region_value==0 and item.position_value==0:
			pass
		else:
			if item.account_value.get()==1 and item.cell_value.get()==1 and item.keyword_value.get()==1 and item.orient_value.get()==1 and item.region_value.get()==1:subway.download_subway(cookies,type="all")
			if item.account_value.get() == 1:subway.download_subway(cookies,type="account")
			if item.cell_value.get()==1:subway.download_subway(cookies,type="cell") #二元表达式
			if item.keyword_value.get()==1:subway.download_subway(cookies,type="keyword")
			if item.orient_value.get()==1:subway.download_subway(cookies,type="orient")
			if item.region_value.get()==1:subway.download_subway(cookies,type="region")

	def super_d(self,item,cookies):
		super_r = Newsuper_r(self.sdate, self.edate)
		if item.cell_value.get()==0 and item.keyword_value.get()==0 and item.orient_value.get()==0 and item.region_value.get()==0 and item.position_value.get()==0:
			pass
		else:
			if item.cell_value.get()==1:super_r.download_newsuper(cookies,type="cell")
			if item.orient_value.get()==1:super_r.download_newsuper(cookies,type="orient")
			if item.position_value.get()==1:super_r.download_newsuper(cookies,type="position")

	def aipush_d(self,item,cookies):
		aidownload = Aipush(self.sdate, self.edate)
		if item.account_value.get()==0 and item.ai_creative_value.get()==0:
			pass
		else:
			if item.account_value.get()==1:aidownload.download_aipush(cookies,type="account")
			if item.ai_creative_value.get()==1:aidownload.download_aipush(cookies,type="all")

	def taoke_d(self,item,cookies):
		taokedownload = Taoke(self.sdate, self.edate)
		if item.account_value.get()==0 and item.taoke_value.get()==0:
			pass
		else:
			if item.account_value.get()==1:taokedownload.download_taoke(cookies,type="account")
			if item.taoke_value.get()==1:taokedownload.download_taoke(cookies,type="all")











if __name__ == "__main__":
	target=App(window)
	target.load_frame()
	window.mainloop()






