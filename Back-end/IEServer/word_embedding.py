#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:word_embedding
   Author:jasonhaven
   date:18-8-20
-------------------------------------------------
   Change Activity:18-8-20:
-------------------------------------------------
"""

import gensim

model_file = "model/wiki_zh300.model.bin"
model = gensim.models.KeyedVectors.load_word2vec_format(model_file, binary=True)

def check_exists(word):
	return word in model.wv.vocab.keys()


def similarity(word1, word2):
	if not check_exists(word1):
		return word1,False
	if not check_exists(word2):
		return word2,False
	return float(model.similarity(word1, word2)), True


def most_similar(word, topn=5):
	if not check_exists(word):
		return word,False
	return model.most_similar(word, topn=topn), True
