#%%
import pandas as pd
import seaborn as sns
import numpy as np
#%%
data = sns.load_dataset("titanic")
# %%
data.shape # (891, 15)
data.describe() # the first statistical information (min, max, mean, etc.)
# %%
first = ((data["pclass"] == 1) & (data["class"] != "First")).sum()
second = ((data["pclass"] == 2) & (data["class"] != "Second")).sum()
third = ((data["pclass"] == 3) & (data["class"] != "Third")).sum()

print(f"First: {first}, Second: {second}, Third: {third}") #First: 0, Second: 0, Third: 0
# this means we can delete the one of the columns => delete "class"

# %%
data = data.drop(columns= "class")
# %%
data = data.drop(columns= "adult_male")
# drop "class" and "adult_male" columns because they are irrelevant for our analysis
# %%
data.head(10)
# %%
data["age"][(data["age"].isnull()) & (data["who"] == "child")]
# no missing age for children
# %%
data["age"].isnull().sum() # 177 missing values which we'll fill with the mean of age
data["age"] = data["age"].fillna(data["age"].mean())
# %%
data["age"].isnull().sum() # no more missing values
# %%
southampton = ((data["embark_town"] == "Southampton") & (data["embarked"] != "S")).sum()
cherbourg = ((data["embark_town"] == "Cherbourg") & (data["embarked"] != "C")).sum()
queenstown = ((data["embark_town"] == "Queenstown") & (data["embarked"] != "Q")).sum()

print(f"Southampton: {southampton}, Cherbourg: {cherbourg}, Queenstown: {queenstown}")
# again we can delete one of the columns. In this case we'll delete "embarked" because the "embark_town" is more understandable
# %%
data = data.drop(columns="embarked") # no need
data = data.drop(columns="deck") # too many missing values
# %%
not_alone = ((data["sibsp"] > 0) & (data["alone"] != False)).sum()
alone = ((data["sibsp"] == 0) & (data["alone"] != True)).sum()


print(f"Alone: {alone}, Not Alone: {not_alone}")
# alone == False and sibsp > 0 are identical but alone == True and sibsp == 0 are not 
# so we leave as is
# %%
new_data = data.to_csv("/Users/can/Documents/UNI/WiSe 24:25/Intro-to-Python/python package/mypackage/src/mypackage/titanic_new.csv")
# saved the new cleaned data as a new csv file into the mypackage folder in the source folder