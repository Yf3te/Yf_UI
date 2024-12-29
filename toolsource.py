#burpsuite
import subprocess
import sys
import  re
from subprocess import Popen, PIPE
import colorama
def run_burp(self):
    # VBS脚本的路径
    vbs_path = r'E:\yf\burp\BurpSuite2405\EN无窗口.VBS'
    script_dir = r'E:\yf\burp\BurpSuite2405'

    # 首先切换到指定目录，然后执行VBS脚本
    try:
        # 切换目录并执行脚本
        subprocess.run(f'cmd /c "cd /d {script_dir} && cscript {vbs_path}"', check=True, shell=True)
        print("脚本执行成功")
    except subprocess.CalledProcessError as e:
        print(f"脚本执行失败: {e}")

#密探
def run_mitan(self):
    # 目标目录和批处理文件路径
    target_dir = r'E:\yf\7-tools\6-综合工具\mitan\mitan1.17'
    batch_file = r'start.bat'
    # 切换到指定目录并执行批处理文件
    try:
        # 执行命令：先切换目录，再执行 start.bat
        subprocess.run(f'cmd /c "cd /d {target_dir} && {batch_file}"', check=True, shell=True)
        print("批处理文件执行成功")
    except subprocess.CalledProcessError as e:
        print(f"批处理文件执行失败: {e}")
#cs
def run_cs(self):
    # VBS脚本的路径
    vbs_path = r'E:\yf\7-tools\4-内网工具集\CobaltStrike4.8汉化版\CobaltStrike4.8汉化版\Client\Cobalt_Strike_CN.vbs'
    script_dir = r'E:\yf\7-tools\4-内网工具集\CobaltStrike4.8汉化版\CobaltStrike4.8汉化版\Client'

    # 首先切换到指定目录，然后执行VBS脚本
    try:
        # 切换目录并执行脚本
        subprocess.run(f'cmd /c "cd /d {script_dir} && cscript {vbs_path}"', check=True, shell=True)
        print("脚本执行成功")
    except subprocess.CalledProcessError as e:
        print(f"脚本执行失败: {e}")
#Tscanplus
def run_Tscanplus(self):
    # TscanPlus 可执行文件的路径
    exe_path = r'E:\yf\7-tools\6-综合工具\Tscanplus\TscanPlus_Win_Arm64.exe'

    # 运行程序
    try:
        subprocess.run([exe_path], check=True)
        print("TscanPlus 执行成功")
    except subprocess.CalledProcessError as e:
        print(f"TscanPlus 执行失败: {e}")
    except FileNotFoundError:
        print(f"文件未找到: {exe_path}")


#命令执行
def execute_command(self):
    # 获取输入框中的命令
    command = self.lineEdit.text()
    if command:
        # 将命令添加到历史列表中
        self.history.append(command)
        # 将命令添加到下拉框中
        self.comboBox.addItem(command)

        # 在这里你可以执行命令并捕获其输出
        print(f"执行命令: {command}")
    # 打印调试信息，确保命令是正确的
    print(f"Executing command: {command}")

    try:
        # 执行命令并捕获输出
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=False,  # 以二进制模式读取输出，后续手动解码
        )

        # 尝试解码输出为 UTF-8
        try:
            stdout = result.stdout.decode('utf-8')
        except UnicodeDecodeError:
            # 如果 UTF-8 解码失败，则尝试 GBK
            stdout = result.stdout.decode('gbk', errors='ignore')

        # 同样处理 stderr
        try:
            stderr = result.stderr.decode('utf-8')
        except UnicodeDecodeError:
            stderr = result.stderr.decode('gbk', errors='ignore')

        # 检查解码后的结果
        stdout = stdout or "无标准输出"
        stderr = stderr or "无错误输出"

        # 显示标准输出或错误信息
        if stdout.strip():  # 如果有标准输出
            self.textBrowser.setText(stdout)
        elif stderr.strip():  # 如果有错误输出
            self.textBrowser.setText(f"命令执行失败:\n{stderr}")
        else:  # 如果都为空
            self.textBrowser.setText("命令未返回任何信息。")

    except subprocess.CalledProcessError as e:
        # 如果命令执行失败，显示错误信息
        print(f"Command failed with error: {e.stderr}")
        self.textBrowser.setText(f"命令执行失败: {e.stderr}")

    except Exception as e:
        # 捕获其他异常并显示
        print(f"Unexpected error: {str(e)}")
        self.textBrowser.setText(f"发生错误: {str(e)}")

#刷新
def refresh_output(self):
    # 刷新输出框，清空内容
    self.textBrowser.clear()

