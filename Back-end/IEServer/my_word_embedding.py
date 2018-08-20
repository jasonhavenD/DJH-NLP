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
	if check_exists(word1) and check_exists(word2):
		return float(model.similarity(word1, word2)), True
	return -1, False  # 单词不存在


def most_similar(word, topn=5):
	if check_exists(word):
		return model.most_similar(word, topn=topn), True
	return -1, False  # 单词不存在
