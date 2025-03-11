#%%
import pandas as pd
import os
#%%
os.chdir("/Users/can/Documents/UNI/WiSe 24:25/Intro-to-Python")
data = pd.read_csv("titanic.csv", index_col=0)
# %%
data.shape
# (891, 11)
data.describe()
# the first statistical information (min, max, mean, etc.)
# %%
data.isna().sum()
# The number of all NA values is 866 so if we dropped them it would mean we wouldn't have a lot 
# of data to work with. So we decided to fill these values with the median of each column.
# Because the fillna() function only works with int values we diceded to ignore the NA values in 
# the "Cabin" column
# %%
data["Age"].fillna(data["Age"].mean(), inplace=True)
# %%
new_data = data.drop(columns=["Cabin"])
# removed the column "Cabin" because it had too many missing values that are of no importance and saved
# the new cleaned data to the variable "new_data"
# %%
new_data.head()
new_data.tail(20)
# %%
new_data.isna().sum()
# %%
new_data.to_csv("/Users/can/Documents/UNI/WiSe 24:25/Intro-to-Python/python package/mypackage/src/mypackage/titanic_new.csv")
# saved the new cleaned data as a new csv file into the mypackage folder in the source folder