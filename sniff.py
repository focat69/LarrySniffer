import requests

def get_daily_nba_player(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            player_data = response.json()

            player_name = player_data.get('player')
            player_name = player_name.get('name')
            if player_name:
                return player_name
            else:
                print("Could not find player name in response.")
                return None
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

url = "https://larrybirdle.netlify.app/.netlify/functions/daily"
daily_player = get_daily_nba_player(url)
if daily_player:
    print("Today's NBA Player:")
    print(daily_player)
