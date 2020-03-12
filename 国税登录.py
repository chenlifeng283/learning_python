#https://zhuanlan.zhihu.com/p/94402506

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image
from aip import AipOcr
import time



# 验证码的获取和处理
def get_captcha(url):
    
    browser.get(url)
    # 要按“登录”，才会跳出登录界面
    # 下面的方法也挺形象的
    linkelem = browser.find_element_by_link_text('登录')
    linkelem.click()

    # 验证码图片的ID是yhming
    png = browser.find_element_by_id("yhmimg")
    # 将图片截屏保存
    png.screenshot('yhm.png')


    # 处理验证码
    img = Image.open('yhm.png')
    img = img.convert('L') # P模式转换为L模式(灰度模式默认阈值127)
    count = 165
    table = []
    for i in range(256):
        if i <count:
            table.append(0)
        else:
            table.append(1)

    img = img.point(table,'1')
    img.save('yhm1.png')


#验证码的识别
def discern_captcha(imageF):

    #要使用百度云OCR，要注册，得到以下三个信息
    APP_ID = '***'
    API_KEY = '***'
    SECRET_KEY = '***'

    #初始化对象
    client = AipOcr(APP_ID,API_KEY,SECRET_KEY)

    #读取图片
    with open(imageF,'rb') as f:
        image = f.read()

    #定义参数变量
    options = {'language_type':'ENG',}# 识别语言类型，默认为'CHN_ENG'中英文混合
    #  调用通用文字识别
    result = client.basicGeneral(image,options)
    #print(result)
    
    for word in result['words_result']:
        captcha = (word['words'])
        captcha = captcha.replace(" ","")
        print(captcha)
    return captcha


#登陆网页
def login(username,password,captcha):

    browser.find_element_by_id('username').send_keys(username)  # 找到账号框并输入账号
    browser.find_element_by_id('password').send_keys(password)  # 找到密码框并输入密码
    browser.find_element_by_id('yhmcode').send_keys(captcha)  # 找到验证码框并输入验证码
    browser.find_element_by_id('yhmlogin').click()  # 找到登陆按钮并点击
    #time.sleep(5)
    #browser.find_element_by_link_text('证明开具').click()
    time.sleep(5)
    
    browser.get('https://etax.zhejiang.chinatax.gov.cn/zjgfdacx/sscx/wszmcy/wszm_cy.html')
    time.sleep(2)
    #actions = ActionChains(browser)
    #time.sleep(5)
    #actions.move_to_element_with_offset(mylabel,0,0).click()
    #time.sleep(5)
    #browser.find_element_by_link_text('在线办理').click()

def select_type(date):
    browser.find_element_by_xpath('//div[@class="btn-group  bootstrap-select   show-tick form-control"]').click()

    time.sleep(3)
    #browser.find_element_by_xpath('//div//span[@class = "text"]').click()
    browser.find_element_by_link_text('年月').click()

    browser.find_element_by_id('sqrq_m').clear()
    time.sleep(1)
    browser.find_element_by_id('sqrq_m').send_keys(date)

def input_captcha():
    # 验证码图片的ID是yhming
    png = browser.find_element_by_id("codeImage")
    # 将图片截屏保存
    png.screenshot('code.png')


    # 处理验证码
    img = Image.open('code.png')
    img = img.convert('L') # P模式转换为L模式(灰度模式默认阈值127)
    count = 165
    table = []
    for i in range(256):
        if i <count:
            table.append(0)
        else:
            table.append(1)

    img = img.point(table,'1')
    img.save('code1.png')

    captcha = discern_captcha('code1.png')

    browser.find_element_by_id('check_code').send_keys(captcha)

    browser.find_element_by_id('queryBtn').click()
    time.sleep(5)

def getPDF():
    nums = browser.find_elements_by_xpath('//tbody[@id = "content"]//tr')
    count = 0
    for num in nums:
        #print(num)
        count = count + 1
    print('一共有%s条记录'%count)

    jksList= []
    for i in range(count):
        b = browser.find_element_by_xpath('//tbody[@id = "content"]//tr[%s]//td[1]//div'%(i+1))
        jksList.append(b.text)

    jksList = list(set(jksList))
    print(jksList)

    for i in range(len(jksList)):
        #q=wb.find_element_by_xpath('//div[contains(text(),"433016200100562801")]/../following-sibling::td[5]//a')
        q=browser.find_element_by_xpath('//div[contains(text(),"%s")]/../following-sibling::td[5]//a[contains(text(),"开具")]'%jksList[i])
        q.click()

    
    
def main():
    #获取图片
    url1 = 'https://etax.zhejiang.chinatax.gov.cn/zjgfdzswj/main/index.html'
    get_captcha(url1)

    #验证图片获取文本
    imagef1='yhm1.png'
    captcha = discern_captcha(imagef1)

    # 登录
    username = '91330109741011065X'
    password = 'A1234567'
    login(username,password,captcha)
    
    #二级界面输入、验证码
    date = '2020-01'
    select_type(date)
    input_captcha()
    getPDF()

browser=webdriver.Chrome() #实例化对象
main()

time.sleep(10)
browser.quit()
    








    






    
