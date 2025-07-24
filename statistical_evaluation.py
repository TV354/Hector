import pandas as pd
import requests
import numpy as np
import pandas as pd
import numpy.random as npr
import matplotlib.pyplot as plt

import Goal_botcount_ratio as gbr
import find_goals as fg
import bot_lists as bl
import get_run_time as grt
import ball_movements as bm


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
        for l in range(0, 50, 5):

            current_gbr = gbr.Goal_botcount_ratio(dataframes[i], l)

            # convert all created dfs to a singular array
            for n in current_gbr.index:
                temp_gbr_statistic.append([50 - l, current_gbr.loc[n, 'attacker count'], current_gbr.loc[n, 'defender count'], current_gbr.loc[n, 'attacker count'] / current_gbr.loc[n, 'defender count']])

    gbr_statistic = pd.DataFrame(temp_gbr_statistic, columns=['part of field in %', 'attacker count', 'defender count', 'ratio'])

    

    ## CODE FOR CREATING THE PLOTS OF THE CODE
    ## if you have any questions about the functionality of this, ask somebody else, i have no idea how this stuff works

    # Visualization
    field_parts = sorted(gbr_statistic['part of field in %'].unique())
    bar_width = 0.3

    for part in field_parts:
        group = gbr_statistic[gbr_statistic['part of field in %'] == part]

        fig, axes = plt.subplots(1, 2, figsize=(14, 5))

        # Attacker plot
        attacker_counts = group['attacker count'].value_counts().sort_index()
        attacker_x = np.arange(len(attacker_counts))
        axes[0].bar(attacker_x, attacker_counts.values, color='skyblue', width=bar_width)
        axes[0].set_xticks(attacker_x)
        axes[0].set_xticklabels(attacker_counts.index)
        axes[0].set_title(f"{part}% Field — Goals by Attacker Count")
        axes[0].set_xlabel("Attacker Count")
        axes[0].set_ylabel("Goals Scored")

        # Defender plot
        defender_counts = group['defender count'].value_counts().sort_index()
        defender_x = np.arange(len(defender_counts))
        axes[1].bar(defender_x, defender_counts.values, color='salmon', width=bar_width)
        axes[1].set_xticks(defender_x)
        axes[1].set_xticklabels(defender_counts.index)
        axes[1].set_title(f"{part}% Field — Goals by Defender Count")
        axes[1].set_xlabel("Defender Count")
        axes[1].set_ylabel("Goals Scored")

        plt.tight_layout()
        plt.show()


def bo_analysis(dataframes):

    for df in dataframes:

        ball_own = bm.ball_ownership(df)
        
        goaltimes = fg.find_goals(df)

        B_Y = ''

        latest = 0

        owned = []

        periods = []


        for i in range(0, len(goaltimes)):

            if ("Y_" in goaltimes[i][1]):
                B_Y = ' Y'
            else:
                B_Y = ' B'

            for l in range(1, len(ball_own.index)):
                
                if ((ball_own.iloc[l]['time'] > goaltimes[i][0]) and (ball_own.iloc[l - 1]['time'] <= goaltimes[i][0])):

                    latest = ball_own.index[l - 1]
                    break

            for l in range(latest, 0, -1):

                if (B_Y in ball_own.iloc[goaltimes[l][0]]['bot']):

                    owned.append(l)
                    print("test")
                
                else:
                    break

            periods.append[owned[0] - owned[len(owned) - 1]]

         # Create a DataFrame and count goals per possession duration
        df_plot = pd.Series(periods).value_counts().sort_index()

        # Plot
        plt.figure(figsize=(10, 6))
        plt.plot(df_plot.index, df_plot.values, marker='o', linestyle='-', color='purple')
        plt.title("Number of Goals by Length of Possession Period")
        plt.xlabel("Possession Length (in frames or units)")
        plt.ylabel("Number of Goals")
        plt.grid(True)
        plt.tight_layout()
        plt.show() 









#gbr_analysis(dataframes)
gbr_analysis(dataframes)