# -*- coding:utf-8*-
# 利用PyPDF2模块合并同一文件夹下的所有PDF文件
# 只需修改存放PDF文件的文件夹变量：file_dir 和 输出文件名变量: outfile


import os
from PyPDF2 import PdfFileReader, PdfFileWriter
import time
import win32api
import win32print
from tkinter import*
from tkinter import filedialog
import random


# 使用os模块的walk函数，搜索出指定目录下的全部PDF文件
# 获取同一目录下的所有PDF文件的绝对路径
def getFileName(filedir):

    file_list = [os.path.join(filedir, filespath) \
                 for filespath in os.listdir(filedir) \
                 if str(filespath).endswith('pdf')
                 ]
                 
    return file_list if file_list else []
    
'''    
def getFileName(filedir):
    for a,b,filenames in os.walk(filedir):
# os.walk(filedir)可以分别获取当前文件夹下的文件夹、子文件夹、各文件
        # print(filenames)
        
# 本例中要获取filenames，是一个列表
        file_list = [file for file in filenames if str(file).endswith('pdf') ]
# 用列表生成式，从filenames列表中，获取后缀名为pdf的文件，生成列表
        return file_list if file_list else []
'''


# 合并同一目录下的所有PDF文件
def MergePDF(filepath, outfile):

    output = PdfFileWriter()
    outputPages = 0
    pdf_fileName = getFileName(filepath)

    if pdf_fileName:
        for pdf_file in pdf_fileName:
            txt.insert("end","路径：%s\n"%pdf_file)

            # 读取源PDF文件
            input = PdfFileReader(open(pdf_file, "rb"))

            # 获得源PDF文件中页面总数
            pageCount = input.getNumPages()
            outputPages += pageCount
            txt.insert("end","页数：%d\n"%pageCount)

            # 分别将page添加到输出output中
            for iPage in range(pageCount):
                output.addPage(input.getPage(iPage))

        txt.insert("end","合并后的总页数:%d.\n"%outputPages)
        # 写入到目标PDF文件
        outputStream = open(os.path.join(filepath, outfile), "wb")
        output.write(outputStream)
        outputStream.close()
        txt.insert("end","PDF文件合并完成！\n")

    else:
        txt.insert("end","没有可以合并的PDF文件！\n")

def print_pdf(print_file):
    try:
        win32api.ShellExecute (0,"print",print_file,None,".",0)
    except:
        txt.insert("end","找不到<合并表.pdf>\n")

def select_folder():
    root=Tk()
    root.title("选择需要合并的目标文件夹")
    root.withdraw()
    folderpath = filedialog.askdirectory()
    return folderpath
# 主函数
def main():
    time1 = time.time()
    global file_dir 
    file_dir = select_folder() #os.path.abspath('.') # 存放PDF的原文件夹,os.getcwd
    global outfile
    outfile = "合并表%s.pdf"%random.randint(1,100) # 输出的PDF文件的名称
    MergePDF(file_dir, outfile)
    time2 = time.time()
    txt.insert("end",'总共耗时：%s s.\n' %(time2 - time1))

def print_all():
    print_pdf(os.path.join(file_dir, outfile))

fm_main=Tk()
fm_main.title("合并PDF文件")
lab = Label(fm_main,text="合并该程序所在文件夹里的PDF文件！！！\n\n")
txt = Text(fm_main)
btn = Button(fm_main,text="开始合并",command=main)
btn2= Button(fm_main,text="打印",command=print_all)

lab.pack()
txt.pack()
btn.pack()
btn2.pack()
fm_main.mainloop()
