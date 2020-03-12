#https://zhuanlan.zhihu.com/p/94402506

# 自动登陆电子税务局，下载电子缴款书
# 有验证码
# browser.find_element*对应的都有一个elements,是找到符合条件的所有元素，可迭代


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


#验证码的识别，百度的这个图片识别精度太差了，是要付钱才有更好的服务？
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
    
    # 生成的result是一个字典
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
    
    # 首页登录后，要点好几个才能到税单打印页面，情况有点复杂，不会处理，直接get二级界面
    browser.get('https://etax.zhejiang.chinatax.gov.cn/zjgfdacx/sscx/wszmcy/wszm_cy.html')
    time.sleep(2)
    #actions = ActionChains(browser)
    #time.sleep(5)
    #actions.move_to_element_with_offset(mylabel,0,0).click()
    #time.sleep(5)
    #browser.find_element_by_link_text('在线办理').click()

def select_type(date):
    # 选中下拉选择框，选类型
    browser.find_element_by_xpath('//div[@class="btn-group  bootstrap-select   show-tick form-control"]').click()

    time.sleep(3)
    
    #用下面的xpath方法，怎么也选不上，好像写法并没有什么问题，用link_text可以
    #browser.find_element_by_xpath('//div//span[@class = "text"]').click()
    browser.find_element_by_link_text('年月').click()
    
    # 选择日期，先中文本框，清除内容，再send_keys输入内容
    browser.find_element_by_id('sqrq_m').clear()
    time.sleep(1)
    browser.find_element_by_id('sqrq_m').send_keys(date)

# 二级界面里还有图片验证，验证一步可以单独写成函数，直接调用，这里不改了。
# 选择查询类型、输入日期、验证码，点击查询，获得PDF文件列表
def input_captcha():
    # 验证码图片的ID是codeImage
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

    #取得图片后，调用验证函数
    captcha = discern_captcha('code1.png')
    #选中文本框，输入
    browser.find_element_by_id('check_code').send_keys(captcha)
    #点击查询按钮
    browser.find_element_by_id('queryBtn').click()
    time.sleep(5)

#下载PDF文件
#按税种列表，特点是一行一个税种，后面点“开具”按钮就能下载到pDF文件，但实际的PDF中是多税种合并的，
#所以点所有“开具”，PDF文件有重复，需判断，按”税款单编号”筛选。
# 思路：1.判断有多少行--2.每一行的第一个是“缴款单编号”，得到这个列表--3.去重，按缴款单编号打印 
#      4.按去重后的缴款单编号，反定位所在的td, 5."开具"按钮就在前述的td的兄弟td里。

def getPDF():
    #获得列表中内容行数
    #//tbody//tr，有多少行就有多少tr
    #elements定位所有tbody下的tr
    nums = browser.find_elements_by_xpath('//tbody[@id = "content"]//tr')
    #计数，得到的nums算不算列表，不知道能不能用len(nums)或类似方法，得到计数，没试。
    count = 0
    for num in nums:
        #单纯计数，不需要内容
        #print(num)
        count = count + 1
    print('一共有%s条记录'%count)
    
    #count是多少，就循环多少次，得到“缴款单编号”列表，并去掉重得编号
    jksList= []
    for i in range(count):
        #缴款单编号在//tbody//每一个tr下//第一个td下//div的文本
        b = browser.find_element_by_xpath('//tbody[@id = "content"]//tr[%s]//td[1]//div'%(i+1))
        jksList.append(b.text)
        
    #set去重，再list恢复成列表形式
    jksList = list(set(jksList))
    print(jksList)
    
    # 反查每一个缴款单号码所在的标签，用兄弟节点的方法定位”开具”按钮
    for i in range(len(jksList)):
        
        #缴款单在div下，定位//div[contains(text(),"%s")]
        # /..定位到上一节点，即div的上一节点td
        # following-sibling::td[5],上述td的第5个兄弟td,即“开具”按钮所在的td
        # 最后是a标签
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
    username = '***'
    password = '***'
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
    








    






    
