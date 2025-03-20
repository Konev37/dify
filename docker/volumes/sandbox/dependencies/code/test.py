import ctypes
import json
import os
import sys
import traceback


# setup sys.excepthook
def excepthook(type, value, tb):
    sys.stderr.write("".join(traceback.format_exception(type, value, tb)))
    sys.stderr.flush()
    sys.exit(-1)


sys.excepthook = excepthook

lib = ctypes.CDLL("/var/sandbox/sandbox-python/python.so")
print(lib)
lib.DifySeccomp.argtypes = [ctypes.c_uint32, ctypes.c_uint32, ctypes.c_bool]
lib.DifySeccomp.restype = None

os.chdir("/var/sandbox/sandbox-python")

lib.DifySeccomp(65537, 1001, 1)

# declare main function here
# 测试代码可以写在此处
# ------------------------------------
# sandbox不支持使用临时文件，只能纯内存操作
import json

import requests
from bs4 import BeautifulSoup
from typing import List
import re


def main() -> dict:
    contents = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Accept-Language': 'zh-CN,zh;q=0.9'
    }

    for url in urls:
        try:
            # 内存中完成所有操作（无临时文件）
            with requests.Session() as session:
                response = session.get(url, headers=headers, timeout=15)
                response.raise_for_status()

                # 自动检测编码
                if response.encoding is None:
                    response.encoding = 'utf-8'

                # 使用轻量级清洗策略
                soup = BeautifulSoup(response.text, 'html.parser')

                # 移除噪音标签
                for tag in soup(['script', 'style', 'noscript', 'meta', 'link', 'header', 'footer']):
                    tag.decompose()

                # 合并空白字符
                text = soup.get_text(separator='\n', strip=True)
                text = re.sub(r'\n{3,}', '\n\n', text)  # 压缩连续空行
                text = text[:2048]  # 强制限制前2048个字符
                contents.append(text)
                contents.append('<br><br>')
        except Exception as e:
            print(f"❌ 抓取失败: {url} | 错误类型: {type(e).__name__}")
            contents.append("")

    return {'result_details': json.dumps(contents, ensure_ascii=False)}  # 将列表包装为字典
# -------------------------------------


from base64 import b64decode
from json import dumps, loads

# execute main function, and return the result
# inputs is a dict, and it
inputs = b64decode("e30=").decode("utf-8")
output = main(**json.loads(inputs))

# convert output to json and print
output = dumps(output, indent=4)

result = f"""<<RESULT>>
{output}
<<RESULT>>"""

print(result)
