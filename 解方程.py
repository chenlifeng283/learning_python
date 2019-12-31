import mpmath
import sympy

while True:
    try:
        print('----------------------------------------')
        func_str=input('输入方程式，以x为未知数:')

#判断方程式包含等号和未知数X的正则表达式怎么写
        if '=' not in func_str:
            print('方程式要带‘=’，你是小学没毕业吗！！！重写！！！')
        
        elif 'x' not in func_str and 'X' not in func_str:
            print('你是瞎吗?写了以x为未知数,我要跳错误了！！！重写！！！')
             
        else:
            func_str2=func_str.replace('=','-').replace('X','x')
            x=sympy.Symbol('x') #申明未知数    
            a=sympy.solve([func_str2],[x]) #写入需要解的方程体
            #验证一：补缴税额（包含冲减前多缴或有留抵）+所需发票或冲减=未调整前差异


            print('x的值为：%s'%a[x])
    except:
        print('输入的方程式有错误,如3x要写成3*x')
