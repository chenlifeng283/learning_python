import requests
from bs4 import BeautifulSoup


def start_get(url):
    headers= {"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Mobile Safari/537.36"}
    r = requests.get(url,headers=headers)
    return r.content

def get_soup(text):
    soup = BeautifulSoup(text,'html.parser')
    #<class 'bs4.BeautifulSoup'>
    #soup是解析后的源代码
    
    list1 = soup.find_all('tr')
    #<class 'bs4.element.ResultSet'>
    #list1是一个列表，每一个列表元素是一个<tr>中间包含子标签</tr>,即下文中的content

    
    list2 = list1[2:len(list1)-2]
    #<class 'list'>
    #切片list1,得到list2,

    
    for content in list2:

        #每一个content,通过find_all,找出每一个<td>..</td>形成一个列表：td_content
        td_content=content.find_all('td')
        print("货币-%s的中行折算价为：%s"%(td_content[0].text,td_content[5].text))



def main():
    for i in range(9):
        url = 'https://www.boc.cn/sourcedb/whpj/index_%s.html'%i
        text1=start_get(url)
        get_soup(text1)

    

if __name__ == "__main__":
    main()
    
