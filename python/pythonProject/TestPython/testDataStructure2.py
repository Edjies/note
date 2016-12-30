def testDictIterator():
    d = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4
    }
    # 遍历字典key值
    for item in d:
        print(item)
        print(d[item])


testDictIterator()