# %%
import pandas as pd
import os
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
from mypackage.analysis import Analyzer
# %%
# data = pd.read_csv("cleaned_data.csv", index_col=0)
csv_path = os.path.join(os.path.dirname(__file__), 'cleaned_data.csv')
data = pd.read_csv(csv_path, index_col = 0)
# %%
# to make the visualizations easier to implement we'll use a class 'Visualizer' that inherits the functions of
# the 'Analyzer' class. This helps keep our code clean and makes it more efficient
# => no need to write the functions again.
# %%
class Visualizer(Analyzer):
    """Visualizer creates visualizations of the analyzed data through the 'Analyzer' class.
    It includes methods for plotting distributions, generating heatmaps and
    creating scatterplots.
    
    
    Attributes
    ----------
    data: pandas.DataFrame
        The Titanic dataset that is going to be analyzed.
    
    """


    def __init__(self, data):
        """Initializes the class instance with the given (Titanic) dataset.
        
        
        Parameters
        ----------
        data: pandas.DataFrame
            The Titanic dataset that is going to be analyzed.
            
        """
        # check if the dataset is stored as a pandas DataFrame
        assert isinstance(data, pd.DataFrame), ("Data must be a pandas DataFrame")
        
        super().__init__(data)



    def distribution_numerical(self, column: str):
        """Plots the distribution of observations for a numerical variable
        using a histogram and a kde curve.
        
        
        Parameters
        ----------
        column: str
            The name of the column to analyze. This should be a name of one
            of the columns in the Titanic dataset and must represent
            a numerical variable.
        
        
        Notes
        -----
        Although this method can technically be used with categorical variables,
        it is designed for numerical variables.
        
        
        Examples
        --------
        visualizer = Visualizer(data)
        
        visualizer.distribution_numerical(column = "age")
       
        visualizer.distribution_numerical(column = "fare")
        
        This will generate a histogram that shows the distribution of the numerical
        variables 'age' and 'fare' with an overlaid kde curve.
        
        """
        # check if the passed column exists in the dataset
        assert column in self.data.columns, f"Column '{column}' does not exist in the dataset."
        
        plt.figure(figsize = (8,5))  # creates a new figure
        sns.histplot(self.data[column], kde = True, color = "blue")  # generates a
        # histogram with an overlaid kde curve and sets the color to blue
        plt.title(f"Distribution of {column}")  # adds a title
        plt.xlabel(column)  # label the x-axis with column name
        plt.ylabel("frequency")  # adds label for the y-axis
        plt.show()  # displays the histogram and the kde curve
        
    
    
    def plot_survival_rate(self, group_by_column: str):
        """Plots survival rates grouped by a categorical variable as a barplot.
        
        
        Parameters
        ----------
        group_by_column: str
            The name of the column used to group survival rates.
            This should be a categorical variable.
            
        
        Examples
        --------
        visualizer = Visualizer(data)
        
        visualizer.plot_survival_rate("who")
        
        visualizer.plot_survival_rate("pclass")
        
        This will generate barplots of the survival rates grouped by the
        specific categorical variable ('who', 'pclass').
        
        """
        # check if the column used to group the survival rates exists in the dataset
        assert group_by_column in self.data.columns, f"Column '{group_by_column}' does not exist in the dataset."
        
        # computes survival rates grouped by the specified column
        survival_rates = self.survival_rate(group_by_column)
        
        plt.figure(figsize = (8,5))  # creates a new figure
        survival_rates.sort_values().plot(kind = "bar", color = "darkgrey", alpha = 0.7)
        # plots survival rates as a barplot, sorts values for better visualization
        plt.title(f"Survival rates grouped by {group_by_column}")  # adds title
        plt.xlabel(group_by_column)  # adds label to the x-axis
        plt.ylabel("Survival Rate")  # adds label to the y-axis
        plt.xticks(rotation = 360)  # rotates labels for better visualization
        plt.ylim((0,1))  # sets limits for the y-axis from 0 to 1 since survival rates are proportions
        plt.show()  # displays the barplot


    
    def ccf_mean_heatmap(self):
        """Creates a heatmap to visualize the average ticket price by
        embarked town and passenger class.
        
        
        Notes
        -----
        This method uses the pivot table generated by the method
        'ccf_categorization_mean' from the Analyzer class.
        
        
        Examples
        --------
        visualizer = Visualizer(data)
        
        visualizer.ccf_mean_heatmap()
        
        This will generate a heatmap which contains
        - the three embarked towns as rows (Cherbourg, Queenstown, Southampton)
        - the three passenger classes as columns (1st, 2nd, 3rd)
        - the average ticket price by embarked town and passenger class as values
        
        """
        # generates the pivot table using the 'ccf_categorization_mean' method
        # from the Analyzer class
        # The pivot table contains average ticket prices grouped by
        # embarked town and passenger class.
        pivot_table_mean = self.ccf_categorization_mean()
        
        plt.figure(figsize=(8, 6))  # creates a new figure
        sns.heatmap(pivot_table_mean, annot=True, fmt=".2f", cmap="coolwarm")
        # creates a heatmap to visualize the average ticket prices, annot = True
        # to display the values inside the cells
        plt.title("Average Fare by Embark Town and Passenger Class")  # adds title
        plt.xlabel("Passenger Class")  # adds label to the x-axis
        plt.ylabel("Embark Town")  # adds label to the y-axis
        plt.show()  # displays the heatmap
    
    
    
    def ccf_count_heatmap(self):
        """Creates a heatmap to visualize the passenger count by
        embarked town and passenger class.
        
        
        Notes
        -----
        This method uses the pivot table generated by the method
        'ccf_categorization_count' from the Analyzer class.
        
        
        Examples
        --------
        visualizer = Visualizer(data)
        
        visualizer.ccf_count_heatmap()
        
        This will generate a heatmap which contains
        - the three embarked towns as rows (Cherbourg, Queenstown, Southampton)
        - the three passenger classes as columns (1st, 2nd, 3rd)
        - the passenger count by embarked town and passenger class as values
        
        """
        # generates the pivot table using the 'ccf_categorization_count' method
        # from the Analyzer class
        # The pivot table contains the passenger count grouped by
        # embarked town and passenger class.
        pivot_table_count = self.ccf_categorization_count()

        plt.figure(figsize = (8,6))  # creates a new figure
        sns.heatmap(pivot_table_count, annot=True, fmt=".2f", cmap="coolwarm")
        # creates a heatmap to visualize the passenger count, annot = True to
        # display the values inside the cells
        plt.title("Passenger Count by Embark Town and Passenger Class")  # adds a title
        plt.xlabel("Passenger Class")  # labels the x-axis
        plt.ylabel("Embark Town")  # labels the y-axis
        plt.show()  # displays the heatmap
        
        
    def plot_contingency_heatmap(self, column1: str, column2: str):
        """Creates a heatmap to visualize the contingency table between
        two categorical variables.
        
        
        Parameters
        ----------
        column1: str
            The name of the first column to analyze.
            This should be a categorical variable.
        column2: str
            The name of the second column to analyze.
            This should also be a categorical variable.
            
            
        Examples
        --------
        visualizer = Visualizer(data)
        
        visualizer.plot_contingency_heatmap("survived", "pclass")
        
        This will generate a heatmap which includes
        - the survival status as rows (0 and 1 for not survived and survived)
        - the three passenger classes (1st, 2nd, 3rd)
        - the frequencies for each combination of 'survived' and 'pclass' as values
        
        """
        # check if the passed columns exist in the dataset
        assert column1 in self.data.columns, f"Column '{column1}' does not exist in the dataset."
        assert column2 in self.data.columns, f"Column '{column2}' does not exist in the dataset."
        
        # generates a contingency table for every combination of values
        # between column1 and column2
        contingency_table = pd.crosstab(self.data[column1], self.data[column2])
        
        plt.figure(figsize=(8, 6))  # creates a new figure
        sns.heatmap(contingency_table, annot=True, cmap="coolwarm", fmt="d")
        # generates a heatmap to visualize the relationship between two categorical variables,
        # annot = True to display the frequencies inside the cells
        plt.title(f'Contingency Table: {column1} vs {column2}')  # adds a title
        plt.xlabel(column2)  # labels the x-axis with the name of column2
        plt.ylabel(column1)  # labels the y-axis with the name of column1
        plt.show()  # displays the heatmap



    def basic_scatterplot(self, column1: str, column2: str):
        """Creates a scatterplot to visualize the relationship
        between two numerical variables.
        
        
        Parameters
        ----------
        column1: str
            The name of the column that is used for the x-axis.
            This should be a numerical variable.
        column2: str
            The name of the column that is used for the y-axis.
            This should also be a numerical variable.
            
        
        Notes
        -----
        The y-axis is set to a logarithmic scale.
        alpha = 0.5 is used for better visibility of the scatter points
        
        
        Examples
        --------
        visualizer = Visualizer(data)
        
        visualizer.basic_scatterplot("age", "fare")
        
        This will generate a scatterplot and visualize how age relates to
        the ticket price.
        
        """
        # check if the passed columns exist in the dataset
        assert column1 in self.data.columns, f"Column '{column1}' does not exist in the dataset."
        assert column2 in self.data.columns, f"Column '{column2}' does not exist in the dataset."
        
        plt.figure(figsize=(10, 6))  # creates a new figure
        sns.regplot(x = column1, y = column2, data=data, scatter_kws={'alpha': 0.5})
        # generates a scatterplot using seaborn, scatter_kws={'alpha': 0.5} sets
        # transparency of points to 0.5 for better visualization
        plt.yscale('log')  # makes the y-axis logarithmic

        fare_ticks = [1, 5, 10, 20, 50, 100, 200, 500]  # example values (ticket prices)
        # for better visualization
        plt.yticks(fare_ticks, fare_ticks)
        plt.title(f"Scatterplot of {column1} vs {column2}")  # adds title
        plt.xlabel(column1)  # adds label to the x-axis using the name of column1
        plt.ylabel(column2)  # adds label to the y-axis using the name of column2
        plt.show()  # displays the scatterplot
    
    
    
    def scatterplot_sorted_by(self, column1: str, column2: str, hue: str):
        """Creates a scatterplot to visualize the relationship between two
        numerical variables grouped by categorical variable.
        
        Parameters
        ----------
        column1: str
            The name of the column that is used for the x-axis.
            This should be a numerical variable.
        column2: str
            The name of the column that is used for the y-axis.
            This should also be a numerical variable.
        hue: str
            The name of the column representing the groups.
            This should be a categorical variable.
            
        
        Notes
        -----
        The y-axis is set to a logarithmic scale.
        
        
        Examples
        --------
        visualizer = Visualizer(data)
        
        visualizer.scatterplot_sorted_by("age","fare", hue="pclass")
        
        This will generate a scatterplot and visualize how age relates to
        the ticket price grouped by the ticket price.
        
        """
        # check if the passed columns exist in the dataset
        assert column1 in self.data.columns, f"Column '{column1}' does not exist in the dataset."
        assert column2 in self.data.columns, f"Column '{column2}' does not exist in the dataset."
        assert hue in self.data.columns, f"Column '{hue}' does not exist in the dataset."
       
        sns.lmplot(x = column1, y = column2, data=data, hue = hue, aspect=1.5, scatter_kws={'alpha': 0.5})
        # generates a scatterplot using seaborn, scatter_kws={'alpha': 0.5} sets
        # transparency of points to 0.5 for better visualization
        plt.yscale('log')  # makes the y-axis logarithmic

        fare_ticks = [1, 5, 10, 20, 50, 100, 200, 500]  # example values (ticket prices)
        # for better visualization
        plt.yticks(fare_ticks, fare_ticks)  # setting the ticks for the y axis
        plt.title(f"Scatterplot of {column1} vs {column2} by {hue}")  # adds title
        plt.xlabel(column1)  # adds label to the x-axis using the name of column1
        plt.ylabel(column2)  # adds label to the y-axis using the name of column2
        plt.show()  # displays the scatterplot

    
# %%
# The following part includes a few function calls to check our written methods.

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
# %%
visualizer.basic_scatterplot("age", "fare")
# %%
visualizer.scatterplot_sorted_by("age","fare", hue="pclass")
