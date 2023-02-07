"""
Jude Moore
Class: CS 677
Date: 11/22/2022
Homework Problems: 1-6 (run program)
Description: This python file runs all the homework problems at once, so that
they print to the console at the same time without having to run each file
individually.
"""

from warnings import simplefilter

import pandas as pd

from question_3_through_6 import *
from questions_1_through_2 import *

"""
There is a FutureWarning that is triggered in the code, so this is used 
to prevent it from popping up. The code runs in Python 3.9, sklearn 1.0.2.
(The latest version of Anaconda.) 
This should be revisited when Anaconda/sklearn updates!
"""
simplefilter(action='ignore', category=FutureWarning)

# Read data from the text file into dataframe:
bank_note_data = pd.read_csv('data_banknote_authentication.txt', delimiter=',',
                             header=None,
                             names=['F1', 'F2', 'F3', 'F4', 'True_Label'])

# Add a color label to the dataframe (Question 1(1)):
bank_note_data['Color_Label'] = \
    bank_note_data.apply(lambda row: get_color_label(row), axis=1)

# Print table with data from Question 1(2):
print("\nStandard Deviation and Mean of Class 0, 1, and All:")
create_class_table(bank_note_data)

# Split the data in half and read them to .csv files for easier use.
# Read data from files and put into dataframe (Question 2(1)):
train_x = pd.read_csv('data/train_x.csv')
testing_x = pd.read_csv('data/testing_x.csv')

# Plot data into pdf files for Question 2(1):
plot_bills_data(train_x)

# Add column 'Prediction' for simple classifier to add prediction to:
testing_x['Prediction'] = ' '

# Predict using simple classifier with the testing dataframe (Question 2(3)):
get_predictions = predict_bills(testing_x)

# Print out a table of data of predictions by simple classifier (Question 2(5)):
print("\nCalculate the Statistics and Accuracy of Simple Classifiers:")
calculate_simple_table(get_predictions)

# Drop the unimportant columns into a new dataframe for Question 3:
testing2_x = testing_x.drop(['Prediction', 'Color_Label'], axis=1)
train2_x = train_x.drop('Color_Label', axis=1)

# Train and test k-NN when k = 3
k3_df = kNN_prediction(train2_x, testing2_x, 3, "K=3")
testing2_x = testing2_x.drop(['K=3'], axis=1)

# Train and test k-NN when k = 5
k5_df = kNN_prediction(train2_x, testing2_x, 5, "K=5")
testing2_x = testing2_x.drop(['K=5'], axis=1)

# Train and test k-NN when k = 7
k7_df = kNN_prediction(train2_x, testing2_x, 7, "K=7")
testing2_x = testing2_x.drop(['K=7'], axis=1)

# Train and test k-NN when k = 9
k9_df = kNN_prediction(train2_x, testing2_x, 9, "K=9")
testing2_x = testing2_x.drop(['K=9'], axis=1)

# Train and test k-NN when k = 11
k11_df = kNN_prediction(train2_x, testing2_x, 11, "K=11")
testing2_x = testing2_x.drop(['K=11'], axis=1)

# Calculate the accuracy of each dataframe derived:
k3_df_accuracy = calculate_column_accuracy(k3_df, "K=3")
k5_df_accuracy = calculate_column_accuracy(k5_df, "K=5")
k7_df_accuracy = calculate_column_accuracy(k7_df, "K=7")
k9_df_accuracy = calculate_column_accuracy(k9_df, "K=9")
k11_df_accuracy = calculate_column_accuracy(k11_df, "K=11")

# Plot the accuracy to a graph (Question 3(2)):
plot_accuracy(k3_df_accuracy, k5_df_accuracy, k7_df_accuracy, k9_df_accuracy,
              k11_df_accuracy)

# Print table of data for Question 3(3):
print("\nOptimal value k* is k = 5, Accuracy Table below:")
calculate_statistics_knn(k5_df, "K=5")

