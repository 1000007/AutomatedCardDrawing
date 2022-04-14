from send_message.word_detect import *
from random import choice
from data.talk_data.base_talk import others_answer

def match(msg,talk_data):
	for row in talk_data:
		if row[0] in msg:
			return [True,row[1][0]]
	return [False,choice(others_answer["no_answer"])]

def talk_to_user(rev,talk_data,ws):
	msg=rev["raw_message"]
	sender = rev['user_id']
	group_id = ""
	if_help = help_menu(msg)
	if if_help[0] == True:
		return if_help[1]
	if_del = del_data(msg,talk_data)
	if if_del[0] == True:
		return if_del[1]
	if_add = add_data(msg,talk_data)
	if if_add[0] == True:
		return if_add[1]
	return match(msg,talk_data)[1]

def talk_to_group_user(rev,talk_data, ws):
	msg=rev["raw_message"]
	sender = rev['user_id']
	group_id = rev["group_id"]
	if_help = help_menu(msg)
	if if_help[0] == True:
		return if_help[1]
	print(msg)









	if_rollcard111 = rollcard111(msg)
	if if_rollcard111 == True:
		return if_rollcard111[1]

	if_setu = mao_pic(msg)
	if if_setu[0] == True:
		return if_setu[1]
	return match(msg,talk_data)[1]

def add_friends(rev, ws):
	print(rev)
	sender = rev['user_id']
	msg = rev['comment'].split('回答:')[1]
	if_add = add_friend(sender, msg, ws)
	obj = {
		'isOK': if_add[0],
		'flag': rev['flag'],
		'friendsName': if_add[1]
	}
	return obj

def talk_to_gourp(rev,talk_data, ws):
	msg=rev["raw_message"]
	user_id=rev["user_id"]
	group_id=rev["group_id"]
	if_ban = detect_ban(msg,user_id,group_id, ws)
	if if_ban[0] == True:
		return if_ban[1]
	if match(msg,talk_data)[0]==True:
		return match(msg,talk_data)[1]
	return ""

