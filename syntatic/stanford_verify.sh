#!/bin/bash

## Atention: java 8 is required
stan_parser='stanford-parser/'   
if [ ! -f $stan_parser ]; then
	echo 'stanford parser dir not found, downloading:'
	wget 'https://nlp.stanford.edu/software/stanford-parser-full-2016-10-31.zip'
	unzip 'stanford-parser-full-2016-10-31.zip'
	mv 'stanford-parser-full-2016-10-31/' 'stanford-parser/'
fi

eng_models='stanford-english-models.jar'     
if [ ! -f $eng_models ]; then
	echo 'english models not found, downloading:'
	wget 'https://nlp.stanford.edu/software/stanford-english-corenlp-2016-10-31-models.jar'
	mv 'stanford-english-corenlp-2016-10-31-models.jar' 'stanford-english-models.jar'
fi

pos_tagger='stanford-postagger/'     
if [ ! -f $pos_tagger ]; then
	echo 'post tagger not found, downloading:'
	wget 'https://nlp.stanford.edu/software/stanford-postagger-2016-10-31.zip'
	unzip 'stanford-postagger-2016-10-31.zip'
	mv 'stanford-postagger-2016-10-31/' 'stanford-postagger/'
fi

