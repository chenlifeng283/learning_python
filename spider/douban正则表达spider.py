# 要点：1.用正则表达式全匹配字符串，有时是最直接的方法。
#       2.写代码时，要先设计好“块”，用几个函数实现步骤+主函数main，最后用main()调用
#       3.正则表达式
#
#

import re
import requests

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
    

def getMovielist(Mlist,html):
    q = r'.span\sclass..title..([\u4e00-\u9fa5]+)..span.'
    # .代表任意一个字符，<>=等都可以用点号代替，没有.{2}这种写法，
    # 字母、下划线、横杠等要完全匹配，可以直接写，想匹配A，就写A。
    # 空格 \s
    #[\u4e00-u9fa5]是表示汉字，写法和[a-zA-Z]一致。
    # + 代表1个或多个加号前面的内容，*号是0个或多个

    
    print(re.findall(q,html))
    
    for i in re.findall(q,html):
        Mlist.append(i)
    
                   
def printOut(Mlist):
    try:
        with open("1.txt",'a',encoding="utf-8") as f : # a是追加方式写入，encoding不写往往会跳错误。
        
            for content in Mlist:
                f.write(content + '\n')
        print("input right...")
    except:
        print("input wrong....")
    

def main():
    Mlist=[]
    for i in range(10):
        url = r'https://movie.douban.com/top250?start=%s&filter='%(i*25)
        # 括号没加会出错误，本来会爬不到，但douban的这个排名URL有个特点，第一页start=0,第二页start=25
        # 但start = 1,2,3....都有数据，所有没跳错，是一个去掉前一个电影的重复。
        html = getHTMLtext(url)
        getMovielist(Mlist,html)
    printOut(Mlist)
    
    
if __name__ == "__main__":
    main()
        
        
