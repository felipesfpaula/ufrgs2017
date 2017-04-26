#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pickle
import csv

testing = open('testing_dataset.pickle', 'rb')
training = open('training_dataset.pickle', 'rb')


test  = pickle.load(testing)
train = pickle.load(training)


def toCSV(file_name,data_pickle):

	with open('%s.csv' % file_name,'w') as testingcsv:
		fields = ['ID','author','board_id','label','label_fg','message_type','post_type','text']
		writer = csv.DictWriter(testingcsv,fieldnames=fields)

		writer.writeheader()
		for ID, forum in data_pickle.iteritems():
			writer.writerow({'ID':ID,'author':forum.author,
									 'board_id':forum.board_id,
									 'label':forum.label,
									 'label_fg':forum.label_fg,
									 'message_type':forum.message_type,
									 'post_type':forum.post_type,
									 'text':forum.text.encode('utf-8')})

toCSV('testing_dataset.csv',test)
toCSV('training_dataset.csv',train)
testing.close()
training.close()