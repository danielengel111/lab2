import math


def median(list_of_values):
    """
    returns the median of a list of values
    :param list_of_values: the values to calculate the median
    :return: the median
    """
    sorted_list = sorted(list_of_values)
    center_index = int(len(list_of_values)/2) # round to int required because division always produces float

    # Median value depends on length on list
    if len(list_of_values)%2 == 0:
        result = (sorted_list[center_index] + sorted_list[center_index-1])/2
    else:
        # Now we need only 1 index for exact value
        result = sorted_list[center_index]
    return result


def mean(list_of_values):
    """
    returns the mean of a list of values
    :param list_of_values: the values to calculate the mean
    :return: the mean
    """
    return sum(list_of_values)/len(list_of_values)


def variance(list_of_values):
    """
    returns the variance of a list of values
    :param list_of_values: the values to calculate the variance
    :return: the variance
    """
    average = mean(list_of_values)
    squared_sum = sum([(x - average)**2 for x in list_of_values])
    return squared_sum/(len(list_of_values)-1)


def covariance(first_list_of_values, second_list_of_values):
    """
    calculates the covariance of two lists of values
    :param first_list_of_values: the first list of values
    :param second_list_of_values: the second list of values
    :return: the covariance
    """
    result = 0
    # Place your code here
    first_mean = mean(first_list_of_values)
    second_mean = mean(second_list_of_values)
    result = sum([(x - first_mean) * (y - second_mean) for x, y in zip(first_list_of_values, second_list_of_values)])
    result /= (len(first_list_of_values) - 1)
    return result


def correlation(first_list_of_values, second_list_of_values):
    """
    calculates the correlation of two lists of values
    :param first_list_of_values: the first list of values
    :param second_list_of_values: the second list of values
    :return: the correlation
    """
    result = 0
    # Place your code here
    first_standard_deviation = math.sqrt(variance(first_list_of_values))
    second_standard_deviation = math.sqrt(variance(second_list_of_values))
    result = covariance(first_list_of_values, second_list_of_values)
    result /= first_standard_deviation * second_standard_deviation
    return result

