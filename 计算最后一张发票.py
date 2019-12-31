# !/usr/bin/env python
# -*- coding:utf-8 -*-
#计算最后一张发票
'''工程挂靠原则上想拿多少钱，就拿多少票和税款来抵，到最后一笔核算的时候，如果考虑成一张普通发票（因为不带税额抵扣）  
那么，计算是很简单的，但如果涉及到专票，税额可以抵扣，是一个动态的变化过程，不能简单的计算出’应开多少票‘，这实际转  
化为一个一元一次方程问题了.
'''
import xlrd
from sympy import *
import tkinter as tk
from tkinter import filedialog

root=tk.Tk()
root.withdraw()
fpath=filedialog.askopenfilename()
print(fpath)


data = xlrd.open_workbook(fpath)

sheet = data.sheet_by_name('工程结算-发票、税额增补计算')

#方程：(H15-X/(1+税率）*税率-A)*(1+12%)+SUM(H23:H25)+X+（A税额对应的发票金额）=I6
#倒数第二张发票问题
未交增值税 = sheet.cell_value(14,7) #H15
税率 = eval(input('输入最后一张票的税率，如‘0.13’,普通发票输入‘0’:'))
last_two_tax = eval(input('输入倒数第二张发票税额,没有输入’0‘:'))
金额 = eval(input('倒数第二张发票的金额，没能输入’0‘:'))
差异 = sheet.cell(5,8).value # I6
水利 = sheet.cell_value(22,7)
if type(水利)== str:
        水利 = 0
印花 = sheet.cell(23,7).value
if type(印花) == str:
    印花 = 0
个税 = sheet.cell(24,7).value
if type(个税) == str:
    个税 = 0
          
          
           
x=Symbol('x') #申明未知数
if 税率 == 0:
    a=solve([(未交增值税-last_two_tax)*1.12+x+水利+印花+个税+金额-差异],[x])
        
else:
    a=solve([(未交增值税-x/(1+税率)*税率-last_two_tax)*1.12+x+水利+印花+个税+金额-差异],[x]) #写入需要解的方程体
#验证一：补缴税额（包含冲减前多缴或有留抵）+所需发票或冲减=未调整前差异

print(a)
