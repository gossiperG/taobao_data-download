import sys

# bn = [0,9,945,46,5,486];
# kb={'dengzhi':45,'huge':56}
# bn.append(18)#给列表添加元素，默认末尾添加
# bn.insert(1,45)#指定位置插入元素
# bn.extend([47,123,89])#添加多个元素，但注意必须以列表形式[]，也可以添加添加任何可迭代对象（元组、集合，字典等）
# bn.extend(kb.values())#extend字典实例
# print(bn)
# del bn[2]#通过del语句删除列表元素，注意这里del是语句，不同于前面的insert、append等函数
# bn.remove(45)#通过remove函数删除指定内容，但注意如果列表出现多个重复值，remove默认只是删除第一个值，需要删除全部需要搭配循环语句实现
# print(bn)
# #bn.pop(4)#通过pop函数删除指定位置内容，（）为要删除的位置
# bn.sort()#ture为降序，false为升序，必须首字母大写系统才能识别
# bu[4:6]=[45,89,64]#更改多个值
# bn.insert(4,456)#指定位置插入
# bn.clear()#清空列表

#
# print(bn)
# print(bn.pop());#就算在print中进行执行，pop函数也会执行实际修改
# print(sorted(bn))#sorted与sort基本相同，差别在于sort一般只用于列表，而sort使用面向的变量范围更为广泛，具体可百度
# print(bn[1],'\n',bn[0])#使用\n进行换行的用法，将\n当做独立字符段，加‘’间隔
# an=['ajk','saf','fhskj','axflvk']
# an.reverse()#此类函数最终不涉及返回值，因此不能直接在print中执行，否则返回none
# print()
#
# # def jh=(a1,a2,*a3,**a4):
# # print('a1=',a1,'a2=',a2,'a3=',a3,'a4=',a4)
# # pass #ctrl+/快速注释和取消注释


# ac=['asf','af','fsdakj']
# for acc in ac:
#     print(acc)
#     print('please input:',acc)
# print('ok!,we are end of', acc)

# gh='salar'
# for r in gh:
#     # print('end=',r,'\n')
#     print(r, end=" ")#这样用end时，代表结尾为，等同于/n
#
# ty = range(1,8)#一个1-7的数字集合
# list(ty)
# print('\n',list(ty))#通过list函数将range转化为列表

# itt=[]
# for it in range(1,11):
#     itt.append(it**2) #错误写法itt=itt.append(it**2)#为it里面每一项都平方的意思,函数的本质是执行计算过程，函数前缀的对象是将被计算之后返回赋值的对象，因此不能也不需要额外添加变量进行赋值；
# print(itt)

# ash=[3,24,12,3]
# min(ash)#类似的还有min\max\sum等聚合函数
# print(min(ash))#min(object)和
#
# akh=[ah*2 for ah in ash]#列表解析，循环语句可以为range、list
# print(akh)

# num=list(range(1,100001))
# for ld in num:
#     print(ld)


# print(help(range))

# for kb in  range(1,11,2):#range 三个参数，起步、终止，间距
#     print(kb)

# lifang=[num1**3 for num1 in range(2,14,2)]
# print(lifang)


# al=[7,8,9]
# ak=al[:]
# # ak=al
# ak.append(11)
# al.append(21)
# print(ak,'\n',al)#常见复制赋值错误：将my_foods赋给friend_foods，而不是将my_foods的副本存储到friend_foods（见）。这种语法实际上是让Python将新变量friend_foods关联到包含在my_foods中的列表，因此这两个变量都指向同一个列表。


# print(ak,'\n',al)#正确的复制赋值做法，那么元组和字典等其他对象也是这样？


# 在本章中，我们学会了运算和变量，还了解了选择、循环两种流程控制结构。现在，让我们做一个复杂些的练习，把学到的东西一起重温一下。
# 假设我可以全额贷款买房。房子的总价为50万。为了吸引购房者，房贷前四年利率有折扣，分别1%、2%、3%、3.5%。
# 其余的年份里，房贷的年利率都是5%。我逐年还款，每次最多偿还3万元。那么，完全还清房款最少需要多少年？
# 想一想如何用Python来解决这个问题。如果想清楚了，就可以写程序尝试一下。学习编程的最好方式就是亲自动手，努力解决问题。下面是笔者的解决方案，仅供参考。
# i = 0
# residual = 500000
# interest_tuple = (0.01, 0.02, 0.03, 0.035)
# repay = 30000
#
# while residual > 0:
#     i = i + 1
#     print("第", i, "年还是要还钱")
#     if i <= 4:
#         interest = interest_tuple[i - 1#索引值得注意
#     else:
#         interest = 0.05
#     residual = residual * (interest + 1) - repay
#
# print("第", i+1, "年终于还完了")
#
# #元组#
# kb=(455,89,97)
# cj=(45645,565,65,23)
#cj+kb#元组合并
# for ju in kb:
#     print(ju)
# kb=(455,78)
# print(kb)#元组不能被索引修改，但可以被重新赋值

# byc=['yu','ku','cm','lk']
# bbc=['kz',]
# for bio in  byc:
#     if bio!='ku' :#检查是关系判断时不考虑大小写,使用 and和or可以多个条件
#         print(bio.upper())
#     else:
#         print(bio.title())#if条件语句的基本使用

# guess=input()
# if guess in byc:
# 	print('yes!')
# elif guess in bbc:
# 	print(guess,"?,maybe it's a good thinks!")
# else:
# 	print('NO!please again!')#简单的猜谜游戏，配套循环语句更佳

# age=int(input())
# if age <12:
# 	print("child")
# elif age<18:
# 	print("teenage")
# elif age<60:
# 	print("adult")#可以默认，不用else语句，并用elif指定所有可能的条件及语句，防止恶意代码跑else的漏洞，用多个不含else和elif的if语句指定对象也有类似功能

# users=['heyi','yuyi','kimi','sta']
# users_invaild=['kimi','sandy']
# users.append(input())
# for user in users:
#     if user not in users_invaild:
#         if user == 'admin':
#             print('hello!',user,"would you like to reconfigure the users' authority")
#         elif user=='yuyi':
#             print('Hi!'+user+'I am sorry to remind you that you will lost you authority in 3 days')
#         else:
#             print('Hello!',user)
#     else:
#         print(user,'close you pc in 1 minutes!')


