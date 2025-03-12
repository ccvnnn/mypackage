#%%
import pandas as pd
import os
#%%
os.chdir("/Users/can/Documents/UNI/WiSe 24:25/Intro-to-Python")
data = pd.read_csv("titanic.csv", index_col=0)
# %%
data.shape # (891, 11)
data.describe() # the first statistical information (min, max, mean, etc.)
# %%
data.isna().sum()
# The number of all NA values is 866 (mostly in the "Cabin" column) so if we dropped them it would mean we wouldn't have a lot 
# of data to work with. So we decided to remove the column "Cabin" because it had too many missing values that are of no importance and saved
# the new cleaned data to the variable "new_data"
# %%
data["Age"].fillna(data["Age"].mean(), inplace=True)
# because the "Age" column had only a couple NA values we filled them  with the mean of the entire column
# %%
new_data = data.drop(columns=["Cabin"])
# removed the column "Cabin" because it had too many missing values that are of no importance and saved
# the new cleaned data to the variable "new_data"
# %%
new_data.head()
new_data.tail(20)
# quick check if everything was changed 
# %%
new_data.isna().sum()
# %%
new_data.to_csv("/Users/can/Documents/UNI/WiSe 24:25/Intro-to-Python/python package/mypackage/src/mypackage/titanic_new.csv")
# saved the new cleaned data as a new csv file into the mypackage folder in the source folder