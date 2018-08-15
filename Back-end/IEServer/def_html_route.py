#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:def_html_route
   Author:jasonhaven
   date:18-8-15
-------------------------------------------------
   Change Activity:18-8-15:
-------------------------------------------------
"""
from flask import Flask, render_template

app = Flask(__name__)

__dir__ = ['find_error', 'server_error', 'main', 'index', 'keyword', 'main_keyword', 'ner', 're']


@app.route('/BITIE/404')
def find_error():
	'''
	404页面
	:return:
	'''
	return render_template('404.html')


@app.route('/BITIE/500')
def server_error():
	'''
	500页面
	:return:
	'''
	return render_template('500.html')


'''
首页的右侧内部页面定义
'''


@app.route('/BITIE/main.html')
def main():
	return render_template('main.html')


@app.route('/BITIE/main_keyword.html')
def main_keyword():
	return render_template('main_keyword.html')


@app.route('/BITIE/main_ner.html')
def main_ner():
	return render_template('main_ner.html')


@app.route('/BITIE/main_re.html')
def main_re():
	return render_template('main_re.html')


'''
左侧栏目方法定义
'''
@app.route('/BITIE/keyword.html')
def keyword():
	'''
	关键字提取
	:return:
	'''
	return render_template('keyword.html')


@app.route('/BITIE/ner.html')
def ner():
	'''
	命名实体识别
	:return:
	'''
	return render_template('ner.html')


@app.route('/BITIE/re.html')
def re():
	'''
	实体关系抽取
	:return:
	'''
	return render_template('re.html')


@app.route('/BITIE/')
@app.route('/BITIE/index')
@app.route('/BITIE/index.html')
def index():
	'''
	首页
	:return:
	'''
	return render_template('index_bak.html')  # index.html会有动画失效的问题
