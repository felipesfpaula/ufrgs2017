import html

class MessageParser:

	def __init__(self,message):
		self.message = html.unescape(message)
		self.message_text = self.clean_message() 

	def extract_emoticons(self):
		_emoticons_ = []
		emoticons_list = self.message.split('<img class="emoticon')[1:]
		for e in emoticons_list:
			_emoticons_.append(e.split('emoticon-')[1].split('"')[0])
		return _emoticons_

	def extract_tags(self):
		return {'N':self.message.count('<STRONG>Neg</STRONG>')+self.message.count('<STRONG>Negative</STRONG>'),
				'P':self.message.count('<STRONG>Pos</STRONG>')+self.message.count('<STRONG>Positive</STRONG>')}

	def clean_message(self):
		raw = ''
		tag = False

		for m in self.message:
			
			if m == '<':
				tag = True

			elif m == '>':
				tag = False
				raw += ' '

			elif not tag:
				raw += m


		return raw

	def __len__(self):
		return len(self.message_text)



# features
# -BR
# &nbsp; == space
# emoticon-smileyhappy
# />Pos:
# emoticon-smileytongue
# emoticon-smileyvery-happy
# emoticon-smileysad
# />Negative:
# <STRONG>Neg</STRONG>
# <STRONG>Pos</STRONG>:
# <STRONG>Positive</STRONG>

if "__main__":
	message = """asdf ece<img class="emoticon emoticon-smileyvery-happy" id="smileyvery-happy" sr<img class="emoticon emoticon-smileyvery-happy" id="smileyver
	  <img class="emoticon emoticon-smileyvery-happy" id="smileyver  <img class="emoticon emoticon-smileyvery-happy" id="smileyverasdf>asdf"""

	m = MessageParser(message)
	print len(m)