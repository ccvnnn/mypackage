# %%
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
        """Provides statistical summaries for a specific column in the dataset.
        
        
        Parameters
        ----------
        column: str
            The name of the column to analyze. This should be a name of one
            of the columns in the Titanic dataset.
        
        
        Returns
        -------
        panda.Series
            A Series containing basic statistics about the specific column.
            
            numerical variables use the following statistics:
            count: number of non-missing values
            mean: average of the values
            std: standard deviation
            min: minimum value
            25%, 50%, 75%: percentiles (quartiles and median)
            max: maximum value
            
            categorial variables use the following statistics:
            count: number of non-missing values
            unique: number of categories
            top: most frequent category
            freq: frequency of the most frequent category
            
        Notes
        -----
        The output statistics depend on the type of the column as described
        in 'Returns.'
        
        
        Examples
        --------
        analyzer.get_stats(column="age")
        
        Output:
        count    891.000000
        mean      30.295365
        std       13.058707
        min        0.420000
        25%       22.000000
        50%       32.000000
        75%       35.000000
        max       80.000000
        Name: age, dtype: float64
        
        
        analyzer.get_stats(column="embark_town")
        
        count             889
        unique              3
        top       Southampton
        freq              644
        Name: embark_town, dtype: object
        
        """
        return self.data[column].describe()


   
    def cramers_v(self, chi2, contingency_table):
        n = contingency_table.sum().sum()
        min_dim = min(contingency_table.shape) - 1
        return np.sqrt(chi2 / (n * min_dim))
    
    
    
    def chi_square_test(self, column1: str, column2: str):
        """Does a Chi-Square test to analyze the relationship
        between two categorical variables.
       
       
        Parameters
        ----------
        column1, column2: str
           The names of the columns to analyze. These should be two strings
           corresponding to the column names in the Titanic dataset.
        
        
        Returns
        -------
        chi2: float
           The Chi-Square statistic which measures the difference between
           observed and expected frequencies.
        p: float
           The p-value indicating statistical significance.
        v: float
           Cramer's V value which measures the strength of association
           between the two variables.
       
           
        Notes
        -----
        The Chi-Square test is only used for categorical variables.
        A p-value < 0.05 indicates a statistically significant relationship
        between the two categorical variables.
        Cramer's V value ranges from 0 to 1. Values close to 0 indicate weak
        association and values near 1 indicate a strong association.
       
       
        Examples
        --------
        analyzer.chi_square_test(column1 = "pclass", column2 = "survived")
        
        Ouptput:
        There is a statistically significant relationship between pclass and survived
        Out[13]: (102.88898875696056, 4.549251711298793e-23, 0.33981738800531175)
        
        """
        contigency_table = pd.crosstab(self.data[column1], self.data[column2])
        chi2, p, dof, expected = chi2_contingency(contigency_table)
        v = self.cramers_v(chi2, contigency_table)

        alpha = 0.05
        if p < alpha: print(f"There is a statistically significant relationship between {column1} and {column2}")
        else: print(f"\n There is no significant relationship between {column1} and {column2} \n")
       
        return chi2, p, v
    
    
    
    def ccf_categorization_mean(self):
        """City-Class-Fare categorization gives us the avergage/amount
        price paid per class for every embarked town"""

        grouped = self.data.groupby(["embark_town", "pclass"])["fare"]
        grouped_stats = grouped.agg(["mean", "min", "max", "count"]).reset_index()
        pivot_table_mean = grouped_stats.pivot(index='embark_town', columns='pclass', values='mean')
    
        return pivot_table_mean
    

    def ccf_categorization_count(self):
        grouped = self.data.groupby(["embark_town", "pclass"])["fare"]
        grouped_stats = grouped.agg(["mean", "min", "max", "count"]).reset_index()
        pivot_table_count = grouped_stats.pivot(index='embark_town', columns='pclass', values = 'count')
        return pivot_table_count
    

    def survival_rate(self, group_by_column: str):
        """ computes survival rates grouped by a specific column (categorial variable)"""
        survival_rates = self.data.groupby(group_by_column)["survived"].mean()
        return survival_rates


# %%
analyzer = Analyzer(data)
# %%
# use the ccf_categorization method to analyze the average fare by embark town
# and passenger class and the passenger count by embark town and passenger "class"

analyzer.ccf_categorization_mean()
# Average fare by embark town and passenger class:
# pclass                1          2          3
# embark_town
# Cherbourg    104.718529  25.358335  11.214083
# Queenstown    90.000000  12.350000  11.183393
# Southampton   70.364862  20.327439  14.644083

analyzer.ccf_categorization_count()
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
analyzer.chi_square_test("age", "fare")
