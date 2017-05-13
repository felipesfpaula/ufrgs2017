from collections import Counter
from nltk.tokenize import word_tokenize
import nltk
import itertools
import numpy as np
from syntatic.parsing import *
import cPickle as pickle


## Find unique tokens in the corpus and returns token dictionary
def create_unigram_tokens(corpus, corpus_frequencies_filename = None):
	freqs = Counter(list(itertools.chain.from_iterable(corpus)))
	tokens = map(lambda x:x[0],freqs.most_common())
	if corpus_frequencies_filename:
		with open(corpus_frequencies_filename + '.txt','w') as freq_out:
			for word in tokens:
				freq_out.write((word + u' ' + str(freqs[word]) + u'\n').encode('utf-8'))

	ans = dict(zip(tokens, range(0,len(tokens)) ))	

	pickle.dump(ans, open(corpus_frequencies_filename + '.pickle', 'wb'))
	return ans


def char_ngram_tokenizer(text,n=2):
	tokens = word_tokenize(text)
	return [b[i:i+n] for b in tokens for i in range(len(b)-(n-1))]

## Returns a ngram frequency vector with dimension 1 x | tokens | 
def ngram_vectorize(tokenized_text,tok2id):
	feat_vec = np.zeros(shape=(len(tok2id),1))
	for word in tokenized_text:
		feat_vec[tok2id[word]] += 1 
	return feat_vec.T

def extract_ngram_for_training(corpus_plain_text,tokenizer):
	corpus = [ tokenizer( (text).encode('utf8').decode('utf8') ) for text in corpus_plain_text]
	tokens2id = create_unigram_tokens(corpus)
	feats = [ ngram_vectorize(text,tokens2id) for text in corpus]
	return (np.vstack(feats), tokens2id)

def extract_syntatic_feats_for_training(corpus_plain_text):
	corpus = [ extract_productions_triples_taggedsent( (text).encode('utf8').decode('utf8') ) for text in corpus_plain_text]
	prod2id = create_unigram_tokens([ prod for item in corpus for prod in item['prods']], 'prod_dictionary' )
	triples = []
	for item in corpus:
		for trip in item['triples']:
			for subtrip in trip:
				for subsubtrip in trip:
					for i in subsubtrip:
						# triples.append([i[0][0]+i[0][1]+i[1]+ i[2][0]+i[2][1] ])
						triples.append([ str((i[0][1], i[1], i[2][1])) ])

	trip2id = create_unigram_tokens(triples, 'trip_dictionary' )



def extract_bigram_for_training(corpus_plain_text):
	return extract_ngram_for_training(corpus_plain_text,nltk.bigrams)

def extract_unigram_for_training(corpus_plain_text):
	return extract_ngram_for_training(corpus_plain_text, word_tokenize)

def extract_char_bigram_for_training(corpus_plain_text):
	return extract_ngram_for_training(corpus_plain_text,lambda x: char_ngram_tokenizer(x,n=2))

def extract_char_trigram_for_training(corpus_plain_text):
	return extract_ngram_for_training(corpus_plain_text,lambda x: char_ngram_tokenizer(x,n=3))

## Used at run time to classify text
def extract_unigram(str,unigramDict):
	pass

def extract_bigram(str,bigramDict):
	pass
