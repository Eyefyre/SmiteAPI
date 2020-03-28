from bs4 import BeautifulSoup
import requests
import json
import re
import subprocess
import sys
import os
import html

ScriptPath = os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))) + "\\gods\\"
BaseURL = "https://smite.gamepedia.com/List_of_gods"

GodID = 0
AbilityID = 0
def Arthurian():
    return "1"
 
def Celtic():
    return "2"
 
def Chinese():
    return "3"
 
def Egyptian():
    return "4"
 
def Greek():
    return "5"
 
def Hindu():
    return "6"
 
def Japanese():
    return "7"
 
def Mayan():
    return "8"
 
def Norse():
    return "9"
 
def Polynesian():
    return "10"
 
def Roman():
    return "11"
 
def Slavic():
    return "12"

def Voodoo():
    return "13"
 
def Yoruba():
    return "14"
response = requests.get(BaseURL, timeout=5)
content = BeautifulSoup(response.content, "html.parser")
godList = content.find("table", attrs={"class": "blue-window"}).findAll("tr")

URLArray = []

for godLink in godList:
    godURL = godLink.findAll("td")[1:2]
    if len(godURL) > 0:
        if godURL[0].a["href"] != "/Baba_Yaga" and godURL[0].a["href"] != "/Tsukuyomi":
            URLArray.append(godURL[0].a["href"])
