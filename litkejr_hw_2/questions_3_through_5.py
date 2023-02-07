"""
Jude Moore
Class: CS 677
Date: 11/15/2022
Homework Problems: 3-5
Description:
    3) Use ensemble learning to predict returns in years 4 and 5.
    4) Find the TP, FP, TN, FN, TPR, and TNR of each prediction type.
    5) Plot the returns from each prediction type on a graph along with the
        results of a buy-and-hold strategy.
"""
from tabulate import tabulate
import matplotlib.pyplot as plt


def ensemble_learning(dataframe, year_df):
    """
    This function takes the columns 'W=2', 'W=3', and 'W=4' and based on if
    there are more '+' or '-' between the three, it will add a '+' or '-' to the
    'Ensemble' column
    :param dataframe: A pandas dataframe. The dataframe to filter through
    :param year_df: The year before the year to filter through
    :return: No return, it just adds a value to the 'Ensemble'
    """
    ensemble_list = []  # empty list to store data
    for index in range(len(dataframe)):
        # Iterate through dataframe at specific year:
        if dataframe.loc[index, 'Year'] > year_df:
            # Add column values to ensemble_list:
            ensemble_list.append(dataframe.loc[index, "W=2"])
            ensemble_list.append(dataframe.loc[index, "W=3"])
            ensemble_list.append(dataframe.loc[index, "W=4"])

        # Calculate amount of ensemble_list positives and negatives:
        positive_counts = ensemble_list.count('+')
        negative_counts = ensemble_list.count('-')

        # Calculate if there are more negatives or positives and add to column:
        if negative_counts > positive_counts:
            dataframe.at[index, 'Ensemble'] = '-'
        else:
            dataframe.at[index, 'Ensemble'] = '+'

        # Clear the ensemble_list for the next iteration:
        ensemble_list.clear()


def ensemble_accuracy(dataframe, year_df, name_df):
    """
    This function determines the accuracy of the ensemble_learning function
    results and prints it out into a table
    :param dataframe: A pandas dataframe. The dataframe to filter through
    :param year_df: An integer. The year before the year to filter through
    :param name_df: A string. The name of the dataframe
    :return: No return, it prints out a table based on the accuracy of the
    ensemble method
    """
    # Initialize integers to add to based on accuracy:
    ensemble_accurate = 0
    ensemble_inaccurate = 0

    for index in range(len(dataframe) - 1):
        # Iterate through dataframe at specific year:
        if dataframe.loc[index, 'Year'] > year_df:
            # If column "Ensemble" was accurate, add to the correct number:
            if dataframe.loc[index + 1, "True_Label"] == \
                    dataframe.loc[index, "Ensemble"]:
                ensemble_accurate += 1
            else:
                ensemble_inaccurate += 1

    # Make a list of lists of the data gathered:
    table_list = [[' ', 'Ensemble'], ['Accurate', ensemble_accurate],
                  ['Inaccurate', ensemble_inaccurate],
                  ['Percent Accurate',
                   ensemble_accurate / (
                           ensemble_inaccurate + ensemble_accurate)]]

    # Print out the data as a table:
    print('\nProbability of ' + name_df + ' Based on Ensemble:')
    print(tabulate(table_list))


def calculate_statistics(dataframe, year_df, column_name):
    """
    Calculate the accuracy of the given column_name column predictions and
    return as a list
    :param dataframe: The dataframe to filter through
    :param year_df: The year before the year to filter through
    :param column_name: The name of the column to determine accuracy
    :return: Returns a list of data with the true positive, the false positive,
    true negative, false negative, the accuracy of predictions, the
    true positive rate, and the true negative rate
    """
    # Initialize integers to keep track of accuracy:
    true_positive = 0
    false_positive = 0
    true_negative = 0
    false_negative = 0

    for index in range(len(dataframe) - 1):
        # Iterate through dataframe at specific year:
        if dataframe.loc[index, 'Year'] > year_df:
            # Figure out if the prediction was a TP, FP, TN, or FN:
            if dataframe.loc[index + 1, "True_Label"] == '+':
                if dataframe.loc[index, column_name] == '+':
                    true_positive += 1
                else:
                    false_negative += 1
            else:
                if dataframe.loc[index, column_name] == '+':
                    false_positive += 1
                else:
                    true_negative += 1

    # Add all the data to a list:
    data_list = [column_name, true_positive, false_positive, true_negative,
                 false_negative,
                 get_accuracy(true_positive, false_positive, true_negative,
                              false_negative),
                 true_positive_rate(true_positive, false_negative),
                 true_negative_rate(true_negative, false_positive)]

    return data_list  # return the list


def get_accuracy(true_positive, false_positive, true_negative, false_negative):
    """
    Takes the TP, FP, TN, and FN and calculates the accuracy by taking the
    TP and TN total and dividing it by the total of all
    :param true_positive: Prediction and True_Label is '+'
    :param false_positive: Prediction is '+' and True_Label is '-'
    :param true_negative: Prediction and True_Label is '-'
    :param false_negative: Prediction is '-' and True_Label is '+'
    :return: Returns the rate of accuracy as a decimal that can be interpreted
    as a percentage
    """
    total_amount = true_positive + false_positive + true_negative + \
                   false_negative
    accurate_percent = (true_positive + true_negative) / total_amount

    return accurate_percent


