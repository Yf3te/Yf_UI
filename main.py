# main_ui.py
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QPushButton, QWidget
from PyQt5 import QtCore
from 页面1 import Ui_Dialog  # 导入页面1.py界面
from 页面2 import Ui_Dialog2  # 导入页面2.py界面
import sys
from PyQt5.QtGui import QIcon # 导入 QIcon 类
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1104, 876)
        MainWindow.setWindowIcon(QIcon("2_QEM_icon.ico"))
        MainWindow.setWindowTitle("Yf_UI")
        # 创建 QStackedWidget 来显示不同的页面
        self.stackedWidget = QStackedWidget(MainWindow)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1104, 876))

        # 页面 1 - 信息收集（加载 页面1.py 界面）
        self.page_1 = QtWidgets.QWidget()
        self.stackedWidget.addWidget(self.page_1)
        self.page_1_ui = Ui_Dialog()  # 创建1.py界面实例
        self.page_1_ui.setupUi(self.page_1)  # 加载1.py界面

        # 页面 2 - 脚本处理（加载 页面2.py 界面）
        self.page_2 = QtWidgets.QWidget()
        self.stackedWidget.addWidget(self.page_2)
        self.page_2_ui = Ui_Dialog2()  # 创建2.py界面实例
        self.page_2_ui.setupUi(self.page_2)  # 加载2.py界面

        # 切换按钮
        self.button_1 = QtWidgets.QPushButton(MainWindow)
        self.button_1.setGeometry(QtCore.QRect(40, 10, 121, 26))
        self.button_1.setText("信息收集")
        self.button_1.clicked.connect(self.show_page_1)

        self.button_2 = QtWidgets.QPushButton(MainWindow)
        self.button_2.setGeometry(QtCore.QRect(200, 10, 121, 26))
        self.button_2.setText("常用工具")
        self.button_2.clicked.connect(self.show_page_2)

    def show_page_1(self):
        self.stackedWidget.setCurrentIndex(0)  # 显示页面1

    def show_page_2(self):
        self.stackedWidget.setCurrentIndex(1)  # 显示页面2


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # 创建并初始化主界面
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()  # 创建主界面实例
    ui.setupUi(MainWindow)  # 设置UI界面

    MainWindow.show()  # 显示主界面

    sys.exit(app.exec_())  # 启动事件循环