# zhangxiaoshan={'weigh':'42','heigh':'160','age':'45','f_food':'45'}
# print('what do you want to know?')
# search=str(input())
# dimension=['weigh','heigh','age','f_food']
# if search in dimension:
#     print(zhangxiaoshan[search],',So you want to know this?')
# else:
#     print("Sorry we can't find what you want to know, please check your input again!")#字典索引及搭配条件语句使用
# print('If any else you want to complement? enter you content or press l to exit!')
# complement_d=str(input())
# while complement_d!='l':
#     zhangxiaoshan[complement_d]=str(input())#在此通过input实现了对字典的新键值补充写入
#     print('If any else you want to complement? enter you content or press l to exit!')
#     complement_d = str(input())
# print(zhangxiaoshan)#通过循环语句实现对字典的循环写入


# dd=zhangxiaoshan.keys()#同理，如果是对值的遍历的话则是用values(),但对值的提取需要注意重复性的问题
# print(dd)#可以keys()直接在print中使用，但是返回dict_keys(['weigh', 'heigh', 'age', 'f_food'])，也即没有指定变量名
# for k,v in zhangxiaoshan.items():
#     print("she's "+str(k)+' is '+str(v))

# # print(str(zhangxiaoshan.values()))#对于数值类的值的比较可以使用sorted函数进行比较
# vv=zhangxiaoshan.values()
# print(type(vv))#只索引具体位置的值怎么办？
# print(sorted(vv))
# print(set(vv))#set() 函数创建一个无序不重复元素集

# zhangxiaoshan2=[]
# for fg in range(4):
#     zhangxiaoshan2.append(zhangxiaoshan)
#     print(fg,zhangxiaoshan2)#字典嵌套在列表中
# print(zhangxiaoshan2)
#
# ch_k = str(input())
# ch_v = input()
# for ch in zhangxiaoshan2:
#     ch[ch_k]=ch_v
# print(zhangxiaoshan2)#字典嵌套列表中进行循环写入键值



#集合-set
# jihe={54,4586,4865,565,56}#用{}括起来的是集合，集合是无序的,因此不能索引
# jihe.remove(54)#remove方法
# print(jihe)









#条件#
# age=input('hey!miss zhangxiaoshan,would you like to tell me your age?')
# # age+=input('so 5 years later your age will be?')#非覆盖性赋值，而是追加性赋值
# age2=input('so 5 years later your age will be?')
# age3=int(age2)%2#求模运算符，取得余数
#
# if  int(age) == int(age2)+5:
#     print('yes!you are excellent!')
# else:
#     print('Oh!I am sorry for your IQ exactly')
# print(age,age2,age3)
# input(str(age3)+'how are you?')#input仅支持输入一个变量，因此多个字符串可以用+连接，不可用‘，’，同时为了防止字符串与数字不能串联，可用str解决

#循环#
# num=input('Guess the number in my mind now?')
# ans='12'
# kb = True #注意pycharm中只能大写有提示，小写无提示
# while kb== True:#①使用标志作为循环条件，搭配if条件变更标志状态
#     if num==ans:
#         kb== False
#         print('oh yes!what a clever boy you are!')
#     else:
#         print('No!Guess again!')
#         num=input()

# while True:#无限循环，除非指定条件使之终止
#     if num==ans:
#         break
#     else:
#         num = input('again please!')#②使用TRUE和break搭配条件语句进行判断；continue 逻辑于此相反，

# new_user=['gsdjk','djk','sdhjk']
# old_user=[]
# i=0
# while i<3:
#     if

# current_number = 0
# while current_number < 10:
#     current_number += 1
#     if current_number % 2 == 0:
#         continue
#     print(current_number)


#coding=utf-8

# print("打卡开始")
# count = 1 #定义一个整数，表示读取该用户的次数
# while count < 9:
#     count = int(input("请输入你的序号:"))
#     print("第",count,"个小天使报道：",count)
#     if count == 6:
#         break
#     count = count + 1#此类break和while的语句，促进循环进程的语句应该放在条件判断之后，有利于通过判断决定是否继续循环进程
#
# print("打卡结束")


#coding=utf-8

# print("打卡开始")
# count = 1 #定义一个整数，表示读取该用户的次数
# while count < 9:
#     count = int(input("请输入你的序号:"))
#     if count == 3 or count == 4:
#         continue
#     print("第",count,"个小天使报道：",count)#这一类continue的千万注意if的逻辑，在这里，符合if的条件也即TRUE的话就打回去上一步继续循环，否则FALSE的话就执行CONTINUE，继续下一步
#     count =count + 1
#
# print("打卡结束")




# while new_user:#[列表遍历和值的跨列表转移]while默认为空为FALSE，非空为TRUE
#     deled=new_user.pop()
#     old_user.append(deled)
#     print('the new users had del\n'+deled)
# print('new_user='+new_user)
# print('old_user'+old_user)

# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)
# while 'cat' in pets:
#     pets.remove('cat')
#
# # print(pets)
# #以上通过循环实现对列表
# bv=set(pets)
# print(bv,type(bv),list(bv),)#set函数返回的是一个为set类型的集合，需要用list函数转化为list,遇到外部有引号的需要先用eval去掉引号然后进行执行,
# #另外需要注意的就是list(bv).remove('cat')这种写法返回none，暂时搞不清楚，问题有待结局！
# print(bv,type(bv),tuple(bv))#类似的也可以转化为元组

# ghk=('dfkjds')
# print(set(ghk))#这里的set很有意思
#
# x = set('eleven')
# y = set('twelve')
# print(x,y)
# #({'l', 'e', 'n', 'v'}, {'e', 'v', 'l', 't', 'w'})
# print(x & y)  #交集
# #{'l', 'e', 'v'}
# print(x | y)  #并集
# #{'e', 'v', 'n', 'l', 't', 'w'}
# print(x - y)  #差集
# #{'n'}
# print(y -x)   #差集
# #{'t', 'w'}
# print(x ^ y)  #补集
# #{'t', 'n', 'w'}
# print(y ^ x)  #补集
# #{'w', 'n', 't'}

