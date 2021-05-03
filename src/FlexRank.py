import re
import requests
from bs4 import BeautifulSoup

message = input("Enter LOL Username here:")

response = requests.get('https://www.op.gg/summoner/userName='+message)
soup = BeautifulSoup(response.text, 'html.parser')

tier2 = str(soup.find('div', {'class': 'sub-tier__rank-tier'})) #Collects your Flex 5:5 Tier
tier2 = re.sub(r'<[^>]+>', '', tier2, 0).strip() #Defines the specific part that you want to crawl and divide it into text
if tier2 == 'Unranked':
    print("Flex 5:5 Rank: Unranked")
if tier2 == "None":
    print("User not found.")
else:
    lp2 = str(soup.find('div', {'class': 'sub-tier__league-point'}))
    lp2 = re.sub(r'<[^>]+>', '', lp2, 0).strip()
    winlose = str(soup.find('span', {'class': 'sub-tier__gray-text'}))
    winlose = re.sub(r'<[^>]+>', '', winlose, 0).strip()
    lp3 = lp2.split("/ ")[0]
    winlose2 = lp2.split("/ ")[1]
    ratio2 = str(soup.find('div', {'class': 'sub-tier__gray-text'}))
    ratio2 = re.sub(r'<[^>]+>', '', ratio2, 0).strip()
    print(f'Flex 5:5 Rank: {tier2}ㅣ{lp3}ㅣ{winlose2}ㅣ{ratio2}')