from bs4 import BeautifulSoup
import requests
import json
import re
import subprocess
import sys
import os
import html

ScriptPath = os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))) + "\\passives\\"
BaseURL = "https://smite.gamepedia.com/Items"

ItemID = 16

response = requests.get(BaseURL, timeout=5)
content = BeautifulSoup(response.content, "html.parser")
itemInfo = content.findAll('h3')
URLArray = []

for item in itemInfo:
    if(item.find("span") != None):
        if(item.find("span").text.strip() == "Tier I" or item.find("span").text.strip() == "Tier II" or item.find("span").text.strip() == "Tier III"):
            ItemTable = item.find_next_sibling("table")
            ItemTable = ItemTable.findAll(
                "td", attrs={"class": "tooltip-hover"})
            for Item in ItemTable:
                URLArray.append(Item.p.find("a")["href"])
for URL in URLArray:
    ItemID +=1
    response = requests.get("https://smite.gamepedia.com" + URL, timeout=5)
    content = BeautifulSoup(response.content, "html.parser")
    infoBox = content.find("table", attrs={"class": "infobox"})
    infoRows = infoBox.findAll("tr")
    ItemName = infoRows[0].text.strip()
    ItemPicture = infoRows[1].find("img")["src"]
    ItemTier = None
    ItemCost = None
    TotalCost = None
    for row in infoRows[3:]:
        if row.th.text.strip() == "Cost:":#
            if row["style"] != "display: none;":
                ItemCost = int(row.find("td").text.strip())
                TotalCost = ItemCost
        if row.th.text.strip() == "Item Tier:":
            ItemTier = int(row.find("td").text.strip().replace(
                "Tier", "").replace(" ", ""))
        if row.th.text.strip() == "Total Cost:":
            if row["style"] != "display: none;":
                TotalCost = int(row.find("td").text.strip())


    ItemObject = {
        "id": ItemID,
        "name": ItemName,
        "picture": ItemPicture,
        "item_types": [],
        "item_tier": ItemTier,
        "cost": ItemCost,
        "total_cost":TotalCost,
        "passives": [],
        "stat_changes": [],
        "previous_tiers": [],
        "next_tiers": []
    }

    for row in infoRows[3:]:
        if row.th.text.strip() == "Item Type:":
            ItemTypes = row.find("td").text.strip().split(", ")
            for itType in ItemTypes:
                ItemObject["item_types"].append(itType)
        if row.th.text.strip() == "Stats:":
            stats = row.find("td").get_text(strip=True, separator="<br>")
            stats = stats.split("<br>")
            for stat in stats:
                ItemObject["stat_changes"].append(stat)
        if row.th.text.strip() == "Passive Effect:":
            if row["style"] != "display: none;":
                passives = row.find("td").get_text(
                    strip=True, separator="<br>")
                passives = passives.split("<br>")
                for passive in passives:
                    ItemObject["passives"].append(passive)
    print("Creating " + ItemName)
    with open(ScriptPath + ItemName + '.json', 'w') as outfile:
        json.dump(ItemObject, outfile)
