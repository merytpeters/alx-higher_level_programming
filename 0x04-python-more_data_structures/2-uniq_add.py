#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list == [] or my_list is None:
        return []
    seen_num = set()
    sum = 0
    for num in my_list:
        if num not in seen_num:
            sum += num
            seen_num.add(num)
    return (sum)
