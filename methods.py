import requests
from time import sleep
CONST_URL = "https://api.telegram.org/bot708914610:AAFtLSerk5aw-72yKKvljZbrrRSmd4yHV8I/"

class methods:
	def __init__(self):

		pass

	def get_updates_json(self, request):
		params = {'timeout': 100, 'offset': None}
		response = requests.get(request + 'getUpdates', data=params)
		return response.json()

	def get_chat_id(self,update):
		chat_id = update['message']['chat']['id']
		return chat_id

	def last_update(self,data):
		results = data['result']
		total_updates = len(results) - 1
		return results[total_updates]

	def get_chat_text(self,update):
		chat_text = update['message']['text']
		return chat_text

	def send_mess(self,chat, text):
		params = {'chat_id': chat, 'text': text}
		response = requests.post(CONST_URL + 'sendMessage', data=params)
		return response
	def send_mess_all(self,id_list, text):
		for id in id_list:
			params = {'chat_id': id, 'text': text}
			response = requests.post(CONST_URL + 'sendMessage', data=params)
	def show_messages_from_users(self, data):
		users_id = []
		users_name = []
		users_message = []
		for i in data['result']:
			if not(i['message']['from']['id'] in users_id):
				users_id.append(i['message']['from']['id'])
				full_name = i['message']['from']['first_name']
				if 'last_name' in i['message']['from']:
					full_name += ' ' + i['message']['from']['last_name']
				users_name.append(full_name)
				if 'sticker' in i['message']:
					users_message.append([ i['message']['sticker']['set_name'] ])
				elif'text' in i['message']:
					users_message.append([ i['message']['text'] ])
				else:
					users_message.append([ "UNKNOWN MEDIA" ])
			else:
				text = 'UNKNOWN MEDIA'
				if 'sticker' in i['message']:
					text = i['message']['sticker']['set_name']
				elif 'text' in i['message']:
					text = i['message']['text']
				users_message[users_id.index(i['message']['from']['id'])].append(text)
		return users_id, users_message, users_name

	def find_text(message):
		paths = open('file_path', 'r')
		for file in paths:
			tmp_file = open(file[:-1], 'r')
			for item in tmp_file:
				if not(item.find(message) == -1):
					return item
			tmp_file.close()
		return "404_error"
	def all_users(self):
		users_id, users_message, users_name = self.show_messages_from_users(self.get_updates_json(CONST_URL))
		return len(users_id)
	#import difflib
	#print(difflib.SequenceMatcher(None, 'hello world', 'hello').ratio() )
	users_id, users_message, users_name = show_messages_from_users(get_updates_json(CONST_URL))
	#print(get_chat_text(last_update(get_updates_json(CONST_URL))))

	#update_id = last_update(get_updates_json(CONST_URL))['update_id']
	#f = open('all_users', 'w')
	#while True:
	#    if update_id == last_update(get_updates_json(CONST_URL))['update_id']:
	#    	print (get_chat_text(last_update(get_updates_json(CONST_URL))))
	#    	#if not( str(get_chat_id(last_update(get_updates_json(CONST_URL)))) in all_users):
	#    	#print ( (str(get_chat_id(last_update(get_updates_json(CONST_URL))))))
	#    	message = get_chat_text(last_update(get_updates_json(CONST_URL)))
	#    	send_mess(get_chat_id(last_update(get_updates_json(CONST_URL))), find_text(message))
	#    	update_id += 1
	#    sleep(1)
	#f.close()
	#print('message sent to {} users'.format(len(users_id)))
	for name in users_name:
		print(name)
	#for i in range(len(users_id)):
	#		print('user: {} \nid: {} \nmessages:{}'.format(users_name[i], users_id[i], users_message[i]))
	#print (get_chat_text(last_update(get_updates_json(CONST_URL))))
	print('finished')