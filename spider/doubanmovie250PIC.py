# 要点：1.用正则表达式全匹配字符串，有时是最直接的方法。
#       2.写代码时，要先设计好“块”，用几个函数实现步骤+主函数main，最后用main()调用
#       3.关键在这句<img width="100" alt="霸王别姬" src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2561716440.webp" class="">
#       4.BeautifulSoup解析得到一个对象，可以很方便的引用标签，如：x.p.a.img,x对象下的P标签的a链接标签下的Img标签，只要是网页源码上有的，可层层下找。
#


# 下载电影图片，每个图片的文件名为电影名，和图片内容对应。
import re
import requests
from bs4 import BeautifulSoup


def getHTMLtext(url):
    try:
        headers = {"User-Agent":"Mozilla/5.0"}
        r = requests.get(url,headers = headers)
        r.raise_for_status
        
        r.encoding = r.apparent_encoding
        # 分析get到的内容是用什么编码的，再赋值给编码方式
        #会拖慢程序，可以直接观察网站源码，直接找到编码方式并赋值
        
        return r.text
    except:
        return ""
    


def getMoviePicList(PicList,html):
    soup = BeautifulSoup(html,'html.parser')
    allPIC = soup.find_all("div",class_="pic")
    #如果直接找img标签，那会抓到很多不需要的图片地址，
    #所有影片图片都在<div class="pic">下
    
    for PIC in allPIC:
        PicList.append([PIC.img.attrs["alt"],PIC.img.attrs["src"]])
        # img的"alt"属性是电影名，后面用作文件名
        # img的"src"属性是图片链接，后面打开下载
        # 把这两个字段组成列表，添加到PicList里，形成嵌套列表

    return PicList
                          
                   
def printOut(num,PicList):
    headers = {"User-Agent":"Mozilla/5.0"}
    for i in range(num):   # 可以预设一次下载几部，完善一下的话可以规定下载第几名到第几名
        filename = PicList[i][0] # 取电影名
        fileURL = PicList[i][1]  # 取对应的链接

        r= requests.get(fileURL,headers=headers)
    
        with open("%s.png"%filename,'wb') as f :
            f.write(r.content)
     
    

def main():
    PicList = []
    for i in range(10):
        url = r'https://movie.douban.com/top250?start=%s&filter='%(i*25)
        # 括号没加会出错误，本来会爬不到，但douban的这个排名URL有个特点，第一页start=0,第二页start=25
        # 但start = 1,2,3....都有数据，所有没跳错，是一个去掉前一个电影的重复。
        html = getHTMLtext(url)
        PicList = getMoviePicList(PicList,html)
                                                                   
                                                                   
    #print(PicList)                                                               
    num = int(input("需要下载前多少部(最多250）："))
    printOut(num,PicList)
    
   
    
    
if __name__ == "__main__":
    main()
        
        
