"""
# FILE: profiling_snippet.py
# Use this first to understand your data and find missing values.
# Requires: pip install ydata-profiling pandas
# working example using the California housing dataset, 
# replace with your own data by commenting out the fetch_california_housing() 
# lines and uncommenting the pd.read_csv line. 
"""
import pandas as pd
from sklearn.datasets import fetch_california_housing
from ydata_profiling import ProfileReport

# --- INSTRUCTIONS ---
# 1. Change the data variable to your filename/path & comment out the fetch_california_housing() lines if you want to read from a csv instead of using the sample dataset. Make sure to uncomment the pd.read_csv line and replace 'your_data.csv' with your actual file path.
# 2. Run: python 01_data_profiling.py
# 3. Open 'data_report.html' in any browser.
data = fetch_california_housing()
data = pd.DataFrame(fetch_california_housing().data,
                    columns=fetch_california_housing().feature_names)
data['MedHouseVal'] = fetch_california_housing().target
# data = pd.read_csv('your_data.csv') # uncomment to read from csv

print("Generating Data Profile... this may take a minute.")
profile = ProfileReport(data, title="Hackathon Data Report", explorative=True)

# Saves an interactive report to your folder
profile.to_file("data_report.html")
print("Done! Open data_report.html to see the results.")
