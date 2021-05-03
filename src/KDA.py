import re
import requests
from bs4 import BeautifulSoup

message = input("Enter LOL Username here:")

response = requests.get('https://www.op.gg/summoner/userName='+message)
soup = BeautifulSoup(response.text, 'html.parser')

kill = str(soup.find('span', {'class': 'Kill'})) #Collects your kill stat
kill = re.sub(r'<[^>]+>', '', kill, 0).strip() # Divides it into text
death = str(soup.find('span', {'class': 'Death'}))
death = re.sub(r'<[^>]+>', '', death, 0).strip()
assist = str(soup.find('span', {'class': 'Assist'}))
assist = re.sub(r'<[^>]+>', '', assist, 0).strip()
ratio = str(soup.find('span', {'class': 'KDARatio'}))
ratio = re.sub(r'<[^>]+>', '', ratio, 0).strip()
per = str(soup.find('span', {'class': 'CKRate tip'}))
per = re.sub(r'<[^>]+>', '', per, 0).strip()

print(f"KDA: {kill}K {death}D {assist}Aㅣ{ratio}{per}")