#函数#
# def stu_remind(date,name):
#     print('hello! '+name.title()+', I am grant to tell you that you have study these substantial content in '+date)
#     print('>>>')
#
# stu_remind('2021-02-18','kimi')

# def yourname(l,s,m=''):#通过将有默认值的形参放置末尾，尽可能减少出现bug，比如不需要强制使用关键字输入实参来规避错误，注意这种写法不要等号两边留空
#     if m:#if+一个对象，也即指的是默认这个对象非空为TRUE
#         name1=l+m+s
#         return name1
#     else:
#         name2=l+s
#         return name2#使用return非返回值的形式
#
# yourname('huang','yaoming')
# print(yourname('huang','yaoming'))

# oi=1
# while True:
#     oi += 1
#     if oi==12:
#         break#如果条件成立，那么循环就此终止，不继续之后的语句和循环
#     print(oi)


# def build_person(first_name, last_name, age=''):
#     """返回一个字典，其中包含有关一个人的信息"""#函数文本解释块，需要用三个"
#     person = {'first': first_name, 'last': last_name}
#     if age:
#         person['age'] = age
#         return person
# kl=input('first name:')
# ko=input('last name:')
# musician = build_person(kl, ko, age=27)
# print(musician)


#一个可持续键入专辑信息的语句#
# def misic_inf(musicname,album,siger=''):
#     info={}
#     info[musicname]=input('music_name:')
#     info[album]=input('album:')
#     info[siger] = input('siger:')
#     if info[siger]=='':
#         info.pop(siger)#如果可选形参为空，则用pop删掉
#         return info
#         # print('music_info:',info)
#     else:
#         # print('music_info:',info)
#         return info
#
# # print(misic_inf('a1','b1',))
#
#
# # misic_inf('m1','a1','s1')
# num=1
# serial=1
# hg={}
# while True:
#     print("Is any other music you want to fill in? 'P' to exit or 'C' to continue!")
#     judge=input()
#     if judge.upper()=='P':
#         break
#     hg[num]=misic_inf('music_name' + str(num), 'music_album' + str(serial), 'singer')#注意在此就能看出来典型的函数返回变量还是输出语句的重要性,用print语句非返回值，用此函数进行赋值的话返回none
#     if num%2==0:
#         serial+=1
#     # misic_inf(input('music_num:')+input('album_num:')+input('singer_num:'))
#     num += 1
# print(hg)

#列表在函数中的传递#
# def list_round(nums,new):
#     while nums:
#         del_num=nums.pop()#这里很神奇，直接先写函数那么在函数里面的自动填补无法识别你的参数变量是列表，因此只能直接写
#         new.append(del_num)
#     print(new)
# nums1 = ['fg','df','ds']
# new1=[]
# list_round(nums1,new1)
# print(nums1)


# def build_profile(first, last, **user_info):
#     """创建一个字典，其中包含我们知道的有关用户的一切"""
#     profile={}
#     profile['first_name'] = first
#     profile['last_name'] = last
#     for key, value in user_info.items():#这种函数方法处理字典比上面的更为高效
#         profile[key] = value
#         return profile
#
# user_profile = build_profile('albert', 'einstein',
# location='princeton',
# field='physics')
# print(user_profile)

#任意参数实参
# def sanwich_mes(*sans_youwany):#传递任意数量实参
#     for san in sans_youwany:
#         print(san)
#
# sanwich_mes('fdkhj','dfkj','dsfkj')

# def user_profile(firstname,lastname,**describe):#**define_name表示创建一个空字典并允许传递任意数量的关键字参数
#     user_mes={}
#     for key,value in describe.items():#注意字典的循环一定要用items函数
#         user_mes[key] = value
#     # return user_mes
#     print('Hello!\t'+firstname+lastname,'\nplease confirm your mes',user_mes)#必须厘清目标需要返回一个变量还是打印语句


#函数的封装、调用与导入
# import user as u#对导入模块文件进行重命名，重命名后原文件名失效，仅限于全文件导入的这种import方法
#
# u.user_profile('huang','yaoming',age='18',intrest='play game',birthplace='zhuhai')#通过import语句调用从其他文件中封装好的函数，import语句一般写完函数的引用后自动补充，使用这种方法需要用点连接文件名和所调用的函数

#导入模块指定的函数#
# from user import user_profile as test1,sanwich_mes as test2#注意这种导入方法在函数没有使用的时候显示灰色,可以使用as进行别名命名，避免出现函数名字与现有函数重名，重命名后原函数名将失效，对指定函数命名只限于from...import语句
# test1('huang','yaoming',age='18',intrest='play game')#使用from和import可以直接使用
# test2('jkds','asdhf')
# from user import *#导入全部函数，与import类似，但弊端一样，慎用


#类：本质上就是对统一归类需要的方法进行封装，多个类本质共享变量
import random


# class Restaurant():#类的命名注意首字母大写，切记
#     def __init__(self,name,type):#__init__一种特殊的约定俗成的方法，每当你根据Dog类创建新实例时，Python都会自动运行它，封装self,以指定后面方法引用。一般在创建对象时,会把一些公用的字段都放入init方法,init方法一般用于初始化,因为创建对象时,有些是需要先创建
#         self.name=name
#         self.type=type
#
#     def desribe_restaurant(self):
#         print('Welcome to '+self.name+' restaurant! we are provide the '+self.type+' service!')
#
#     def open_des(self):
#         print(self.name+' restaurant is doing business!')
#
#
# r1 = Restaurant('diandoude','chinese food')
# print(r1.name+' welcome for you!')
# r1.open_des()
# r1.desribe_restaurant()


# class User():
#     def __init__(self,f_name,l_name,**info):#能否在这里使用**生成任意关键词
#         self.fn=f_name
#         self.ln=l_name
#         mes={}
#         for k1,v1 in info.items():
#             mes[k1]=v1
#         self.infor=mes#只能通过这种创建变量并传递的方法使用任意关键字变量，不能直接循环+self.mes[k1]=v1
#
#     def describe(self):
#         print(self.fn+self.ln,self.infor)
#
#
# u1=User('HUANG','YAOMING',age='18',instrest='game')
# u1.describe()

