"""
Jude Moore
Class: CS 677
Date: 11/15/2022
Homework Problems: 1-2
Description:
    1) Calculate the probability of 2, 3, 4 positive and negative days.
    2) Use predicting labels of sequences to determine whether the next day
        would be a positive or negative day.
"""
from tabulate import tabulate


def get_true_label(row):
    """
    This function determines the True Label of the dataframe row given, and
    returns it to be placed into "True_Label" column
    :param row: A row in a dataframe
    :return: The True Label of the row
    """
    if row['Return'] >= 0:
        return "+"
    else:
        return "-"


def default_probability(filtered_df):
    """
    Determines the default probability that on any given day, the next will be
    a positive day
    :param filtered_df: A dataframe already filtered by date
    :return: The chance (percentage) that the next day will be positive
    """
    positive_days = filtered_df['True_Label'].value_counts()["+"]
    return positive_days / len(filtered_df)


def conditional_probability(filtered_df, consecutive_days, sequence_string):
    """
    This function determines with a given filtered dataframe, after so many
    consecutive '-' or '+' what the probability of another positive day is
    :param filtered_df: A dataframe already filtered by date
    :param consecutive_days: Number of consecutive days to search for
    :param sequence_string: Either '+' or '-' to search through True Labels
    :return: The probability of a positive after the given consecutive
    sequence of labels
    """
    # Empty sequence list for future use.
    sequence = []

    # Initialize counting the positive and negative days after a sequence.
    positive_outcomes = 0
    negative_outcomes = 0

    # Create the sequence using the consecutive days and string given.
    for item in range(consecutive_days):
        sequence.append(sequence_string)

    for index in range(len(filtered_df) - 1):
        # Iterate through the dataframe depending on consecutive days.
        if consecutive_days == 3:
            if index >= 3:  # Determine if there is a sequence match
                if filtered_df.loc[index - 2, "True_Label"] == sequence[0]:
                    if filtered_df.loc[index - 1, "True_Label"] == sequence[1]:
                        if filtered_df.loc[index, "True_Label"] == sequence[2]:
                            if filtered_df.loc[index + 1, "True_Label"] == '+':
                                positive_outcomes += 1
                            else:
                                negative_outcomes += 1
        elif consecutive_days == 2:
            if index >= 2:  # Determine if there is a sequence match
                if filtered_df.loc[index - 1, "True_Label"] == sequence[0]:
                    if filtered_df.loc[index, "True_Label"] == sequence[1]:
                        if filtered_df.loc[index + 1, "True_Label"] == '+':
                            positive_outcomes += 1
                        else:
                            negative_outcomes += 1
        else:  # Determine if there is a sequence match
            if filtered_df.loc[index, "True_Label"] == sequence[0]:
                if filtered_df.loc[index + 1, "True_Label"] == '+':
                    positive_outcomes += 1
                else:
                    negative_outcomes += 1

    # Calculate and return the average:
    return positive_outcomes / (positive_outcomes + negative_outcomes)


def make_probability_table(filtered_df):
    """
    This function takes a date filtered dataframe and utilizes the other
    functions above to print out a table that includes the default probability
    and conditional probability depending on consecutive days
    :param filtered_df: A dataframe already filtered by date
    :return: No return. Just gathers data and prints it in a table
    """
    table_list = [['Default Probability', 'Chances of -,-,-,+',
                   'Chances of -,-,+', ' Chances of -,+',
                   'Chances of +,+,+,+', 'Chances of +,+,+', "Chances of +,+"],
                  [default_probability(filtered_df),
                   conditional_probability(filtered_df, 3, '-'),
                   conditional_probability(filtered_df, 2, '-'),
                   conditional_probability(filtered_df, 1, '-'),
                   conditional_probability(filtered_df, 3, '+'),
                   conditional_probability(filtered_df, 2, '+'),
                   conditional_probability(filtered_df, 1, '+')]]

    print(tabulate(table_list))  # prints list of lists as a table.


def find_sequence_w2(a_sequence, row_index, filtered_df, original_df):
    """
    This function calculates the prediction if W = 2
    :param a_sequence: A sequence of positive and negatives to search for
    :param row_index: The index of the row the program is currently in
    :param filtered_df: A dataframe already filtered by date
    :param original_df: The dataframe not filtered by date
    :return: No return. Just updates the appropriate column with the prediction
    """
    # Initializes an integers that counts how many times the sequence occurs:
    number_of_sequences_positive = 0
    number_of_sequences_negative = 0

    # Iterate through the dataframe.
    for index in range(len(filtered_df) - 1):
        if index >= 2:
            # Determine if the sequence occurs, and if followed by '+' or '-'
            if a_sequence[0] == filtered_df.loc[index - 2, "True_Label"]:
                if a_sequence[1] == filtered_df.loc[index - 1, "True_Label"]:
                    if a_sequence[2] == filtered_df.loc[index, "True_Label"]:
                        if filtered_df.loc[index + 1, "True_Label"] == '+':
                            number_of_sequences_positive += 1
                        else:
                            number_of_sequences_negative += 1

    # Depending on integer results, add the prediction to the column.
    if number_of_sequences_positive > number_of_sequences_negative:
        original_df.at[row_index, 'W=2'] = '+'
    elif number_of_sequences_negative > number_of_sequences_positive:
        original_df.at[row_index, 'W=2'] = '-'
    else:
        original_df.at[row_index, 'W=2'] = '+'


