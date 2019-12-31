# --*-- coding:utf-8 --*--
import json
import time

Class Contact(object):
    def __inin__(self):
        with open("contact.txt","r",encoding = 'utf-8') as f:
            self.data = json.loads(f.read())
    
    def main_menu(self):
        
        while True:
            print('通讯录'.center(20,'='))
            menu = {'1':'快速查找','2':'添加联系人','3':'显示所有联系人'}
            for k,v in menu.items():
            print(k + ' ' + v)
            command = input('请选择你的操作》')
            if command == '1':
                self.seach()
            elif command == '2':
                self.add_contact()
            elif command == '3':
                self.show()
            elif command == 'q':
                print('退出。。。')
                break
    
    def search(self):
        print('快速查找'.center(20,'='))
        find_info = input('请输入查找信息》')
        count = 0 
        for i in range(len(self.data)):
            if count > len(self.data):
                print('未找到该联系人')
                break
            if fin_info in self.data[i]['name']:
                self.person_info(self.data[i])
            elif find_info in self.data[i]['phone_number']:
                self.person_info(self.data[i])
            else:
                pass
        count += 1
        
    def person_info(self,info):
        print('已为你找到：{}'.format(info['name']))
        menu = {'1':'查看个人信息','2':'修改信息','3':'删除联系人','4':'呼叫联系人'}
      
        
      
      
            
            

