import cPickle as pickle
from forum import ForumPost

training_dataset = pickle.load(open('training_dataset.pickle','rb'))

for key, value in training_dataset.iteritems():
	print value.label_fg