# class User1():
#     def __init__(self,f_name,l_name,*info):#能否在这里使用**生成任意关键词
#         self.fn=f_name
#         self.ln=l_name
#         self.info=info#对于任意数量的实参传递，则可以直接赋值，基本与单纯的def同
#     def describe(self):#通过self在各个方法中做第一形参勾连类中的方法
#         print(self.fn+self.ln,self.info)
#
#
# u1=User1('HUANG','YAOMING','18','game')
# u1.describe()

# class Car():
#     def __init__(self,make,year):
#         self.make=make
#         self.year=year
#         self.miles_def=0#在默认方法这里创建属性并直接指定值，不需要实参
#
#     def mile(self,miles=0):#通过方法改写属性的值，也可用类.属性=new_value的方法修改属性值，还有就是通过方法里面写语句修改
#         if miles<self.miles_def:
#             print('REjection!')
#         else:
#             self.miles_def=miles
#             print('we support max mile till '+str(self.miles_def))
#
#     def sum_miles(self,day):#self在类中其他方法的作用在于通过赋值self这个主体将方法中的实参变为属性值及方法    共享给其他方法
#         self.miles_def*=day
#         sk='so under this condition, your sum miles is '+str(self.miles_def)
#         return sk

#类的封装和导入
#Import file_name (as define_file_name)
#From file_name import function1_name,function2_name(as define_function2_name)…


# audi=Car('audi','1912')
# audi.mile(112)
# audi.sum_miles(5)

#子类与父类#
# class E_car(Car):
#     def __init__(self,make,year):
#         super().__init__(make,year)#注意这里不用加:及self
#
#     def e_power(self,power):
#         print(power)
#
#     def mile(self,miles=4):#在子类中重写父类方法,继承中的多态
#         self.miles_def=miles
#         print(miles,self.sum_miles(4))
#
# TESLE=E_car('tesle','1997')
# TESLE.mile()
#
#
# class Lcar():
# #将实例用作属性L_car():
#     def __init__(self,make1,year1):
#         self.carmes=Car(make1,year1)#注意这里引入别的类的的后如果要求必要实参，必须加上，不能直接Car()这样子，至于赋值，可以指定默认值，也可以通过指定形参赋值
#
#
# fengtian=Lcar('tesle','1997')
# print(fengtian.carmes.make)#这样子无论传递引用类的属性和方法都可以传递到对应属性值


# message = "This car can go approximately " + str(range)
# message += " miles on a full charge."
# print(message)#一个参数通过运算操作符顺利完成两个文案输出，挺好

#小练习#
# class ICECREAM(Restaurant):#类的命名注意首字母大写，切记
#     def __init__(self,name,type,*flavors):#__init__一种特殊的约定俗成的方法，每当你根据Dog类创建新实例时，Python都会自动运行它，封装self,以指定后面方法引用。
#         Restaurant.__init__(self,name,type)#子类对父类构造方法的调用，可以直接以引用类类名调用构造，不一定用super（），但super函数会帮我们自动找到基类的方法，而且还自动为我们传入self参数，避免子类进行新的构造函数覆盖基类构造函数（或者使用父类名。父类构造方法（）进行调用，效果与super同）
#         # self.name=name
#         # self.type=type#继承父类后这一类属性值形参赋值不用谢
#         self.sflavors=flavors #给子类定义属性和方法，放在init后面就是默认要执行的属性赋值和方法
#
#     # def desribe_restaurant(self):
#     #     print('Welcome to '+self.name+' restaurant! we are provide the '+self.type+' service!')
#     #
#     # def open_des(self):
#     #     print(self.name+' restaurant is doing business!')
#
#     def ice_cream(self):
#         print('We support these type ice cream: ',list(self.sflavors))
#
#
# usar=ICECREAM('kfc','fast food','lemon','pear','starwberry')
# usar.ice_cream()

#关于super()#
#通常情况下，我们在子类中定义了和父类同名的方法，那么子类的方法就会覆盖父类的方法。而super关键字实现了对父类方法的改写
#(增加了功能，增加的功能写在子类中，父类方法中原来的功能得以保留)。也可以说，super关键字帮助我们实现了在子类中调用父类的方法,原则：优先传递最近一级引用类的构造，之后再传递引用类的嵌套类构造，有同时class V(C,A)（）多个类引用的的话遵从由左到右原则


#collection模块 orderidct类，让导入字典不仅能录入键入的键值对，还能记录他们的添加顺序

# from random import randint
# k=random.randint(1,5)
# k2=randint(4,8)
# print(k,k2)#from...import这种导入方法则是兼容两种写法

# import random
# jk=random.randint(1,3)#两种不同的导入方法，在调用引用类的方法和属性时写法都不一样
# print(jk)

# from random import randint
# class sides():
#     def __init__(self):
#         self.num=6
#
#     def roll_die(self):
#         i=0
#         while True:
#             i += 1
#             if i<11:
#                 roll_num=randint(1,self.num)
#                 print(roll_num)
#             else:
#                 print('game over!')
#                 break
#
#
# play_sides=sides()
# print(play_sides.roll_die())#这种情况下出现最后总是出现none怎么办？
# play_sides.roll_die()#解答上面的问题，因为本来类的方法返回就是print语句（如果是return值，那就还好），外面再嵌套就会出现none,是因为python函数使用return返回值，若不用return而使用print输出值，那么这函数默认还有一个返回值为None



# import sys#系统标准库
# print(sys.argv)#查看我们当前运行文件所在的目录

# import xlrd
# file_path='C:\\Users\\90773\\Desktop\\ceshi.xlsx'#文件名注意使用反斜杠或者双斜杠
# with xlrd.open_workbook(file_path) as file_object:
#     # content_ceshi=file_object.read()
#     # content1=file_object.read()
#     print(file_object)

# filename='C:\\Users\\90773\\Desktop\\数据库账号.txt'
# with open(filename,encoding='utf-8') as zhanghao:#注意编码形式，默认不加就使用gbk编码，那样子对encoding不一样的就不行，另外在这里with是一个代码块，类似while等一样，语句变量只在代码块内运行,自带open函数的参数open(file, mode='r', buffering=-1, encoding=None,errors=None, newline=None, closefd=True, opener=None)
#     # content=zhanghao.read()
#     # print(content)
#
#     # for lines in zhanghao:
#     #     print(lines.rstrip())#上下两种读取方式同时print的时候竟然只是返回一个？rstrip用作删除空白行
#
#     lins=zhanghao.readline()#好像只读取了一行内容，是因为编码原因还是？
#
# for li in lins:
#     print(li)

