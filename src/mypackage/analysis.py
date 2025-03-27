# %%
import pandas as pd
import numpy as np
import os
import scipy
from scipy.stats import chi2_contingency
# %%
# data = pd.read_csv("cleaned_data.csv", index_col=0)
csv_path = os.path.join(os.path.dirname(__file__), 'cleaned_data.csv')
data = pd.read_csv(csv_path, index_col = 0)
# %%
data.head(n = 10)
# %%
class Analyzer:
    """The Analyzer class provides methods for statistical and categorical
    analyses of the Titanic dataset.
    
    
    Attributes
    ----------
    data: pandas.DataFrame
        The Titanic dataset that is going to be analyzed.
    
    """
    
    
    def __init__(self, data):
        """Initializes the class instance with the given (Titanic) dataset
        
        
        Parameters
        ----------
        data: pandas.DataFrame
            The Titanic dataset that is going to be analyzed.
            
        """
        assert isinstance(data, pd.DataFrame), ("Data must be a pandas DataFrame")
        assert not data.empty, "The dataset must not be empty."
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
        pandas.Series
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
        The output statistics depends on the type of the column as described
        in 'Returns'.
        
        
        Examples
        --------
        analyzer = Analyzer(data)
        
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
        assert column in self.data.columns, f"Column '{column}' does not exist in the dataset."
        
        return self.data[column].describe()


   
    def cramers_v(self, chi2, contingency_table):
        """Calculates Cramer's V to measure the association between
        two catgorical variables.
        
        
        Parameters
        ----------
        chi2: flaot
            The Chi-Square statistic from the contingency table.
        contingency_table: pandas.DataFrame
            The contigency table which contains the frequencies for
            categories of the two categorical variables.
        
        
        Returns
        -------
        float
            Cramer's V value which measures the strength of association
            between the two categorical variables.
        
        
        Notes
        -----
        Cramer's V value ranges from 0 to 1. Values close to 0 indicate weak
        association and values near 1 indicate a strong association.
        This method is used for the Chi-Square test between two categorical
        variables.

        """
        assert isinstance(chi2, (float, int)), "The 'chi2' value must be a numeric value."
        assert contingency_table.size > 0, "Contingency table must not be empty."
        
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
        analyzer = Analyzer(data)
        
        analyzer.chi_square_test(column1 = "pclass", column2 = "survived")
        
        Ouptput:
        There is a statistically significant relationship between pclass and survived
        Out[13]: (102.88898875696056, 4.549251711298793e-23, 0.33981738800531175)
        
        """
        assert column1 in self.data.columns, f"Column '{column1}' does not exist in the dataset."
        assert column2 in self.data.columns, f"Column '{column2}' does not exist in the dataset."
        
        contingency_table = pd.crosstab(self.data[column1], self.data[column2])
        
        assert not contingency_table.empty, "Contingency table must not be empty."
        
        chi2, p, dof, expected = chi2_contingency(contingency_table)
        v = self.cramers_v(chi2, contingency_table)

        alpha = 0.05
        if p < alpha: print(f"There is a statistically significant relationship between {column1} and {column2}")
        else: print(f"\n There is no significant relationship between {column1} and {column2} \n")
       
        return chi2, p, v
    
    
    
    def ccf_categorization_mean(self):
        """City-Class-Fare_categorization_mean computes the avergage
        ticket price paid per class for every embarkation town
        
        
        Returns
        -------
        pandas.DataFrame
            pivot-table which includes
            - the three embarkation towns as rows (Cherbourg, Queenstown, Southampton)
            - the three classes as columns (1st, 2nd, 3rd)
            - the average ticket price (fare) paid per class for
              every embarkation town as values
        
        
        Examples
        --------
        analyzer = Analyzer(data)
        
        analyzer.ccf_categorization_mean()
        
        Output:
        pclass                1          2          3
        embark_town
        Cherbourg    104.718529  25.358335  11.214083
        Queenstown    90.000000  12.350000  11.183393
        Southampton   70.364862  20.327439  14.644083
        
        """
        grouped = self.data.groupby(["embark_town", "pclass"])["fare"]
        grouped_stats = grouped.agg(["mean", "min", "max", "count"]).reset_index()
        pivot_table_mean = grouped_stats.pivot(index='embark_town', columns='pclass', values='mean')
    
        return pivot_table_mean
    

    def ccf_categorization_count(self):
        """City-Class-Fare_categorization_count computes the passenger count for
        every passenger class by embarkation towns
    
        
        Returns
        -------
        pandas.DataFrame
            pivot-table which includes
                - the three embarkation towns as rows (Cherbourg, Queenstown, Southampton)
                - the three classes as columns (1st, 2nd, 3rd)
                - the passenger count for every passenger class
                  by embarkation towns as values
        
        
        Examples
        --------
        analyzer = Analyzer(data)
        
        analyzer.ccf_categorization_count()
        
        Output:
        pclass         1    2    3
        embark_town
        Cherbourg     85   17   66
        Queenstown     2    3   72
        Southampton  127  164  353
        
        """
        grouped = self.data.groupby(["embark_town", "pclass"])["fare"]
        grouped_stats = grouped.agg(["mean", "min", "max", "count"]).reset_index()
        pivot_table_count = grouped_stats.pivot(index='embark_town', columns='pclass', values = 'count')
        return pivot_table_count
    

    def survival_rate(self, group_by_column: str):
        """Computes survival rates grouped by a categorical variable.
        
        
        Parameters
        ----------
        group_by_column: str
            The name of the column used to group survival rates.
            This should be a categorical variable.
            
            
        Returns
        -------
        pandas.Series
            A Series containing the survival rates for each category of the
            categorical variable.
            
        
        Examples
        --------
        analyzer = Analyzer(data)
        
        analyzer.survival_rate("who")
        
        Output:
        who
        child    0.590361
        man      0.163873
        woman    0.756458
        Name: survived, dtype: float64
        
        analyzer.survival_rate("pclass")
        
        Output:
        pclass
        1    0.629630
        2    0.472826
        3    0.242363
        Name: survived, dtype: float64
            
        """
        assert group_by_column in self.data.columns, f"Column '{group_by_column}' does not exist in the dataset."
        
        survival_rates = self.data.groupby(group_by_column)["survived"].mean()
        return survival_rates


# %%
analyzer = Analyzer(data)
