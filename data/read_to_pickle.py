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
			dataset[post_number] = ForumPost(os.path.join(posts_path,f),post_number)
			dataset[post_number].label = label
			dataset[post_number].label_fg = ''.join(list(label_fg)[:-1])
		except Exception, e:
			pass
	return dataset


def out_of_dataset(training_path,testing_path):
	labels_training =  { tup.split("\t")[0] : tup.split("\t")[1:3] for tup in open(os.path.join(training_path,'labels.tsv'),'r').readlines() }
	labels_testing =  { tup.split("\t")[0] : tup.split("\t")[1:3] for tup in open(os.path.join(testing_path,'labels.tsv'),'r').readlines() }
	labels_extra =  { tup.split("\t")[0] : tup.split("\t")[1:3] for tup in open('extra_tags.txt','r').readlines() }

	posts_path = os.path.join(training_path,'posts')
	the_file_names = [ file for r,d,f in os.walk(posts_path) for file in f]
	dataset = {}
	for f in the_file_names:
		post_number = re.sub('\D', '', f)
		if not (post_number in labels_training) and not (post_number in labels_testing) and not (post_number in labels_extra):
			dataset[post_number] = ForumPost(os.path.join(posts_path,f),post_number)
		else:
			pass


	return dataset

def read_extra_labels(folder_path):
	labels = { tup.split("\t")[0] : tup.split("\t")[1:3] for tup in open('extra_tags.txt','r').readlines() }
	posts_path = os.path.join(folder_path,'posts')
	the_file_names = [ file for r,d,f in os.walk(posts_path) for file in f]
	dataset = {}
	for f in the_file_names:
		post_number = re.sub('\D', '', f)
		try:
			label = labels[post_number][0]
			label_fg = labels[post_number][1]
			dataset[post_number] = ForumPost(os.path.join(posts_path,f),post_number)
			dataset[post_number].label = label
			dataset[post_number].label_fg = ''.join(list(label_fg)[:-1])
		except Exception, e:
			pass
	return dataset



#out_dataset = out_of_dataset(os.path.join('clp-data','data','training'),os.path.join('clp-data','data','testing') )
#pickle.dump(out_dataset, open('ufrgs2017/data/out_dataset.pickle', 'wb'))

extra_dataset = read_extra_labels(os.path.join('clp-data','data','training'))
pickle.dump(extra_dataset, open('ufrgs2017/data/extra_dataset.pickle', 'wb'))


# training_dataset = forum_reader(os.path.join('clp-data','data','training'))
# testing_dataset = forum_reader(os.path.join('clp-data','data','testing'))

# pickle.dump(training_dataset, open('ufrgs2017/data/training_dataset.pickle', 'wb'))
# pickle.dump(testing_dataset, open('ufrgs2017/data/testing_dataset.pickle', 'wb'))
