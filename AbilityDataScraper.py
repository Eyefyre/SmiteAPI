from bs4 import BeautifulSoup
import requests,json,re,subprocess,sys,os

ScriptPath = os.path.dirname(os.path.realpath(__file__)) + "\\AbilitiesJSON\\"
URLArray = []
BaseURL = "https://smite.gamepedia.com"
response = requests.get(BaseURL + "/Gods", timeout=5)
content = BeautifulSoup(response.content, "html.parser")
AllLinks = content.findAll("td")
for link in AllLinks:
    Links = link.find_all("span")
    for href in Links:
        children = href.find_all("a")
        for child in children:
            URLArray.append(BaseURL + child['href'])
AbilityID = 0
GodID = 0
GodURL = BaseURL + "/god/"
APIURL = "https://smiteapi.adammackle.com/god/"
URLArray.sort()
for URL in URLArray:
    GodID += 1
    response = requests.get(URL, timeout=5)
    content = BeautifulSoup(response.content, "html.parser")
    AbilityInfo = content.findAll('table', attrs={"class": "wikitable"})
    for i in range(5):
        AbilityID += 1
        Ability = AbilityInfo[i]
        AbilityNameFull = Ability.tr.text.strip().split(" - ")
        AbilitySlot = AbilityNameFull[0] 
        AbilityName = AbilityNameFull[1]
        Allparts = Ability.findAll("td")
        print("Creating " + AbilityName + ".json")
        AbilityObject = {
            "Abilities": [
                {
                    "PutRequest": {
                        "Item": {
                            "ID": {
                                "S": str(AbilityID)
                            },
                            "Name": {
                                "S": AbilityName
                            },
                            "Description": {
                                "S": Allparts[5].text.strip()
                            },
                            "Slot":{
                                "S": AbilitySlot
                            },
                            "Picture":{
                                "S": Allparts[4].img['src'].strip()
                            },
                            "God":{
                                "M": {
                                    "ID": {
                                        "S": str(GodID)
                                    },
                                    "URL": {
                                        "S": APIURL + str(GodID)
                                    }
                                }
                            }
                        }
                    }
                }
            ]
        }
        with open(ScriptPath + AbilityName + '.json', 'w') as outfile:
            json.dump(AbilityObject, outfile)