# newfiletest='C:\\Users\\90773\\Desktop\\testwfile.txt'
# with open(newfiletest,'a') as wfile: #写入的时候，如果写入的文件不存在，系统将自动创建它，读取的时候只会出现查找不到的错误，四种模式：'r'  'w'  'a'[附加模式]  'r+'[同时读取和写入]
#     wfile.write("\nI like python!")
#     wfile.write('\n'+str(78754))

# import time
# while True:
#     print('Hello! please input your name:\n')
#     your_name = input()
#     print('Welcome to python world!\n')
#     print('So tell me why you want to study python?\n')
#     your_reason = input()
#     logfile='C:\\Users\\90773\\Desktop\\log_file.txt'
#     with open(logfile,'a') as log:
#         log.write(str(time.time())+'\n'+your_name+'\n'+your_reason)#时间戳这里有点问题，有待解决
#     if  your_reason=='q':
#         break

# try:#try语句，类似于excel中的iferror
#     ans=5/5
# except ZeroDivisionError:#在这里把except理解为once更好
#     print('zero error!')
# else:
#     print(ans)
#
# help(FileNotFoundError)


#读取多个文件时可以考虑做成函数，将多个文件地址封装在列表中进行循环#
# bookfile='C:\\Users\\90773\\Desktop\\testwfile.txt'
# try:
#     with open(bookfile,encoding='utf-8') as book:
#         bookread=book.read()
#         stringnum=bookread.split()#返回一个根据空格键分隔的列表[附记：似乎有点明白了，用点嵌连对象的通常是python额外包的函数，也即是类的方法或者模块得到方法，而不需要.的是自带的函数]
# except FileNotFoundError:
#     print("sorry!we can't find your file!")
# else:
#     print(len(stringnum))#(注意len函数)


#json文件，方便多种程序语言之间共享打开的一种数据格式#
# import json#需要导入
# num=[7,5,89,8,77]
# jsonfilename='C:\\Users\\90773\\Desktop\\list_test.json'
# with open(jsonfilename,'w') as jl:
#     json.dump(num,jl)#调用json模块中的dump方法进行写入，但是注意和普通的write写法不一样，这里是将对象作为实参数据，普通write则是内置函数
# #注意json的with语句中不能同时写入和读取，需要分开两个with语句进行读写操作
# with open(jsonfilename) as kl:
#     fileload=json.load(kl)
#     print(fileload)


# inp=input('how old are you?')#input语句作为变量赋值只会返回输入的部分，不返回提示输入的部分
# print(inp)


#代码重构：通过调整代码整体结构层次以提高易读性和条理性
import json
import random
# userfile='D:\\python_file\\json_test_file\\userfile.json'
# usernames=['zhangyixing','邓紫棋','huhaiquan','胡歌']
# with open(userfile,'w',encoding='utf-8') as usfile:
#     json.dump(usernames,usfile,ensure_ascii=False)
# with open(userfile,encoding='utf-8') as usfile2:
#     readname=json.load(usfile2)
#     print(readname)
# def checkname():
#     try:
#         with open(userfile) as usfc:
#             usernamer=json.load(usfc)
#             return usernamer
#     except  FileNotFoundError:
#             return None
#
# def getnewname():
#     us_temp=input('please input your name:')
#     return us_temp
#
# def getusername():
#     username=checkname()
#     if username:
#         k=random.randint(0,3)#注意中间是，而非：
#         print('welcome to you! '+username[k])
#     else:
#         username=getnewname()
#         print('welcome to you! '+username)

#用类的做法#
# class Getusername():
#     def __init__(self):
#         self.userfile = 'D:\\python_file\\json_test_file\\userfile.json'
#         self.usernames = ['zhangyixing', '邓紫棋', 'huhaiquan', '胡歌']
#         with open(self.userfile, 'w', encoding='utf-8') as usfile:
#             json.dump(self.usernames, usfile, ensure_ascii=False)
#         # self.name=input('please input your name:')
#         with open(self.userfile,encoding='utf-8') as usfc:
#             self.usernamel=json.load(usfc)
#
#     def checkname(self,name):
#         self.name = name
#         while self.name in self.usernamel:
#             print('sorry!'+self.name+' this name has been used! please rename you name ')
#             # self.name = input('please input your name:')
#             # print('welcome for your join ' + self.name)
#         self.usernames.append(self.name)#json的追加好像只能以这种方式了
#         with open(self.userfile,'w',encoding='utf-8') as usw:
#             json.dump(self.usernames,usw,ensure_ascii=False)#写入json文件时注意加ensure_ascii=False，不然尽管open语句设置了utf8编码，但是写入依然默认ascii编码
#         with open(self.userfile,encoding='utf-8') as usq:
#             self.final=json.load(usq)
#             print(self.final)
#
#
#
#
# User=Getusername()
# User.checkname()

#关于main





# def getname(firstname,lastname,middlename=''):
#     if middlename:
#         fullname = firstname + middlename + lastname
#         return fullname#一个函数中最终只能返回一个return?
#     else:
#         fullname = firstname+lastname
#         return fullname
#
# # print(getname('huang','yaoming','si'))



# list_name=['zhengfu','gongmin','diren']
# list_name[0]=15
# list_name[1]=23
# list_name[2]=27
#
# print(list_name)


#isinstance()函数（用来判断两个输入参数类型是否一致）
# print(isinstance(36,int))

#一些条件表达式的变体
#①
# kt=45
# if 45>kt>12:
#     print('中等')
# elif 70>kt>45:
#     print('高级')
# else:
#     print('都还不错')
#②
# x=int(input('x:'))
# y=int(input('y:'))
# mv=x if x>y else y#注意这里和列表生成器一样用法，但是与正常的if语句不同 没有:
# print(mv)

