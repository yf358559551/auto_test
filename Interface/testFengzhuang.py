# -*- coding: utf-8 -*-
# @File    : testFengzhuang.py
import json
from Public.test_requests import requ
reques=requ()
class TestApi(object):
	def __init__(self,url,token,connent,fangshi):
		self.url=url
		self.token=token
		self.connent=connent
		self.fangshi=fangshi
	def testapi(self):
		if self.fangshi=='POST':
			self.parem = json.loads(self.connent)
			self.response=reques.post(self.url,self.token,self.parem)
		elif self.fangshi=="GET":
			self.parem = {'key': self.key, 'info': self.connent}
			self.response = reques.get(url=self.url,params=self.parem)
		return self.response
	def getJson(self):
		json_data = self.testapi()
		return json_data