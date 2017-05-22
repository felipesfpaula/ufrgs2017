#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding=utf8


from data.read_to_pickle import *
# from data.forum import *
# from sklearn.linear_model import LogisticRegression
# import numpy as np 
# from train.feats import *

# out_dataset = pickle.load(open('ufrgs2017/data/out_dataset.pickle', 'rb'))
# training_dataset = pickle.load(open('ufrgs2017/data/training_dataset.pickle','rb'))
# testing_dataset = pickle.load(open('ufrgs2017/data/testing_dataset.pickle','rb'))

# def corpus_reader(dataset):
# 	for key, value in dataset.iteritems():
# 		yield (value.message).encode('utf8').decode('utf8')

# def idf(td_mat):
# 	td_mat[td_mat > 0] = 1
# 	doc_freq = np.sum(td_mat,axis=0)
# 	ans = np.log( (1 + td_mat.shape[0])/(1 + doc_freq)) + 1
# 	return ans.reshape((ans.shape[0],1))

# def tfidf(td_mat):
# 	ans = td_mat * idf(td_mat).T
# 	return ans


# targets = [ (value.label).encode('utf8').decode('utf8') for key, value in training_dataset.iteritems()]

# unigrams_matrix, token_unigram_2id = extract_unigram_for_training(corpus_reader(training_dataset))


# lg = LogisticRegression(multi_class='multinomial',solver='newton-cg',max_iter=500)

# lg.fit(unigrams_matrix, targets)

# amber = []
# crisis = []
# green = []
# red = []

# for key, value in out_dataset.iteritems():
# 	plain_text = (value.message).encode('utf8').decode('utf8')
# 	post_number = key
# 	tst = extract_unigram([plain_text],token_unigram_2id)
# 	pred_proba = lg.predict_proba(tst)
# 	pred = lg.predict(tst)[0]
# 	if pred == u'amber':
# 		amber.append({'number' : post_number, 'text':plain_text, 'prob': pred_proba})
# 	elif pred == u'crisis' :
# 		crisis.append({'number' : post_number, 'text':plain_text, 'prob': pred_proba})
# 	elif pred == u'green' :
# 		green.append({'number' : post_number, 'text':plain_text, 'prob': pred_proba})
# 	else:
# 		red.append({'number' : post_number, 'text':plain_text, 'prob': pred_proba})		

# def posts_writer(name,list):
# 	with open(name,'w') as out:
# 		for item in list:
# 			#str(item['number']) + u" " + str(item['prob']) + 
# 			out.write( '\n' + str(item['number']) + " \n" + str(item['prob']) + " " + item['text'].encode('utf8') + '\n' )

# posts_writer('crisis.txt',crisis)
# posts_writer('amber.txt',amber)
# posts_writer('red.txt',red)
# posts_writer('green.txt',green)

