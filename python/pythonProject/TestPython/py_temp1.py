def test_pass():
    """
    empty block are required
    :return:
    """
    try:
        pass
    except Exception:
        pass

test_pass()


def testCompare(a, b, c):
    if a > b > c or c > b > a:
        print('{}, {}, {} is sorted'.format(a, b, c))
    else:
        print('{}, {}, {} is not sorted'.format(a, b, c))



testCompare(1, 2 ,3)
testCompare(2, 1, 3)