def find_outlier(integers):
    count = []
    _count = []
    for i in integers:
        if i % 2 == 0:
            count.append(i)
        elif i % 2 != 0:
            _count.append(i)
    if len(count) < len(_count):
        for j in count:
            return j
    elif len(_count) < len(count):
        for j in _count:
            return j
print(find_outlier([1,0,0]))