#dir（）函数
# print(dir(list))#返回对应数据容器的操作函数
# # print(dir(tuple))
# kmi=[12,456,657,78]
# print(kmi.__init__())
# print(kmi)

#魔法函数？？？也就是构造函数，通常被__ __所包围，一般就是一个类中被创建时自动调用的函数，实例化对象时可以传入参数
#公有和私有？ python内部采用了一种叫 name mangling(名字改编)的技术，也即对一个类的方法前加__即可将其私有化，只能由类内部进行访问，外部不可访问，其实，name mangling(名字改编)技术，只是把双下划线开头的变量进行了改名而已。实际上在外部使用“_类名__变量名“即可访问双下划线开头的私有变量了：
#p._Person__name【eg】
#使用print调用__doc__属性，可以带格式查看这个模块的简介
# print(list.__doc__)

#算术运算
# class Jiafa:
# 	def __init__(self,num):
# 		self.num=num
#
# 	def __mul__(self, other):
# 		return int.__mul__(self.num,other)
#
# jia=Jiafa(15)
# print(jia.__mul__(4))



# #类的拾遗{覆盖的概念？补充}
# class Og:#class_name: 和 class_name:两种方法都行
# 	def __init__(self,kl):
# 		self.name=kl
#
# 	def x_name(self):
# 		return self.name+' Welcome for your asign!'
#
#

# cjk = Og('mcn')
# print(cjk.name)
# print(cjk.x_name())
# cjk.name='sak'
# print(cjk.name)
# print(cjk.x_name())
# cjk.x_name='54'#方法已经被新建的同名属性覆盖了，调用不了原先类的方法
# print(cjk.x_name)
#
# class Ig(Og):
# 	def game(self,game):
# 		self.game(game)
#
# #一些其他的函数：
# print(issubclass(Ig,Og))#issubclass（class，classinf）如 果第一个参数（class）是第二个参数（classinfo）的一个子类，则k回Tue，否则返回False
# print(isinstance(cjk,Ig))#isinstance（object，classinf）如果第一个参数（object）是第二个参数（classinto）的实例财象，则返回Tuve，否则返回False
# print(hasattr(Ig,'game'))#hasattr（object，name）用来测试一个对象里是否有指定的属性，第一个参数（objec）是对象，第二个参数（name）是属性名（属性的字符串名字）,注意属性名要用‘'括起来
# print(getattr(cjk,'name'))#getattr（object，namel，default）返回对象指定的属性值，如果指定的属性不存在，则这回default（可选参数，若没有设置default参数，则地出异常;setattrobject，name，value）可以设置对象中指定属性的值，如果指定的属性不存在，则会新建属性并赋值;delattfobject，name）用于删除对象中指定的属性，如果属性不存在，地出异常

#lambda表达式
# -Python写一些执行脚本时，使用lambda就可以省下定义函数过程，比如说我们只是需要写个简单的脚本来管理服务器时间，我们就不要专门定义一个函数然后再写调用，使用lambda就可以使得代码更加精简。[有点像列表生成器]
# def yr(x):
# 	x*=4
# 	return x
#
# yc=lambda t: t*4 #嗯，在lambda里面：前面是传参，后面就是返回变量的表达式，等号前面就是变量名，整一个函数最终就是一个表达式
# yi=lambda i,p:i*8+p+9#可以传入多个参数，但最终返回参数只能一个
#
# print(yr(5))
# print(yc(5))
# print(yi(4,12))
#拓展用法：
# kl=map(lambda i,ci:(i,ci),list89,list2)
# print(list(kl))


#内嵌函数:函数内调用函数，有点类似类里的方法
# def food(x,y):
# 	if x<y:
# 		return str(x)+' yuan is enough for fish!'
# 	else:
# 		def addmoney(k):
# 			if y+k>10:
# 				return 'buns'
# 			else:
# 				return 'drink'
#
# 		return addmoney(int(input( str(y) + ' is not enough so you can think about add some money such food:')))
#
# print(food(10,6))


#闭包
# def fun1(x):
# 	x*=2
# 	def fun2(y):
# 		y=x+1
# 		return y
# 	return x#[非闭包]

#eg1
# def fun1(x):
# 	x*=2
# 	def fun2(y):
# 		y*=x+1
# 		return y
# 	return fun2#[闭包],特点就是返回的是内嵌的函数
#
# print(fun1(5)(3))#调用的时候需要给齐参数

#eg2
# def fun1(x):
# 	x*=2
# 	def fun2():
# 		nonlocal x
# 		y=x+1
# 		return y
# 	return fun2()#[闭包],但与上面不一样，这里以函数的形式写法直接返回函数复制，调用函数就不需要两次传参
#
# print(fun1(5))

#汉诺塔与递归：每次循环将问题对象编程n-1，在汉诺塔实例中也即每次执行n的n-1和1的分离，实现腾出盘子
# def hanoi(n, x, y, z):
# 	if n == 1:
# 		print(x, '-->', z)
# 	else:
# 		hanoi(n - 1, x, z, y)#n-1移到y[中介1]
# 		hanoi(1, x, y, z)#（中介2）
# 		hanoi(n - 1, y, x, z)#(中介3)#这三步代表移动的步骤，所以n个汉诺塔的移动需要经过hanoi(n-1)+hanoi(n-1)+1=2haoni(n-1)+1
#
# n = int(input('请输入层数：'))
# hanoi(n, 'x', 'y', 'z')

# for i in range(5):
# 	print(i)


#递归联系2 斐波那契数列
# def fibon(n):
# 	if n==1:
# 		final=1
# 	elif n==2:
# 		final=1
# 	else:
# 		final=fibon(n-1)+fibon(n-2)
# 	return final
#
# print(fibon(8))



# import  time
# # print(time.localtime())#获取时间
# #写一个计时器,要点在于用条件语句判定起始和终止的时刻，并且通过构造一个列表容器封装起始和终止时间的差值，并利用这个差值的特点进行索引返回值
# class timerecord():
# 	def __init__(self):
# 		self.final=[]
# 		self.name=['year','month','day','hour','minutes','seconds']
#
# 	def timestart(self):
# 		self.start=time.localtime()
#
# 	def timestop(self):
# 		if not self.start:
# 			print('please start!')
# 		else:
# 			self.stop=time.localtime()
# 			for i in range(6):
# 				self.final.append(self.stop[i]-self.start[i])
# 				if self.final[i]:
# 					return str(self.final[i])+self.name[i]
# 			self.stop=0
# 			self.start=0
#
# t=timerecord()
# t.timestart()
# time.sleep(62)
# print(t.timestop())
#
# print(list.__doc__)