for URL in URLArray:
    GodID += 1
    response = requests.get("https://smite.gamepedia.com" + URL, timeout=5)
    content = BeautifulSoup(response.content, "html.parser")
    godInfo = content.find("table", attrs={"class": "infobox"}).findAll("tr")
    GodTitle = None
    GodPantheon = None
    GodPowerType = None
    GodAttackType = None
    GodClass = None
    GodDifficulty = None
    GodReleaseDate = None
    GodFavorCost = None
    GodGemCost = None
    GodPantheonID = None
    GodName = godInfo[0].th.text.strip()
    GodCard = godInfo[1].find("img")["src"]
    GodLore = ""

    LoreTag = content.find("span",attrs={"id":"Lore"})
    for pTag in LoreTag.parent.next_siblings:
        if pTag.name == "h2":
            break
        if pTag.name == "p":
            GodLore += pTag.text.strip().replace("\"","'")
    for row in godInfo:
        if row.th != None:
            if row.th.text.strip() == "Title:":
                GodTitle = row.find("td").text.strip()
            if row.th.text.strip() == "Pantheon:":
                GodPantheon = row.find("td").text.strip()
            if row.th.text.strip() == "Type:":
                types = row.find("td").text.strip().split(",")
                GodPowerType = types[1]
                GodAttackType = types[0]
            if row.th.text.strip() == "Class:":
                GodClass = row.find("td").text.strip()
            if row.th.text.strip() == "Difficulty:":
                GodDifficulty = row.find("td").text.strip()
            if row.th.text.strip() == "Release date:":
                GodReleaseDate = row.find("td").text.strip()
            if row.th.text.strip() == "Favor:":
                GodFavorCost = int(row.find("td").text.strip().replace(",","").replace("(Free)","").strip())
            if row.th.text.strip() == "Gems:":
                GodGemCost = int(row.find("td").text.strip().replace(",","").replace("(Free)","").strip())
    def getPantheonID(argument):
        switcher = {
            "Arthurian": Arthurian,
            "Celtic": Celtic,
            "Chinese": Chinese,
            "Egyptian": Egyptian,
            "Greek": Greek,
            "Hindu": Hindu,
            "Japanese": Japanese,
            "Mayan": Mayan,
            "Norse": Norse,
            "Polynesian": Polynesian,
            "Roman": Roman,
            "Slavic": Slavic,
            "Voodoo": Voodoo,
            "Yoruba": Yoruba
        }
        # Get the function from switcher dictionary
        func = switcher.get(argument, lambda: "Invalid month")
        # Execute the function
        return func()
    GodObject = {
        "id": GodID,
        "name": GodName,
        "title": GodTitle,
        "card": GodCard,
        "pantheon": {
            "name": GodPantheon,
            "url": "https://smiteapi.adammackle.com/pantheons/" + getPantheonID(GodPantheon)
        },
        "power_type": GodPowerType,
        "attack_type": GodAttackType,
        "role": GodClass,
        "lore": GodLore,
        "gem_cost": GodGemCost,
        "favor_cost": GodFavorCost,
        "difficulty": GodDifficulty,
        "release_date": GodReleaseDate,
        "stats": [],
        "abilities": [],
        "related_achievements": [],
        "skins": []
    }
    for row in godInfo:
        if row.th != None:
            if row.th.text.strip() == "Health:":
                GodObject["stats"].append({"stat": "Health", "value": row.find("td").text.strip()})
            if row.th.text.strip() == "Mana:":
                GodObject["stats"].append({"stat": "Mana", "value": row.find("td").text.strip()})
            if row.th.text.strip() == "Speed:":
                GodObject["stats"].append({"stat": "Speed", "value": row.find("td").text.strip()})
            if row.th.text.strip() == "Range:":
                GodObject["stats"].append({"stat": "Range", "value": row.find("td").text.strip()})
            if row.th.text.strip() == "Attack/Sec:":
                GodObject["stats"].append({"stat": "Attack Speed", "value": row.find("td").text.strip()})
            if row.th.text.strip() == "Damage:":
                GodObject["stats"].append({"stat": "Basic Attack Damage", "value": row.find("td").text.strip()})
            if row.th.text.strip() == "Progression:":
                GodObject["stats"].append({"stat": "Progression", "value": row.find("td").text.strip()})
            if row.th.text.strip() == "Physical:":
                GodObject["stats"].append({"stat": "Physical Protection", "value": row.find("td").text.strip()})
            if row.th.text.strip() == "Magical:":
                GodObject["stats"].append({"stat": "Magical Protection", "value": row.find("td").text.strip()})
            if row.th.text.strip() == "HP5:":
                GodObject["stats"].append({"stat": "HP5", "value": row.find("td").text.strip()})
            if row.th.text.strip() == "MP5:":
                GodObject["stats"].append({"stat": "MP5", "value": row.find("td").text.strip()})

    GodAchievements = content.findAll("table", attrs={"class":"wikitable"})
    for Achievement in GodAchievements:
        if Achievement.find_previous_sibling("h2") != None:
            if Achievement.find_previous_sibling("h2").find("span") != None:
                if Achievement.find_previous_sibling("h2").find("span").text.strip() == "Achievements":
                    url = 'https://smiteapi.adammackle.com/achievements/' + Achievement.find("span").text.strip().replace("?","%3F")
                    resp = requests.get(url=url)
                    data = resp.json()
                    AchievementID = data["id"]
                    GodObject["related_achievements"].append({"name": Achievement.find("span").text.strip(), "url": "https://smiteapi.adammackle.com/achievements/" + str(AchievementID)})

    GodAbilities = content.findAll("table")
    for GodAbility in GodAbilities:
        if GodAbility.find_previous_sibling("h2") != None:
            if GodAbility.find_previous_sibling("h2").find("span").text.strip() == "Abilities":
                Abilities = GodAbility.findAll("table",attrs={"class":"wikitable"})
                for ability in Abilities:
                    AbilityID += 1
                    AbilityName = ability.find("tr",attrs={"class":"prettytable"}).find("span").text.strip()
                    GodObject["abilities"].append({"name": AbilityName, "url": "https://smiteapi.adammackle.com/abilities/" + str(AbilityID)})
                    AbilitySlot = ability.find("tr",attrs={"class":"prettytable"}).text.strip().replace(AbilityName,"").replace("-","").strip()
                    AbilityImage = ability.find("img")["src"]
                    AbilityDescription = ability.findAll("tr")[2].findAll("td")[1].text.strip()

                    AbilityObject = {
                        "id":AbilityID,
                        "name":AbilityName,
                        "slot":AbilitySlot,
                        "icon":AbilityImage,
                        "ability_type":"",
                        "description":AbilityDescription,
                        "stats":[],
                        "god":{
                            "name":GodName,
                            "url":"https://smiteapi.adammackle.com/gods/" + str(GodID)
                        }
                    }
                    AbilityStats = ability.findAll("tr")[3:]
                    for stat in AbilityStats:
                        if(stat["style"] != "display: none;"):
                            sta = stat.findAll("td")
                            for st in sta:
                                if st.text.strip().split(":")[0] == "Ability Type":
                                    AbilityObject["ability_type"] = st.text.strip().split(":")[1].strip()
                                else:
                                    if st.text.strip() != "" and st.text.strip() != "Ability Video":
                                        AbilityObject["stats"].append(st.text.strip()) 
                    #print("Creating " + AbilityName)
                    # with open(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "\\abilities\\" + str(AbilityID) + "." +  AbilityName + '.json', 'w') as outfile:
                    #     json.dump(AbilityObject, outfile)
                
    
    # SkinsTag = content.find("span",attrs={"id":"God_Skins"})
    # for pTag in LoreTag.parent.next_siblings:
    #     if pTag.name == "h2":
    #         break
    #     if pTag.name == "ul":
    #         GodSkinIcon = pTag.find("img")["src"]
    #         GodSkinName = pTag.text.strip()
    SkinsInfo = content.findAll("div",attrs={"class":"tabbertab"})
    for Skin in SkinsInfo:
        SkinName = Skin["title"]
        SkinCard = Skin.find("table",attrs={"class":"wikitable"}).findAll("tr")
        SkinCardImage = SkinCard[1].find("img")["src"]
        GodObject["skins"].append({"name": SkinName, "card": SkinCardImage})
    print("Creating " + GodName)
    with open(ScriptPath + str(GodID) + "." + GodName + '.json', 'w') as outfile:
        json.dump(GodObject, outfile)