def find_sequence_w3(a_sequence, row_index, filtered_df, original_df):
    """
    This function calculates the prediction if W = 3
    :param a_sequence: A sequence of positive and negatives to search for
    :param row_index: The index of the row the program is currently in
    :param filtered_df: A dataframe already filtered by date
    :param original_df: The dataframe not filtered by date
    :return: No return. Just updates the appropriate column with the prediction
    """
    # Initializes an integers that counts how many times the sequence occurs:
    number_of_sequences_positive = 0
    number_of_sequences_negative = 0

    # Iterate through the dataframe.
    for index in range(len(filtered_df) - 1):
        if index >= 3:
            # Determine if the sequence occurs, and if followed by '+' or '-'
            if a_sequence[0] == filtered_df.loc[index - 3, "True_Label"]:
                if a_sequence[1] == filtered_df.loc[index - 2, "True_Label"]:
                    if a_sequence[2] == filtered_df.loc[
                        index - 1, "True_Label"]:
                        if a_sequence[3] == filtered_df.loc[
                            index, "True_Label"]:
                            if filtered_df.loc[index + 1, "True_Label"] == '+':
                                number_of_sequences_positive += 1
                            else:
                                number_of_sequences_negative += 1

    # Depending on integer results, add the prediction to the column.
    if number_of_sequences_positive > number_of_sequences_negative:
        original_df.at[row_index, 'W=3'] = '+'
    elif number_of_sequences_negative > number_of_sequences_positive:
        original_df.at[row_index, 'W=3'] = '-'
    else:
        original_df.at[row_index, 'W=3'] = '+'


def find_sequence_w4(a_sequence, row_index, filtered_df, original_df):
    """
    This function calculates the prediction if W = 4
    :param a_sequence: A sequence of positive and negatives to search for
    :param row_index: The index of the row the program is currently in
    :param filtered_df: A dataframe already filtered by date
    :param original_df: The dataframe not filtered by date
    :return: No return. Just updates the appropriate column with the prediction
    """
    # Initializes an integers that counts how many times the sequence occurs:
    number_of_sequences_positive = 0
    number_of_sequences_negative = 0

    # Iterate through the dataframe.
    for index in range(len(filtered_df) - 1):
        if index >= 4:
            # Determine if the sequence occurs, and if followed by '+' or '-'
            if a_sequence[0] == filtered_df.loc[index - 4, "True_Label"]:
                if a_sequence[0] == filtered_df.loc[index - 3, "True_Label"]:
                    if a_sequence[1] == filtered_df.loc[index - 2,
                                                        "True_Label"]:
                        if a_sequence[2] == filtered_df.loc[
                            index - 1, "True_Label"]:
                            if a_sequence[3] == filtered_df.loc[
                                index, "True_Label"]:
                                if filtered_df.loc[index + 1,
                                                   "True_Label"] == '+':
                                    number_of_sequences_positive += 1
                                else:
                                    number_of_sequences_negative += 1

    # Depending on integer results, add the prediction to the column.
    if number_of_sequences_positive > number_of_sequences_negative:
        original_df.at[row_index, 'W=4'] = '+'
    elif number_of_sequences_negative > number_of_sequences_positive:
        original_df.at[row_index, 'W=4'] = '-'
    else:
        original_df.at[row_index, 'W=4'] = '+'


def predictions_accuracy(dataframe, year_df, name_df):
    """
    This function calculates the accuracy of the predictions: W = 2, W = 3,
    W = 4, and Ensemble, and prints it out into a table
    :param dataframe: The dataframe not filtered by date
    :param year_df: The year to filter the dataframe through
    :param name_df: The name of the stock as a string.
    :return: No return, it just calculates accuracy and prints a table
    """

    # Counts how many accurate and inaccurate predictions there were:
    w2_accurate_predictions = 0
    w2_inaccurate_predictions = 0

    w3_accurate_predictions = 0
    w3_inaccurate_predictions = 0

    w4_accurate_predictions = 0
    w4_inaccurate_predictions = 0

    # Iterate through column W = 2 and count predictions:
    for index in range(len(dataframe) - 1):
        if dataframe.loc[index, 'Year'] > year_df:
            if dataframe.loc[index + 1, "True_Label"] == \
                    dataframe.loc[index, "W=2"]:
                w2_accurate_predictions += 1
            else:
                w2_inaccurate_predictions += 1

    # Iterate through column W = 3 and count predictions:
    for index in range(len(dataframe) - 1):
        if dataframe.loc[index, 'Year'] > year_df:
            if dataframe.loc[index + 1, "True_Label"] == \
                    dataframe.loc[index, "W=3"]:
                w3_accurate_predictions += 1
            else:
                w3_inaccurate_predictions += 1

    # Iterate through column W = 4 and count predictions:
    for index in range(len(dataframe) - 1):
        if dataframe.loc[index, 'Year'] > year_df:
            if dataframe.loc[index + 1, "True_Label"] == \
                    dataframe.loc[index, "W=4"]:
                w4_accurate_predictions += 1
            else:
                w4_inaccurate_predictions += 1

    # Put the data into a list of lists
    table_list = [[' ', 'W = 2', 'W = 3', 'W = 4'],
                  ['Accurate', w2_accurate_predictions,
                   w3_accurate_predictions, w4_accurate_predictions],
                  ['Inaccurate', w2_inaccurate_predictions,
                   w3_inaccurate_predictions, w4_inaccurate_predictions],
                  ['Percent Accurate',
                   w2_accurate_predictions /
                   (w2_inaccurate_predictions + w2_accurate_predictions),
                   w3_accurate_predictions /
                   (w3_inaccurate_predictions + w3_accurate_predictions),
                   w4_accurate_predictions /
                   (w4_inaccurate_predictions + w4_accurate_predictions)]]

    # Print title of the table and list of lists as a table:
    print('\nProbability of ' + name_df + ' Based on W = 2, 3, 4:')
    print(tabulate(table_list))
