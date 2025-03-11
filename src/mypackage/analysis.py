#%%
import pandas as pd
import numpy as np
# %%
data = pd.read_csv("titanic_new.csv", index_col=0)
# %%
data.head()
# %%
class Analyzer:
    """Analyzer class gives us functions that are crucial for analysis of a dataset."""
    def __init__(self, method):
        self.method = method
    
    def statistics(self, data, column: str):
        Mean = data[column].mean()
        Median = data[column].median()
        Std = data[column].std()
        Var = data[column].var()
    
    def multiple_variable(self, data, column1: str, column2: str):
        Korr = data.corr(data[column1],data[column2])

    
# %%
def all_sex(data):
    all_male = sum(data["Sex"]== "male")
    all_female = sum(data["Sex"]== "female")
    

