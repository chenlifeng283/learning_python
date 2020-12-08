#合并当前文件夹下的工作薄到新工作薄

import xlwings as xw
import os
import pandas as pd
mypath = os.getcwd()
#print(mypath)

# 使用os模块的walk函数，搜索出指定目录下的全部xlsx\xls文件
# 获取同一目录下的所有excel文件的绝对路径
def getFileName(filedir):

    file_list = [os.path.join(root, filespath) \
                 for root, dirs, files in os.walk(filedir) \
                 for filespath in files \
                 if str(filespath).endswith('xlsx')  \
                 or str(filespath).endswith('xls') \
                 or str(filespath).endswith('xlsm')
                 ]
    return file_list if file_list else []


def mergeExcel(fileList):
	app = xw.App(visible = False,add_book=True)
	wb = app.books.active
	
	wb.sheets[0].range('A1:Z1000').api.NumberFormatLocal = "@"
	#调用Excel的api设置格式（VBA思路）
	
	list_final=[] #把每个工作薄的每张工作表的数据存入列表
	for i in fileList:       
		newWb = app.books.open(i) #遍历工作薄
		sheetNums = newWb.sheets.count
		for j in range(sheetNums):   #遍历工作表
			if newWb.sheets[j].used_range.value != None:  # 空工作返回值为None
				list_final=list_final + newWb.sheets[j].used_range.value
				#用xw获得的Value本身是个二维列表，不能用list_final.append()
		newWb.close() #每次处理完一个都关闭
	
	x = pd.DataFrame(list_final) # list_final各元素长度不一，不能直接写回excel,转换
	wb.sheets[0].range("A1").options(index=False,header=False).value = x #不要index,columns	
	wb.save(mypath + '\\' + '汇总表-all.xlsx')
	wb.close()
	app.quit()


def main():
	fileList = getFileName(mypath)
	print(fileList)
	mergeExcel(fileList)
	


if __name__ == '__main__':
	main()
