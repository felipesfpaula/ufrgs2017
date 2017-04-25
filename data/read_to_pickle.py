import xmltodict
import cPickle as pickle
import sys,os
import re
from forum import ForumPost


def forum_reader(folder_path):
	labels =  { tup.split("\t")[0] : tup.split("\t")[1:3] for tup in open(os.path.join(folder_path,'labels.tsv'),'r').readlines() }
	posts_path = os.path.join(folder_path,'posts')
	the_file_names = [ file for r,d,f in os.walk(posts_path) for file in f]
	dataset = {}
	for f in the_file_names:
		post_number = re.sub('\D', '', f)
		try:
			label = labels[post_number][0]
			label_fg = labels[post_number][1]
			dataset[post_number] = ForumPost(os.path.join(posts_path,f))
			dataset[post_number].label = label
			dataset[post_number].label_fg = ''.join(list(label_fg)[:-1])
		except Exception, e:
			pass
	return dataset

training_dataset = forum_reader(os.path.join('..','..','clp-data','data','training'))
testing_dataset = forum_reader(os.path.join('..','..','clp-data','data','testing'))

pickle.dump(training_dataset, open('training_dataset.pickle', 'wb'))
pickle.dump(testing_dataset, open('testing_dataset.pickle', 'wb'))
