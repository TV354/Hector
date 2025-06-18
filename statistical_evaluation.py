import pandas as pd
import requests
import pandas as pd
import numpy.random as npr

import Goal_botcount_ratio as gbr
import find_goals as fg
import bot_lists as bl
import get_run_time as grt

# Define the GitHub repo and folder path
user = "TV354"
repo = "Hector"
folder = "Dataframes/for Evaluation"
branch = "main"

# GitHub API URL to list folder contents
api_url = f"https://api.github.com/repos/{user}/{repo}/contents/{folder}?ref={branch}"

# Request folder contents
response = requests.get(api_url)
response.raise_for_status()  # Raise error if request failed
files = response.json()

# Filter only CSV files and download each one
dataframes = []
for file_info in files:
    if file_info['name'].endswith('.csv'):
        raw_url = file_info['download_url']  # Raw file download URL
        df = pd.read_csv(raw_url, index_col=0)
        dataframes.append(df)


gbr_statistic = []

for i in range(0, len(dataframes)):
    for l in range(50, 100, 10):
        for n in range(0, len(gbr.Goal_botcount_ratio(dataframes[i], l))):
            if (gbr.Goal_botcount_ratio(dataframes[i], l).loc[n, "side"] == "Y_side"):
                gbr_statistic.append([l, gbr.Goal_botcount_ratio(dataframes[i], l).loc[n, "botcount yellow"], gbr.Goal_botcount_ratio(dataframes[i], l).loc[n, "botcount blue"]])

print(len(gbr_statistic))

