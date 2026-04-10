# AutoViz Example Code Snippet
""" Meant to facilitate EDA (Exploratory Data Analysis) by providing a 
    quick and easy way to visualize data from a CSV file. Allows users to 
    generate a variety of plots and charts to understand the distribution, 
    relationships, and patterns in the data that may be interesting to explore.
    Can also be used to visualize data from a DataFrame directly, but this example uses a CSV file.
    Can also indentify outliers, missing values, and other data quality issues 
    that may need to be addressed before further analysis."""

from autoviz import AutoViz_Class
AV = AutoViz_Class()

# Visualizing a CSV file directly
filename = "data.csv" # Replace with your actual file path. If the file is in the same directory, just use the file name.
# target_variable = "column_name" # uncomment and replace depVar below if you want to specify a target variable for analysis.

dft = AV.AutoViz(
    filename, 
    sep=",", 
    depVar= "", 
    dfte=None, # replace with name of DataFrame if using pandas DataFrame instead of CSV file.
    header=0, 
    verbose=1, 
    lowess=False, 
    chart_format="svg", 
    max_rows_analyzed=150000, 
    max_cols_analyzed=30
)
