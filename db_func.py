# 数据库操作类
import sqlite3
import time

DB_DIR = './db/'

# 向数据库中插入留言
def insert_remark(text, email=''):
	conn = sqlite3.connect(DB_DIR + 'remark.db')
	c = conn.cursor()
	c.execute('''
INSERT INTO `remark` values (?, ?, ?);
''', (int(time.time()), email, text))
	conn.commit()
	conn.close()
