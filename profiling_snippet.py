# FILE: 01_data_profiling.py
# Use this first to understand your data and find missing values.
# Requires: pip install ydata-profiling pandas

import pandas as pd
from ydata_profiling import ProfileReport

# --- INSTRUCTIONS ---
# 1. Change 'your_data.csv' to your filename.
# 2. Run: python 01_data_profiling.py
# 3. Open 'data_report.html' in any browser.

df = pd.read_csv('your_data.csv')

print("Generating Data Profile... this may take a minute.")
profile = ProfileReport(df, title="Hackathon Data Report", explorative=True)

# Saves an interactive report to your folder
profile.to_file("data_report.html")
print("Done! Open data_report.html to see the results.")
