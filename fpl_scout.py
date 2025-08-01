import requests
import pandas as pd

url = "https://fantasy.premierleague.com/api/bootstrap-static/"
response = requests.get(url)
data = response.json()

elements = pd.DataFrame(data['elements'])
teams = pd.DataFrame(data['teams'])
positions = pd.DataFrame(data['element_types'])  # Correct key

# Map team and position names
elements['team'] = elements['team'].map(teams.set_index('id')['name'])
elements['position'] = elements["element_type"].map(positions.set_index('id')['singular_name'])  # Fix here

# Select relevant columns
players = elements[['first_name', 'second_name', 'position', 'team', 'now_cost', 'total_points', 'form', 'minutes', 'selected_by_percent']]
players['now_cost'] = players['now_cost'] / 10
players['name'] = players['first_name'] + ' ' + players['second_name']
players = players.drop(['first_name', 'second_name'], axis=1)  # Fix here

players['value'] = players['total_points'] / players['now_cost']

# Print top players
print('\nTop 10 Players by Total Points:')
print(players.sort_values('total_points', ascending=False).head(10)[['name', 'team', 'position', 'total_points', 'now_cost']])

print('\nBest Value Players (Points per $):')
print(players.sort_values('value', ascending=False).head(10)[['name', 'team', 'position', 'total_points', 'now_cost']])
