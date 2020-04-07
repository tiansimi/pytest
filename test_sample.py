__author__ = 'TQ'
'''
pytest用例规则：
测试文件以test_开头（以_test结尾也可以）
测试类以Test开头，并且不能带有 init 方法
测试函数以test_开头
断言使用assert
'''
# content of test_sample.py
import pytest


def func(x):
    return x + 1


def test_answer():
    assert func(3) == 4


# 当用例多的时候写一个测试类ui
class Testclass():
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")  # hasattr() 函数用于判断对象是否包含对应的属性








