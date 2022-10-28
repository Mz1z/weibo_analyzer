from flask import Flask, render_template, request
import sqlite3
import creeper
import os

# 日志、临时文件存放目录
LOG_DIR = './log/'
# 数据库存放目录
DB_DIR = './db/'

app = Flask(__name__)


# 初始化
# 启动检查
def init_and_check():
	# 检查数据库
	# 。。。
	
	# 检查日志
	if not os.path.exists(LOG_DIR + 'view.log'):
		# 不存在则创建
		with open(LOG_DIR + 'view.log', 'w', encoding='utf-8') as f:
			pass
		
	
	print('环境检查完毕，正常启动')


# 记录日志(简单，测试用)
def view_log(request):
	ip = request.remote_addr
	if ip == '127.0.0.1':
		# 判断反向代理的存在
		pass
	with open(LOG_DIR + 'view.log', 'a', encoding='utf-8') as f:
		f.write(ip + '\n')

@app.route('/')
def index():
	# 从数据中读取数据
	# 。。。
	# 测试使用直接爬虫数据
	c = creeper.Creeper()
	topic_list = c.get_topic_list().get_list()

	# 日志
	view_log(request)
	
	return render_template('index.html', topic_list=topic_list)
	
@app.route('/raw')
def index_raw():
	c = creeper.Creeper()
	topic_list = c.get_topic_list().sort_by_rawhot()
	
	# 日志
	view_log(request)
	
	return render_template('index.html', topic_list=topic_list)
	
# 统计
@app.route('/statistic')
def statistic():
	with open(LOG_DIR + 'view.log', 'r', encoding='utf-8') as f:
		text = f.read()
	return text


if __name__ == '__main__':
	init_and_check()
	app.run('0.0.0.0', 9999)
