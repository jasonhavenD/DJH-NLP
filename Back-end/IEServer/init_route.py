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
import mimetypes
import os
from flask import Flask, make_response, render_template, send_from_directory, request, flash, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)

__dir__ = ['404', '500', 'main', 'index', 'keyword', 'main_keyword', 'ner', 're', 'dataset']


@app.errorhandler(404)
def page_not_found(error):
	return render_template('404.html'), 404


@app.errorhandler(500)
def server_interval(error):
	return render_template('500.html'), 500


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


@app.route('/BITIE/dataset.html')
def dataset():
	'''
	常用数据集下载
	:return:
	'''
	return render_template('dataset.html')


@app.route('/BITIE/index')
@app.route('/BITIE/index.html')
def index():
	'''
	首页
	:return:
	'''
	return render_template('index.html')  # 使用模板会有动画失效的问题


'''
文件上传下载
'''

basepath = os.path.dirname(__file__)  # 当前文件所在路径
UPLOAD_FOLDER = 'upload'
ALLOWED_EXTENSIONS = set(['txt', 'doc', 'csv'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['JSON_AS_ASCII'] = False
upload_path = os.path.join(basepath, UPLOAD_FOLDER)

DOWNLOAD_FOLDER = 'download'


@app.route('/BITIE/download/<filename>', methods=['GET'])
def download(filename):
	if os.path.exists(os.path.join(DOWNLOAD_FOLDER, filename)) and os.path.isfile(
			os.path.join(DOWNLOAD_FOLDER, filename)):
		response = make_response(send_from_directory(DOWNLOAD_FOLDER, filename, as_attachment=True))
		mime_type = mimetypes.guess_type(filename)[0]
		response.headers['Content-Type'] = mime_type
		response.headers["Content-Disposition"] = "attachment; filename={};".format(filename.encode().decode('latin-1'))
		return response
	return render_template('404.html')


# 用于判断文件后缀
def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


app.config['SECRET_KEY'] = '123456'


@app.route('/BITIE/upload', methods=['POST', 'GET'])
def upload_file():
	'''
	上传文件
	:return:
	data:dict
		status:True/False
		text:content of file
		desc:description of status
	'''
	data = {}
	data['status'] = False
	data['desc'] = ''
	data['text'] = ''

	if request.method == 'POST':
		if 'myfile' not in request.files:
			flash('No file part')
			data['desc'] = '请求访问错误！'
			return jsonify(data)

	file = request.files['myfile']

	if file.filename == '':
		flash('No selected file')
		data['desc'] = '请求文件不存在！'
		return jsonify(data)

	if file and allowed_file(file.filename):
		filename = secure_filename(file.filename)
		file.save(os.path.join(upload_path, filename))
		with open(os.path.join(upload_path, filename), 'r', encoding='utf-8') as f:
			text = f.read()
		data['status'] = True
		data['text'] = text
		return jsonify(data)
	return render_template('404.html')


'''
业务处理
'''
#
# from keyword_extract import extract as ke
#
#
# @app.route("/BITIE/keyword_extract")
# def keyword_extract():
# 	app.logger.info('keyword_extract....')
#
# 	result = ke("123456")
#
# 	return jsonify(result)
