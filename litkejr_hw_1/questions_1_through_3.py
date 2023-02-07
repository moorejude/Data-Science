"""
Jude Moore
Class: CS 677
Date: 11/9/2022
Homework Problems: 1 through 3
Description:
    1. Calculate the standard deviation, mean, negative returns, and
    non-negative returns, and put them into 5 tables based on year.
    2. (Please see PDF for these answers.)
    3. Calculate aggregate table across all five years in problem 1 for MCD
    and SPY.
"""
from read_stock_data_from_file import MCD_data_matrix


def pull_yearly_data(date_str, year_str, a_data_list):
    """
    This function reads data that has already been converted
    into lists within a list and pulls return data from the date and year
    specified.
    :param date_str: The name of the day ('Monday' through 'Friday') to pull
    data from.
    :param year_str: The year as a string from the csv file.
    :param a_data_list: A list of lists of the .csv data
    :return: Returns a list of floats of all the returns from the day and year
    with the given list provided.
    """
    date_list = []
    year_list = []
    average_list = []

    # dig through the lists within a list for the specified date string given
    for element in a_data_list:
        for data_point in element:
            if date_str in data_point:
                date_list.append(element)  # append data to a list

    # pull data from the previous list that has the specified year given
    for dates in date_list:
        if year_str in dates:
            year_list.append(dates)  # append data to a list.

    # pull only the 'returns' data
    for i in range(len(year_list)):
        average_list.append(year_list[i][13])

    return convert_to_float(average_list)  # return only the 'returns' data


def convert_to_float(a_list):
    """
    This function takes a list of strings and converts it into a
    list of floats.
    :param a_list: Takes a list of strings.
    :return: A list of floats.
    """
    a_list = [eval(i) for i in a_list]
    return a_list


def calculate_mean(a_list):
    """
    This function takes a list provided and calculates the mean of that list.
    :param a_list: A list of floats or integers.
    :return: The mean of the list.
    """
    the_mean = sum(a_list) / len(a_list)
    return the_mean


def standard_deviation(a_list, mean):
    """
    This function calculates the standard deviation of the provided list.
    :param a_list: A list of floats or integers.
    :param mean: The mean of the provided list.
    :return: returns the standard deviation calculated
    """
    squared_results = []

    # Subtract the mean from every element in the list (as absolute value):
    subtracted_list = [abs(x - mean) for x in a_list]

    # For every element in the list, square it with itself:
    for element in subtracted_list:
        square_numbers = element * element
        squared_results.append(square_numbers)

    # Calculate the variance by calculating the mean of the squared numbers
    variance = calculate_mean(squared_results)

    # get the square root of the variance, which will be the standard deviation
    the_standard_deviation = variance ** 0.5

    return the_standard_deviation


def get_negative_returns(a_list):
    """
    This function runs through a list and pulls out all the negative numbers
    in that list and returns a list with only the negative numbers.
    :param a_list: A list with negative and positive integers or floats.
    :return: A list with only negative numbers.
    """
    negative_returns = []

    for element in a_list:
        if element < 0:
            negative_returns.append(element)

    return negative_returns


def get_positive_returns(a_list):
    """
    This function runs through a list and pulls all the positive numbers in that
    list and returns a list with only the positive numbers.
    :param a_list: A list with negative and positive integers or floats.
    :return: A list with only positive numbers.
    """
    positive_returns = []

    for element in a_list:
        if element >= 0:
            positive_returns.append(element)

    return positive_returns


def print_yearly_table(year):
    """
    This function prints out data in a table using the other functions in this
    file for easy reading.
    :param year: Takes a year that the data will focus on.
    :return: No return, just prints the data in tables for the user to read.
    """
    day_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    table_list = [['Day:', 'Mean:', 'Standard Deviation:', 'Negative Days:',
                   'Mean of Negative Days:', 'SD of Negative Days:',
                   'Positive Days:', 'Mean of Positive Days:',
                   'SD of Positive Days:']]

    # Makes lists within a list for each day of the year provided.
    for day in range(len(day_list)):
        # Uses the functions above to get the list, mean, and standard dev.
        get_list = pull_yearly_data(day_list[day], year, MCD_data_matrix)
        get_mean = calculate_mean(get_list)
        get_deviation = standard_deviation(get_list, get_mean)

        # Uses the functions above to get all the negative and positive days
        get_negative_days = get_negative_returns(get_list)
        negative_mean = calculate_mean(get_negative_days)
        get_positive_days = get_positive_returns(get_list)
        positive_mean = calculate_mean(get_positive_days)

        # Appends them into a list to print out as a table:
        table_list.append(
            [day_list[day], get_mean, get_deviation, len(get_negative_days),
             negative_mean,
             standard_deviation(get_negative_days, negative_mean),
             len(get_positive_days), positive_mean,
             standard_deviation(get_positive_days, positive_mean)])

    # prints in rows:
    print(*table_list, sep="\n")


def aggregate_data(date_str, a_data_list):
    """
    This function instead of pulling both date and year data like the function
    "pull_yearly_data" above, it takes a look at all data on a specific date
    and not the year.
    :param date_str: A string of the day ('Monday' through 'Friday')
    :param a_data_list: The lists within a list to pull data from, from csv file
    :return: A list with all the returns from that specific day.
    """
    date_list = []
    average_list = []

    # For every list within a list, append to new list if date string matches
    for element in a_data_list:
        for data_point in element:
            if date_str in data_point:
                date_list.append(element)

    # Pull only the returns from the list.
    for i in range(len(date_list)):
        average_list.append(date_list[i][13])

    # Return the list of returns for those days as a float.
    return convert_to_float(average_list)


def print_aggregate_table(data_list):
    """
    Similar to the "print_yearly_data" function above, this function formulates
    and prints a table of aggregate data from the data_list provided for the
    user to see.
    :param data_list: The data list to gather data from and put into a list.
    (From CSV file.)
    :return: Does not return anything, just prints out the table.
    """
    day_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    table_list = [['Day:', 'Mean:', 'Standard Deviation:', 'Negative Days:',
                   'Mean of Negative Days:', 'SD of Negative Days:',
                   'Positive Days:', 'Mean of Positive Days:',
                   'SD of Positive Days:']]

    for day in range(len(day_list)):
        # Uses the functions above to get the list, mean, and standard dev.
        get_list = aggregate_data(day_list[day], data_list)
        get_mean = calculate_mean(get_list)
        get_deviation = standard_deviation(get_list, get_mean)

        # Uses the functions above to get all the negative and positive days
        get_negative_days = get_negative_returns(get_list)
        negative_mean = calculate_mean(get_negative_days)
        get_positive_days = get_positive_returns(get_list)
        positive_mean = calculate_mean(get_positive_days)

        # Appends them into a list to print out as a table:
        table_list.append(
            [day_list[day], get_mean, get_deviation, len(get_negative_days),
             negative_mean,
             standard_deviation(get_negative_days, negative_mean),
             len(get_positive_days), positive_mean,
             standard_deviation(get_positive_days, positive_mean)])

    # prints in rows:
    print(*table_list, sep="\n")
