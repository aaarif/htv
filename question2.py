def mult_recursive(num):
    # num should be larger than 10
    count = 0
    if num > 10:
        ls_num = str(num)
        if len(ls_num) > 1:
            rs = int(ls_num[0]) * int(ls_num[1])
            count += 1
            if len(str(rs)) > 1:
                count += mult_recursive(rs)
    return count


if __name__ == '__main__':
    count = mult_recursive(39)
    print("Output: {}".format(count))
