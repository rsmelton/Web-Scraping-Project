'''
Robert Scott Melton
CS323-001
Mini Project 2 - Web Scraping
3/17/2023

The page that I scraped holds information about the UA basketball team (2022-2023) 
including statistics such as Minutes played, Fields goals made, Field goal attempts, 
and many more. What I did with this information was to display each players name, 
position they play, and all of their statistics from all the games they have played.
The data structure I used to store all this information was a dictionary.
The keys being the names of the players and then having a list for all of the
players stats each. At the very end I include a key that explains the stats
for all their shorthands.
'''

import time
import requests
import bs4

url = "https://www.espn.com/mens-college-basketball/team/stats/_/id/333"
reqs = requests.get(url)
# print(reqs)

# Put webpage into a beautiful soup object.
soup = bs4.BeautifulSoup(reqs.content, features="html.parser")

# Extract some meaningful data from the beautiful soup object
table = soup.find_all('table')[2]
rows = table.find_all('tr', class_= "Table__TR Table__TR--sm Table__even")

ua_basketball_players_names = []

for row in rows:
    cell_data = row.find('td').text
    ua_basketball_players_names.append(cell_data)

table = soup.find_all('table')[3]
rows = table.find_all('tr', class_= "Table__TR Table__TR--sm Table__even")
# print(rows)

stat_to_be_looked_at = ["MIN: ", "FGM: ", "FGA: ", "FTM: ", "FTA: ", "3PM: ", "3PA: ", "PTS: ", "OR: ", "DR: ", "REB: ", "AST: ", "TO: ", "STL: ", "BLK: "]

# New dictionary that holds all the players names as their keys with their stats as their values.
UA_basketball_players_with_statistics = {}

i = 0
# Loops over the rows in the table that we grabbed above and grabs the stats that we want
for row in rows:

    # Creates new empty list for each new player in the dictionary
    UA_basketball_players_with_statistics[ua_basketball_players_names[i]] = []

    # Finds and adds all the players stats to their entry in the dictionary:
    minutes_played = row.find_all('td')[0].text
    UA_basketball_players_with_statistics[ua_basketball_players_names[i]].append(minutes_played)

    field_goals_made = row.find_all('td')[1].text
    UA_basketball_players_with_statistics[ua_basketball_players_names[i]].append(field_goals_made)

    field_goal_attempts = row.find_all('td')[2].text
    UA_basketball_players_with_statistics[ua_basketball_players_names[i]].append(field_goal_attempts)

    free_throws_made = row.find_all('td')[3].text
    UA_basketball_players_with_statistics[ua_basketball_players_names[i]].append(free_throws_made)

    free_throw_attempts = row.find_all('td')[4].text
    UA_basketball_players_with_statistics[ua_basketball_players_names[i]].append(free_throw_attempts)

    three_pointers_made = row.find_all('td')[5].text
    UA_basketball_players_with_statistics[ua_basketball_players_names[i]].append(three_pointers_made)

    three_pointer_attempts = row.find_all('td')[6].text
    UA_basketball_players_with_statistics[ua_basketball_players_names[i]].append(three_pointer_attempts)

    points = row.find_all('td')[7].text
    UA_basketball_players_with_statistics[ua_basketball_players_names[i]].append(points)

    offensive_rebounds = row.find_all('td')[8].text
    UA_basketball_players_with_statistics[ua_basketball_players_names[i]].append(offensive_rebounds)

    defensive_rebounds = row.find_all('td')[9].text
    UA_basketball_players_with_statistics[ua_basketball_players_names[i]].append(defensive_rebounds)

    rebounds = row.find_all('td')[10].text
    UA_basketball_players_with_statistics[ua_basketball_players_names[i]].append(rebounds)

    assists = row.find_all('td')[11].text
    UA_basketball_players_with_statistics[ua_basketball_players_names[i]].append(assists)

    turnovers = row.find_all('td')[12].text
    UA_basketball_players_with_statistics[ua_basketball_players_names[i]].append(turnovers)

    steals = row.find_all('td')[13].text
    UA_basketball_players_with_statistics[ua_basketball_players_names[i]].append(steals)

    blocks = row.find_all('td')[14].text
    UA_basketball_players_with_statistics[ua_basketball_players_names[i]].append(blocks)

    i = i + 1

    # Breaks as soon as we get the last stat we need from each row.
    if (i > len(ua_basketball_players_names) - 1):
        break

# Prints out all the players names with their position and their statistics
print("Below are all the players and their season total stats for the University of Alabama Basketball team (2022-2023):")
print()

for key in UA_basketball_players_with_statistics.keys():
    print(key, end=', ')

    for i in range(0, len(UA_basketball_players_with_statistics[key])):

        if (i == len(UA_basketball_players_with_statistics[key]) - 1):
            print(stat_to_be_looked_at[i], end='')
            print(UA_basketball_players_with_statistics[key][i])
        else:
            print(stat_to_be_looked_at[i], end='')
            print(UA_basketball_players_with_statistics[key][i], end=', ')
print()

# Key dictionary for all the shorthand stats and their meanings:

shorthand_stats_key = { stat_to_be_looked_at[0]: "Minutes Played",
                        stat_to_be_looked_at[1]: "Field goals made",
                        stat_to_be_looked_at[2]: "Field goal attempts",
                        stat_to_be_looked_at[3]: "Free throws made",
                        stat_to_be_looked_at[4]: "Free throw attempts",
                        stat_to_be_looked_at[5]: "3-point field goals made",
                        stat_to_be_looked_at[6]: "3-point field goal attempts",
                        stat_to_be_looked_at[7]: "Points",
                        stat_to_be_looked_at[8]: "Offensive Rebounds",
                        stat_to_be_looked_at[9]: "Defensive Rebounds",
                        stat_to_be_looked_at[10]: "Rebounds",
                        stat_to_be_looked_at[11]: "Assists",
                        stat_to_be_looked_at[12]: "Turnovers",
                        stat_to_be_looked_at[13]: "Steals",
                        stat_to_be_looked_at[14]: "Blocks"}

print("Key for all the shorthand stats and their meanings:")
for key, value in shorthand_stats_key.items():
    print(key, value)