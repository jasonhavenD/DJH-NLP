#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:keyword_extract
   Author:jasonhaven
   date:18-8-16
-------------------------------------------------
   Change Activity:18-8-16:
-------------------------------------------------
"""
import jieba.analyse


def tfidf4zh(text, topK=20, idf_path='', stop_words_path='', withWeight=True, allowPOS=()):
	if idf_path != '':
		jieba.analyse.set_idf_path(idf_path)
	if stop_words_path != '':
		jieba.analyse.set_stop_words(stop_words_path)
	tags = jieba.analyse.extract_tags(text, topK=topK, withWeight=withWeight, allowPOS=allowPOS)
	return tags


def tfidf4en(text, topK=20, idf_path='', stop_words_path='', withWeight=True, allowPOS=()):
	return [(1, 1), (2, 2)]


def textrank4zh(text, topK=20, idf_path='', stop_words_path='', withWeight=True, allowPOS=('nr', 'ns', 'n', 'vn', 'v','eng')):
	if idf_path != '':
		jieba.analyse.set_idf_path(idf_path)
	if stop_words_path != '':
		jieba.analyse.set_stop_words(stop_words_path)
	tags = jieba.analyse.textrank(text, topK=topK, withWeight=withWeight, allowPOS=allowPOS)
	return tags


def textrank4en(text, topK=20, idf_path='', stop_words_path='', withWeight=True, allowPOS=('nr', 'ns', 'n', 'vn', 'v')):
	return [(1, 1), (2, 2)]
