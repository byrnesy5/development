
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt


# Import Data
conn = sqlite3.connect('C:/Users/ByrnesA/github_development/database.sqlite')

df = pd.read_sql('SELECT * FROM Match', conn)
df.head()

conn.close()


for x in df.columns:
    print(x)


df[['home_player_X1', 'home_player_Y1', 'home_player_1']].tail()


df.season.value_counts()

# Create target
def result_func(home,away):
    if home > away:
        return 'win'
    elif home < away:
        return 'lose'
    else:
        return 'draw'

df['result'] = df.apply(lambda x: result_func(x['home_team_goal'], x['away_team_goal']), axis=1)

df['result'].value_counts()



df_trim = df[['match_api_id', 'result', 'B365H', 'B365D', 'B365A']]

df_trim.describe()


df_trim['card'].value_counts()


df_trim['B365H'].hist(bins = 20)