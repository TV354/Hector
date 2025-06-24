import pandas as pd
import requests
import pandas as pd
import numpy.random as npr
import matplotlib.pyplot as plt

import Goal_botcount_ratio as gbr
import find_goals as fg
import bot_lists as bl
import get_run_time as grt



# Define the GitHub repo and folder path
user = "TV354"
repo = "Hector"
folder = "Dataframes/Evaluation"
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

def gbr_analysis(dataframes):
    # array for the goal-botcount-ratio for evaluation
    temp_gbr_statistic = []

    # loop through all dfs
    for i in range(0, len(dataframes)):

        # check multiple parts of the field
        for l in range(50, 100, 10):

            current_gbr = gbr.Goal_botcount_ratio(dataframes[i], l)

            # convert all created dfs to a singular array
            for n in current_gbr.index:
                temp_gbr_statistic.append([100 - l, current_gbr.loc[n, 'attacker count'], current_gbr.loc[n, 'defender count'], current_gbr.loc[n, 'attacker count'] / current_gbr.loc[n, 'defender count']])

    gbr_statistic = pd.DataFrame(temp_gbr_statistic, columns=['part of field in %', 'attacker count', 'defender count', 'ratio'])

    

    ## CODE FOR CREATING THE PLOTS OF THE CODE
    ## if you have any questions about the functionality of this, ask somebody else, i have no idea how this stuff works

    field_parts = sorted(gbr_statistic['part of field in %'].unique())
    num_parts = len(field_parts)

    fig, axes = plt.subplots(num_parts, 2, figsize=(14, 5 * num_parts))
    if num_parts == 1:
        axes = axes.reshape(1, 2)

    # Determine global x-axis ranges to enforce consistent bar width
    max_attackers = gbr_statistic['attacker count'].max()
    max_defenders = gbr_statistic['defender count'].max()
    attacker_range = range(0, max_attackers + 1)
    defender_range = range(0, max_defenders + 1)

    for idx, part in enumerate(field_parts):
        group = gbr_statistic[gbr_statistic['part of field in %'] == part]

        # Count frequencies and reindex with full range to ensure consistent bar width
        attacker_counts = group['attacker count'].value_counts().sort_index().reindex(attacker_range, fill_value=0)
        defender_counts = group['defender count'].value_counts().sort_index().reindex(defender_range, fill_value=0)

        # Plot attacker bars
        axes[idx, 0].bar(attacker_counts.index, attacker_counts.values, color='skyblue', width=0.8)
        axes[idx, 0].set_title(f"{part}% Field — Goals by Attacker Count")
        axes[idx, 0].set_xlabel("Attacker Count")
        axes[idx, 0].set_ylabel("Goals Scored")
        axes[idx, 0].set_xticks(attacker_range)

        # Plot defender bars
        axes[idx, 1].bar(defender_counts.index, defender_counts.values, color='salmon', width=0.8)
        axes[idx, 1].set_title(f"{part}% Field — Goals by Defender Count")
        axes[idx, 1].set_xlabel("Defender Count")
        axes[idx, 1].set_ylabel("Goals Scored")
        axes[idx, 1].set_xticks(defender_range)

    plt.tight_layout()
    plt.show()


gbr_analysis(dataframes)