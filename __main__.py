from train.feats import *
import cPickle as pickle
from sklearn.cross_validation import cross_val_score
from sklearn.naive_bayes import MultinomialNB

training_dataset = pickle.load(open('ufrgs2017/data/training_dataset.pickle','rb'))
targets = [ (value.label).encode('utf8').decode('utf8') for key, value in training_dataset.iteritems()]

def corpus_reader():
	for key, value in training_dataset.iteritems():
		yield  (value.text).encode('utf8').decode('utf8')

unigrams_matrix, token2id = extract_unigram_for_training(corpus_reader())

classifier = MultinomialNB()
scores = cross_val_score(classifier, unigrams_matrix, targets, cv=10)
print scores