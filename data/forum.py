import xmltodict
import cPickle as pickle
import sys,os
import re


class ForumPost(object):
	
	def __init__(self,xml_file_name,post_number=None):
		with open(xml_file_name,'r') as data:
			self.post_number = post_number
			parsed_data = xmltodict.parse(data.read())
			self.post_type = parsed_data.keys()[0]
			self.message_type = parsed_data[self.post_type][u'message'][u'@type']
			message = parsed_data[self.post_type][u'message']
			self.board_id = message[u'board_id'][u'#text']
			try:
				self.original_text = message[u'body'][u'#text']
				self.message = self.clean_message(self.original_text)
			except Exception, e:
				self.original_text = ""
				self.message = ""
			self.author =  message[u'author'][u'login'][u'#text']
			self.label = ''
			self.label_fg = ''

	def clean_message(self,message):
		text = ''
		index = 0

		if '<' not in message:
			return messsage
		count = 0

		while index < len(message):
			inicio = index
			opening = message[inicio:].find('<')
			if opening == -1:
				text += message[inicio+1:-1]
				break
			else:
				if inicio == 0:
					text += message[inicio:opening+inicio]
				else:
					text += message[inicio+1:opening+inicio]
				index+= opening

			closing = message[index:].find('>')
			if 'emoticon-' in message[opening:closing+index]:
				#given <img class="emoticon emoticon-smileyhappy" id...>
				#extract smileyhappy
				emoticon = message[opening:closing+index].split('emoticon-')[1].split('"')[0]
				text += ' #%s' % emoticon
				text += ' '			
			index += closing
		text = text.replace("&nbsp;", " ")
		text = text.replace("&lt;", "")
		text = text.replace("&gt;", "")
		text = text.replace("(", "")
		text = text.replace(")", "")
		text = text.replace("_", "")
		text = text.replace(".", " . ")

		return text