# AutoViz Example Code Snippet
""" Meant to facilitate EDA (Exploratory Data Analysis) by providing a 
    quick and easy way to visualize data from a CSV file. Allows users to 
    generate a variety of plots and charts to understand the distribution, 
    relationships, and patterns in the data that may be interesting to explore.
    Can also be used to visualize data from a DataFrame directly, but this example uses a CSV file.
    Can also indentify outliers, missing values, and other data quality issues 
    that may need to be addressed before further analysis.
    Working example using the California housing dataset from sklearn."""


from autoviz import AutoViz_Class
import pandas as pd
from sklearn.datasets import fetch_california_housing

AV = AutoViz_Class()

data = fetch_california_housing() 
data = pd.DataFrame(fetch_california_housing().data, 
                    columns=fetch_california_housing().feature_names)
data['MedHouseVal'] = fetch_california_housing().target
# Visualizing a CSV file directly
filename = "data.csv" # Replace with your actual file path. If the file is in the same directory, just use the file name.
# target_variable = "column_name" # uncomment and replace depVar below if you want to specify a target variable for analysis.

dft = AV.AutoViz(
    filename="", # leave blank if using dfte instead of filename
    sep=",", 
    depVar= "", 
    dfte=data, # replace with name of DataFrame if using pandas DataFrame instead of CSV file.
    header=0, 
    verbose=2, # change to 1 for output in notebook
    lowess=False, 
    chart_format="svg", 
    max_rows_analyzed=150000, 
    max_cols_analyzed=30
)
