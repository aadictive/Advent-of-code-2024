"""
Method to check is an integer list is sorted in ascending order
Return False if there are duplicate integers
"""


def check_int_if_sorted_asc_no_dup(input):
    return all(input[i] < input[i + 1] for i in range(len(input) - 1))


"""
Method to check is an integer list is sorted in descending order
Return False if there are duplicate integers
"""


def check_int_if_sorted_desc_no_dup(input):
    return all(input[i] > input[i + 1] for i in range(len(input) - 1))


"""
Method to check is an integer list is sorted in ascending order
"""


def check_int_if_sorted_asc_incl_dup(input):
    return all(input[i] <= input[i + 1] for i in range(len(input) - 1))


"""
Method to check is an integer list is sorted in descending order
"""


def check_int_if_sorted_desc_incl_dup(input):
    return all(input[i] >= input[i + 1] for i in range(len(input) - 1))
