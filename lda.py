import cPickle as pickle
import gensim
import logging
from nltk.tokenize import word_tokenize

def corpus_reader():
    for key, value in training_dataset.iteritems():
        yield  (value.text).encode('utf8').decode('utf8')


training_dataset = pickle.load(open('data/training_dataset.pickle','rb'))
lines = [word_tokenize(line.encode('utf8').decode('utf8')) for line in corpus_reader()]
dic = gensim.corpora.dictionary.Dictionary(documents=lines)
corpus = [dic.doc2bow(line) for line in lines]

lda = gensim.models.ldamodel.LdaModel(corpus=corpus, id2word=dic, num_topics=10, update_every=1, chunksize=10000, passes=1)
lda.save('topic_1')
print(lda.print_topics(10))