# Read BU ID data from a csv file to a dataframe:
BU_id = pd.read_csv('data/BU_id.csv')

# Use simple classifier to predict if BU ID is fake or real (Question 3(5)):
print("\nPredict if BU Id is Fake or Real Using Simple Classifier:")
predict_bills(BU_id)
print(BU_id)

# Use k-NN (k=5) to predict if BU ID is fake or real (Question 3(5)):
print("\nPredict if BU Id is Fake or Real Using k-nn K=5:")
BU_k5 = kNN_prediction(train2_x, BU_id, 5, "K=5")
print(BU_k5)

# Question 4: take best value of k (5) and truncate each feature:
no_f1_reg_df = kNN_feature_selection(train2_x, testing2_x, 5,
                                     ['F2', 'F3', 'F4'],
                                     'F1')

no_f2_reg_df = kNN_feature_selection(train2_x, testing2_x, 5,
                                     ['F1', 'F3', 'F4'],
                                     'F2')

no_f3__reg_df = kNN_feature_selection(train2_x, testing2_x, 5,
                                      ['F1', 'F2', 'F4'],
                                      'F3')

no_f4_reg_df = kNN_feature_selection(train2_x, testing2_x, 5,
                                     ['F1', 'F2', 'F3'],
                                     'F4')

# Question 4: Calculate the accuracy of truncated features:
print("\nPrediction Accuracy if F1 is removed:")
print(calculate_column_accuracy(no_f1_reg_df, "Prediction"))
print("\nPrediction Accuracy if F2 is removed:")
print(calculate_column_accuracy(no_f2_reg_df, "Prediction"))
print("\nPrediction Accuracy if F3 is removed:")
print(calculate_column_accuracy(no_f3__reg_df, "Prediction"))
print("\nPrediction Accuracy if F4 is removed:")
print(calculate_column_accuracy(no_f4_reg_df, "Prediction"))

# Question 5: Train and test using logistical regression:
print("\nRegression Accuracy:")
regCla_df = regression_classifier(train2_x, testing2_x)
print(calculate_column_accuracy(regCla_df, 'Prediction'))

# Question 5(2): Summarize the data to a table:
print("\nRegression Accuracy Table:")
calculate_statistics_knn(regCla_df, 'Prediction')

# Question 5(5): Predict if BU ID using logistical regression is real or fake
BU_id = BU_id.drop(['K=5'], axis=1)
regCla_BU_df = regression_classifier(train2_x, BU_id)
print("\nPredict if BU Id is Fake or Real Using Regression:")
print(regCla_BU_df)

# Drop the 'Prediction' column from previous testing for Question 6:
testing2_x = testing2_x.drop(['Prediction'], axis=1)

# Question 6: take logistical regression and truncate each feature:
no_f1_reg_df = regression_feature_selection(train2_x, testing2_x,
                                            ['F2', 'F3', 'F4'],
                                            'F1')

no_f2_reg_df = regression_feature_selection(train2_x, testing2_x,
                                            ['F1', 'F3', 'F4'],
                                            'F2')

no_f3_reg_df = regression_feature_selection(train2_x, testing2_x,
                                            ['F1', 'F2', 'F4'],
                                            'F3')

no_f4_reg_df = regression_feature_selection(train2_x, testing2_x,
                                            ['F1', 'F2', 'F3'],
                                            'F4')

# Question 6: Calculate the accuracy of truncated features:
print("\nRegression Accuracy if F1 is removed:")
print(calculate_column_accuracy(no_f1_reg_df, "Prediction"))
print("\nRegression Accuracy if F2 is removed:")
print(calculate_column_accuracy(no_f2_reg_df, "Prediction"))
print("\nRegression Accuracy if F3 is removed:")
print(calculate_column_accuracy(no_f3__reg_df, "Prediction"))
print("\nRegression Accuracy if F4 is removed:")
print(calculate_column_accuracy(no_f4_reg_df, "Prediction"))
