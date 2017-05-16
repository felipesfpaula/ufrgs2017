# from train.feats import *
# import cPickle as pickle
# from sklearn.cross_validation import cross_val_score
# from sklearn.naive_bayes import MultinomialNB
# from sklearn.ensemble import RandomForestClassifier
# from sklearn import svm
# import numpy as np 
# from syntatic.parsing import *
# from data.read_to_pickle import *
# from data.forum import *
# from train.feats import *

import model_eval.eval_batch

# print extract_productions_and_triples("This is a very simple sentence. However, another sentence follows.") 

# training_dataset = pickle.load(open('ufrgs2017/data/training_dataset.pickle','rb'))
# testing_dataset = pickle.load(open('ufrgs2017/data/testing_dataset.pickle','rb'))

# targets = [ (value.label).encode('utf8').decode('utf8') for key, value in training_dataset.iteritems()]
# targets_test = [ (value.label).encode('utf8').decode('utf8') for key, value in testing_dataset.iteritems()]

# def corpus_reader():
# 	for key, value in training_dataset.iteritems():
# 		yield (value.message).encode('utf8').decode('utf8')

# def corpus_test_reader():
# 	for key, value in testing_dataset.iteritems():
# 		yield (value.message).encode('utf8').decode('utf8')

# count = 0
# cps = []
# white = 0
# for txt in corpus_reader():
# 	cps.append(txt)

# p_cps = parse_corpus_for_training([])
# pickle.dump(p_cps, open('parsed_corpus.pickle', 'wb'))

# f1,f2 = extract_syntatic_feats_for_training(p_cps)

# unigrams_matrix, token_unigram_2id = extract_unigram_for_training(corpus_reader())
# # bigrams_matrix, token2id = extract_bigram_for_training(corpus_reader())
# # char_trigrams_matrix, token2id = extract_char_trigram_for_training(corpus_reader())

# tst_unigrams = extract_unigram(corpus_test_reader(),token_unigram_2id)



# def idf(td_mat):
# 	td_mat[td_mat > 0] = 1
# 	doc_freq = np.sum(td_mat,axis=0)
# 	ans = np.log( (1 + td_mat.shape[0])/(1 + doc_freq)) + 1
# 	return ans.reshape((ans.shape[0],1))

# def tfidf(td_mat):
# 	ans = td_mat * idf(td_mat).T
# 	return ans

# clf = svm.SVC(probability=True)
# lg = LogisticRegression(multi_class='multinomial',solver='newton-cg',max_iter=500)
# # clf.fit(csc_matrix(unigrams_matrix), targets)
# # predictions =  clf.predict(csc_matrix(tst_unigrams))
# # print clf.predict_proba(csc_matrix(tst_unigrams))
# # # accuracy_score(y_true, y_pred)
# lg.fit(csc_matrix(tfidf(unigrams_matrix)), targets)
# predictions =  lg.predict(csc_matrix(tfidf(tst_unigrams)))
# print classification_report(targets_test, predictions)

# lg = LogisticRegression(multi_class='multinomial',solver='newton-cg',max_iter=500)
# scores = cross_val_score(lg, csc_matrix(tfidf(unigrams_matrix)),targets, cv=5,scoring='f1_macro')
# print scores


# vectorizer = CountVectorizer(min_df=1)
# X = vectorizer.fit_transform(corpus_reader())
# transformer = TfidfTransformer(smooth_idf=False)
# tfidf_uni = transformer.fit_transform(unigrams_matrix)
# transformer = TfidfTransformer()
# vectorizer = CountVectorizer(min_df=1)
# sklearn.feature_extraction.text.TfidfVectorizer()

# tfidf_uni = tfidf(unigrams_matrix)
# # tfidf_bigrams = bigrams_matrix * idf(bigrams_matrix).T

# tfidf_uni = normalize(tfidf_uni, axis=1, norm='l1')
# # tfidf_bigrams = normalize(tfidf_bigrams, axis=1, norm='l1')

# unigrams_matrix = normalize(unigrams_matrix, axis=1, norm='l1')
# # bigrams_matrix = normalize(bigrams_matrix, axis=1, norm='l1')

# clf = svm.SVC()
# scores = cross_val_score(clf, X,targets, cv=10)
# print scores

# clf = svm.SVC()
# scores = cross_val_score(clf, csc_matrix(unigrams_matrix),targets, cv=10)
# print scores

# clf = svm.SVC()
# scores = cross_val_score(clf, csc_matrix(bigrams_matrix),targets, cv=10)
# print scores

# clf = svm.SVC()
# classifier = RandomForestClassifier()
# scores = cross_val_score(classifier, csc_matrix( np.hstack((char_trigrams_matrix,bigrams_matrix, unigrams_matrix))  ),targets, cv=10,scoring='f1_macro')
# print scores

# clf1 = svm.SVC()
# clf2 = svm.SVC()
# clf3 = svm.SVC()

# eclf1 = VotingClassifier(estimators=[('clf1',clf1),('clf2',clf2),('clf3',clf3)],voting='hard')



# clf = svm.SVC()
# scores = cross_val_score(clf, unigrams_matrix,targets, cv=10,scoring='f1_macro')
# print scores


# classifier = RandomForestClassifier()
# scores = cross_val_score(classifier, np.hstack((unigrams_matrix,bigrams_matrix)), targets, cv=10)
# print scores

# classifier = RandomForestClassifier()
# scores = cross_val_score(classifier, np.hstack((tfidf_uni,tfidf_bigrams )),targets, cv=10)
# print scores


# clf = svm.SVC()
# scores = cross_val_score(clf, np.hstack((tfidf_uni,tfidf_bigrams )),targets, cv=10)
# print scores

# scores = cross_val_score(clf, np.hstack((unigrams_matrix,bigrams_matrix)), targets, cv=10)
# print scores


# bigrams_matrix, token2id = extract_bigram_for_training(corpus_reader())
# char_trigrams_matrix, token2id = extract_char_trigram_for_training(corpus_reader())

# classifier = RandomForestClassifier()
# scores = cross_val_score(classifier, np.hstack((unigrams_matrix,bigrams_matrix,char_trigrams_matrix)), targets, cv=10)
# print scores
# classifier = RandomForestClassifier()
# scores = cross_val_score(classifier, np.hstack((f1,f2)), targets, cv=2)
# print scores

