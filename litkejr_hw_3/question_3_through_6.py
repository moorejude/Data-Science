"""
Jude Moore
Class: CS 677
Date: 11/22/2022
Homework Problems: 3 - 6
Description:
    3. Plot a graph showing the accuracy of k-NN classifier when k = 3, 5, 7, 9
        and 11. Find optimal value k*, and compute the performance. Use k* to
         find if BU ID would be considered real or fake bill.
    4. Feature selection with k-nn: 4 cases, where each case has a different
        feature dropped.
    5. Use logistic regression and compute the performance. Use logistic
        regression to find if BU ID would be considered real or fake bill.
    6. Feature selection with logistic regression: 4 cases, where each case has
        a different feature dropped.
"""
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from questions_1_through_2 import *


def kNN_prediction(training_df, testing_df, k, column_name):
    """
    This function uses a training dataframe to train k-NN with value k,
    and then predicts if each bill is good or fake in a new column in
    the testing dataframe
    :param training_df: The dataframe used for training
    :param testing_df: The dataframe to be tested
    :param k: The value of 'k' for k-NN problem
    :param column_name: A list of columns that are being tested for
    :return: The testing dataframe with a new column of predictions using
    k-NN.
    """
    # Drop empty columns and rows
    training_df.dropna()

    # Get the values of the features column as X:
    X = training_df[['F1', 'F2', 'F3', 'F4']].values

    # Get the True Labels for each row as Y:
    Y = training_df[['True_Label']].values

    # Split into testing for X and Y:
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=1,
                                                        random_state=0)

    # Bring it to scale and fit the training X
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)

    # Initiate kNeighbors and feed it the training data:
    classifier = KNeighborsClassifier(n_neighbors=k)
    classifier.fit(X_train, y_train.ravel())

    # Initiate empty list to store predictions:
    get_predictions = []

    # Use the testing dataframe to test logistic regression by each row:
    for index, row in testing_df.iterrows():
        # Feed everything except for the last row (true_label):
        get_predictions.append(classifier.predict([row[:-1]]))

    # Initiate an empty list to pull the integer (0 or 1) from predictions:
    get_integers = []

    # Get the predictions as a list:
    for index in range(len(testing_df)):
        get_integers.append(get_predictions[index][0])

    # Append the predictions to a new column:
    testing_df[column_name] = list(get_integers)

    return testing_df


def calculate_column_accuracy(dataframe, column_name):
    """
    This function takes a dataframe and a column within that dataframe to check
    for the accuracy of the predictions in the column
    :param dataframe: The dataframe to calculate
    :param column_name: The column to check against True_Label
    :return: Returns the percentage of accuracy of the predictions
    """
    # Initialize integers to keep track:
    true_positive = 0
    false_positive = 0
    true_negative = 0
    false_negative = 0

    for index, row in dataframe.iterrows():
        # Sort by the column given and True_Label of the dataframe:
        if row[column_name] == 0:
            if row['True_Label'] == 0:
                true_positive += 1
            else:
                false_positive += 1
        else:
            if row['True_Label'] == 1:
                true_negative += 1
            else:
                false_negative += 1

    # Return the accuracy of the given predictions in column_name
    return get_accuracy(true_positive, false_positive,
                        true_negative, false_negative)


def plot_accuracy(k3_accuracy, k5_accuracy, k7_accuracy, k9_accuracy,
                  k11_accuracy):
    """
    This function plots the accuracy of k = 3, 5, 7, 9, and 11 to a graph
    :param k3_accuracy: The accuracy percentage when k=3
    :param k5_accuracy: The accuracy percentage when k=5
    :param k7_accuracy: The accuracy percentage when k=7
    :param k9_accuracy: The accuracy percentage when k=9
    :param k11_accuracy: The accuracy percentage when k=11
    :return: No return, just plots a graph to a png file
    """
    y_axis_accuracy = [k3_accuracy, k5_accuracy, k7_accuracy, k9_accuracy,
                       k11_accuracy]
    x_axis_k = [3, 5, 7, 9, 11]

    # Plot the graph with x_axis and y_axis:
    plt.figure()  # open new file
    plt.plot(x_axis_k, y_axis_accuracy)
    plt.title("k-NN Classifier Accuracy")
    plt.xlabel('k')
    plt.ylabel('Accuracy')
    plt.grid()
    plt.savefig("output/knn_accuracy_graph.png")
    plt.clf()  # scrub the file for the next.


def calculate_statistics_knn(dataframe, column_name):
    """
    Takes a dataframe and calculates the TP, FP, TN, and FN and prints it out
    to a table on the Python console
    :param dataframe: The dataframe to calculate
    :param column_name: The column to check against True_Label
    :return: No return, just prints out a table with the data
    """
    # Initialize integers to keep track:
    true_positive = 0
    false_positive = 0
    true_negative = 0
    false_negative = 0

    for index, row in dataframe.iterrows():
        # Sort by the column given and True_Label of the dataframe:
        if row[column_name] == 0:
            if row['True_Label'] == 0:
                true_positive += 1
            else:
                false_positive += 1
        else:
            if row['True_Label'] == 1:
                true_negative += 1
            else:
                false_negative += 1

    # Add all the data to a list:
    data_list = [['TP', 'FP', 'TN', 'FN', 'Accuracy', 'TPR', 'TNR'],
                 [true_positive, false_positive, true_negative,
                  false_negative,
                  get_accuracy(true_positive, false_positive, true_negative,
                               false_negative),
                  true_positive_rate(true_positive, false_negative),
                  true_negative_rate(true_negative, false_positive)]]

    print(tabulate(data_list))  # Print the list of lists as a table


