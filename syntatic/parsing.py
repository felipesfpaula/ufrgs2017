from nltk import Tree
from nltk.parse.stanford import StanfordDependencyParser
from nltk.parse.stanford import StanfordParser
from nltk.tag import StanfordPOSTagger
from nltk.internals import find_jars_within_path
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.tokenize import TweetTokenizer
import nltk.internals
import os
import re



tknzr = TweetTokenizer()
## you need java 8
current_dir = os.path.dirname(__file__)

nltk.internals.config_java(options='-mx20g')

path_to_stanford_parser =  os.path.join(current_dir,'stanford-parser','stanford-parser.jar')
path_to_stanford_parser_models = os.path.join(current_dir,'stanford-english-models.jar')
stanford_dep_parser = StanfordDependencyParser(path_to_jar=path_to_stanford_parser, path_to_models_jar=path_to_stanford_parser_models)
stanford_parser = StanfordParser(path_to_jar=path_to_stanford_parser, path_to_models_jar=path_to_stanford_parser_models)

stanford_tagger = StanfordPOSTagger(os.path.join(current_dir,'stanford-postagger','models','english-left3words-distsim.tagger'), os.path.join(current_dir,'stanford-postagger','stanford-postagger-3.7.0.jar'))


## Very very ugly please improve
def sentence_splitting(text_block):
	sentences = []
	for sent in sent_tokenize(text_block):
		if len(sent) > 120:
			# print sent, len(sent)
			comma_split = sent.split(',')
			if len(comma_split) > 1:
				# print 'comma'
				for subsent in comma_split:
					# print subsent , len(subsent)
					sentences.append(subsent)
		else:
			sentences.append(sent)


	sentences2 = sentences
	sentences = []
	for sent in sentences2:
		if len(sent) > 120:
			# print sent, len(sent)
			comma_split = sent.split('\n')
			if len(comma_split) > 1:
				# print 'breakline'
				for subsent in comma_split:
					# print subsent , len(subsent)
					sentences.append(subsent)
		else:
			sentences.append(sent)

	sentences2 = sentences
	sentences = []
	for sent in sentences2:
		if len(sent) > 120:
			comma_split = sent.split('and')
			if len(comma_split) > 1:
				# print 'breakline'
				for subsent in comma_split:
					# print subsent , len(subsent)
					sentences.append(subsent)
		else:
			sentences.append(sent)

	sentences2 = sentences
	sentences = []
	for sent in sentences2:
		if len(sent) > 3:
			sentences.append(sent)

	return sentences


def extract_productions_triples_taggedsent(text_block):

	if re.sub('\s+','',text_block) == '':
		return {'triples':[],'prods':[],'taggedsent':[]}

	sentences = [ tknzr.tokenize(sent) for sent in sentence_splitting(text_block)]
	# Process really big sentences
	tagged_sentences = stanford_tagger.tag_sents(sentences)

	tagged_sentences = [sent for sent in tagged_sentences if sent != []]
	prods = [parse.productions() for sent in tagged_sentences for parse in stanford_parser.tagged_parse(sent)]
	prods = [[str(prod) for prod in prodset if prod.is_nonlexical() ] for prodset in prods ]

	prods = [subprod for prod in prods for subprod in prod]
	triples = [ [tree.triples() for tree in t] for t in stanford_dep_parser.tagged_parse_sents(tagged_sentences)]
	triples = [ [triple for triple in tripleset] for tripleset in triples ]

	triples = [subtriple for trip in triples for subtriple in trip]
	triples = [subtriple for trip in triples for subtriple in trip]
	triples = [ str((i[0][1], i[1], i[2][1])) for i in triples ]

	return {'triples':triples,'prods':prods,'taggedsent':tagged_sentences}