# import sys
# # print(sys.path)
# print(sys.argv)

# list89=[45,56,'dsfgk',12]
# list2=['sdf','df','dsf']

# for i,ci,ki in zip(list89,list2,range(5)):#使用zip变量进行多个遍历并行,但是遵从水桶原理，以最短容器为最终长度
# 	ti=str(i)+ci+str(ki)
# 	print(ti)

# import pygame
# pic=pygame.image.load('mygame/pic/ship.bmp')
# rect1=pygame.rect.Rect(0,0,1244,2304)#创建一个rect变量
# print(pic.get_rect())
# print(rect1)

# dict1={'weigh':'42','heigh':'160','age':'45','f_food':'45'}
# print(str(dict1).replace(''))


# import re
# 配合正则表达式删除数字中的逗号【分隔号】
# s = 'Today is Sunday, I bought $ 100,000.'
# p = re.compile(r'\d,\d')
#
# print(p.search(s))
# while 1:
# 	m = p.search(s)
# 	if m:
# 		mm = m.group()
# 		s = s.replace(mm, mm.replace(',', ''))
# 	else:
# 		break





# import pygame
# import random
# from pygame.sprite import Sprite
#
# image=pygame.transform.scale(pygame.image.load('mygame/pic/monster.png'),(30,30))
# screen=pygame.display.set_mode((1200,750))
# sc_rect=screen.get_rect()
# im_rect=image.get_rect()
# im_rect.bottom=sc_rect.height/2
# im_rect.x=sc_rect.width/2
#
# # images=Sprite.groups()
# num_x = random.randint(0, 7)
# print(type(num_x))
#
# while True:
#     for event in pygame.event.get():
#         if event.type==pygame.QUIT:
#             sys.exit()
#         else:
#             i=1
#             while i<5:
#                 num_x = random.randint(0, 7)
#                 i+=1
#                 im_rect.x=6*im_rect.width*num_x
#                 screen.blit(image,im_rect)
#         pygame.display.flip()


#使用python的turtle画图形
# import  turtle
# turtle.pensize(4)
# turtle.pencolor('red')
#
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(20)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(450)
# turtle.forward(80)
#
# turtle.mainloop()

#占位符语法：
# a=45
# b=89
# print('%d+%d/%d' % (a,b,a)) #返回45+89/45，
# print('%d %% %d = %d' % (a, b, a % b))#在文本''中使用占位符，%d是整数的占位符，%f是小数的占位符，%%表示百分号（因为百分号代表了占位符，所以带占位符的字符串中要表示百分号必须写成%%，不带''的%是指示前后占位符映射对应值的关系,映射关系一一对应，有多少个占位符就在%后面使用()并用,分隔对应值配置位置
# conn.execute("INSERT INTO tmp1 VALUES ('%s','%s','%s')"%('huang','男','23'))#使用占位符进行insert的插入


# print([x for x in range(0,8)])#注意列表生成器在print中使用需要加入响应的容器符合，不然返回<generator object <genexpr>，也即一个迭代生成器对象代码，而不是想要的值
# print(*(x for x in range(0,8)))


#pass简析：一般在python中用作占位符，占住不需要执行什么操作但留空间的语句和函数中
# def print_name(name):
#     pass#如果不设置一个pass，而又没有具体的操作赋予函数的话将难以终结函数的，因此使用pass占位功能意义重大
#
# print_name('skfhf')


#yield简析:yield 的作用就是把一个函数变成一个 generator，带有 yield 的函数不再是一个普通函数，Python 解释器会将其视为一个 generator-它和普通函数不同，生成一个 generator 看起来像函数调用，但不会执行任何函数代码，直到对其调用 next()（在 for 循环中会自动调用 next()）才开始执行。虽然执行流程仍按函数的流程执行，但每执行到一个 yield 语句就会中断，并返回一个迭代值，下次执行时从 yield 的下一个语句继续执行。

# file='C:\\Users\\90773\\Desktop\\dfas.txt'
# def yield_practice(j):
#     with open(file,encoding='utf-8') as f:
#         k=0
#         try:
#             j = int(j)
#             while k<j:
#                 yield f.readline(j)
#                 k+=1
#         except:
#             return
#
# for i in yield_practice(12):
#     print(i)
#
# print(next(yield_practice(12)))



# #枚举函数，enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中,也可以用list转化读取
# se=['dfas','asfd','asfd']
# kj=enumerate(se)
# print(kj)
# print(list(kj))
# #返回：[(0, 'dfas'), (1, 'asfd'), (2, 'asfd')]


# yi=[45,456,89898,12,2]
# y=12
# k=yi.index(y)
# print(k)


# print(1/3-(1-2/3)<0.0000001)#浮点值的比较，计算机无法穷尽浮点值

import requests

headers={
	'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
	'cookie':'crumb=BXVgJ4sp2TdxNWNkNTg4M2YwNWE3MTI0ZDM4YjUxYTZiMzRkOTEz; _ga=GA1.2.1962831436.1641387472; _gid=GA1.2.2021381156.1641387472; ss_cvr=a1f01949-ea85-4984-b761-431195d324da|1641387472824|1641387472824|1641387472824|1; ss_cvt=1641387472824; affiliatly_v3=id_token=5f4b3f737e0d290bff0d5f8116bbf1cc&id_user=81576&aff_uid=2&duration=2592000&expire_time=1643979473',
	'Referer':'https://jablehk.com/'
}

# pic = requests.get('https://jablehk.com/hongkonggirls2/ginnyt?itemId=kjcjhuchco6jfjyrjycr6ct4ycslfc.jpg', headers=headers).content
# with open(r'C:\Users\90773\Desktop'+'23.jpg', 'wb') as pw:
# 	pw.write(pic)

