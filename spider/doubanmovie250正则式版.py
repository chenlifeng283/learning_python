
import re 
import requests

def getRespone(url):
	headers = {"User-Agent":"Mozilla/5.0"}
	data = requests.get(url,headers = headers)
	data = data.text
	return data


def get_picList(data,piclist):
	#正则表达式中用了两个组，再用findall找出来，
	#形成了一个有两个元素的元组组成的列表。
	#括号分组千万小心啊，把最后的括号向后了一步，取到了链接后的双引号，不会跳错，但下不到任何东西
	re1 = r'alt=\"(.+?)\"\ssrc=\"(.+?)\"'
	piclist2= re.findall(re1,data)
	for pic in piclist2:
		piclist.append(pic)

	
	return piclist


def download_pic(picurl):
	data = requests.get(picurl,headers= {"User-Agent":"Mozilla/5.0"})
	data = data.content
	return data

def save_pic(piclist):
	for k in range(len(piclist)):
		filename = piclist[k][0]
		fileurl = piclist[k][1]
		with open(r'C:\Users\陈云开\Desktop\learning python\爬虫\douban_movietop250PIC\top%s：%s.jpg'%(k+1,filename),'wb') as f :
			f.write(download_pic(fileurl))


def main():
	piclist = []
	for i in range(10):
		url = r'https://movie.douban.com/top250?start=%s&filter='%(i*25)
		data = getRespone(url)
		piclist = get_picList(data,piclist)
	save_pic(piclist)
	#print(piclist[1][0])
	#print(piclist[1][1])



if __name__ == '__main__':
	main()


