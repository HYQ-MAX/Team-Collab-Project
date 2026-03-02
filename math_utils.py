#!/usr/bin/env python3
# coding:utf-8
# author:
# datetime:2026/3/2 15:58
# software: PyCharm
# Explanation:
# math_utils.py
# math_utils.py（补充后）
def sum_two(a, b):
    """
    两数求和函数
    :param a: 数字1（int/float）
    :param b: 数字2（int/float）
    :return: 两数之和
    :raises TypeError: 若参数非数字类型则抛出异常
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("参数必须为整数或浮点数")
    return a + b

def find_max(num_list):
    """
    求列表最大值函数
    :param num_list: 数字列表（元素为int/float）
    :return: 列表中的最大值
    :raises ValueError: 若列表为空；TypeError: 若列表含非数字元素
    """
    if not num_list:
        raise ValueError("列表不能为空")
    for num in num_list:
        if not isinstance(num, (int, float)):
            raise TypeError("列表元素必须为整数或浮点数")
    return max(num_list)