#%%
import pandas as pd
import seaborn as sns
import numpy as np
import os 
#%%
data = sns.load_dataset("titanic")
# %%
data.shape # (891, 15)
data.describe() # the first statistical information of the numerical data
# (min, max, mean, etc.)
# %%
# check whether the two columns "pclass" and "class" share the same information
first = ((data["pclass"] == 1) & (data["class"] != "First")).sum()
second = ((data["pclass"] == 2) & (data["class"] != "Second")).sum()
third = ((data["pclass"] == 3) & (data["class"] != "Third")).sum()

print(f"First: {first}, Second: {second}, Third: {third}") #First: 0, Second: 0, Third: 0
# this means we can delete one of the columns  => delete "class"

# %%
data = data.drop(columns= "class")
# deletes the column "class"
# %%
data = data.drop(columns= "adult_male")
# drop "adult_male" column because it's irrelevant for our analysis
# %%
((data["age"].isnull()) & (data["who"] == "child")).sum() # 0
((data["age"].isnull()) & (data["who"] == "woman")).sum() # 53
((data["age"].isnull()) & (data["who"] == "man")).sum() # 124
# no missing age for children, 53 missing values for women, 124 missing values for men
# %%
data["age"].isnull().sum() 
# 177 missing values (in the column age) which we'll fill with 
# the average age depending on the column "who" (woman or man) since there is no
# missing age for children
data.groupby("who")["age"].mean().round()
# who
# child     6.0
# man      33.0
# woman    32.0
men_age = 33
women_age = 32
data.loc[data["who"] == "woman", "age"] = data.loc[data["who"] == "woman", "age"].fillna(women_age)
data.loc[data["who"] == "man", "age"] = data.loc[data["who"] == "man", "age"].fillna(men_age)
# %%
data["age"].isnull().sum() # 0 --> no more missing values
# %%
# check whether the two colums "embark_town" and "embarked" share the same information
southampton = ((data["embark_town"] == "Southampton") & (data["embarked"] != "S")).sum()
cherbourg = ((data["embark_town"] == "Cherbourg") & (data["embarked"] != "C")).sum()
queenstown = ((data["embark_town"] == "Queenstown") & (data["embarked"] != "Q")).sum()

print(f"Southampton: {southampton}, Cherbourg: {cherbourg}, Queenstown: {queenstown}")
# Southampton: 0, Cherbourg: 0, Queenstown: 0
# again we can delete one of the columns. In this case we'll delete "embarked" 
# because the "embark_town" is more understandable
# %%
data = data.drop(columns="embarked") # no need
data = data.drop(columns="deck") # too many missing values and too little information
# %%
not_alone = ((data["sibsp"] > 0) & (data["alone"] != False)).sum()
alone = ((data["sibsp"] == 0) & (data["alone"] != True)).sum()


print(f"Alone: {alone}, Not Alone: {not_alone}")
# alone == False and sibsp > 0 are identical but alone == True and sibsp == 0 are not 
# so we leave as it is
# %%
output_folder = os.path.join(os.getcwd())
output_file = os.path.join(output_folder, "cleaned_data.csv")
data.to_csv(output_file)
# saved the cleaned data as a new csv file ("cleaned_data.csv") 
# into the mypackage folder in the source folder

# %%
