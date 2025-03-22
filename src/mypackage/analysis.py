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
    

    def ccf_categorization(self):
        grouped = self.data.groupby(["embark_town", "pclass"])["fare"]

        grouped_stats = grouped.agg(["mean", "min", "max", "count"]).reset_index()
        pivot_table_mean = grouped_stats.pivot(index='embark_town', columns='pclass', values='mean')
        pivot_table_count = grouped_stats.pivot(index='embark_town', columns='pclass', values = 'count')
        print("Average fare by embark town and passenger class:")
        print(pivot_table_mean)
  
        print("\nPassenger count by embark town and passenger class:")
        print(pivot_table_count)
        # return pivot_table_mean, pivot_table_count
    
    def survival_rate(self, group_by_column : str):
        """ computes survival rates grouped by a specific column (categorial variable)"""
        survival_rates = self.data.groupby(group_by_column)["survived"].mean()
        return survival_rates
    
    
# %%
def all_sex(data):
    all_male = sum(data["Sex"]== "male")
    all_female = sum(data["Sex"]== "female")
# Diese Funktion ist einfach hier. Ich weiß jetzt nicht ob die relevant sein könnte deswegen steht diese hier.
# %%
analyzer = Analyzer(data)
# %%
# use the ccf_categorization method to analyze the average fare by embark town
# and passenger class and the passenger count by embark town and passenger class
analyzer.ccf_categorization()
# Average fare by embark town and passenger class:
# pclass                1          2          3
# embark_town                                  
# Cherbourg    104.718529  25.358335  11.214083
# Queenstown    90.000000  12.350000  11.183393
# Southampton   70.364862  20.327439  14.644083

# Passenger count by embark town and passenger class:
# pclass         1    2    3
# embark_town               
# Cherbourg     85   17   66
# Queenstown     2    3   72
# Southampton  127  164  353

# %%
# use the survival_rate method to compute survival rates
# grouped by a categorial variable
# here are some examples 
analyzer.survival_rate("who")
# who
# child    0.590361
# man      0.163873
# woman    0.756458

analyzer.survival_rate("pclass")
# pclass
# 1    0.629630
# 2    0.472826
# 3    0.242363

# %%
# use the chi_square_test method to check if there is a statistically significant
# relationship between two categorial variables
# here are some examples
analyzer.chi_square_test(column1 = "pclass", column2 = "survived")
# There is a statistically significant relationship between pclass and survived
# Chi-Square Statistic: 102.8890
# P-value: 4.549251711298793e-23 < 0.05

analyzer.chi_square_test(column1 = "who", column2 = "survived")
# There is a statistically significant relationship between who and survived
# Chi-Square Statistic: 283.9231
# P-value: 2.2227620817798914e-62 < 0.05


# %%
# use the get_stats method to receive basic statistics 
# (mean, std, min, max, median etc.) for the respective column of the dataset
# here are some examples
analyzer.get_stats(column="pclass")
analyzer.get_stats(column="age")
analyzer.get_stats(column="survived")

# this method also works for categorial variables like "sex" and "embark_town"
# you will receive count (absolute frequency), unique (number of categories),
# top (most frequent category) and freq (absolute frequency of the most frequent
# category)
analyzer.get_stats(column="sex") 
analyzer.get_stats(column="embark_town")
# %%

# check change in fare price with each class.
# with what fare price is a passenger in class 1,2 or 3?

# is the fare price different for each city where the passengers embarked
## did passengers pay more for first class in southampton that passengers in compton?

# %%
class_fare_df = data.groupby("pclass").agg(
    avg_fare = ("fare", "mean"),
    min_fare = ("fare", "min"),
    max_fare = ("fare", "max")
)

class_fare_df

# %%
