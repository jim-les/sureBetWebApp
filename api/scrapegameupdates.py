import os
import time
import datetime
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def initializeDriver(webdriver, Service, ChromeOptions, user_data_dir, ChromeDriverManager,url):
    options = ChromeOptions()
    prefs = {"download.default_directory":""}
    options.add_argument(f"--user-data-dir={user_data_dir}")
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    browser.get(url)
    return browser

#Create a user data directory in the project directory
user_data_dir = os.path.join(os.getcwd(), 'chrome_user_data')
if not os.path.exists(user_data_dir):
    os.makedirs(user_data_dir)


api_url = "http://127.0.0.1:8000/incompletegames/"
update_game_url = "http://127.0.0.1:8000/updategame/"
browser = initializeDriver(webdriver, Service, ChromeOptions, user_data_dir, ChromeDriverManager, api_url)
time.sleep(10)

response = requests.get(api_url)

if response.status_code == 200:
    data = response.json()
    # print(f"Data received from server is {data}")
    # process data
else:
    print(f'Error: {response.status_code}')

total_games_available = len(data)
total_game_checked = 0
for x in data:
    # print(x)
    browser.get(x['game_url'])
    home_team_xpath = "/html/body/div[4]/div[5]/div/div/div[1]/section/ul[2]/li[1]/h2/a"
    away_team_xpath = "/html/body/div[4]/div[5]/div/div/div[1]/section/ul[2]/li[3]/h2/a"
    game_result_xpath = "/html/body/div[4]/div[5]/div/div/div[1]/section/ul[2]/li[2]/p[2]"
    game_halfs_ended_xpath = "/html/body/div[4]/div[5]/div/div/div[1]/section/ul[2]/li[2]/h2"
    game_halfs_ended_alternate_xpath = "/html/body/div[4]/div[5]/div/div/div[1]/section/ul[2]/li[2]/h2[2]"
    home_team = browser.find_element("xpath", home_team_xpath)
    away_team = browser.find_element("xpath", away_team_xpath)
    game_result = browser.find_element("xpath", game_result_xpath)
    game_halfs_ended = browser.find_element("xpath", game_halfs_ended_xpath)
    home_score, away_score = game_result.text.split(":")

    if "(" in game_halfs_ended.text:
        if int(home_score) > int(away_score):
            game_winner = home_team.text
            game_winner = "home team"
        elif int(away_score) > int(home_score):
            game_winner = away_team.text
            game_winner = "away team"
        else:
            game_winner = "draw"

        data = {
            'winner': game_winner,
            'gameid': x['id']
        }
        response = requests.post(update_game_url, data=data)
        # print(f"GAME COMPLETE {home_team.text} vs {away_team.text} ended with the result {game_result.text}. The home score is {home_score} and the away score is {away_score}.")
    elif "After Penalties" in  game_halfs_ended.text:
        if int(home_score) > int(away_score):
            game_winner = home_team.text
            game_winner = "home team"
        elif int(away_score) > int(home_score):
            game_winner = away_team.text
            game_winner = "away team"
        else:
            game_winner = "draw"

        game_halfs_ended_alternate = browser.find_element("xpath", game_halfs_ended_alternate_xpath)
        if "(" in game_halfs_ended_alternate.text:
            data = {
                'winner': game_winner,
                'gameid': x['id']
            }
            response = requests.post(update_game_url, data=data)
        else:
            print(f"{game_halfs_ended_alternate.text}")
    else:
        pass
        # print(f"GAME INCOMPLETE {home_team.text} vs {away_team.text} ended with the result {game_result.text}. The home score is {home_score} and the away score is {away_score}.")
    total_game_checked += 1
    print(f"{total_game_checked} games checked out of {total_games_available} \n")



browser.quit()