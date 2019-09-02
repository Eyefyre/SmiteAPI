from bs4 import BeautifulSoup
import requests,json,re,subprocess,sys,os

ScriptPath = os.path.dirname(os.path.realpath(__file__)) + "\\GodsJSON\\"
URLArray = []
HeadingRemoveList = ["Summary\n", "Voicelines:\n", "Voice actor:\n", "Stats\n", "Basic Attack\n","Protection\n", "Regen\n", "*Numbers in parentheses are the amount gained at each level\n"]
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

GodID = 0
AbilityID = 0
AbilityURL = BaseURL + "/ability/"
URLArray.sort()
for URL in URLArray:
    GodID+= 1
    if GodID != 1:
        AbilityID+=5
    response = requests.get(URL, timeout=5)
    content = BeautifulSoup(response.content, "html.parser")
    GodInfo = content.find('table', attrs={"class": "infobox"}).find_all("tr")
    GodHeadings = []
    GodText = []
    for godKey in GodInfo:
        if(godKey.th != None):
            GodHeadings.append(godKey.th.text)
        if(godKey.td != None):
            GodText.append(godKey.td.text)
    PictureURL = GodInfo[1].find("img")['src']
    for heading in HeadingRemoveList:
        if heading in GodHeadings:
            GodHeadings.remove(heading)
    voicelineIndex = GodText.index(GodHeadings[0].strip() + " voicelines\n")
    GodText.pop(voicelineIndex)
    GodText.pop(voicelineIndex)
    LoreInfo = content.find('div', attrs={"class": "mw-parser-output"})
    LoreAll = LoreInfo.findAll(['h2', 'p'])
    LoreString = ""
    print("Creating " + GodHeadings[0].strip() + ".json")
    for i in range(5, 15):
        if(LoreAll[i].name == "h2"):
            break
        else:
            LoreString += LoreAll[i].text.strip()
    StatsStartIndex = GodHeadings.index("Health:\n")
    GodText = ["NULL" if x=="\n" else x for x in GodText]
    GodHeadings = [w.replace(':\n', '') for w in GodHeadings]
    GodText = [w.replace(':\n', '') for w in GodText]
    AbilityInfo = content.findAll('table', attrs={"class": "wikitable"})
    AbilityNames = []
    AbilitySlots = []
    for i in range(5):
        AbilityName = AbilityInfo[i].tr.text.strip().split(" - ")
        AbilityNames.append(AbilityName[1])
        AbilitySlots.append(AbilityName[0])
    
    GodObject = {
        "Gods": [
            {
                "PutRequest": {
                    "Item": {
                        "ID": {
                            "S": str(GodID)
                        },
                        "Name": {
                            "S": GodHeadings[0].strip()
                        },
                        "Picture":{
                            "S": PictureURL.strip()
                        },
                        "Lore":{
                            "S": LoreString.strip()
                        }
                    }
                }
            }
        ]
    }
    APIAbilityURL = "https://smiteapi.adammackle.com/ability/"
    StatID = 0
    GodObject["Gods"][0]["PutRequest"]["Item"].update({"Stats":{"L":[]}})
    GodObject["Gods"][0]["PutRequest"]["Item"].update({"Abilities":{"L":[]}})
    for x in range(1,StatsStartIndex):       
        GodObject["Gods"][0]["PutRequest"]["Item"].update({GodHeadings[x].lower().strip():{"S":GodText[x].strip()}})
    for y in range (StatsStartIndex,len(GodHeadings)):
        StatID+=1
        GodObject["Gods"][0]["PutRequest"]["Item"]["Stats"]["L"].append({"M":{"ID":{"S":str(StatID)},"Name":{"S":GodHeadings[y].strip()},"Base":{"S":GodText[y].strip()},}},)
    for z in range(len(AbilityNames)):
        GodObject["Gods"][0]["PutRequest"]["Item"]["Abilities"]["L"].append({"M":{"ID":{"S":str((AbilityID + (z+1)))},"Name":{"S":AbilityNames[z].strip()},"Slot":{"S":AbilitySlots[z].strip()},"URL":{"S":APIAbilityURL + str((AbilityID + (z+1)))},}},)
    with open(ScriptPath + GodHeadings[0].strip() + '.json', 'w') as outfile:
        json.dump(GodObject, outfile)