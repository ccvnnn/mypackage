#%%
import pandas as pd
import numpy as np
import scipy
from scipy.stats import chi2_contingency
# %%
data = pd.read_csv("cleaned_data.csv", index_col=0)
# %%
data.head(n = 10)
# %%
class Analyzer:
    """Analyzer class gives us functions that are crucial for analysis of a dataset."""
    def __init__(self, data):
        self.data = data
    
    def get_stats(self, column: str):
        return data[column].describe()

    def chi_square_test(self, column1: str, column2: str):
       contigency_table = pd.crosstab(self.data[column1], self.data[column2])
       chi2, p, dof, expected = chi2_contingency(contigency_table)

       alpha = 0.05
       if p < alpha: print(f"There is a statistically significant relationship between {column1} and {column2}")
       else: print(f"\n There is no significant relationship between {column1} and {column2} \n")
       print(f"\n Chi-Square Statistic: {chi2:.4f}")
       print(f"P-value: {p}\n\n")

    
    
# %%
def all_sex(data):
    all_male = sum(data["Sex"]== "male")
    all_female = sum(data["Sex"]== "female")
# Diese Funktion ist einfach hier. Ich weiß jetzt nicht ob die relevant sein könnte deswegen steht diese hier.
# %%
analyzer = Analyzer(data)

# %%
# test cases
analyzer.chi_square_test(column1 = "pclass", column2 = "survived")
analyzer.chi_square_test(column1 = "age", column2 = "survived")
analyzer.chi_square_test(column1 = "age", column2 = "pclass")
# %%
# test cases
analyzer.get_stats(column="pclass")
analyzer.get_stats(column="age")
# %%

# check change in fare price with each class.
# with what fare price is a passenger in class 1,2 or 3?

# is the fare price different for each city where the passengers embarked
## did passengers pay more for first class in southampton that passengers in compton?

# %%
def class_fare_categorization():
    pass