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
from data import *
import numpy as np


def extract(text, show_num, algorithm, input_type, language):
	'''
	:param text:输入文本数据
	:param show_num: 显示数据大小
	:param algorithm: 实现算法
	:param input_type: 数据来源0表示网页输入，1表示上传文件
	:return:
	'''
	words = "原 标题 抗议 蔡 当局 篡改 高中 历史课 纲 台湾 学者 连署 多时 争议 多方 后 仍 不顾 许多 专家 谆谆告诫 其 同路人 护航 全面 准备 让 未来 学子 接受 这份 既 专业 缺乏  发声 台 教育部门 日前 通过 历史 新 课 将 中国史 放 Each month over 50 million developers come to Stack Each month Each month over 50 million developers come to Stack Each month Each month over 50 million developers come to Stack Each month Each month over 50 million developers come to Stack Each month Each month over 50 million developers come to Stack Each month Each month over 50 million developers come to Stack Each month Each month over 50 million developers come to Stack Each month Each month over 50 million developers come to Stack Each month".split(' ')
	if len(words) > show_num:
		weights = np.random.random(show_num)
	else:
		weights = np.random.random(len(words))
	result = {}

	for k, v in zip(words, weights):
		result[k] = v

	print(len(result))

	import operator
	return sorted(result.items(), key=operator.itemgetter(1), reverse=True)
