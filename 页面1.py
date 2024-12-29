from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import subprocess
import re
import time
import os
import socket
from urllib.parse import urlparse
from function1 import *
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1104, 876)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 10, 121, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 50, 141, 16))
        self.label_2.setObjectName("label_2")
        self.textBrowser_2 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_2.setGeometry(QtCore.QRect(480, 70, 256, 192))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(480, 50, 121, 20))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(310, 170, 151, 51))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 90, 121, 51))
        self.pushButton_2.setObjectName("pushButton_2")

        self.textBrowser_3 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_3.setGeometry(QtCore.QRect(810, 70, 256, 192))
        self.textBrowser_3.setObjectName("textBrowser_3")

        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(810, 50, 101, 16))
        self.label_4.setObjectName("label_4")

        self.textBrowser_4 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_4.setGeometry(QtCore.QRect(740, 340, 341, 191))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(750, 310, 131, 16))
        self.label_5.setObjectName("label_5")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(40, 340, 241, 191))
        self.textEdit.setObjectName("textEdit")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(40, 310, 191, 16))
        self.label_6.setObjectName("label_6")
        self.textEdit_2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(320, 340, 241, 191))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(320, 310, 161, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(590, 420, 72, 15))
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(580, 410, 141, 41))
        self.pushButton_4.setObjectName("pushButton_4")


        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(50, 560, 81, 16))
        self.label_9.setObjectName("label_9")

        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(290, 590, 93, 28))
        self.pushButton_5.setObjectName("pushButton_5")

        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(290, 630, 141, 21))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_2.setGeometry(QtCore.QRect(290, 660, 101, 21))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_3.setGeometry(QtCore.QRect(290, 760, 101, 21))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_4.setGeometry(QtCore.QRect(290, 730, 141, 21))
        self.checkBox_4.setObjectName("checkBox_4")

        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(290, 690, 93, 28))
        self.pushButton_6.setObjectName("pushButton_6")

        self.textBrowser_5 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_5.setGeometry(QtCore.QRect(430, 580, 191, 261))
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.textBrowser_6 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_6.setGeometry(QtCore.QRect(870, 580, 221, 261))
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(430, 560, 81, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(870, 560, 81, 16))
        self.label_11.setObjectName("label_11")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(30, 280, 1071, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(30, 540, 1071, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Dialog)
        self.line_3.setGeometry(QtCore.QRect(20, 40, 16, 811))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(Dialog)
        self.line_4.setGeometry(QtCore.QRect(1090, 40, 16, 811))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(Dialog)
        self.line_5.setGeometry(QtCore.QRect(30, 30, 1071, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(Dialog)
        self.line_6.setGeometry(QtCore.QRect(30, 840, 1071, 16))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")

        self.pushButton_7 = QtWidgets.QPushButton(Dialog)
        self.pushButton_7.setGeometry(QtCore.QRect(290, 790, 93, 28))
        self.pushButton_7.setObjectName("pushButton_7")

        self.textBrowser_7 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_7.setGeometry(QtCore.QRect(630, 580, 231, 261))
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(630, 560, 81, 16))
        self.label_12.setObjectName("label_12")

        self.textEdit_4 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_4.setGeometry(QtCore.QRect(40, 70, 251, 191))
        self.textEdit_4.setObjectName("textEdit_4")

        self.textEdit_5 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_5.setGeometry(QtCore.QRect(40, 580, 241, 261))
        self.textEdit_5.setObjectName("textEdit_5")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        #连接函数
        self.pushButton.clicked.connect(lambda: extractbah(self))
        self.pushButton_2.clicked.connect(self.call_icpsearch)
        self.pushButton_4.clicked.connect(lambda: generate_fofa_query(self))
        self.pushButton_5.clicked.connect(lambda: extract_ip(self))
        self.pushButton_6.clicked.connect(lambda: extract_domain(self))
        self.pushButton_7.clicked.connect(lambda: extract_cidr(self))

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Yf3_te"))
        self.label.setText(_translate("Dialog", "信息收集整理UI"))
        self.label_2.setText(_translate("Dialog", "请输入公司名列表"))
        self.label_3.setText(_translate("Dialog", "备案号&公司列表"))

        self.pushButton.setText(_translate("Dialog", "备案号公司url提取"))

        self.pushButton_2.setText(_translate("Dialog", "调用Icpsearch"))

        self.label_4.setText(_translate("Dialog", "主域名列表"))
        self.label_5.setText(_translate("Dialog", "fofa搜索语法"))
        self.label_6.setText(_translate("Dialog", "请输出组织名、公用名"))
        self.label_7.setText(_translate("Dialog", "请选择性输入哈希值"))

        self.pushButton_4.setText(_translate("Dialog", "fofa语法生成"))

        self.label_9.setText(_translate("Dialog", "url列表"))

        self.pushButton_5.setText(_translate("Dialog", "ip整理"))

        self.checkBox.setText(_translate("Dialog", "带有http(s)协议"))
        self.checkBox_2.setText(_translate("Dialog", "带有端口"))
        self.checkBox_3.setText(_translate("Dialog", "带有端口"))
        self.checkBox_4.setText(_translate("Dialog", "带有http(s)协议"))

        self.pushButton_6.setText(_translate("Dialog", "域名整理"))

        self.label_10.setText(_translate("Dialog", "IP列表"))
        self.label_11.setText(_translate("Dialog", "域名列表"))

        self.pushButton_7.setText(_translate("Dialog", "c段整理"))

        self.label_12.setText(_translate("Dialog", "c段列表"))

    def call_icpsearch(self):
        # 获取每一行输入
        input_text = self.textEdit_4.toPlainText()
        lines = input_text.splitlines()  # 按行分割

        # 清空输出框
        self.textBrowser_2.clear()

        # 逐行处理每一行数据
        for line in lines:
            line = line.strip()  # 去除每行的空格和换行符
            if line:  # 如果该行不为空
                result = self.run_command(line)
                self.textBrowser_2.append(f"查询：{line}\n结果：\n{result}\n{'-' * 40}\n")
    def fill_command_from_combobox(self):
        # 获取被点击的命令并填充到 lineEdit 中
        command = self.commandComboBox.currentText()
        self.lineEdit.setText(command)


    def run_command(self, query):
        # 执行 ICPSearch.exe 命令
        command = rf'E:\yf\7-tools\1-信息收集\ICP主域名批量\ICPSearch.exe -d {query}'  # 使用原始字符串防止路径问题
        try:
            # 执行命令并捕获输出
            result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, encoding='utf-8')
            return result
        except subprocess.CalledProcessError as e:
            # 处理错误输出
            return f"执行失败: {e.output}"

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
