from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import subprocess
import re
import time
import os
import socket
from urllib.parse import urlparse
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1104, 876)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 10, 120, 15))
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

        self.pushButton_8 = QtWidgets.QPushButton(Dialog)
        self.pushButton_8.setGeometry(QtCore.QRect(580, 350, 131, 41))
        self.pushButton_8.setObjectName("pushButton_8")

        self.textEdit_4 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_4.setGeometry(QtCore.QRect(40, 70, 251, 191))
        self.textEdit_4.setObjectName("textEdit_4")

        self.textEdit_5 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_5.setGeometry(QtCore.QRect(40, 580, 241, 261))
        self.textEdit_5.setObjectName("textEdit_5")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        #连接函数
        self.pushButton.clicked.connect(self.extractbah)
        self.pushButton_2.clicked.connect(self.call_icpsearch)
        self.pushButton_4.clicked.connect(self.generate_fofa_query)
        self.pushButton_5.clicked.connect(self.extract_ip)
        self.pushButton_6.clicked.connect(self.extract_domain)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "信息收集整理工具"))
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

        self.pushButton_8.setText(_translate("Dialog", "httpx导航"))
    def extractbah(self):
        # 获取 textBrowser_2 中的所有文本
        input_text = self.textBrowser_2.toPlainText()

        # 按行分割输入文本
        lines = input_text.splitlines()

        # 清空 textBrowser_2
        self.textBrowser_2.clear()

        # 定义正则表达式
        icp_pattern = r'\[icpCode\]: ([京津沪渝黑吉辽蒙冀晋陕宁甘青新藏川贵云粤桂琼苏浙皖鲁闽赣湘鄂豫][A-Z]?\d?-?[ICP备]*\d{4,10}号)'  # ICP码正则
        company_pattern = r'\[Unit\]: ([\u4e00-\u9fff]+(?:[\u4e00-\u9fff]+)*)'  # 公司名称正则
        url_pattern = r'www\.((?:\d{1,3}\.){3}\d{1,3}|[a-zA-Z0-9-]+\.[a-zA-Z]{2,})'
        # 用于存储去重后的ICP码和公司名称
        icp_codes = set()
        companies = set()
        urls = set()

        # 逐行处理
        for line in lines:
            # 查找 ICP 码
            icp_match = re.search(icp_pattern, line)
            if icp_match:
                icp_code = icp_match.group(1)  # 提取ICP码
                icp_codes.add(icp_code)  # 添加到 set 中，自动去重

            # 查找公司名称
            company_match = re.search(company_pattern, line)
            if company_match:
                company_name = company_match.group(1)  # 提取公司名称
                companies.add(company_name)  # 添加到 set 中，自动去重

            # 查找url
            urls_match = re.search(url_pattern, line)
            if urls_match:
                url = urls_match.group(1)
                urls.add(url)

        # 输出去重后的公司名称到 textBrowser_2
        # self.textBrowser_2.append(f"去重后的公司：")
        for company in companies:
            self.textBrowser_2.append(company)

        # 输出去重后的ICP码到 textBrowser_2
        # self.textBrowser_2.append(f"去重后的ICP码：")
        for icp_code in icp_codes:
            self.textBrowser_2.append(icp_code)

        for url in urls:
            self.textBrowser_3.append(url)

        # 分隔符，用于区分不同的输出
        # self.textBrowser_2.append('-' * 40)


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



    def generate_fofa_query(self):
        # 获取用户输入的数据，并去除空行和多余的换行符
        domain = [d.strip() for d in self.textBrowser_3.toPlainText().splitlines() if d.strip()]  # 去除空行并去掉两端空白
        org_name = [o.strip() for o in self.textEdit.toPlainText().splitlines() if o.strip()]
        icon_hash = [h.strip() for h in self.textEdit_2.toPlainText().splitlines() if h.strip()]

        # 构建查询语法
        domain_query = " || ".join([f'domain="{d}"' for d in domain]) if domain else ""
        cert_query = " || ".join([f'cert="{o}"' for o in org_name]) if org_name else ""
        icon_hash_query = " || ".join([f'icon_hash="{h}"' for h in icon_hash]) if icon_hash else ""

        # 合并查询条件，去除空的部分
        fofa_query_parts = filter(None, [domain_query, cert_query, icon_hash_query])
        fofa_query = " || ".join(fofa_query_parts)

        # 显示生成的 Fofa 查询语法
        self.textBrowser_4.setText(fofa_query)


    def extract_ip(self):
        """从 URL 列表中提取 IP 地址"""
        url_list = self.textEdit_5.toPlainText().splitlines()
        ip_list = set()

        # 获取复选框状态
        ip_with_protocol = self.checkBox.isChecked()  # IP 是否带协议
        ip_with_port = self.checkBox_2.isChecked()  # IP 是否带端口

        # 定义正则表达式来匹配 IP 地址
        ip_regex = re.compile(
            r'(?<!\w)(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(?!\w)'
        )

        for url in url_list:
            url = url.strip()
            if not url:
                continue

            # 使用正则表达式提取 IP 地址
            ip_matches = ip_regex.findall(url)

            # 如果匹配到 IP 地址
            for ip_address in ip_matches:
                ip_str = ip_address

                # 提取协议，如果没有协议则默认使用 http
                parsed_url = urlparse(url)
                protocol = parsed_url.scheme if parsed_url.scheme else 'http'

                # 如果勾选了协议选项，使用提取的协议
                if ip_with_protocol:
                    ip_str = f'{protocol}://{ip_str}'

                # 处理是否带端口
                if ip_with_port:
                    # 从 URL 中提取端口
                    port = parsed_url.port
                    if port:
                        ip_str = f'{ip_str}:{port}'  # 如果勾选了带端口，添加端口

                ip_list.add(ip_str)

        # 更新 IP 列表显示框
        self.textBrowser_5.setText('\n'.join(sorted(ip_list)))


    def extract_domain(self):
        """从 URL 列表中提取域名"""
        url_list = self.textEdit_5.toPlainText().splitlines()
        domain_list = set()

        # 获取复选框状态
        domain_with_protocol = self.checkBox_4.isChecked()  # 域名是否带协议
        domain_with_port = self.checkBox_3.isChecked()  # 域名是否带端口

        for url in url_list:
            url = url.strip()
            if not url:
                continue

            # 使用 urlparse 提取协议、域名和端口
            parsed_url = urlparse(url)

            # 获取域名，如果是 IP 地址则跳过
            domain = parsed_url.hostname
            if domain and not re.match(r'\d+\.\d+\.\d+\.\d+', domain):  # 排除 IP 地址
                domain_str = domain
                # 如果勾选了带协议，使用 URL 中实际的协议（http 或 https）
                if domain_with_protocol:
                    protocol = parsed_url.scheme if parsed_url.scheme else 'http'  # 默认使用 http
                    domain_str = f'{protocol}://{domain_str}'
                # 如果勾选了带端口，并且 URL 中有端口
                if domain_with_port and parsed_url.port:
                    domain_str = f'{domain_str}:{parsed_url.port}'

                domain_list.add(domain_str)

        # 更新 域名 列表显示框
        self.textBrowser_6.setText('\n'.join(sorted(domain_list)))


    def extract_cidr(self):
        """从 URL 列表中提取 C 段并统计出现次数，按出现次数从多到少排序"""
        url_list = self.textEdit_5.toPlainText().splitlines()
        cidr_count = {}  # 用于存储每个 C 段及其出现次数

        for url in url_list:
            url = url.strip()
            if not url:
                continue

            # 使用 urlparse 提取协议、主机名和端口
            parsed_url = urlparse(url)
            domain = parsed_url.hostname

            # 获取 IP 地址
            ip_address = None
            try:
                ip_address = socket.gethostbyname(domain)
            except socket.gaierror:
                pass  # 无法解析时忽略

            if ip_address:
                # 获取 C 段（IP 地址前缀）
                cidr = '.'.join(ip_address.split('.')[:3]) + '.0/24'  # 获取 C 段

                # 统计 C 段出现的次数
                if cidr in cidr_count:
                    cidr_count[cidr] += 1
                else:
                    cidr_count[cidr] = 1

        # 将 C 段及其出现次数按出现次数降序排序
        sorted_cidr = sorted(cidr_count.items(), key=lambda item: item[1], reverse=True)

        # 更新 C 段 列表显示框
        cidr_display = '\n'.join([f'{cidr} - {count} 次' for cidr, count in sorted_cidr])
        self.textBrowser_7.setText(cidr_display)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