#
# import json
# mv="""{"code":"200","msg":null,"result":{"trend_for_618":"1","loginType":"7","nickName":"skechers官方旗舰店","onestop":"0","mamaclub_myresource_w":"1","proxyType":"8","oldToken":"CST5r8","isAdMarketingUser":"1","mamaclub_myasset_w":"1","operId":"1104204309","outsideNumID":"783329018","token":"df038a1b","isMamaClubUser":"1","forbidFinance":"0","pin":"3","tbsellerType":"1","custId":"1104204309","operName":"skechers官方旗舰店:推广01","accountProxyType":"NONE","hash":"df038a1ba5d37da7","memberId":"29976126"},"hostName":"newbpfe033006244135.center.na620","analyseTraceId":null}"""
#
# jk=json.loads(mv)  #load 和 loads的区别
# print(jk["result"]["token"])

cookies='JSESSIONID=F52126C5CA67DEBC6D651FC6F43F395E,l=eBSlUrSVgdGcme6CBOfwourza77OSIRAguPzaNbMiOCPOyXJ5lPhW6L0h1tvC3GVhswBR3lFyc9uBeYBq7VonxvtK6Po_fkmn,cna=Ikt5GuQOVC4CAT2QMfoj3L/F,cancelledSubSites=empty,tfstk=cRmNB_1GHhKNs-EXylZ2lBrlecK1ZHMinMy7SV1J8yaA5JaGiVfYK5wTL-6FiPf..,csg=66c1c30f,unb=2210639251036,skt=cf1b90ef0e9567c4,cookie2=104b9104313c57a18a5f310eda491dd5,sgcookie=E100xiR8FqD3BQ9YnInY7A76eZgRmaQw33RWATpdMVmRKu3yhf%2F2y6d184TbQOwImfU8Q6cRaBW6cHc6MyL5ZUsIRMmpMo5oW1zjmIOJ0vEK440%3D,_tb_token_=ebeb6ee34fe5e,_samesite_flag_=true,t=9f080df220c95b6573bccea136b18362,__wpkreporterwid_=64ed1b9b-03f6-4731-abf9-bbdfd144007e,uc1=cookie14=UoewAwiXdhaqVA%3D%3D&cookie21=Vq8l%2BKCLiYYu,isg=BElJvW_JTAu1PjB-BkzdP8K-WHWjlj3I1DBnmOu-xTBvMmlEM-ZNmDfgcJaEatUA,_cc_=URm48syIZQ%3D%3D,sn=skechers%E5%AE%98%E6%96%B9%E6%97%97%E8%88%B0%E5%BA%97%3A%E6%8E%A8%E5%B9%BF01,xlly_s=1,'
# header_download = {'Sec-Fetch-Mode': 'navigate',
# 				   'Sec-Fetch-Dest': 'document',
# 				   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
# 				   'Accept-Encoding': 'gzip,deflate,br',
# 				   'Accept-Language': 'zh-CN,zh;q=0.9',
# 				   'Upgrade-Insecure-Requests': '1',
# 				   'Host': 'download-subway.simba.taobao.com',
# 				   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
# 				   'cookie': cookies
# 				   }
# url1='https://download-subway.simba.taobao.com/download.do?spm=a2e2i.23211836.ce272de26.d5325113b.7f3368f815YMsW&custId=1104204309&token=edbf3460&taskId=21446686'
# kh=requests.get(url1,headers=header_download)
# with open('key1.zip','wb') as fp:
# 	fp.write(kh.content)


# _header={
# 	'accept':'application/json, text/javascript, */*; q=0.01',
# 	'accept-encoding':'gzip, deflate, br',
# 	'accept-language':'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
# 	'origin':'https://subway.simba.taobao.com',
# 	'referer':'https://subway.simba.taobao.com/',
# 	'sec-fetch-mode':'cors',
# 	'sec-fetch-site':'same-origin',
# 	'cookie':cookies,
# 	'x-requested-with':'XMLHttpRequest',
# 	'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
# }
#
# header4 = {'Referer': 'https://subway.simba.taobao.com/',
# 		  'Accept-Encoding': 'gzip,deflate,br',
# 		  'Accept-Language': 'zh-CN,zh;q=0.9',
# 		  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
# 		  'Origin': 'https://subway.simba.taobao.com',
# 		  'Accept': 'application/json, text/javascript, */*; q=0.01',
# 		  'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
# 		  'X-Requested-With': 'XMLHttpRequest',
# 		  'Host': 'subway.simba.taobao.com',
# 		  'cookie': cookies,
# 		  }
# url1='https://subway.simba.taobao.com/bpenv/getLoginUserInfo.htm'
#
# kh=requests.post(url1,headers=header4)
# print(json.loads(kh.content.decode('utf-8'))['result']["token"])

# import re
# filename='456456'
# re_filename=re.compile(".*%s_(.*)" % (filename))
# fistr='456456_guanjiac'
# k=re.findall(re_filename,fistr)
# if k:
# 	print(1)


#
# import execjs
# import time
#
# current_time=1644822512057 #int(time.time()*1000)
# with open(r'D:\python_file\非自用工具箱\token_dymatic\dynamicToken.js',"r",encoding="utf-8") as file1:
# 	jk=file1.read()
# kj=execjs.compile(jk).call('get_token',current_time,'1644822441865029976126','3')
# print(kj)


from base64 import b64decode,b64encode, b16encode, b16decode
import json

# with open(r'.\user_data\request_data\2022-02-16_cookies.json','rb') as ce:  #记得用rb模式打开
# 	m=base64.b16encode(base64.b64encode(ce.read()))
# n=base64.b64decode(base64.b16decode(m))
# print('m:',m)
# print('n:',str(n,encoding='utf-8'))
#
# with open(r'.\user_data\request_data\2022-02-16_cookies.json','r') as ce:
# 	print(ce.read())
#
# with open('text.json','wb') as p:
# 	p.write(m)

# with open('text.json','rb') as b:
# 	kl=json.loads(str(base64.b64decode(base64.b16decode(b.read())), encoding='utf-8'))
# 	print(type(kl))

with open(r'.\user_data\account_data\account.json', 'rb') as accountjson:
	_retrieve =json.loads(b64decode(b16decode(accountjson.read())).decode('gbk'))#,encoding='utf-8'))

print(type(_retrieve))