def true_positive_rate(true_positive, false_negative):
    """
    Calculates the true positive of the given TP and FN
    :param true_positive: Prediction and True_Label is '+'
    :param false_negative: Prediction is '-' and True_Label is '+'
    :return: The TPR or true positive rate
    """
    return true_positive / (true_positive + false_negative)


def true_negative_rate(true_negative, false_positive):
    """
    Calculates the true positive of the given TN and FP
    :param true_negative: Prediction and True_Label is '-'
    :param false_positive: Prediction is '+' and True_Label is '-'
    :return: The TNR or true negative rate
    """
    return true_negative / (true_negative + false_positive)


def get_statistics_table(dataframe, year_df, stock_name):
    """
    This function takes a dataframe, calculates the accuracy of the predictions
    for each type of prediction and prints it out in a table
    :param dataframe: The dataframe to filter through
    :param year_df: The year before the year to filter through
    :param stock_name: A string. The name of the dataframe
    :return: No return. Just prints out a table of the statistical data gathered
    """
    # Get all the data as lists:
    get_w2 = calculate_statistics(dataframe, year_df, 'W=2')
    get_w3 = calculate_statistics(dataframe, year_df, 'W=3')
    get_w4 = calculate_statistics(dataframe, year_df, 'W=4')
    get_ensemble = calculate_statistics(dataframe, year_df, 'Ensemble')

    # Put all the data gathered into a list of lists:
    table_data = [['Type', 'TP', 'FP', 'TN', 'FN', 'Accuracy',
                   'TPR', 'TNR'], get_w2, get_w3, get_w4, get_ensemble]

    # Print out the list of lists as a table:
    print("\n" + stock_name + " Statistics:")
    print(tabulate(table_data))


def calculate_stock(dataframe, year_df, column_name):
    """
    Calculate the stock returns given the dataframe and the column that is
    making the predictions
    :param dataframe: A pandas dataframe. The dataframe to filter through
    :param year_df: An integer. The year before the year to filter through
    :param column_name: The name of the column to use as the prediction for
    the return
    :return: The amount of money earned each day as a list
    """
    money_amount = []
    prediction_positives = []

    for index in range(len(dataframe) - 1):
        # Iterate through dataframe at specific year:
        if dataframe.loc[index, 'Year'] > year_df:
            # Depending on the prediction, append the correct return to the list
            if dataframe.loc[index, column_name] == '+':
                prediction_positives.append(
                    dataframe.loc[index + 1, 'Return'])
            else:
                prediction_positives.append(0.0)

    # For every return, calculate the amount of money over time starting at 100
    for a_return in range(len(prediction_positives)):
        if a_return == 0:  # If this is the first return ($100)
            money_amount.append(100 * (1 + prediction_positives[a_return]))
        else:
            money_amount.append(money_amount
                                [a_return - 1] *
                                (1 + prediction_positives[a_return]))

    return money_amount


def buy_and_hold(dataframe, year_df):
    """
    Calculate the returns with the given dataframe if the strategy is to
    "buy and hold"
    :param dataframe: A pandas dataframe. The dataframe to filter through
    :param year_df: An integer. The year before the year to filter through
    :return: The amount of money earned each day as a list
    """
    money_amount = []
    prediction_positives = []

    for index in range(len(dataframe) - 1):
        # Iterate through dataframe at specific year and add all returns to list
        if dataframe.loc[index, 'Year'] > year_df:
            prediction_positives.append(dataframe.loc[index + 1, 'Return'])

    # For every return, calculate the amount of money over time starting at 100
    for a_return in range(len(prediction_positives)):
        if a_return == 0:  # If this is the first return ($100)
            money_amount.append(100 * (1 + prediction_positives[a_return]))
        else:
            money_amount.append(money_amount
                                [a_return - 1] *
                                (1 + prediction_positives[a_return]))

    return money_amount


def plot_data(w2_list, w3_list, w4_list, ensemble_list, bh_list, name):
    """
    Takes lists of returns data and plots it on a line graph
    :param w2_list: List of returns if W=2 is the predictor
    :param w3_list: List of returns if W=3 is the predictor
    :param w4_list: List of returns if W=4 is the predictor
    :param ensemble_list: List of returns if Ensemble is the predictor
    :param bh_list: List of returns with buy and hold strategy
    :param name: A string. The name of the stock
    :return: No return. It just plots the data into a graph and saves the graph
    as a .png in the same folder as the program
    """

    # X-axis is the length of all the given lists (500 days):
    x_axis = [x for x in range(len(w2_list))]

    # Plot the graphs with x_axis days and the lists of returns:
    plt.figure()  # open new file
    plt.plot(x_axis, w2_list, label="W=2")
    plt.plot(x_axis, w3_list, label="W=3")
    plt.plot(x_axis, w4_list, label="W=4")
    plt.plot(x_axis, ensemble_list, label="Ensemble")
    plt.plot(x_axis, bh_list, label="Buy and Hold")
    plt.title(name + ": Money Earned vs. # of Trading Days")
    plt.xlabel('Trading Days')
    plt.ylabel('Money Earned')
    plt.legend()
    plt.grid()
    plt.savefig(name + "_graph.png")
    plt.clf()  # scrub the file for the next.
