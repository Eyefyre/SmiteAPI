from bs4 import BeautifulSoup
import requests
import json
import re
import subprocess
import sys
import os
import html

ScriptPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "\\Achievements\\"
BaseURL = "https://smite.gamepedia.com/Achievements"

achievementID = 0

response = requests.get(BaseURL, timeout=5)
content = BeautifulSoup(response.content, "html.parser")
AchievementInfo = content.find_all('table', attrs={"class": "wikitable"})

for achievement in AchievementInfo:
    achievementID += 1
    achievementDs = achievement.findAll("td")
    achievementText = achievementDs[1].findAll("dl")
    achievementIcon = achievementDs[0].img["src"]
    achievementName = achievementText[0].text.strip()
    achievementDescription = achievementText[1].text.strip()
    if(achievement.find_previous_sibling('h2') != None):
        achievementCategory = achievement.find_previous_sibling('h2').find('span').text.strip()

    achievementObject = {
        "id": achievementID,
        "name": achievementName,
        "category": achievementCategory,
        "icon": achievementIcon,
        "description": achievementDescription
    }
    achievementName = achievementName.replace("?"," ")
    print("Creating " + achievementName + ".json")
    with open(ScriptPath + achievementName + '.json', 'w') as outfile:
        json.dump(achievementObject, outfile)

