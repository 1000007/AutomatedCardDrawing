import json
from data.load_data import read_file
from send_message.send_message import send_message
from send_message.talk_to_user import *
from random import randint
import random
self_qq = json.load(open("./config.json", encoding='utf-8'))["self_qq"]
ban_words = json.load(open("./config.json", encoding='utf-8'))["ban_words"]
class msg_talker():
	def __init__(self):
		self.talk_data = read_file()

	def private_msg(self,rev, ws):
		if rev["sub_type"] != "friend":
			return send_message('你还不是我的好友',rev['user_id'], ws,"private")
		return send_message(talk_to_user(rev, self.talk_data, ws), rev["user_id"], ws, "private")

	def group_msg(self,rev, ws):
		print(rev["raw_message"])
		if "单抽出奇迹" in rev["raw_message"] :
			flag1='responding:1 draw'
			print(flag1)
			rolldice1 = randint(1,1000)
			print(rolldice1)

			if rolldice1 in range(0,700):
				with open("allbox.txt", encoding='utf-8') as f:
					lines = f.readlines()
					output11 = random.choice(lines)
					return send_message(output11, rev['group_id'], ws, "group")
			if rolldice1 in range(700,710):
				with open("rarebox.txt", encoding='utf-8') as f:
					lines = f.readlines()
					output11 = random.choice(lines)
					return send_message(output11, rev['group_id'], ws, "group")
			if rolldice1 in range(710,713):
				with open("limitedbox.txt", encoding='utf-8') as f:
					lines = f.readlines()
					output11 = random.choice(lines)
					return send_message(output11, rev['group_id'], ws, "group")
			elif rolldice1 in range(713,1001):
				with open("materialbox.txt", encoding='utf-8') as f:
					lines = f.readlines()
					output11 = random.choice(lines)
					return send_message(output11, rev['group_id'], ws, "group")


		if "鸭来" in rev["raw_message"] :
			flag1='responding:5 draws'
			print(flag1)

			draws5 = ''
			with open("rarebox.txt", encoding='utf-8') as f:
				lines = f.readlines()
				output11 = random.choice(lines)
				draws5 = draws5 + output11
			for i in range(4):
				rolldice1 = randint(1, 1000)

				if rolldice1 in range(0, 700):
					with open("allbox.txt", encoding='utf-8') as f:
						lines = f.readlines()
						output11 = random.choice(lines)
						draws5 = draws5 + output11
				if rolldice1 in range(700, 710):
					with open("rarebox.txt", encoding='utf-8') as f:
						lines = f.readlines()
						output11 = random.choice(lines)
						draws5 = draws5 + output11
				if rolldice1 in range(710, 713):
					with open("limitedbox.txt", encoding='utf-8') as f:
						lines = f.readlines()
						output11 = random.choice(lines)
						draws5 = draws5 + output11
				elif rolldice1 in range(713, 1001):
					with open("materialbox.txt", encoding='utf-8') as f:
						lines = f.readlines()
						output11 = random.choice(lines)
						draws5 = draws5 + output11
			return send_message(draws5, rev['group_id'], ws, "group")

		if "拼鸭鸭" in rev["raw_message"] :
			flag1='responding:10 draws'
			print(flag1)
			draws10 = ''
			with open("rarebox.txt", encoding='utf-8') as f:
				lines = f.readlines()
				output11 = random.choice(lines)
				draws10 = draws10 + output11
			with open("limitedbox.txt", encoding='utf-8') as f:
				lines = f.readlines()
				output11 = random.choice(lines)
				draws10 = draws10 + output11

			for i in range(8):
				rolldice1 = randint(1, 1000)
				if rolldice1 in range(0, 700):
					with open("allbox.txt", encoding='utf-8') as f:
						lines = f.readlines()
						output11 = random.choice(lines)
						draws10 = draws10 + output11
				if rolldice1 in range(700, 710):
					with open("rarebox.txt", encoding='utf-8') as f:
						lines = f.readlines()
						output11 = random.choice(lines)
						draws10 = draws10 + output11
				if rolldice1 in range(710, 713):
					with open("limitedbox.txt", encoding='utf-8') as f:
						lines = f.readlines()
						output11 = random.choice(lines)
						draws10 = draws10 + output11
				elif rolldice1 in range(713, 1000):
					with open("materialbox.txt", encoding='utf-8') as f:
						lines = f.readlines()
						output11 = random.choice(lines)
						draws10 = draws10 + output11
			return send_message(draws10, rev['group_id'], ws, "group")






























		if "[CQ:at,qq={}]".format(self_qq) in rev["raw_message"]:
			try:
				# print(rev)
				rev['raw_message']=rev['raw_message'].split("] ")[1]
			except Exception as e:
				print(e)
				pass
			return send_message(talk_to_group_user(rev, self.talk_data, ws), rev["group_id"], ws, "group")

		if randint(1,10)<4 or rev['raw_message'] in ban_words:	
			return send_message(talk_to_gourp(rev, self.talk_data, ws), rev["group_id"], ws, "group")

		return True
	def addFriends(self,rev, ws):
		return send_message(add_friends(rev, ws), rev["user_id"], ws, "friends")