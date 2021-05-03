import re
import requests
from bs4 import BeautifulSoup

message = input("Enter LOL Username here:")

response = requests.get('https://www.op.gg/summoner/userName='+message)
soup = BeautifulSoup(response.text, 'html.parser')

tier = str(soup.find('div', {'class': 'TierRank'})) #Collects your Solo Tier
tier = re.sub(r'<[^>]+>', '', tier, 0).strip() #Defines the specific part that you want to crawl and divide it into text
if tier == 'Unranked':
    print("Ranked Solo: Unranked")
if tier == "None":
    print("User not found.")
else:
    lp = str(soup.find('span', {'class': 'LeaguePoints'}))
    lp = re.sub(r'<[^>]+>', '', lp, 0).strip()
    win = str(soup.find('span', {'class': 'wins'}))
    win = re.sub(r'<[^>]+>', '', win, 0).strip()
    lose = str(soup.find('span', {'class': 'losses'}))
    lose = re.sub(r'<[^>]+>', '', lose, 0).strip()
    ratio = str(soup.find('span', {'class': 'winratio'}))
    ratio = re.sub(r'<[^>]+>', '', ratio, 0).strip()
    league = str(soup.find('div', {'class': 'LeagueName'}))
    league = re.sub(r'<[^>]+>', '', league, 0).strip()
    print(f'Ranked Solo: {tier}ㅣ{lp}ㅣ{win} {lose}ㅣ{ratio}\nLeague: {league}')