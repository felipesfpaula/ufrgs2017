from train.feats import *
import cPickle as pickle
from sklearn.cross_validation import cross_val_score
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
import numpy as np 
from syntatic.parsing import *
from data.read_to_pickle import *
from data.forum import *
from sklearn.preprocessing import normalize
from sklearn.feature_extraction.text import CountVectorizer,TfidfTransformer
from scipy.sparse import csc_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score

from sklearn.linear_model import LogisticRegression


training_dataset = pickle.load(open('ufrgs2017/data/training_dataset.pickle','rb'))
testing_dataset = pickle.load(open('ufrgs2017/data/testing_dataset.pickle','rb'))

targets = [ (value.label).encode('utf8').decode('utf8') for key, value in training_dataset.iteritems()]
targets_test = [ (value.label).encode('utf8').decode('utf8') for key, value in testing_dataset.iteritems()]


def corpus_reader(dataset):
	for key, value in dataset.iteritems():
		yield (value.message).encode('utf8').decode('utf8')


def evaluation(training_mat, testing_mat, targets, targets_test, model):

	## cross validation
	scores = cross_val_score(model, training_mat, targets, cv=5)
	print "accuracy 5-fold-cv mean: ", np.mean(scores)
	print scores

	scores = cross_val_score(model, training_mat, targets, cv=5,scoring='f1_macro')
	print "f1-macro 5-fold-cv mean: ", np.mean(scores)
	print scores

	lg.fit(training_mat, targets)
	predictions =  lg.predict(testing_mat)

	print "Test set: "
	print classification_report(targets_test, predictions)

	print "accuracy: ",accuracy_score(targets_test, predictions)




unigrams_matrix, token_unigram_2id = extract_unigram_for_training(corpus_reader(training_dataset))
bigrams_matrix, token_bigram_2id = extract_bigram_for_training(corpus_reader(training_dataset))
char_trigrams_matrix, token_chartrigram_2id = extract_char_trigram_for_training(corpus_reader(training_dataset))

tst_unigrams = extract_unigram(corpus_reader(testing_dataset),token_unigram_2id)
tst_bigrams = extract_bigram(corpus_reader(testing_dataset),token_bigram_2id)
tst_char_trigrams = extract_char_trigram(corpus_reader(testing_dataset),token_chartrigram_2id)

def idf(td_mat):
	td_mat[td_mat > 0] = 1
	doc_freq = np.sum(td_mat,axis=0)
	ans = np.log( (1 + td_mat.shape[0])/(1 + doc_freq)) + 1
	return ans.reshape((ans.shape[0],1))

def tfidf(td_mat):
	ans = td_mat * idf(td_mat).T
	return ans

print "--- UNIGRAMS --- "
lg = LogisticRegression(multi_class='multinomial',solver='newton-cg',max_iter=500)
evaluation(csc_matrix(tfidf(unigrams_matrix)),csc_matrix(tfidf(tst_unigrams)),targets,targets_test, lg )

print "--- + bigrams ---"
lg = LogisticRegression(multi_class='multinomial',solver='newton-cg',max_iter=500)
evaluation(csc_matrix( np.hstack(( tfidf(unigrams_matrix), tfidf(bigrams_matrix) ))) ,csc_matrix( np.hstack((  tfidf(tst_unigrams),tfidf(tst_bigrams)  ))),targets,targets_test, lg )

print "--- + char_trigrams ---"

lg = LogisticRegression(multi_class='multinomial',solver='newton-cg',max_iter=500)
evaluation(csc_matrix( np.hstack(( tfidf(unigrams_matrix), tfidf(bigrams_matrix), tfidf(char_trigrams_matrix) )) ),csc_matrix( np.hstack((  tfidf(tst_unigrams),tfidf(tst_bigrams),tfidf(tst_char_trigrams)  ))),targets,targets_test, lg )

filtered_targets = map(lambda x: u'not_green' if x != u'green' else  u'green', targets)
filtered_targets_tst= map(lambda x: u'not_green' if x != u'green' else  u'green', targets_test)

print "\n --- FILTERED --- \n "

print "--- UNIGRAMS --- "
lg = LogisticRegression(solver='newton-cg',max_iter=500)
evaluation(csc_matrix( tfidf(unigrams_matrix)),csc_matrix(tfidf(tst_unigrams)),filtered_targets,filtered_targets_tst, lg )

print "--- + bigrams ---"
lg = LogisticRegression(solver='newton-cg',max_iter=500)
evaluation(csc_matrix( np.hstack(( tfidf(unigrams_matrix), tfidf(bigrams_matrix) ))),csc_matrix( np.hstack((  tfidf(tst_unigrams),tfidf(tst_bigrams)  ))),filtered_targets,filtered_targets_tst, lg )

print "--- + char_trigrams ---"

lg = LogisticRegression(solver='newton-cg',max_iter=500)
evaluation(csc_matrix( np.hstack(( tfidf(unigrams_matrix), tfidf(bigrams_matrix), tfidf(char_trigrams_matrix) ))) ,csc_matrix( np.hstack((  tfidf(tst_unigrams),tfidf(tst_bigrams),tfidf(tst_char_trigrams)  ))),filtered_targets,filtered_targets_tst, lg )


# lg = LogisticRegression(multi_class='multinomial',solver='newton-cg',max_iter=500)

# filtered_targets = map(lambda x: u'not_green' if x != u'green' else  u'green', targets)
# filtered_targets_tst= map(lambda x: u'not_green' if x != u'green' else  u'green', targets_test)

# evaluation(csc_matrix(tfidf(unigrams_matrix)),csc_matrix(tfidf(tst_unigrams)),filtered_targets,filtered_targets_tst, lg )



# lg.fit(csc_matrix(tfidf(unigrams_matrix)), targets)
# predictions =  lg.predict(csc_matrix(tfidf(tst_unigrams)))

# print classification_report(targets_test, predictions)

# # lg = LogisticRegression(multi_class='multinomial',solver='newton-cg',max_iter=500)

# # lg.fit(csc_matrix(tfidf(bigrams_matrix)), targets)
# # predictions =  lg.predict(csc_matrix(tfidf(tst_bigrams)))
# # print "bigrams"
# # print classification_report(targets_test, predictions)


# lg = LogisticRegression(multi_class='multinomial',solver='newton-cg',max_iter=500)

# lg.fit(csc_matrix(tfidf(char_trigrams_matrix)), targets)
# predictions =  lg.predict(csc_matrix(tfidf(tst_char_trigrams)))
# print "char trigrams"
# print classification_report(targets_test, predictions)


# lg = LogisticRegression(multi_class='multinomial',solver='newton-cg',max_iter=500)

# lg.fit( csc_matrix(np.hstack(( tfidf(char_trigrams_matrix),tfidf(unigrams_matrix) ))), targets)
# predictions =  lg.predict(csc_matrix( np.hstack(( tfidf(tst_char_trigrams), tfidf(tst_unigrams) )) ))
# print "char trigrams"
# print classification_report(targets_test, predictions)