#oneforall
def oneforall_command(self):
    # 填写 oneforall 的帮助命令到输入框
    command = r'python E:\yf\7-tools\1-信息收集\OneForAll\oneforall.py'
    self.lineEdit.setText(command)

    try:
        # 执行命令
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)

        # 将 ANSI 转义字符转换为 HTML 格式
        clean_output = self.ansi_to_html(result.stdout)

        # 显示命令的标准输出
        self.textBrowser.setText(clean_output)

    except subprocess.CalledProcessError as e:
        # 如果命令执行失败，显示错误信息
        print(f"Command failed with error: {e.stderr}")
        self.textBrowser.setText(f"命令执行失败: {e.stderr}")

    except Exception as e:
        # 捕获其他异常并显示
        print(f"Unexpected error: {str(e)}")
        self.textBrowser.setText(f"发生错误: {str(e)}")


#fuff
def fuff_command(self):
    command = r'E:\yf\7-tools\3-常用工具集\FUZZ\ffuf-main\ffuf_2.1.0_windows_amd64\ffuf.exe -h'
    self.lineEdit.setText(command)

    # 执行命令并显示输出
    try:
        # 执行命令
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)

        # 显示命令的标准输出
        self.textBrowser.setText(result.stdout)

    except subprocess.CalledProcessError as e:
        # 如果命令执行失败，显示错误信息
        print(f"Command failed with error: {e.stderr}")
        self.textBrowser.setText(f"命令执行失败: {e.stderr}")

    except Exception as e:
        # 捕获其他异常并显示
        print(f"Unexpected error: {str(e)}")
        self.textBrowser.setText(f"发生错误: {str(e)}")
#ehole魔改
#httpx
def httpx_command(self):
    command = r'E:\yf\7-tools\3-常用工具集\指纹^&测活\httpx\httpx.exe -h'
    self.lineEdit.setText(command)

    # 执行命令并显示输出
    try:
        # 执行命令
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)

        # 显示命令的标准输出
        self.textBrowser.setText(result.stdout)

    except subprocess.CalledProcessError as e:
        # 如果命令执行失败，显示错误信息
        print(f"Command failed with error: {e.stderr}")
        self.textBrowser.setText(f"命令执行失败: {e.stderr}")

    except Exception as e:
        # 捕获其他异常并显示
        print(f"Unexpected error: {str(e)}")
        self.textBrowser.setText(f"发生错误: {str(e)}")
#fscan
def fscan_command(self):
    command = r'E:\yf\7-tools\4-内网工具集\fscan\fscan.exe -h'
    self.lineEdit.setText(command)

    # 执行命令并显示输出
    try:
        # 执行命令并捕获输出
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=False,  # 以二进制模式读取输出，后续手动解码
        )

        # 尝试解码输出为 UTF-8
        try:
            stdout = result.stdout.decode('utf-8')
        except UnicodeDecodeError:
            # 如果 UTF-8 解码失败，则尝试 GBK
            stdout = result.stdout.decode('gbk', errors='ignore')

        # 同样处理 stderr
        try:
            stderr = result.stderr.decode('utf-8')
        except UnicodeDecodeError:
            stderr = result.stderr.decode('gbk', errors='ignore')

        # 检查解码后的结果
        stdout = stdout or "无标准输出"
        stderr = stderr or "无错误输出"

        # 显示标准输出或错误信息
        if stdout.strip():  # 如果有标准输出
            self.textBrowser.setText(stdout)
        elif stderr.strip():  # 如果有错误输出
            self.textBrowser.setText(f"命令执行失败:\n{stderr}")
        else:  # 如果都为空
            self.textBrowser.setText("命令未返回任何信息。")

    except subprocess.CalledProcessError as e:
        # 如果命令执行失败，显示错误信息
        print(f"Command failed with error: {e.stderr}")
        self.textBrowser.setText(f"命令执行失败: {e.stderr}")

    except Exception as e:
        # 捕获其他异常并显示
        print(f"Unexpected error: {str(e)}")
        self.textBrowser.setText(f"发生错误: {str(e)}")
#host碰撞
def hostp_command(self):
    # 定义命令
    command = r'java -jar E:\yf\7-tools\1-信息收集\HostCollision-2.2.9\HostCollision.jar -h'

    # 将命令显示在输入框中
    self.lineEdit.setText(command)

    try:
        # 执行命令并捕获输出
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=False,  # 以二进制模式读取输出，后续手动解码
        )

        # 尝试解码输出为 UTF-8
        try:
            stdout = result.stdout.decode('utf-8')
        except UnicodeDecodeError:
            # 如果 UTF-8 解码失败，则尝试 GBK
            stdout = result.stdout.decode('gbk', errors='ignore')

        # 同样处理 stderr
        try:
            stderr = result.stderr.decode('utf-8')
        except UnicodeDecodeError:
            stderr = result.stderr.decode('gbk', errors='ignore')

        # 检查解码后的结果
        stdout = stdout or "无标准输出"
        stderr = stderr or "无错误输出"

        # 显示标准输出或错误信息
        if stdout.strip():  # 如果有标准输出
            self.textBrowser.setText(stdout)
        elif stderr.strip():  # 如果有错误输出
            self.textBrowser.setText(f"命令执行失败:\n{stderr}")
        else:  # 如果都为空
            self.textBrowser.setText("命令未返回任何信息。")

    except subprocess.CalledProcessError as e:
        # 如果命令执行失败，显示错误信息
        print(f"Command failed with error: {e.stderr}")
        self.textBrowser.setText(f"命令执行失败: {e.stderr}")

    except Exception as e:
        # 捕获其他异常并显示
        print(f"Unexpected error: {str(e)}")
        self.textBrowser.setText(f"发生错误: {str(e)}")
