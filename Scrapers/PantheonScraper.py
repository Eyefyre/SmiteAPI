from bs4 import BeautifulSoup
import requests
import json
import re
import subprocess
import sys
import os
import html

ScriptPath = os.path.dirname(os.path.realpath(__file__)) + "\\Pantheons\\"
BaseURL = "https://smite.gamepedia.com/Gods"

pantheonID = 0

response = requests.get(BaseURL, timeout=5)
content = BeautifulSoup(response.content, "html.parser")
pantheonInfo = content.findAll('h2')

for pan in pantheonInfo:
    if(pan.find("span") != None):
        pantheonID += 1
        pantheonName = pan.find("span").text.strip().replace(
            "pantheon", "").strip()
        pantheonLore = pan.find_next_sibling("p").text.strip().replace(
            "”", "").replace("“", "").replace("Source", "")
        pantheonIcon = pan.find("span").img["src"]
        pantheonBanner = pan.find_next_sibling(
            "div", attrs={"class": "floatright"}).img["src"]

        pantheonObject = {
            "id": pantheonID,
            "name": pantheonName,
            "icon": pantheonIcon,
            "banner": pantheonBanner,
            "lore": pantheonLore,
            "gods": []
        }

        pantheonGods = pan.find_next_sibling("table").find("td").findChildren("div" , recursive=False)
        for godRow in pantheonGods:
            godName = godRow.text.strip()
            pantheonObject["gods"].append({"name": godName, "url": None})
        print("Creating " + pantheonName)
        with open(ScriptPath + pantheonName + '.json', 'w') as outfile:
            json.dump(pantheonObject, outfile)