# -*- coding: utf-8 -*-

"""
Code Challenge - 
 This is a pre-crawled dataset, taken as subset of a bigger dataset 
 (more than 4.7 million job listings) that was created by extracting data 
 from Monster.com, a leading job board.
 
 Remove location from Organization column?
 Remove organization from Location column?
 
 In Location column, instead of city name, (zip code,job description)
 is given, deal with it.
 
 Seperate the salary column in hourly and yearly basis and after modification
 salary should not be in range form , handle the ranges with average value .
 
 Which organization has highest, lowest, and average salary?
 
 which Sector has how many jobs?
 Which organization has how many jobs
 Which Location has how many jobs?
"""

# Data Preprocessing modules
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Loading the data
dataset = pd.read_csv("monster.csv")

# Dropping unnecessary features
dataset = dataset.drop(['country','country_code','job_board',
'has_expired','page_url','uniq_id'],axis=1)

# Filling the nan values with missing string so that string operation can be applied further
dataset[['location', 'organization']] = dataset[['location', 'organization']].fillna("missing")

# Regex module required to swap the location and organization back to their respective column
import re
regex = re.compile("\,\s*\w{2}\s*\d*")

def  mod_fun(value1, value2):
    if regex.search(value2):
        value1, value2 = value2, value1
    return pd.Series((value1, value2))
#dataset[['location', 'organization']] =  dataset[['location', 'organization']].apply(mod_fun)
dataset[['location', 'organization']] = dataset.apply(lambda x: mod_fun(x["location"], x["organization"]), axis=1)

# Dropping the unnecessary location row
dataset = dataset[dataset["location"].map(lambda x: len(x) <20 )]
dataset = dataset[dataset["location"].map(lambda x: x.isdigit() is False)]

# Applying regex to find hourly and yearly salary
regex1 = re.compile("(/hour|\week)\w*")
regex2 = re.compile("/year\w*")

def mod_sal(sal):
    sal = sal.replace("$", "")
    sal = sal.replace("-", "")
    sal = sal.replace(",", "")
    sal1, sal2 = np.nan, np.nan
    if regex1.search(sal):
        sal = re.findall("\d+\.*\d*",sal)
        sal = [float(x) for x in sal if x!='0.0']
        if 0 in sal:
            sal.remove(0)
        sal1 = sum(sal)/2
    elif regex2.search(sal):
        sal = re.findall("\d+\.*\d*",sal)
        sal = [float(x) for x in sal if x!='0.0']
        if 0 in sal:
            sal.remove(0)
        sal2 = sum(sal)/2
    return pd.Series((sal1, sal2))

dataset["salary"] = dataset["salary"].fillna("missing")
dataset[["hourly_salary","yearly_salary"]] = dataset["salary"].apply(mod_sal)

# Finding the maximum, average and minimum hourly and yearly salary and also their respective organizations
max_hourly_salary = dataset["hourly_salary"].max()
mean_hourly_salary = dataset["hourly_salary"].mean()
min_hourly_salary = dataset["hourly_salary"].min()

print("Maximum hourly salary with organisation:",list(dataset["organization"][dataset["hourly_salary"]==max_hourly_salary]),"->",max_hourly_salary)
print("Mean hourly salary with organisation:",list(dataset["organization"][dataset["hourly_salary"]==mean_hourly_salary]),"->",mean_hourly_salary)
print("Minimum hourly salary with organisation:",list(dataset["organization"][dataset["hourly_salary"]==min_hourly_salary]),"->",min_hourly_salary)

max_yearly_salary = dataset["yearly_salary"].max()
mean_yearly_salary = dataset["yearly_salary"].mean()
min_yearly_salary = dataset["yearly_salary"].min()

print("Maximum yearly salary with organisation:",list(dataset["organization"][dataset["yearly_salary"]==max_yearly_salary]),"->",max_yearly_salary)
print("Mean yearly salary with organisation:",list(dataset["organization"][dataset["yearly_salary"]==mean_yearly_salary]),"->",mean_yearly_salary)
print("Minimum yearly salary with organisation:",list(dataset["organization"][dataset["yearly_salary"]==min_yearly_salary]),"->",min_yearly_salary)

# Finding the jobs regarding sector, organizations and location and also visualizing them
sector_jobs = dataset["sector"].value_counts().reset_index()
sector_jobs.columns = ["sector", "number of jobs"]
