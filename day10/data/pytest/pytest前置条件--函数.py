import pytest


def test_print():
    print("我是一个没有感情的测试函数，只是用我print，测其他的")


def test_output():
    print("我也是一个没有感情的测试函数，只是用我print，测其他的东西")


def setup_module():
    print("所有case执行之前执行setup_module")


def teardown_module():
    print("所有case执行之前执行teardown_module")


def setup_function():
    print("所有case执行之前执行setup_function")


def teardown_function():
    print("所有case执行之前执行teardown_function")


if __name__ == '__main__':
    pytest.main([__file__,'-s'])  # 运行当前文件里面所有用例,
    # -s表示详细模式，否则不会print我们在函数里面的内容，__file__代表的是当前这个py文件，也可以直接写当前这个python文件的名字