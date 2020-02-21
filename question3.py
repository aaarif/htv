def meanmode(array_num):
    is_equal = 0
    mode = None
    mean = sum(array_num) / len(array_num)
    # print("Mean adalah: {}".format(mean))
    count_ls = []
    ls = []
    for i, n in enumerate(array_num):
        count = 0
        for g in array_num:
            if n == g:
                count += 1
        count_ls.append({i: count})
        ls.append(count)
    maxx = max(ls)
    index = None
    for ind, a in enumerate(count_ls):
        if a[ind] == maxx:
            index = ind
            break
    mode = array_num[index]
    # print("MOde adalah: {}".format(mode))
    if mode == mean:
        is_equal = 1
    return is_equal


if __name__ == '__main__':
    is_equal = meanmode([5, 3, 3, 3, 1])
    print("Output: {}".format(is_equal))
