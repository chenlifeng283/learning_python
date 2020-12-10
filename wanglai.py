import xlwings as xw 
import pandas as pd 

def addSheets():
	wb = xw.books.active
	shtNames = [i.name for i in wb.sheets]#工作表名称列表

	sht1 = wb.sheets('目录表')
	sht2 = wb.sheets("样表-其他应付款") #其他应付款
	sht3 = wb.sheets("样表-其他应收款") #其他应收款
	targetSht = wb.sheets(sht1.range("G2").value) #数据来源工作表
	lastRow = targetSht.range("c50000").end('up').row 
	newsheets=[]
	for i in targetSht.range("c2:c"+str(lastRow)):
		if i.value not in shtNames and i.value not in newsheets:
			if i.offset(0,1).value == None:
				sht3.api.Copy(Before=sht3.api)
				xw.sheets.active.name = i.value
				xw.sheets.active.range("B1").value = i.value
				# sht1.activate
				cell = sht1.range("b50000").end('up').offset(1,0)
				cell.value = i.value
				hylink(cell)
			else:
				sht2.api.Copy(Before=sht2.api)
				xw.sheets.active.name = i.value
				xw.sheets.active.range("B1").value = i.value
				# sht1.activate
				cell =sht1.range("f50000").end('up').offset(1,0)
				cell.value = i.value
				hylink(cell)
			newsheets.append(i.value)
	print(newsheets)

def writeIn():
	mydic = {'其他应付款':["保证金收入","退保证金支出"],'其他应收款':["支付保证金","退回保证金"]}
	wb2 = xw.books.active
	sht1 = wb2.sheets('目录表')
	targetSht2 = wb2.sheets(sht1.range("G2").value) #数据来源工作表
	lastRow2 = targetSht2.used_range.last_cell.row
	df = pd.DataFrame(targetSht2.range("A2:F"+str(lastRow2)).value)
	if len(df)==6:
		df=df.T
	df[1]=None
	#print(df)
	df1 = df.loc[:,[2,0,1,4,3]] 
	#重新排序各列，以名字为第一列，后面四列刚好能直接写入各明细表
	if lastRow2 == 2:
		col_C=[targetSht2.range("c2:c"+str(lastRow2)).value]
	else:
		col_C = set(targetSht2.range("c2:c"+str(lastRow2)).value)
		col_C = [x for x in col_C if x != None]
	print(col_C)
	for i in col_C:
		x=df1[df1[2]==i].loc[:,[0,1,4,3]]
		print(x)
		#print(len(x))
		print(i)
		startCell = wb2.sheets(i).range("B50000").end('up').offset(1,0)
		B2_value = wb2.sheets(i).range("B2").value
		startCellrow = startCell.row
		startCell.options(index=False,header=False).value = x
		q=0
		while q<len(x):
			if B2_value=="其他应付款":
				if startCell.offset(q,2).value==None:
					startCell.offset(q,1).value=mydic['其他应付款'][0]
				else:
					startCell.offset(q,1).value=mydic['其他应付款'][1]
			elif B2_value=="其他应收款":
				if startCell.offset(q,2).value==None:
					startCell.offset(q,1).value=mydic['其他应收款'][1]
				else:
					startCell.offset(q,1).value=mydic['其他应收款'][0]
			q+=1



def hylink(rng):
	#rng = xw.Range(cell)
	#rng.api.Select()
	rng.api.Hyperlinks.Add(Anchor=rng.api, Address="", SubAddress= rng.value+"!A1", TextToDisplay=rng.value)


def main():
	addSheets()
	writeIn()
	
if __name__ == '__main__':
	main()
	
