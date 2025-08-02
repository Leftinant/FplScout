import pandas as pd
import requests

def load_fpl_data():
    """Fetch and return core FPL data as DataFrames."""
    url = "https://fantasy.premierleague.com/api/bootstrap-static/"
    response = requests.get(url)
    data = response.json()

    elements = pd.DataFrame(data['elements'])
    teams = pd.DataFrame(data['teams'])
    positions = pd.DataFrame(data['element_types'])

    return elements, teams, positions

def preprocess_player_data(elements, teams, positions):
    
    elements = elements.copy()
    elements['team'] = elements['team'].map(teams.set_index('id')['name'])
    elements['position'] = elements['element_type'].map(positions.set_index('id')['singular_name'])

    players = elements[[
        'first_name', 'second_name', 'position', 'team',
        'now_cost', 'total_points', 'form', 'minutes',
        'selected_by_percent'
    ]].copy()

    
    players['now_cost'] = players['now_cost'] / 10
    players['form'] = players['form'].astype(float)
    players['selected_by_percent'] = players['selected_by_percent'].astype(float)

    players['name'] = players['first_name'] + ' ' + players['second_name']
    players['value'] = players['total_points'] / players['now_cost']

    players.drop(columns=['first_name', 'second_name'], inplace=True)

    return players

def top_players(players, by='total_points', top_n=10, position=None):
    
    df = players.copy()
    if position:
        df = df[df['position'].str.lower() == position.lower()]
    return df.sort_values(by, ascending=False).reset_index(drop=True).head(top_n)

def find_differentials(players, max_ownership=10, min_form=5):
    
    filtered = players[
        (players['selected_by_percent'] < max_ownership) &
        (players['form'] >= min_form)
    ]
    return filtered.sort_values('form', ascending=False).reset_index(drop=True)

def compare_players(players, names, metric_list=None):
    
    if metric_list is None:
        metric_list = ['total_points', 'form', 'value', 'minutes']
    return players[players['name'].isin(names)][['name', 'team', 'position'] + metric_list].reset_index(drop=True)


