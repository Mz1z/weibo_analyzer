# 初始化数据库使用的脚本
import sqlite3
import os

DB_DIR = './db/'

# 创建日志数据库

# 创建热搜数据库

# 创建留言数据库
conn = sqlite3.connect(DB_DIR + 'remark.db')
c = conn.cursor()
c.execute('''CREATE TABLE remark
       (time INTERGER NOT NULL,
       email TEXT,
       text TEXT);''')
conn.commit()
conn.close()

