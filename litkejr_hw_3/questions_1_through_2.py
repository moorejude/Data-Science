"""
Jude Moore
Class: CS 677
Date: 11/22/2022
Homework Problems: 1-2
Description:
    1. For each class and each feature, compute the standard deviation and
        the mean and print them out in a table.
    2. Split the dataset into training and testing, plot good bills and bad
        bills to pdf's using pairplot, and come up with simple classifiers
        to predict the bills and display it in a table.
"""
from matplotlib import pyplot as plt
from tabulate import tabulate
import seaborn as sns


def get_color_label(row):
    """
    This function determines the Color Label of the dataframe row given, and
    returns it to be placed into "Color_Label" column
    :param row: A row in a dataframe
    :return: The Color Label of the row
    """
    if row['True_Label'] == 0:
        return "green"
    else:
        return "red"


def calculate_mean(dataframe, column_name):
    """
    Calculates the mean of a specific column in a dataframe
    :param dataframe: The dataframe
    :param column_name: The column within the dataframe to calculate the
    mean of the column
    :return: The mean of the column in the given dataframe rounded to 2
    decimal places.
    """
    return round(dataframe[column_name].mean(), 2)


def standard_deviation(dataframe, column_name):
    """
    Calculates the standard deviation of a specific column in a dataframe
    :param dataframe: The dataframe
    :param column_name: The column within the dataframe to calculate the
    standard deviation of the column
    :return: The standard deviation of the column in the given dataframe
    rounded to 2 decimal places.
    """
    return round(dataframe[column_name].std(), 2)


def create_class_table(dataframe):
    """
    This function prints out a table to the Python console with the calculated
    standard deviation and mean for features F1, F2, F3, and F4 in the given
    dataframe
    :param dataframe: The dataframe to calculate mean and standard deviation
    of features and classes
    :return: There is no return, just outputs the table to the Python console
    """

    # Separate the dataframes into classes (good and bad):
    green_df = dataframe.loc[(dataframe['True_Label'] == 0)]
    red_df = dataframe.loc[(dataframe['True_Label'] == 1)]

    # Make a list of lists with all the classes and functions:
    class_table = [['Class', 'Mean of F1', 'SD of F1', 'Mean of F2', 'SD of F2',
                    'Mean of F3', 'SD of F3', 'Mean of F4', 'SD of F4'],
                   ['0', calculate_mean(green_df, 'F1'),
                    standard_deviation(green_df, 'F1'),
                    calculate_mean(green_df, 'F2'),
                    standard_deviation(green_df, 'F2'),
                    calculate_mean(green_df, 'F3'),
                    standard_deviation(green_df, 'F3'),
                    calculate_mean(green_df, 'F4'),
                    standard_deviation(green_df, 'F4')],
                   ['1', calculate_mean(red_df, 'F1'),
                    standard_deviation(red_df, 'F1'),
                    calculate_mean(red_df, 'F2'),
                    standard_deviation(red_df, 'F2'),
                    calculate_mean(red_df, 'F3'),
                    standard_deviation(red_df, 'F3'),
                    calculate_mean(red_df, 'F4'),
                    standard_deviation(red_df, 'F4')],
                   ['All', calculate_mean(dataframe, 'F1'),
                    standard_deviation(dataframe, 'F1'),
                    calculate_mean(dataframe, 'F2'),
                    standard_deviation(dataframe, 'F2'),
                    calculate_mean(dataframe, 'F3'),
                    standard_deviation(dataframe, 'F3'),
                    calculate_mean(dataframe, 'F4'),
                    standard_deviation(dataframe, 'F4')]]

    print(tabulate(class_table))  # Print the list of lists into a table


def plot_bills_data(training_x):
    """
    This function takes a training dataframe and generates 2 pairplot's into
    2 separate pdf documents
    :param training_x: A training dataframe.
    :return: No return just an output to 2 pdf documents with one plotting
    'good' bills and the other 'fake' bills.
    """
    # Separate the training dataframe into 'good' and 'fake' bills:
    green_df = training_x.loc[(training_x['True_Label'] == 0)]
    red_df = training_x.loc[(training_x['True_Label'] == 1)]

    # Plot the 'good' bills:
    sns.pairplot(green_df, vars=['F1', 'F2', 'F3', 'F4'])
    plt.savefig('output/good_bills.pdf')

    # Plot the 'fake' bills:
    sns.pairplot(red_df, vars=['F1', 'F2', 'F3', 'F4'])
    plt.savefig('output/fake_bills.pdf')


def predict_bills(testing_x):
    """
    This function uses a testing dataframe and simple classifiers to try to
    predict if the bills in the dataframe are 'good' or 'fake'
    :param testing_x: A testing dataframe.
    :return: Return's the testing frame with a column that predicts if the
    bills are 'fake' or 'good'.
    """
    # Iterate through the dataframe:
    for index, row in testing_x.iterrows():
        # Calculate if 'good' or 'fake' based on these classifiers:
        if row['F1'] > 1 and row['F3'] > 0 and row['F4'] > -1:
            testing_x.at[index, 'Prediction'] = 'good'
        else:
            testing_x.at[index, 'Prediction'] = 'fake'
    return testing_x


def calculate_simple_table(dataframe):
    """
    Takes a dataframe that has a 'Prediction' column with predictions from a
    simple classifier and calculates the TP, FP, TN, and FN and prints it out
    to a table on the Python console
    :param dataframe: A dataframe with a 'Prediction' column
    :return: No return, just prints out the table to the console
    """
    # Initialize integers to keep track of accuracy:
    true_positive = 0
    false_positive = 0
    true_negative = 0
    false_negative = 0

    for index, row in dataframe.iterrows():
        # Sort by the Prediction and Color_Label of the dataframe:
        if row['Prediction'] == 'good':
            if row['Color_Label'] == 'green':
                true_positive += 1
            else:
                false_positive += 1
        else:
            if row['Color_Label'] == 'red':
                true_negative += 1
            else:
                false_negative += 1

    # Add all the data to a list of lists:
    data_list = [['TP', 'FP', 'TN', 'FN', 'Accuracy', 'TPR', 'TNR'],
                 [true_positive, false_positive, true_negative,
                  false_negative,
                  get_accuracy(true_positive, false_positive, true_negative,
                               false_negative),
                  true_positive_rate(true_positive, false_negative),
                  true_negative_rate(true_negative, false_positive)]]

    print(tabulate(data_list))  # Print out the table (list of lists)


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
    total_amount = (true_positive + false_positive + true_negative +
                    false_negative)
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
