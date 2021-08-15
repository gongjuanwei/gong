import pytest


class TestCase:
    def setup_class(self):
        print("所有case执行之前执行setup_class")

    def teardown_class(self):
        print("所有case执行之后执行teardown_class")

    def setup_method(self):
        print("每条case执行之前执行setup_method")

    def teardown_method(self):
        print("每条case执行之后执行setup_method")

    def test_print(self):
        print("我是一个没有感情的测试函数，只是用我print，测其他的")

    def test_output(self):
        print("我也是一个没有感情的测试函数，只是用我print，测其他的东西")


if __name__ == '__main__':
    pytest.main(['-s', __file__])  # 运行当前文件里面所有用例,
    # -s表示详细模式，__file__代表的是当前这个py文件，也可以直接写当前这个python文件的名字
