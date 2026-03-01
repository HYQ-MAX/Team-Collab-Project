# standalone_test.py
# 独立的测试文件，包含所有函数定义

# 数学工具函数
def sum_two(a, b):
    """计算两个数的和"""
    return a + b

def find_max(numbers):
    """找到列表中的最大值"""
    if not numbers:
        raise ValueError("列表不能为空")
    return max(numbers)

def multiply(a, b):
    """计算两个数的乘积"""
    return a * b

def is_even(number):
    """判断数字是否为偶数"""
    return number % 2 == 0

# 测试函数
def test_sum():
    """测试求和函数"""
    assert sum_two(1, 2) == 3
    assert sum_two(-1, 5) == 4
    print("求和函数测试通过！")

def test_max():
    """测试求最大值函数"""
    assert find_max([1, 3, 2]) == 3
    assert find_max([-5, 0, -10]) == 0
    print("最大值函数测试通过！")

def test_multiply():
    """测试乘法函数"""
    assert multiply(3, 4) == 12
    assert multiply(-2, 5) == -10
    print("乘法函数测试通过！")

def test_is_even():
    """测试偶数判断函数"""
    assert is_even(4) == True
    assert is_even(7) == False
    assert is_even(0) == True
    print("偶数判断函数测试通过！")

if __name__ == "__main__":
    print("开始运行所有测试...")
    test_sum()
    test_max()
    test_multiply()
    test_is_even()
    print("所有测试通过！🎉")