#sqlmap
def sqlmap_command(self):
    # 定义命令
    command = r'python E:\yf\7-tools\2-基础漏洞利用工具\sql\sqlmap-master\sqlmap.py -h'
    command1 = r'原因未知，sqlmap程序无法执行，请移步自身工具cmd执行'
    # 将命令显示在输入框中
    self.lineEdit.setText(command)
    self.textBrowser.setText(command1)

#API探测(1)


def api_command(self):
    # 定义要进入的目录和要执行的 Python 命令
    cd_command = r'cd E:\yf\7-tools\5-API测试\API路径提取（自写）'
    python_command = r'python 网站API提取.py'

    # 合并命令：先 `cd` 再执行 Python 脚本
    full_command = f'{cd_command} && {python_command}'

    # 将命令显示在输入框中
    self.lineEdit.setText(full_command)

    try:
        # 执行命令并捕获输出
        result = subprocess.run(
            full_command,
            shell=True,
            capture_output=True,
            text=False,  # 以二进制模式读取输出，后续手动解码
        )

        # 尝试解码输出为 UTF-8
        try:
            stdout = result.stdout.decode('utf-8')
        except UnicodeDecodeError:
            # 如果 UTF-8 解码失败，则尝试 GBK
            stdout = result.stdout.decode('gbk', errors='ignore')

        # 同样处理 stderr
        try:
            stderr = result.stderr.decode('utf-8')
        except UnicodeDecodeError:
            stderr = result.stderr.decode('gbk', errors='ignore')

        # 检查解码后的结果
        stdout = stdout or "无标准输出"
        stderr = stderr or "无错误输出"

        # 显示标准输出或错误信息
        if stdout.strip():  # 如果有标准输出
            self.textBrowser.setText(stdout)
        elif stderr.strip():  # 如果有错误输出
            self.textBrowser.setText(f"命令执行失败:\n{stderr}")
        else:  # 如果都为空
            self.textBrowser.setText("命令未返回任何信息。")

    except subprocess.CalledProcessError as e:
        # 如果命令执行失败，显示错误信息
        print(f"Command failed with error: {e.stderr}")
        self.textBrowser.setText(f"命令执行失败: {e.stderr}")

    except Exception as e:
        # 捕获其他异常并显示
        print(f"Unexpected error: {str(e)}")
        self.textBrowser.setText(f"发生错误: {str(e)}")


#api文件夹
#packerfuzz
def packerfuzzer_command(self):
    # 定义命令
    command = r'python E:\yf\7-tools\5-API测试\Packer-Fuzzer-1.4\Packer-Fuzzer-1.4\PackerFuzzer.py -h'

    # 将命令显示在输入框中
    self.lineEdit.setText(command)

    try:
        # 执行命令，显式指定编码为 utf-8
        result = subprocess.run(command, shell=True, capture_output=True, text=True, encoding='utf-8')

        # 将输出结果显示到输出框中
        if result.stdout:
            self.textBrowser.setPlainText(result.stdout)
        elif result.stderr:
            self.textBrowser.setPlainText(result.stderr)
    except Exception as e:
        # 如果执行失败，显示错误信息
        self.textBrowser.setPlainText(f"Error: {str(e)}")
#jjjjjjs
def jjjjjjjs_command(self):
    # 定义命令
    command = r'python E:\yf\7-tools\5-API测试\jjjjjjjjjjjjjs\jjjjjjjjjjjjjs.py'

    # 将命令显示在输入框中
    self.lineEdit.setText(command)

    try:
        # 执行命令，显式指定编码为 utf-8
        result = subprocess.run(command, shell=True, capture_output=True, text=True, encoding='utf-8')

        # 将输出结果显示到输出框中
        if result.stdout:
            self.textBrowser.setPlainText(result.stdout)
        elif result.stderr:
            self.textBrowser.setPlainText(result.stderr)
    except Exception as e:
        # 如果执行失败，显示错误信息
        self.textBrowser.setPlainText(f"Error: {str(e)}")
#goby
#nuclei