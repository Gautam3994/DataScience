import pandas as pd

jobsDf = pd.read_csv("glassdoor_jobs.csv")
salsDf = pd.read_csv("glassdoor_salaries.csv")

jobsDf['Company Name'] = jobsDf['Company Name'].str.lower()
jobsDf['Company Name'] = jobsDf['Company Name'].str.split("\n").str[0]



