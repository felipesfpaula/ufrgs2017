from collections import Counter
from nltk.tokenize import word_tokenize
import itertools
import numpy as np

## Find unique tokens in the corpus and returns token dictionary
def create_unigram_tokens(corpus, corpus_frequencies_filename = None):
	freqs = Counter(list(itertools.chain.from_iterable(corpus)))
	if corpus_frequencies_filename:
		with open(corpus_frequencies_filename,'w') as freq_out:
			for word in freqs.keys():
				freq_out.write((word + u' ' + str(freqs[word]) + u'\n').encode('utf-8'))
	return dict(zip(freqs.keys(), range(0,len(freqs)) ))	

## Returns a ngram frequency vector with dimension 1 x | tokens | 
def ngram_vectorize(tokenized_text,tok2id):
	feat_vec = np.zeros(shape=(len(tok2id),1))
	for word in tokenized_text:
		feat_vec[tok2id[word]] += 1 
	return feat_vec.T

def extract_unigram_for_training(corpus_plain_text):
	corpus = [ word_tokenize( (text).encode('utf8').decode('utf8') ) for text in corpus_plain_text]
	tokens2id = create_unigram_tokens(corpus)
	feats = [ ngram_vectorize(text,tokens2id) for text in corpus]
	return (np.vstack(feats), tokens2id)

## Used at run time to classify text
def extract_unigram(str,unigramDict):
	pass

def extract_bigram(str,bigramDict):
	pass
