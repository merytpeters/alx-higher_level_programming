#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == [] or my_list is None:
        return 0
    sum_products = 0
    sum_weights = 0
    weighted_avg = 0

    for score, weight in my_list:
        sum_products += score * weight
        sum_weights += weight
    weighted_avg = sum_products / sum_weights
    return (weighted_avg)
