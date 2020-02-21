def second_great_low(list_of_number):
    sec_low = None
    sec_great = None
    list_of_number_set = set(list_of_number)
    sorted_list = sorted(list_of_number_set)
    if len(sorted_list) > 3:
        sec_low = sorted_list[1]
        sec_great = sorted_list[len(sorted_list) - 2]
    elif len(list_of_number) == 2:
        if list_of_number[0] < list_of_number[1]:
            sec_low = list_of_number[1]
            sec_great = list_of_number[0]
        else:
            sec_low = list_of_number[0]
            sec_great = list_of_number[1]
    elif len(sorted_list) == 2 and len(list_of_number) == 3:
        sec_low = list_of_number[1]
        sec_great = list_of_number[1]

    return sec_low, sec_great


if __name__ == '__main__':
    sec_l, sec_g = second_great_low([7, 7, 9])
    print("Output: {} {}".format(sec_l, sec_g))
