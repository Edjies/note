import numpy as np


def test_1():
    # 获取元素的位置
    a = np.array([1, 2, 3, 4 , 5, 6])
    length = a.shape[0]
    if 12 in a:
        itemindex = np.argwhere(a==5)[0][0] - length
        print(itemindex)
    else:
        print(None)

    b = np.array([[1, 2, 3], [3, 4, 5], [4, 5, 6], [7,8, 9]])
    print(b.shape)
    print(b[1])

def test_2():
    # 获取最大和最小元素的位置并删除
    a = np.array([1, 2, 3, 4, 5, 6, 7])
    max = np.max(a)
    remove_index = [np.argmax(a), np.argmin(a)]
    print(remove_index)
    new_a = np.delete(a, remove_index)
    print(a)
    print(new_a)


def test_3():
    """
    :return:
    """
    a1 = np.array([1, 2, 3, 4])
    a2 = np.array([2, 4, 6, 8])
    print(abs((a2 - a1)/a2 * 100))




test_3()