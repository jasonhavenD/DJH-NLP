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
from summa import keywords


def tfidf4zh(text, topK=20, idf_path='', stop_words_path='', withWeight=True, allowPOS=()):
	if idf_path != '':
		jieba.analyse.set_idf_path(idf_path)
	if stop_words_path != '':
		jieba.analyse.set_stop_words(stop_words_path)
	tags = jieba.analyse.extract_tags(text, topK=topK, withWeight=withWeight, allowPOS=allowPOS)
	return tags, True


def tfidf4en(text, topK=20, idf_path='', stop_words_path='', withWeight=True, allowPOS=()):
	if idf_path != '':
		jieba.analyse.set_idf_path(idf_path)
	if stop_words_path != '':
		jieba.analyse.set_stop_words(stop_words_path)
	tags = jieba.analyse.extract_tags(text, topK=topK, withWeight=withWeight, allowPOS=allowPOS)
	return tags, True


def textrank4zh(text, topK=20, idf_path='', stop_words_path='', withWeight=True,
                allowPOS=('nr', 'ns', 'n', 'vn', 'v', 'eng')):
	if idf_path != '':
		jieba.analyse.set_idf_path(idf_path)
	if stop_words_path != '':
		jieba.analyse.set_stop_words(stop_words_path)
	tags = jieba.analyse.textrank(text, topK=topK, withWeight=withWeight, allowPOS=allowPOS)
	return tags,True


def textrank4en(text, topK=20, radio=0.2):
	kw=keywords.keywords(text, radio, words=topK,scores=True)
	return kw,True