def kNN_feature_selection(training_df, testing_df, k, column_list, drop_column):
    """
    This function uses a training dataframe to train k-NN with optimal
    value k*, and then predicts if each bill is good or fake in a new column in
    the testing dataframe. However, it will drop a feature (column) as a part of
    feature selection
    :param training_df: The dataframe used for training
    :param testing_df: The dataframe to be tested
    :param k: The value of 'k' for k-NN problem
    :param column_list: A list of columns that are being tested for
    :param drop_column: The name of the column being dropped (the feature
    being excluded)
    :return: The testing dataframe with a new column of predictions using
    k-NN.
    """
    # Drop empty columns and rows
    training_df.dropna()
    # Drop the feature not being tested for:
    testing_df = testing_df.drop([drop_column], axis=1)

    # Get the values of the features column as X:
    X = training_df[column_list].values

    # Get the True Labels for each row as Y:
    Y = training_df[['True_Label']].values

    # Split into testing for X and Y:
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=1,
                                                        random_state=0)

    # Bring it to scale and fit the training X
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)

    # Initiate kNeighbors and feed it the training data:
    classifier = KNeighborsClassifier(n_neighbors=k)
    classifier.fit(X_train, y_train.ravel())

    # Initiate empty list to store predictions:
    get_predictions = []

    # Use the testing dataframe to test logistic regression by each row:
    for index, row in testing_df.iterrows():
        # Feed everything except for the last row (true_label):
        get_predictions.append(classifier.predict([row[:-1]]))

    # Initiate an empty list to pull the integer (0 or 1) from predictions:
    get_integers = []

    # Get the predictions as a list:
    for index in range(len(testing_df)):
        get_integers.append(get_predictions[index][0])

    # Append the predictions to a new column:
    testing_df["Prediction"] = list(get_integers)

    return testing_df


def regression_classifier(training_df, testing_df):
    """
    This function uses a training dataframe to train logistical regression, and
    then predicts if each bill is good or fake in a new column in the testing
    dataframe
    :param training_df: A training dataframe
    :param testing_df: A testing dataframe
    :return: The testing dataframe with a new column of predictions using
    logistical regression.
    """
    # Drop empty columns and rows
    training_df.dropna()

    # Get the values of the features column as X:
    X = training_df[['F1', 'F2', 'F3', 'F4']].values

    # Get the True Labels for each row as Y:
    Y = training_df[['True_Label']].values

    # Split into testing for X and Y:
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=1,
                                                        random_state=0)

    # Bring it to scale and fit the training X
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)

    # Initiate logistic regression and feed it the training data:
    logistic_regression = LogisticRegression()
    logistic_regression.fit(X_train, y_train.ravel())

    # Initiate empty list to store predictions:
    get_predictions = []

    # Use the testing dataframe to test logistic regression by each row:
    for index, row in testing_df.iterrows():
        # Feed everything except for the last row (true_label):
        get_predictions.append(logistic_regression.predict([row[:-1]]))

    # Initiate an empty list to pull the integer (0 or 1) from predictions:
    get_integers = []

    # Get the predictions as a list:
    for index in range(len(testing_df)):
        get_integers.append(get_predictions[index][0])

    # Append the predictions to a new column:
    testing_df['Prediction'] = list(get_integers)

    return testing_df


def regression_feature_selection(training_df, testing_df, column_list,
                                 drop_column):
    """
    This function uses a training dataframe to train logistical regression, and
    then predicts if each bill is good or fake in a new column in the testing
    dataframe. However, it will drop a feature (column) as a part of feature
    selection
    :param training_df: The dataframe used for training
    :param testing_df: The dataframe to be tested
    :param column_list: A list of columns that are being tested for
    :param drop_column: The name of the column being dropped (the feature
    being excluded)
    :return: The testing dataframe with a new column of predictions using
    logistical regression.
    """
    # Drop empty columns and rows
    training_df.dropna()
    # Drop the feature not being tested for:
    testing_df = testing_df.drop([drop_column], axis=1)

    # Get the values of the features column as X:
    X = training_df[column_list].values

    # Get the True Labels for each row as Y:
    Y = training_df[['True_Label']].values

    # Split into testing for X and Y:
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=1,
                                                        random_state=0)

    # Bring it to scale and fit the training X
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)

    # Initiate logistic regression and feed it the training data:
    logistic_regression = LogisticRegression()
    logistic_regression.fit(X_train, y_train.ravel())

    # Initiate empty list to store predictions:
    get_predictions = []

    # Use the testing dataframe to test logistic regression by each row:
    for index, row in testing_df.iterrows():
        # Feed everything except for the last row (true_label):
        get_predictions.append(logistic_regression.predict([row[:-1]]))

    # Initiate an empty list to pull the integer (0 or 1) from predictions:
    get_integers = []

    # Get the predictions as a list:
    for index in range(len(testing_df)):
        get_integers.append(get_predictions[index][0])

    # Append the predictions to a new column:
    testing_df['Prediction'] = list(get_integers)

    return testing_df
