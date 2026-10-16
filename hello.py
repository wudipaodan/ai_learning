# -*- coding: utf-8 -*-
"""我的第一个文件：验证 PyCharm + Git 环境是否打通。"""

print("Hello, GitHub!")

# 检查当前用的是哪个 Python（应该是项目里的 .venv）
import sys
print(f"当前 Python: {sys.version.split()[0]}")
print(f"解释器路径: {sys.executable}")

# 练习：用 Python 判断回文（复习之前学过的）
def is_palindrome(text: str) -> bool:
    """判断字符串是否为回文（两边对称）。"""
    return text == text[::-1]


if __name__ == "__main__":
    for s in ["黄山落叶松叶落山黄", "上海自来水来自海上", "你好世界"]:
        # 注意：Windows 控制台默认是 GBK 编码，输出 emoji（✅❌）会报 UnicodeEncodeError，
        # 所以这里只用中文，不用 emoji。
        result = "是回文" if is_palindrome(s) else "不是回文"
        print(f"「{s}」{result}")
