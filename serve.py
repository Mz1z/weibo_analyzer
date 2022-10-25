from flask import Flask, render_template
import sqlite3
import creeper

app = Flask(__name__)


@app.route('/')
def index():
	# 从数据中读取数据
	# 。。。
	# 测试使用直接爬虫数据
	c = creeper.Creeper()
	topic_list = c.get_topic_list().get_list()
	
	return render_template('index.html', topic_list=topic_list)
	
@app.route('/raw')
def index_raw():
	c = creeper.Creeper()
	topic_list = c.get_topic_list().sort_by_rawhot()
	
	return render_template('index.html', topic_list=topic_list)


if __name__ == '__main__':
	app.run('0.0.0.0', 5000)
