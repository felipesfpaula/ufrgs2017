from train.feats import *
import cPickle as pickle
from sklearn.cross_validation import cross_val_score
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
import numpy as np 


training_dataset = pickle.load(open('ufrgs2017/data/training_dataset.pickle','rb'))
targets = [ (value.label).encode('utf8').decode('utf8') for key, value in training_dataset.iteritems()]

def corpus_reader():
	for key, value in training_dataset.iteritems():
		yield  (value.text).encode('utf8').decode('utf8')

unigrams_matrix, token2id = extract_unigram_for_training(corpus_reader())
bigrams_matrix, token2id = extract_bigram_for_training(corpus_reader())
char_trigrams_matrix, token2id = extract_char_trigram_for_training(corpus_reader())

classifier = RandomForestClassifier()
scores = cross_val_score(classifier, np.hstack((unigrams_matrix,bigrams_matrix,char_trigrams_matrix)), targets, cv=10)
print scores