#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:ner
   Author:jasonhaven
   date:18-8-18
-------------------------------------------------
   Change Activity:18-8-18:
-------------------------------------------------
"""

from stanfordcorenlp import StanfordCoreNLP


'''
Guangdong University of Foreign Studies is located in Guangzhou.
'''
def stanford_ner(text, language='english'):
	nlp = StanfordCoreNLP("/home/jasonhaven/stanford-corenlp-full-2018-02-27")
	if language == 'chinese':
		nlp.lang = 'zh'
	result = nlp.ner(text)

	tag_and_freq = {}
	for tpl in result:
		word, tag = tpl
		if tag not in tag_and_freq.keys():
			tag_and_freq[tag] = 1
		else:
			tag_and_freq[tag] = tag_and_freq[tag] + 1
	nlp.close()# Do not forget to close! The backend server will consume a lot memery.
	return result, tag_and_freq, True
