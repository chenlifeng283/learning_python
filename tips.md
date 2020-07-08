- 安装pyinstaller的问题
  - pip install wheel #必装
  - pip install win32 #必装
  - pip install -i https:pypi.tuna.tsinghua.edu.cn/simple --upgrade setuptools  
  #升级setuptools，其中有个attrs没有，就装不了pyinstaller

- 标签寄存javascript代码
  - 右键“新建标签”
  - 在“网址”里输入：   关键字`javascript:`+`js代码`,其中js代码最好以函数形式写，并调用，如:
  `javacsript:Function clf(){代码};clf()`
  - 在目标页面里，点击标签就可以运行了，用于下载，标记颜色等很好用
  - 可惜javascript出于安全考虑，不能轻易的调用本地文件，否则可以干很多事。自动填表，无法获取数据，只能做个半自动。

