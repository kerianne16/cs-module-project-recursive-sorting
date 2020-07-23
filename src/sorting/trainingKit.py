my_list = [1, 2, 3, 4, 5]

'''
def sum_list(items):
    sum = 0
    for i in items:
        sum = sum + i
    return sum


print(sum_list(my_list))
'''


def sum_list(items):
    if len(items) == 1:  # base case, tells when to stop calling itself
        return items[0]
    else:
        return items[0] + sum_list(items[1:])


print(sum_list(my_list))
