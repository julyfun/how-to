#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Hello World 程序
一个简单的 Python 程序，用于输出问候信息
"""

def main():
    """主函数"""
    print("Hello, World!")
    print("你好，世界！")
    
    # 添加一些额外的信息
    name = input("请输入你的名字: ")
    if name:
        print(f"很高兴认识你, {name}!")
    else:
        print("很高兴认识你，匿名朋友!")

if __name__ == "__main__":
    main()