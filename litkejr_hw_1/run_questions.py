"""
Jude Moore
Class: CS 677
Date: 11/9/2022
Homework Problems: 1-6 (run program)
Description: This python file runs all the homework problems at once, so that
they print to the console at the same time without having to run each file
individually.
"""
from questions_1_through_3 import *
from questions_4_through_6 import *
from read_stock_data_from_file import *

# prints out 5 tables with mean, standard deviation, and positive/negative days
# for each year.
print("\n2016 Data Table:")
print_yearly_table('2016')

print("\n2017 Data Table:")
print_yearly_table('2017')

print("\n2018 Data Table:")
print_yearly_table('2018')

print("\n2019 Data Table:")
print_yearly_table('2019')

print("\n2020 Data Table:")
print_yearly_table('2020')

# prints out a table with aggregate data for MCD and SPY stock -
# calculates mean, standard deviation, and positive/negative days
print("\nAggregate Table Data from 2016-2020 for MCD:")
print_aggregate_table(MCD_data_matrix)

print("\nAggregate Table Data from 2016-2020 for SPY:")
print_aggregate_table(SPY_data_matrix)

# prints out a number if only the positive returns were realized (start $100)
print("\nAmount Only Positive at end of 5 years MCD:")
trade_stock_only_positive(MCD_data_matrix)

# prints out a number if only the positive returns were realized (start $100)
print("\nAmount Only Positive at end of 5 years SPY:")
trade_stock_only_positive(SPY_data_matrix)

# prints out amount earned if someone starts with $100 and buy-and-holds
print("\nBuy-and-Hold 5 years MCD:")
buy_and_hold(MCD_data_matrix)

# prints out amount earned if someone starts with $100 and buy-and-holds
print("\nBuy-and-Hold 5 years SPY:")
buy_and_hold(SPY_data_matrix)

# calculates only positive returns minus the top 10 best
print("\nMinus Ten Best Returns MCD:")
calculate_stock(loss_best_days(MCD_data_matrix, 10))

# calculates only positive returns minus the top 10 best
print("\nMinus Ten Best Returns SPY:")
calculate_stock(loss_best_days(SPY_data_matrix, 10))

# calculates only positive returns plus top 10 worst
print("\nPlus Ten Worst Returns MCD:")
calculate_stock(get_ten_worst_days(MCD_data_matrix))

# calculates only positive returns plus top 10 worst
print("\nPlus Ten Worst Returns SPY:")
calculate_stock(get_ten_worst_days(SPY_data_matrix))

# calculates only positive returns plus 5 worst, minus 5 best
print("\nPlus Five Worst and Minus Five Best MCD:")
calculate_stock(get_worst_best_results(MCD_data_matrix))

# calculates only positive returns plus 5 worst, minus 5 best
print("\nPlus Five Worst and Minus Five Best SPY:")
calculate_stock(get_worst_best_results(SPY_data_matrix))
