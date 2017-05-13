from train.feats import *
import cPickle as pickle
from sklearn.cross_validation import cross_val_score
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
import numpy as np 
from syntatic.parsing import *
from data.read_to_pickle import *
from data.forum import *
# print extract_productions_and_triples("This is a very simple sentence. However, another sentence follows.") 

training_dataset = pickle.load(open('ufrgs2017/data/training_dataset.pickle','rb'))
targets = [ (value.label).encode('utf8').decode('utf8') for key, value in training_dataset.iteritems()]

def corpus_reader():
	for key, value in training_dataset.iteritems():
		# print  (value.original_text).encode('utf8').decode('utf8')
		# yield  [(value.message).encode('utf8').decode('utf8'),(value.original_text).encode('utf8').decode('utf8')]
		yield (value.message).encode('utf8').decode('utf8')


count = 0
cps = []
white = 0
for txt in corpus_reader():
	if re.sub('\s+','',txt) == '':
		continue
	cps.append(txt)

extract_syntatic_feats_for_training(cps)


# count = 0
# for txt in corpus_reader():
# 	print "original:"
# 	print txt[1].encode('utf8')
# 	print 'parsed:'
# 	print txt[0].encode('utf8')
# 	print " "
# extract_syntatic_feats_for_training(cps)

# unigrams_matrix, token2id = extract_unigram_for_training(corpus_reader())
# bigrams_matrix, token2id = extract_bigram_for_training(corpus_reader())
# char_trigrams_matrix, token2id = extract_char_trigram_for_training(corpus_reader())

# classifier = RandomForestClassifier()
# scores = cross_val_score(classifier, np.hstack((unigrams_matrix,bigrams_matrix,char_trigrams_matrix)), targets, cv=10)
# print scores