"""
Jude Moore
Class: CS 677
Date: 11/9/2022
Homework Problems: 4 through 6
Description:
    4. With an "oracle" calculate only the positive returns and the money earned
    in the MCD and SPY stocks.
    5. Consider a buy-and-hold strategy instead of listening to the "oracle"
    6(a). The "oracle" gives wrong results for 10 best return days.
    6(b). The "oracle" gives wrong results for 10 worst return days.
    6(c). The "oracle" gives wrong results for 5 best AND 5 worst return days.
"""
import copy
from questions_1_through_3 import get_positive_returns


def get_returns_list(a_data_file):
    """
    Takes the csv file data in a list of lists and pulls out all the data in the
    'returns' column.
    :param a_data_file: A list of lists of csv data.
    :return: A list of only the returns data: returns_list
    """
    returns_list = []
    for i in range(len(a_data_file)):
        returns_list.append(a_data_file[i][13])

    # get rid of first value in the list (0.0)
    returns_list.pop(0)

    # turn into list of floats
    returns_list = [eval(i) for i in returns_list]
    return returns_list


def trade_stock_only_positive(a_data_list):
    """
    Takes a csv data list and filters through it to find only the positive
    returns. Calculates how much the person would earn in that stock if only
    positive days were realized starting out at $100. (Question 4)
    :param a_data_list: Stock data list from csv files.
    :return: Does not return anything. Only runs other functions to print to
    console.
    """
    returns_list = get_returns_list(a_data_list)

    # Pulls out only the positive returns.
    returns_list = get_positive_returns(returns_list)

    # Calculate the amount of money via returns over time.
    calculate_stock(returns_list)


def buy_and_hold(a_data_list):
    """
    Takes a csv data list and calculates how much the person would earn in that
    stock if all days were realized starting out at $100. (Question 4)
    :param a_data_list: Stock data list from csv files.
    :return: Does not return anything, only prints data to console.
    """
    returns_list = get_returns_list(a_data_list)

    # Calculate the amount of money via returns over time.
    calculate_stock(returns_list)


def loss_best_days(a_data_list, remove_number):
    """
    Calculates a list of returns with the number of the best returns lost.
    :param a_data_list: Stock data list from csv files.
    :param remove_number: Number of best returns to remove
    :return: A list of returns with (remove_number) of the best returns removed.
    """
    returns_list = get_returns_list(a_data_list)
    deepcopy_returns_list = copy.deepcopy(returns_list)

    # Sort the list:
    returns_list.sort()

    minus_best_returns = []

    # Get all the positive results minus the number to remove:
    results = returns_list[: len(returns_list) - remove_number]

    # Sort in sequential order:
    for element in deepcopy_returns_list:
        if element in results:
            minus_best_returns.append(element)

    # Get only positive returns:
    only_positive_returns = get_positive_returns(minus_best_returns)
    return only_positive_returns


def get_ten_worst_days(a_data_list):
    """
    A function that filters through the csv file data and pulls out all the
    positive returns plus the ten worst days.
    :param a_data_list: Csv file data as lists within a list.
    :return: Returns a list of all the positive returns along with the 10 worst
    days.
    """
    # Gather the data:
    returns_list = get_returns_list(a_data_list)

    # Make a deepcopy of the returns list (unchanging).
    deepcopy_returns_list = copy.deepcopy(returns_list)

    # Sort the list to get the worst returns at the beginning:
    returns_list.sort()

    plus_worst_returns = []

    # Get the first 10 worst returns
    first_ten = returns_list[0:10]
    # Get all the positive returns from the list:
    new_list = get_positive_returns(returns_list)

    # Put the 10 worst and all the positive returns into one list:
    for element in first_ten:
        new_list.append(element)

    # Put it all into sequential order:
    for element in deepcopy_returns_list:
        if element in new_list:
            plus_worst_returns.append(element)

    return plus_worst_returns


def calculate_stock(a_data_list):
    """
    A function that takes a list of returns data in sequential order and
    finds out how much would be made over time starting at $100
    :param a_data_list: A list of returns.
    :return: Does not return anything, only prints the final amount on console.
    """
    money_amount = []

    for a_return in range(len(a_data_list)):
        if a_return == 0:  # If this is the first return ($100)
            money_amount.append(100 * (1 + a_data_list[a_return]))
        else:
            money_amount.append(money_amount
                                [a_return - 1] * (1 + a_data_list[a_return]))
    print(money_amount[-1])


def get_worst_best_results(a_data_list):
    """
    This function takes a list of positive returns minus good returns, and
    adds the five worst returns to it and returns that list.
    :param a_data_list: The csv data list.
    :return: A list with the five worst returns added to the list in sequential
    order.
    """
    # Gather the data:
    returns_list = get_returns_list(a_data_list)

    # Make a deepcopy of the list (unchanging)
    deepcopy_returns_list = copy.deepcopy(returns_list)

    # Sort the list to get the worst returns at the beginning:
    returns_list.sort()

    plus_worst_returns = []

    # Get the 5 worst returns (for question 6c)
    worst_five = returns_list[0:5]

    # Get all the positive returns:
    new_returns_list = get_positive_returns(returns_list)

    # Get the 5 best returns (for question 6c)
    best_five = returns_list[-5:]

    # Remove the five best from the positive list of returns:
    for element in new_returns_list:
        if element in best_five:
            new_returns_list.remove(element)

    # Add the five worst to the positive list of returns:
    for element in worst_five:
        new_returns_list.append(element)

    # Sort in sequential order:
    for element in deepcopy_returns_list:
        if element in new_returns_list:
            plus_worst_returns.append(element)

    return plus_worst_returns
