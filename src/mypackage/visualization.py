# %%
import pandas as pd
import matplotlib.pyplot as plt
from analysis import Analyzer 
# %%
# to make the visualizations easier to implement we'll use a class 'Visualizer' that inherits the functions of
# the 'Analzer' class. This helps keep our code clean and makes it more efficient => no need to write the functions again.
class Visualizer(Analyzer):
    """Visualizer creates visualizations of the analyzed data through the 'Analyzer' class"""
    pass
