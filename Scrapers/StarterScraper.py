from bs4 import BeautifulSoup
import requests
import json
import re
import subprocess
import sys
import os
import html

ScriptPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "\\passives\\"
BaseURL = "https://smite.gamepedia.com/Items"

ItemID = 16

response = requests.get(BaseURL, timeout=5)
content = BeautifulSoup(response.content, "html.parser")
itemInfo = content.findAll('h3')

for item in itemInfo:
    if(item.find("span") != None):
        if(item.find("span").text.strip() == "Tier I" or item.find("span").text.strip() == "Tier II" or item.find("span").text.strip() == "Tier III"):
            ItemTable = item.find_next_sibling("table")
            ItemTable = ItemTable.findAll("table", attrs={"class":"skill-tooltip"})
            for Item in ItemTable:
                ItemID+=1
                ItemRows = Item.findAll("tr")
                ItemName = ItemRows[0].th.text.strip()
                ItemPicture = ItemRows[0].find("img")["src"]
                print(ItemPicture)