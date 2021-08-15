import pytest
@pytest.fixture
def my_test():
    print("我是fixture，my_test")
    a = 1
    b = 2
    return a,b


def test_user(my_test):
    print("test_user_mytest",my_test)
    print("test_user_mytest",my_test)
    print("test_user....")

def test_user2(my_test):
    print("test_user_mytest",my_test)
    print("test_user_mytest",my_test)
    print("test_user....")



if __name__ == '__main__':
    pytest.main(['-vs',__file__])
