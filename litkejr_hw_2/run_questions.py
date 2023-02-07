"""
Jude Moore
Class: CS 677
Date: 11/15/2022
Homework Problems: 1-5 (run program)
Description: This python file runs all the homework problems at once, so that
they print to the console at the same time without having to run each file
individually.
"""
from questions_1_through_2 import *
from questions_3_through_5 import *
from read_stock_data_from_file import *

# Add the row 'True_Label' to both dataframes.
MCDdf['True_Label'] = MCDdf.apply(lambda row: get_true_label(row), axis=1)
SPYdf['True_Label'] = SPYdf.apply(lambda row: get_true_label(row), axis=1)

# Filter through first few years for MCD and first four for SPY:
filteredMCD_df = MCDdf.loc[(MCDdf['Date'] >= '2016-01-04')
                           & (MCDdf['Date'] <= '2018-12-31')]
filteredSPY_df = SPYdf.loc[(SPYdf['Date'] >= '2014-01-02')
                           & (SPYdf['Date'] <= '2017-12-29')]

# Question 1: Print out the probability table of MCD and SPY
print("\nProbability of Consecutive Days (MCD):")
make_probability_table(filteredMCD_df)

print("\nProbability of Consecutive Days (SPY):")
make_probability_table(filteredSPY_df)

sequence = []  # An empy list to store sequences for question 2.
# Adding empty columns on prediction types:
MCDdf["W=2"] = " "
MCDdf["W=3"] = " "
MCDdf["W=4"] = " "
MCDdf["Ensemble"] = " "

# Adding empty columns on prediction types:
SPYdf["W=2"] = " "
SPYdf["W=3"] = " "
SPYdf["W=4"] = " "
SPYdf["Ensemble"] = " "

# Question 2: Grab the sequences for W = 2, W = 3, and W = 4:
for i in range(len(MCDdf)):
    # Determine the results of W = 2
    if MCDdf.loc[i, 'Year'] > 2018:
        sequence.append(MCDdf.loc[i - 2, "True_Label"])
        sequence.append(MCDdf.loc[i - 1, "True_Label"])
        sequence.append(MCDdf.loc[i, "True_Label"])
        find_sequence_w2(sequence, i, filteredMCD_df, MCDdf)
        sequence.clear()  # Clear the sequence for next one.

# Question 2: Grab the sequences for W = 2, W = 3, and W = 4:
for i in range(len(MCDdf)):
    # Determine the results of W = 3
    if MCDdf.loc[i, 'Year'] > 2018:
        sequence.append(MCDdf.loc[i - 3, "True_Label"])
        sequence.append(MCDdf.loc[i - 2, "True_Label"])
        sequence.append(MCDdf.loc[i - 1, "True_Label"])
        sequence.append(MCDdf.loc[i, "True_Label"])
        find_sequence_w3(sequence, i, filteredMCD_df, MCDdf)
        sequence.clear()  # Clear the sequence for next one.

# Question 2: Grab the sequences for W = 2, W = 3, and W = 4:
for i in range(len(MCDdf)):
    # Determine the results of W = 4
    if MCDdf.loc[i, 'Year'] > 2018:
        sequence.append(MCDdf.loc[i - 4, "True_Label"])
        sequence.append(MCDdf.loc[i - 3, "True_Label"])
        sequence.append(MCDdf.loc[i - 2, "True_Label"])
        sequence.append(MCDdf.loc[i - 1, "True_Label"])
        sequence.append(MCDdf.loc[i, "True_Label"])
        find_sequence_w4(sequence, i, filteredMCD_df, MCDdf)
        sequence.clear()  # Clear the sequence for next one.

# Question 2: Grab the sequences for W = 2, W = 3, and W = 4:
for i in range(len(SPYdf)):
    # Determine the results of W = 2
    if SPYdf.loc[i, 'Year'] > 2017:
        sequence.append(SPYdf.loc[i - 2, "True_Label"])
        sequence.append(SPYdf.loc[i - 1, "True_Label"])
        sequence.append(SPYdf.loc[i, "True_Label"])
        find_sequence_w2(sequence, i, filteredSPY_df, SPYdf)
        sequence.clear()  # Clear the sequence for next one.

# Question 2: Grab the sequences for W = 2, W = 3, and W = 4:
for i in range(len(SPYdf)):
    # Determine the results of W = 3
    if SPYdf.loc[i, 'Year'] > 2017:
        sequence.append(SPYdf.loc[i - 3, "True_Label"])
        sequence.append(SPYdf.loc[i - 2, "True_Label"])
        sequence.append(SPYdf.loc[i - 1, "True_Label"])
        sequence.append(SPYdf.loc[i, "True_Label"])
        find_sequence_w3(sequence, i, filteredSPY_df, SPYdf)
        sequence.clear()  # Clear the sequence for next one.

# Question 2: Grab the sequences for W = 2, W = 3, and W = 4:
for i in range(len(SPYdf)):
    # Determine the results of W = 4
    if SPYdf.loc[i, 'Year'] > 2017:
        sequence.append(SPYdf.loc[i - 4, "True_Label"])
        sequence.append(SPYdf.loc[i - 3, "True_Label"])
        sequence.append(SPYdf.loc[i - 2, "True_Label"])
        sequence.append(SPYdf.loc[i - 1, "True_Label"])
        sequence.append(SPYdf.loc[i, "True_Label"])
        find_sequence_w4(sequence, i, filteredSPY_df, SPYdf)
        sequence.clear()  # Clear the sequence for next one.

# Determine the accuracy of W = 2, W = 3, and W = 4; Print results:
predictions_accuracy(MCDdf, 2018, 'MCD')
predictions_accuracy(SPYdf, 2017, 'SPY')

# Question 3: Using ensemble learning, add data predictions to column 'Ensemble'
ensemble_learning(MCDdf, 2018)
ensemble_learning(SPYdf, 2017)

# Question 3: Determine the accuracy of using 'Ensemble'
ensemble_accuracy(MCDdf, 2018, 'MCD')
ensemble_accuracy(SPYdf, 2017, 'SPY')

# Question 4: Calculate and print the statistics of the stock
get_statistics_table(MCDdf, 2018, 'MCD')
get_statistics_table(SPYdf, 2017, 'SPY')

# Question 5: Plot a graph that shows the amount earned from all types
plot_data(calculate_stock(MCDdf, 2018, 'W=2'),
          calculate_stock(MCDdf, 2018, 'W=3'),
          calculate_stock(MCDdf, 2018, 'W=4'),
          calculate_stock(MCDdf, 2018, 'Ensemble'),
          buy_and_hold(MCDdf, 2018), 'MCD')

plot_data(calculate_stock(SPYdf, 2017, 'W=2'),
          calculate_stock(SPYdf, 2017, 'W=3'),
          calculate_stock(SPYdf, 2017, 'W=4'),
          calculate_stock(SPYdf, 2017, 'Ensemble'),
          buy_and_hold(SPYdf, 2017), 'SPY')
