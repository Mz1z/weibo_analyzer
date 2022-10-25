import requests
import re
import json
import time
import sqlite3


# 热搜话题类
class Topic():
	def __init__(self, num, raw_hot, onboard_time, category, word, rank):
		self.num = num
		self.raw_hot = raw_hot
		self.onboard_time = onboard_time
		self.category = category
		self.word = word
		self.rank = rank

	def to_string(self):
		return f"排行: {self.rank}, 热度值: {self.num}, 原始热搜值: {self.raw_hot}, 上榜时间: {self.onboard_time}, 分类: {self.category}, 标题: {self.word}"

# 热搜榜单类
class TopicList():
	def __init__(self):
		self.topic_list = []

	def add(self, topic):
		self.topic_list.append(topic)

	def sort_by_rawhot(self):
		_list = list(self.topic_list)  # 整一个副本
		_tmp = None
		for i in range(len(_list)):
			for j in range(i, len(_list)):
				if _list[i].raw_hot < _list[j].raw_hot:  # 排序
					_tmp = _list[i]
					_list[i] = _list[j]
					_list[j] = _tmp
		return _list

	def get_list(self):
		return self.topic_list


url = 'https://weibo.com/ajax/statuses/hot_band'

headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
}

# 爬虫类
class Creeper():
	def __init__(self):
		pass

	def get_topic_list(self):
		r = requests.get(url, headers=headers)
		_data = json.loads(r.text)
		# 获取list
		band_list = _data['data']['band_list']    # 普通热搜
		hotgov = _data['data']['hotgov']    # 政治热搜
		print(json.dumps(band_list, ensure_ascii=False, indent=4))

		# 创建topiclist
		topic_list = TopicList()

		for band in band_list:
			if band.get('raw_hot') == None:   # 广告
				continue
			topic = Topic(
				band['num'],
				band.get('raw_hot'),
				time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(band.get('onboard_time'))),
				band.get('category'),
				band['word'],
				band['rank']
			)
			topic_list.add(topic)

			# 输出测试
			print(
				topic.to_string()
			)

		print('------------------------------------------------------------------------------')
		# 按原始热度排序
		_list = topic_list.sort_by_rawhot()
		for i in _list:
			print(i.to_string())

		return topic_list



if __name__ == '__main__':
	print('start...')
	c = Creeper()
	topic_list = c.get_topic_list()