# 要点：1.requests.get()获取源码，注意headers属性，douban有反爬程序，不模拟成浏览器，status_code 是418，无法获得反馈。
#	   2.用BeautifulSoup解析源码，观察源码，找到要寻找的目标在哪个标签，可以层层遍历（先find_all大范围标签，再find具体)
#	   ，如果只是找影片标签可以直接find.
#      3.能封装成函数就要封装。



-*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import json

# 用于发送请求，获得网页源代码以供解析
# r.content得到的信息和右键点击“显示网页源代码”的内容是一样的，否则就是网站做了anti-spider.
def start_requests(url):
	headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
	r = requests.get(url,headers=headers)
	return r.content

# 接收网页源代码解析出需要的信息
def parse(text):
	soup = BeautifulSoup(text,'html.parser') # 解析
	#（观察源码，影片信息在<div class="item">.....</div>中
	movie_list = soup.find_all('div',class_='item') # 找到所有class属性为item的div标签，形成列表
	result_list = [] #把结果依次存入列表
	for movie in movie_list:
		mydict = {} # 用字典模式存储，方便转换为json存储
		mydict['title'] = movie.find('span',class_= 'title').text #每循环出一个movie数据，影片名藏在class属性为title的span标签里
		mydict['score'] = movie.find('span',class_='rating_num').text
		mydict['quote']	= movie.find('span',class_= 'inq').text
		star = movie.find('div',class_= 'star')
		mydict['comment_num'] = star.find_all('span')[-1].text[:-3]
		result_list.append(mydict)
	return result_list

#将数据写入json
def write_json(result):
	s = json.dumps(result,indent = 4,ensure_ascii = False)
	with open('movies.json','w',encoding = 'utf-8') as f:
		f.write(s)

def main():
	url = 'http://movie.douban.com/top250'
	text = start_requests(url)
	result = parse(text)
	write_json(result)

if __name__ == '__main__':
	main()
