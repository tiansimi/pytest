__author__ = 'TQ'

import pytest


# 不带参数时默认scope="function"
@pytest.fixture()
def login():
    print("输入账号，密码先登录")


# 用例1需要登录
def test_s1(login):
    print("用例1：登录之后其它动作111")


# 用例2不需要登录
def test_s2():  # 不传login
    print("用例2：不需要登录，操作222")


# 用例3需要登录
def test_s3(login):
    print("用例3：登录之后其它动作333")


if __name__ == "__main__":
    pytest.main(["-q", "test_fix.py"])
