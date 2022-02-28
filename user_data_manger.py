"""this file is served management of user_data"""

from base64 import b64decode,b64encode, b16encode, b16decode
import os
import json
import time


class User_account():
	def __init__(self):
		if not os.path.exists(r'.\user_data\account_data'):
			os.makedirs(r'.\user_data\account_data')
		self.user_dict = {'username': '', 'password': ''}

	def user_save(self):
		acc=json.dumps(self.user_dict,ensure_ascii=False).encode('gbk')
		with open(r'.\user_data\account_data\account.json', 'wb') as accountjson:
			accountjson.write(b16encode(b64encode(acc)))

	def user_retrieve(self):
		try:
			with open(r'.\user_data\account_data\account.json', 'rb') as accountjson:
				_retrieve = b64decode(b16decode(accountjson.read())).decode('gbk')
			self.user_dict = json.loads(_retrieve)
		except Exception:
			pass
		return self.user_dict


class Timejudge():
	def __init__(self):
		pass


	def request_j(self):
		path = r'.\user_data\request_data'
		self.request_l = self.judge(path, 'cookies', 9000)
		return self.request_l

	def report_j(self):
		path = r'.\user_data\report_data'
		self.report_l = self.judge(path, 'report', 300)
		return self.report_l

	def judge(self, path, filename, timediff):
		if not os.path.exists(path):
			os.makedirs(path)
		file = os.path.join(path, r'%s_%s.json' % (time.strftime('%Y-%m-%d'), filename))
		l = ''
		try:
			mtime = int(os.stat(file).st_mtime)  # 时序判断
			fdiff = abs(mtime - int(time.time()))
			if fdiff <= timediff:
				with open(file, 'r') as jsonfile:
					for line in jsonfile.readlines():
						line = line.strip()
						l = json.loads(line)
		except Exception:
			pass
		return l
