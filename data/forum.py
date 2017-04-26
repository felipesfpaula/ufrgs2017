import xmltodict
import cPickle as pickle
import sys,os
import re


class ForumPost(object):
	
	def __init__(self,xml_file_name):
		with open(xml_file_name,'r') as data:
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
			self.author =  message[u'author'][u'login'][u'#text']
			self.label = ''
			self.label_fg = ''

	def clean_message(self,message):
		text = ''
		tag = False

		for m in message:
			
			if m == '<':
				tag = True

			elif m == '>':
				tag = False
				text += ' '

			elif not tag:
				text += m
				

		return text