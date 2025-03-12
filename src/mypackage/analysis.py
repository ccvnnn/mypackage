#%%
import pandas as pd
import numpy as np
import scipy
from scipy.stats import chi2_contingency
# %%
data = pd.read_csv("titanic_new.csv", index_col=0)
# %%
data.head()
# %%
class Analyzer:
    """Analyzer class gives us functions that are crucial for analysis of a dataset."""
    def __init__(self, data):
        self.data = data
        self.results = {}
    
    def statistics(self, data, column: str):
        self.column = column
        self.Mean = data[self.column].mean()
        self.Median = data[self.column].median()
        self.Std = data[self.column].std()
        self.Var = data[self.column].var()
        self.Mode = data[self.column].mode()
        self.Max = data[self.column].max()
        self.Min = data[self.column].min()
    
    def get_stats(self):
        return data[self.column].describe()

    
    def chi_square_test(self, column1: str, column2: str):
       contigency_table = pd.crosstab(self.data[column1], self.data[column2])
       chi2, p, dof, expected = chi2_contingency(contigency_table)

       alpha = 0.05
       if p < alpha: print(f"There is a statistically significant relationship between {column1} and {column2}")
       else: print(f"There is no significant relationship between {column1} and {column2}")
       print(f"Chi-Square Statistic: {chi2:.4f}")
       print(f"P-value: {p}")
    
# %%
def all_sex(data):
    all_male = sum(data["Sex"]== "male")
    all_female = sum(data["Sex"]== "female")
# Diese Funktion ist einfach hier. Ich weiß jetzt nicht ob die relevant sein könnte deswegen steht diese hier.
# %%
analyzer = Analyzer(data)

# test cases
analyzer.chi_square_test(column1 = "Pclass", column2 = "Survived")
analyzer.chi_square_test(column1 = "Age", column2 = "Survived")
analyzer.chi_square_test(column1 = "Age", column2 = "Pclass")
# %%
