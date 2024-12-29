### Yf_UI是一个目前用于整理信息收集数据、统一自己常用工具的简单UI界面，其一些功能主要是调用一些现成的工具，后续还会对其它功能进行开发。
工具使用：
```
python main.py
```
目前实现功能如下：
1、Icp批量查询
要修改一下icpsearch的路径，要修改自己安装的位置（绝对路径）。
![image](https://github.com/user-attachments/assets/ae9576ef-a5af-4182-ac37-b23b6252395d)

2、fofa批量语法
3、url的整理。
4、常用工具统一
每个工具的路径需要自己根据工具本身的绝对路径导入，（在toolsource.py当中）
下面简单做个展示
![image](https://github.com/user-attachments/assets/743e825b-eda9-48d8-b8ed-49e6f7faaa54)
常用工具集，共用一个文本框，但是还差一点程序防崩溃的措施，后续会开发
![image](https://github.com/user-attachments/assets/13b7be43-f7ce-44e9-b1ba-60990d951414)
通过点击左侧的工具栏，将会自动填写命令到命令行
![image](https://github.com/user-attachments/assets/95cea709-4407-40f3-9540-07be2b6c9703)
