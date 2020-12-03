#1.第二个默认参数设为第一个参数的值 row9
#2.dataframe以第1列为kye,第3、4列组成列表为value,组成字典 row78


import xlwings as xw 
import re
import pandas as pd
import win32api

def last_row(col1,col2=None):
#确定最后一个非空单元格所在的行号
	if col2 == None:
		col2 = col1
	rng = xw.Range("%s:%s"%(col1,col2))
	col_num = rng.columns.count
	n = rng.last_cell.end('up').row 

	for i in range(1,col_num):
		m = rng.last_cell.offset(0,-i).end('up').row 
		if m>n:
			n = m
	return n 

def clear_empty(rng):
#某一列单元格区域去掉空值，生成不含空值的list	
	list1 = xw.Range(rng).value
	#print(type(list1))
	if isinstance(list1,list):
		list1 = [i for i in list1 if i !=None]
		return list1
	else:
		return [list1]

def tianbiao(startrow):
#把“货物信息“表中找到的数据填到各个激活表中的相应位置。
    ws1=xw.Book("inputSheet.xlsm").sheets("货物信息")
    lastrow1 = ws1.range("c50000").end('up').row
    # 货物信息表里最后一行行号
    arr1 = ws1.range("c3:l"+str(lastrow1)).value

    df1 = pd.DataFrame(arr1)
    df2=df1.loc[range(lastrow1-2),[0,1,2,4,5,7,8,9]]
    df2[1]=""
    df2[2]=df2[2].map(mysplit) 
    #上述写法是pandas的语法糖？
    #正规写法是 map(mysplit,df2[2]),但生成的是一个迭代器，需要list()

    lastrow2 = last_row("T","T") #辅助列确认最后一个非空值
    invoce = clear_empty("t5:t"+str(lastrow2))
    #print(invoce)
    invoce2 = list(set(invoce))
    #print(invoce2)

    if len(invoce) != len(invoce2):
    	win32api.MessageBox(0,"辅助列T列有重复输入","Tips")
    else:
	    to_excel = df2[df2[0].isin(invoce)]
	    #print(to_excel)
	    #startrow = max(last_row("c","j"),last_row("l","r"))+1
	    xw.Range("c"+str(startrow)).options(index=False,header=False).value = to_excel
	    #endrow = max(last_row("c","j"),last_row("l","r"))
    
def mysplit(str1):
	if "*" in str1:
		return str1.split("*")[len(str1.split("*"))-1]
	else:
		return str1

def companyName():
#填入销售单位名称
	ws2=xw.Book("inputSheet.xlsm").sheets("发票信息")
	lastrow3 = ws2.range("c50000").end('up').row 

	data = pd.DataFrame(ws2.range("c3:s"+str(lastrow3)).value)
	data2 = data.loc[range(lastrow3-2),[0,4,16]].set_index([0]) #以0列为索引列
	#print(data2.tail())
	f = lambda x:[x]
	mydic = (data2[4].map(f)+data2[16].map(f)).to_dict() 
	#把第4、16列每个元素处理成list,并相加成新列表
	#把得到的新Series添加到新列（这里实际没赋值加上去）
	#以0列为key,新列为value,to_dict()
	

	mydic2 = {}
	for j,k in mydic.items():
		if "代开" in str(k[1]):
			mydic2[j] = get_name(str(k[1]))
		else:
			mydic2[j] = k[0]
	#print(mydic2['78684026'])
	return mydic2

def compName_toexcel(startrow,endrow):
#输出公司名
	compNameDic = companyName()
	if startrow <= endrow:
		xx = xw.Range("c%d:c%d"%(startrow,endrow)).value
		if isinstance(xx,str):
			xx = [xx]
		xw.Range("d"+str(startrow)).options(transpose = True).value = [compNameDic[i] for i in xx]
			

def get_name(str1):
#提取备注栏的公司名
	partten1 =r"代开企业名称[:：](.+[司部厂行店场户站队处所心校 ]*)"
	realName = re.findall(partten1,str1)
	if realName ==[]:
		return str1
	else:
		return "(代开)"+realName[0]


def col_t():
#标记T列没有被找到的数据
	xw.Range("T:T").color = None
	q = last_row("t")
	if q >=5:
		rng = xw.Range("t5:t"+str(q))
		if rng.value != None:
			ws2 = xw.Book('inputSheet.xlsm').sheets('发票信息')
			ws2_lastrow = ws2.range("c50000").end('up').row
			arr2 = ws2.range("c3:c"+str(ws2_lastrow)).value
			color_count=0
			for i in rng:
				if (i.value not in arr2) and i.value !=None:
					i.color = (225,225,0)
					color_count +=1
	if color_count >0:
		win32api.MessageBox(0,"辅助列T列有未找到数据的，已标记颜色!","Tips")

def main():
	startrow = max(last_row("c","j"),last_row("l","r"))+1
	
	tianbiao(startrow)
	endrow = max(last_row("c","j"),last_row("l","r"))
	print(startrow)
	print(endrow)
	compName_toexcel(startrow,endrow)
	col_t()

if __name__ == '__main__':
	main()

#s = df.groupby([0])[4].apply(lambda x:x.tolist())
#s.to_dict()
