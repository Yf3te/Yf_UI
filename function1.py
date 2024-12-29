import sys
import subprocess
import re
import time
import os
import socket
from urllib.parse import urlparse


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