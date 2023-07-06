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
    #https://www.betexplorer.com/next/soccer/?year=2023&month=04&day=28
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    # browser.get("https://www.betexplorer.com/next/soccer/")
    browser.get(url)
    return browser

#Create a user data directory in the project directory
user_data_dir = os.path.join(os.getcwd(), 'chrome_user_data')
if not os.path.exists(user_data_dir):
    os.makedirs(user_data_dir)


def game_scrape(driver, line):
    game_teams = driver.find_element("xpath", f"/html/body/div[3]/div[5]/div/div/div[1]/section/div[2]/div[2]/div/div/table/tbody[" + str(line) + "]/tr[2]/td[1]/a")
    home_team = driver.find_element("xpath", f"/html/body/div[3]/div[5]/div/div/div[1]/section/div[2]/div[2]/div/div/table/tbody[1]/tr[" + str(line) + "]/td[1]/a/span[1]/strong")
    away_team = driver.find_element("xpath", f"/html/body/div[3]/div[5]/div/div/div[1]/section/div[2]/div[2]/div/div/table/tbody[1]/tr[" + str(line) + "]/td[1]/a/span[2]/strong")
    print(home_team.text, " vs ", away_team.text)

def get_tournament_html(driver, line, By, api_url, date_today, current_month, current_year):
    tournament = driver.find_element("xpath", f"/html/body/div[3]/div[5]/div/div/div[1]/section/div[2]/div[2]/div/div/table/tbody[" + str(line) + "]")
    competition = tournament.find_element(By.CLASS_NAME, "js-tournament")
    print(f"Getting games for {competition.text}")
    game_count = 2#starts from two due to the anticipation that 1 is the tournament name.
    while True:
        try:

            game = tournament.find_element(By.XPATH, f"/html/body/div[3]/div[5]/div/div/div[1]/section/div[2]/div[2]/div/div/table/tbody[" + str(line) + "]/tr[" + str(game_count) + "]")
            #                                          /html/body/div[3]/div[5]/div/div/div[1]/section/div[2]/div[2]/div/div/table/tbody[1]/tr[2]/td[1]/a
            game_link = game.find_element(By.XPATH, f"/html/body/div[3]/div[5]/div/div/div[1]/section/div[2]/div[2]/div/div/table/tbody[" + str(line) + "]/tr[" + str(game_count) + "]/td[1]/a")
            game_link = game_link.get_attribute('href')
            home_team = game.find_element(By.XPATH, f"/html/body/div[3]/div[5]/div/div/div[1]/section/div[2]/div[2]/div/div/table/tbody[" + str(line) + "]/tr[" + str(game_count) + "]/td[1]/a/span[1]")
            away_team = game.find_element(By.XPATH, f"/html/body/div[3]/div[5]/div/div/div[1]/section/div[2]/div[2]/div/div/table/tbody[" + str(line) + "]/tr[" + str(game_count) + "]/td[1]/a/span[2]")
            game_odds_ss = game.find_elements(By.CLASS_NAME, f"table-main__odds")
            data = {
                'competition': competition.text,
                'homeTeam': home_team.text,
                'awayTeam': away_team.text,
                'homeOdd': game_odds_ss[0].text,
                'drawOdd': game_odds_ss[1].text,
                'awayOdd': game_odds_ss[2].text,
                'gameDate': date_today,
                'gameMonth': current_month,
                'gameYear': current_year,
                'gameUrl': game_link
            }
            response = requests.post(api_url, data=data)
            #print(f"{home_team.text} vs {away_team.text} with {len(game_odds_ss)} the odds. {game_odds_ss[0].text} X {game_odds_ss[1].text} X {game_odds_ss[2].text} and the game link {game_link}")
            game_count += 1
        except Exception as e:
            # print(e)
            print("STOPPING SEARCH AT", competition.text, "\n")
            break

    # tournament_html = tournament.get_attribute("outerHTML")


today = datetime.datetime.today()
tomorrow = today + datetime.timedelta(days=1)
day_after_tomorrow = tomorrow + datetime.timedelta(days=1)
days = [tomorrow, day_after_tomorrow]

api_url = "http://127.0.0.1:8000/addgame/"


for day in days:
    current_year, current_month, date_today = int(day.strftime("%Y")), int(day.strftime("%m")), int(day.strftime("%d"))
    date_today = f"0{date_today}" if date_today < 10 else str(date_today)
    current_month = f"0{current_month}" if current_month < 10 else str(current_month)
    current_year = f"0{current_year}" if current_year < 10 else str(current_year)

    #print(f"{date_today} - {current_month} - {current_year}")

    soccer_url = f"https://www.betexplorer.com/next/soccer/?year={current_year}&month={current_month}&day={date_today}"
    hockey_url = f"https://www.betexplorer.com/next/hockey/?year={current_year}&month={current_month}&day={date_today}"
    handball_url = f"https://www.betexplorer.com/next/handball/?year={current_year}&month={current_month}&day={date_today}"

    urls = [ soccer_url, handball_url, hockey_url ]

    browser = initializeDriver(webdriver, Service, ChromeOptions, user_data_dir, ChromeDriverManager, soccer_url)
    time.sleep(10)
    # input("Press any button to close the browser.")
    line = 1
    error_count_stop = 0
    while True:
        try:
            get_tournament_html(browser, line, By, api_url, date_today, current_month, current_year)
            error_count_stop = 0
        except Exception as e:
            if error_count_stop == 2:
                break
            else:
                error_count_stop += 1
        # game_scrape(browser, line)
        line += 1
    
    break
    print("\n--------GOING TO NEXT DAY--------\n")

input("Press any button to close the browser.")
browser.quit()