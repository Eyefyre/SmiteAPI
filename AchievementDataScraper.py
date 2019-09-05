from bs4 import BeautifulSoup
import requests,json,re,subprocess,sys,os

ScriptPath = os.path.dirname(os.path.realpath(__file__)) + "\\AchievementsJSON\\"
BaseURL = "https://smite.gamepedia.com"
AchievementID = 0
response = requests.get(BaseURL + "/Achievements", timeout=5)
content = BeautifulSoup(response.content, "html.parser")
AchievementList = content.find_all('table', attrs={"class": "wikitable"})
for table in AchievementList:
    achievement = table.find_all("tr")
    if(table.find_previous_sibling('h2') != None):
       CategoryTitle = table.find_previous_sibling('h2').find('span').text
    else:
        tableParents = table.parents
        for parent in tableParents:
            if parent.parent.has_attr('class') and parent.parent['class'][0] == 'mw-parser-output':
                CategoryTitle = parent.find_previous_sibling('h2').find('span').text
                break
    for achievementrows in achievement:
        AchievementID+=1
        achievementSection = achievementrows.find_all("td")
        NameDesc = achievementSection[1].find_all("dd")
        Name = NameDesc[0].text.strip()
        Name = Name.replace("?"," ")
        print("Creating " + NameDesc[0].text + ".json")
        AchievementObject = { 
        "Achievements": [
            {
                "PutRequest": {
                    "Item": {
                        "ID": {
                            "S": str(AchievementID)
                        },
                        "Name": {
                            "S": NameDesc[0].text
                        },
                        "Picture":{
                            "S": achievementSection[0].img['src']
                        },
                        "Description":{
                            "S": NameDesc[1].text
                        },
                        "Category":{
                            "S": CategoryTitle.strip()
                        }
                    }
                }
            }
        ]
    }
    with open(ScriptPath + Name + '.json', 'w') as outfile:
        json.dump(AchievementObject, outfile)
