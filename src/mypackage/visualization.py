# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from analysis import Analyzer 
# %%
data = pd.read_csv("cleaned_data.csv", index_col=0)
# %%
# to make the visualizations easier to implement we'll use a class 'Visualizer' that inherits the functions of
# the 'Analzer' class. This helps keep our code clean and makes it more efficient => no need to write the functions again.
# %%
class Visualizer(Analyzer):
    """Visualizer creates visualizations of the analyzed data through the 'Analyzer' class"""

    def __init__(self, data):
        super().__init__(data)

    def distribution_numerical(self, column : str):
        """ plots the distribution of a numerical variable """
        plt.figure(figsize = (8,5))
        sns.histplot(self.data[column], kde = True, color = "blue")
        plt.title(f"Distribution of {column}")
        plt.xlabel(column)
        plt.ylabel("frequency")
        plt.show()
        
    
    def plot_survival_rate(self, group_by_column : str):
        """plots survival rates grouped by a specific column (categorial variable)"""
        survival_rates = self.survival_rate(group_by_column)
        plt.figure(figsize = (8,5))
        survival_rates.sort_values().plot(kind = "bar", color = "darkgrey", alpha = 0.7)
        plt.title(f"Survival rates grouped by {group_by_column}")
        plt.xlabel(group_by_column)
        plt.ylabel("Survival Rate")
        plt.xticks(rotation = 360)
        plt.ylim((0,1))
        plt.show()

    
    def ccf_mean_heatmap(self):
        pivot_table_mean = self.ccf_categorization_mean()
        
        # Create a heatmap for average fare
        plt.figure(figsize=(8, 6))
        sns.heatmap(pivot_table_mean, annot=True, fmt=".2f", cmap="coolwarm")
        plt.title("Average Fare by Embark Town and Passenger Class")
        plt.xlabel("Passenger Class")
        plt.ylabel("Embark Town")
        plt.show()
    
    def ccf_count_heatmap(self):
        pivot_table_count = self.ccf_categorization_count()

        plt.figure(figsize = (8,6))
        sns.heatmap(pivot_table_count, annot=True, fmt=".2f", cmap="coolwarm")
        plt.title("Passenger Count by Embark Town and Passenger Class")
        plt.xlabel("Passenger Class")
        plt.ylabel("Embark Town")
        plt.show()
    
    def plot_contingency_heatmap(self, column1: str, column2: str):
        contingency_table = pd.crosstab(self.data[column1], self.data[column2])
        plt.figure(figsize=(8, 6))
        sns.heatmap(contingency_table, annot=True, cmap="coolwarm", fmt="d")
        plt.title(f'Contingency Table: {column1} vs {column2}')
        plt.xlabel(column2)
        plt.ylabel(column1)
        plt.show()


    
# %%
visualizer = Visualizer(data)
# %%
# use the distribution_numerical method to plot the distribution of a
# numerical variable (e.g. age, fare)
visualizer.distribution_numerical(column = "age")
visualizer.distribution_numerical(column = "fare")
# %%
# use the plot_survival_rate method to plot the survival rates (barplot) grouped by a 
# categorical variable (e.g. who, pclass, sex)
visualizer.plot_survival_rate("who")
visualizer.plot_survival_rate("sex")
visualizer.plot_survival_rate("pclass") 
   
# %%
# plot gives us a heatmap which showcases the average price of the different classes in different towns
visualizer.ccf_mean_heatmap()
# %%
visualizer.ccf_count_heatmap()
# %%
# visualizes the correlation between two categorical variables using a heatmap
visualizer.plot_contingency_heatmap("survived", "pclass")