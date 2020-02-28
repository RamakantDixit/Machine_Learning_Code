# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 21:31:37 2020

@author: Kanan
"""

# how to append dictionary in python

dict1={'a':1,'b':2}
dict2={'c':3,'d':4}


#method 1
for key,value in dict1.items():

    dict2[key]=dict1[key]

print(dict2)

 ##method 2

dict3={'a':1,'b':2}

dict4={'c':3,'d':4}

dict3.update(dict4)

print(dict3)

# select year from data frame where year=2000

#surveys_df[surveys_df.year == 2002]
# select year from data frame where year is not2000
#surveys_df[surveys_df.year != 2002]
# select year from data frame where year is from 1980 to 1985
#surveys_df[(surveys_df.year >1980)&(surveys_df.year <1985)]
# surveys_df[surveys_df['species_id'].isin([listGoesHere])]
 #how to find wheather columns contains null or not pd.isnull(surveys_df)
#pd.isnull(surveys_df)
# To select just the rows with NaN values, we can use the 'any()' method

#surveys_df[pd.isnull(surveys_df).any(axis=1)]
#or
#empty_weights = surveys_df[pd.isnull(surveys_df['weight'])]['weight']
# Convert the record_id field from an integer to a float
#surveys_df['record_id'] = surveys_df['record_id'].astype('float64')
#how to merge data frame
#merged_left = pd.merge(left=survey_sub, right=species_sub, how='left', left_on='species_id', right_on='species_id')
# pivot the data frame
#df.pivot(index='fff', columns='bbb', values='baa')