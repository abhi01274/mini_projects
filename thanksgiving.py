"""
Code Challenge
  Name: 
    Thanks giving Analysis
  Filename: 
    Thanksgiving.py
  Problem Statement:
    Read the thanksgiving-2015-poll-data.csv file and 
    perform the following task :

    Discover regional and income-based patterns in what Americans eat for 
    Thanksgiving dinner

    Convert the column name to single word names
    
    Using the apply method to Gender column to convert Male & Female
    Using the apply method to clean up income
    (Range to a average number, X and up to X, Prefer not to answer to NaN)
    
    compare income between people who tend to eat homemade cranberry sauce for
    Thanksgiving vs people who eat canned cranberry sauce?
    
    find the average income for people who served each type of cranberry sauce
    for Thanksgiving (Canned, Homemade, None, etc).
    
    Plotting the results of aggregation
    
    Do people in Suburban areas eat more Tofurkey than people in Rural areas?
    Where do people go to Black Friday sales most often?
    Is there a correlation between praying on Thanksgiving and income?
    What income groups are most likely to have homemade cranberry sauce?

    Verify a pattern:
        People who have Turducken and Homemade cranberry sauce seem to have 
        high household incomes.
        People who eat Canned cranberry sauce tend to have lower incomes, 
        but those who also have Roast Beef have the lowest incomes
        
    Find the number of people who live in each area type (Rural, Suburban, etc)
    who eat different kinds of main dishes for Thanksgiving:
        
  Hint:

"""

# Importing the required modules for data preprocessing and visualizing
import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt

# Importing re module for using it i filtering out the income column
import re

# Importing suppress from contextlib module to handle exceptions
from contextlib import suppress

# Loading the datasets and starting the required preprocessing
with suppress((FileNotFoundError, TypeError, AttributeError, ValueError)):
    # Encoding of the dataset is in Windows 1252 so it should be specified while loading it
    datath_df = pd.read_csv("thanksgiving.csv", encoding="Windows 1252")

    # Fetching the columns name for further reference
    columns_name = list(datath_df.columns)

    # Initializing a code number for each column name
    code_col = [x for x in range(0, 65)]

    # Storing the column name with their codes for further reference
    columns_ref = dict(zip(code_col, columns_name))

    # Initializing the dataframe with the codes of the column
    datath_df.columns = code_col



    # Fetching the data that perform thanksgiving for further processing
    datath_df = datath_df[datath_df[1] == "Yes"]

    # Filling out the empty values with 'Mising' keyword
    datath_df = datath_df.replace(np.nan, 'Mising')



    # Analysing for the state, area  and income based what is consumed in thankgiving dinner
    state_based = datath_df.groupby(64)[2].value_counts().unstack().fillna(0)

    income_based = datath_df.groupby(63)[2].value_counts().unstack().fillna(0)

    area_based = datath_df.groupby(60)[2].value_counts().unstack().fillna(0)

    # Analysis of the sauces prefered by each incomes group people
    sauce_incgrp = datath_df.groupby(8)[63].value_counts().unstack().fillna(0)

    # Filtering the gender and income columns using .apply method
    def gender_filter(value):
        if value == "Male":
            value = 'M'
        elif value == "Female":
            value = 'F'
        else:
            pass
        return value

    datath_df[62] = datath_df[62].apply(gender_filter)
    datath_df[63] = datath_df[63].replace(['Prefer not to answer', 'mising'],['0','0'])

    regex = re.compile("\d+\W*\d+")

    # A function to be passed in .apply() method for filtering out the salaries
    def income_filter(value):
        value = regex.findall(value)
        value = [int(x.replace(",", "")) for x in value]
        return sum(value)/(len(value)+0.1)

    # Using the apply method to filter the income column
    datath_df[63] = datath_df[63].apply(income_filter)

    # Fetching the average incomes for each type sauces

    sauce_compr = datath_df.groupby(8)[63]

    sauce_inc = sauce_compr.mean()

    # Visualizing the average income of the various sauces
    sauces_inc_visual = sauce_inc.plot.bar()

    # Comparing the incomes of canned and homemade sauces
    craneberry_compr = sauce_inc.iloc[[0, 1]]

    # Visualizing the incomes of various craneberry sauces
    craneberry_compr_visual = craneberry_compr.plot.pie(autopct="%1.1f%%")

    # Comparing the toufourkey eaten in Suburban and Rural areas
    toufurkey_compr = area_based.iloc[[1, 2], [-3]]

    # Visualizing the toufurkey eaten by suburban and rural people
    toufurkey_compr.plot.bar(color=["green"])  # yes suburban eat more toufurkey than rural people

    # Checking for a correlation between thankgiving prayer seeker and their income
    prayer_inc = datath_df.groupby(51)[63].value_counts().unstack().fillna(0)

    # Visualizing the relation between prayer seeker and their income
    prayer_inc_visual = prayer_inc.plot.bar()

    # Analyzing the Blackfriday sales activity
    blackfri_sales = datath_df[57].value_counts()

    """
        Verifying a pattern:
        People who have Turducken and Homemade cranberry sauce seem to have
        high household incomes.
        People who eat Canned cranberry sauce tend to have lower incomes,
        but those who also have Roast Beef have the lowest incomes
    """

    pattern_income = datath_df.groupby([2, 8])[63].value_counts().unstack().fillna(0)
