from bs4 import BeautifulSoup
import requests
import json
import re
import subprocess
import sys
import os

ScriptPath = os.path.dirname(os.path.realpath(__file__)) + "\\AbilitiesJSON\\"
URLArray = []
URLArray.append('https://smite.gamepedia.com/Achilles')
URLArray.append('https://smite.gamepedia.com/Agni')
URLArray.append('https://smite.gamepedia.com/Ah_Muzen_Cab')
URLArray.append('https://smite.gamepedia.com/Ah_Puch')
URLArray.append('https://smite.gamepedia.com/Amaterasu')
URLArray.append('https://smite.gamepedia.com/Anhur')
URLArray.append('https://smite.gamepedia.com/Anubis')
URLArray.append('https://smite.gamepedia.com/Ao_Kuang')
URLArray.append('https://smite.gamepedia.com/Aphrodite')
URLArray.append('https://smite.gamepedia.com/Apollo')
URLArray.append('https://smite.gamepedia.com/Arachne')
URLArray.append('https://smite.gamepedia.com/Ares')
URLArray.append('https://smite.gamepedia.com/Artemis')
URLArray.append('https://smite.gamepedia.com/Artio')
URLArray.append('https://smite.gamepedia.com/Athena')
URLArray.append('https://smite.gamepedia.com/Awilix')
URLArray.append('https://smite.gamepedia.com/Bacchus')
URLArray.append('https://smite.gamepedia.com/Bakasura')
URLArray.append('https://smite.gamepedia.com/Baron_Samedi')
URLArray.append('https://smite.gamepedia.com/Bastet')
URLArray.append('https://smite.gamepedia.com/Bellona')
URLArray.append('https://smite.gamepedia.com/Cabrakan')
URLArray.append('https://smite.gamepedia.com/Camazotz')
URLArray.append('https://smite.gamepedia.com/Cerberus')
URLArray.append('https://smite.gamepedia.com/Cernunnos')
URLArray.append('https://smite.gamepedia.com/Chaac')
URLArray.append("https://smite.gamepedia.com/Chang%27e")
URLArray.append('https://smite.gamepedia.com/Chernobog')
URLArray.append('https://smite.gamepedia.com/Chiron')
URLArray.append('https://smite.gamepedia.com/Chronos')
URLArray.append('https://smite.gamepedia.com/Cu_Chulainn')
URLArray.append('https://smite.gamepedia.com/Cupid')
URLArray.append('https://smite.gamepedia.com/Da_Ji')
URLArray.append('https://smite.gamepedia.com/Discordia')
URLArray.append('https://smite.gamepedia.com/Erlang_Shen')
URLArray.append('https://smite.gamepedia.com/Fafnir')
URLArray.append('https://smite.gamepedia.com/Fenrir')
URLArray.append('https://smite.gamepedia.com/Freya')
URLArray.append('https://smite.gamepedia.com/Ganesha')
URLArray.append('https://smite.gamepedia.com/Geb')
URLArray.append('https://smite.gamepedia.com/Guan_Yu')
URLArray.append('https://smite.gamepedia.com/Hachiman')
URLArray.append('https://smite.gamepedia.com/Hades')
URLArray.append('https://smite.gamepedia.com/He_Bo')
URLArray.append('https://smite.gamepedia.com/Hel')
URLArray.append('https://smite.gamepedia.com/Hera')
URLArray.append('https://smite.gamepedia.com/Hercules')
URLArray.append('https://smite.gamepedia.com/Horus')
URLArray.append('https://smite.gamepedia.com/Hou_Yi')
URLArray.append('https://smite.gamepedia.com/Hun_Batz')
URLArray.append('https://smite.gamepedia.com/Isis')
URLArray.append('https://smite.gamepedia.com/Izanami')
URLArray.append('https://smite.gamepedia.com/Janus')
URLArray.append('https://smite.gamepedia.com/Jing_Wei')
URLArray.append('https://smite.gamepedia.com/Jormungandr')
URLArray.append('https://smite.gamepedia.com/Kali')
URLArray.append('https://smite.gamepedia.com/Khepri')
URLArray.append('https://smite.gamepedia.com/King_Arthur')
URLArray.append('https://smite.gamepedia.com/Kukulkan')
URLArray.append('https://smite.gamepedia.com/Kumbhakarna')
URLArray.append('https://smite.gamepedia.com/Kuzenbo')
URLArray.append('https://smite.gamepedia.com/Loki')
URLArray.append('https://smite.gamepedia.com/Medusa')
URLArray.append('https://smite.gamepedia.com/Mercury')
URLArray.append('https://smite.gamepedia.com/Merlin')
URLArray.append('https://smite.gamepedia.com/Ne_Zha')
URLArray.append('https://smite.gamepedia.com/Neith')
URLArray.append('https://smite.gamepedia.com/Nemesis')
URLArray.append('https://smite.gamepedia.com/Nike')
URLArray.append('https://smite.gamepedia.com/Nox')
URLArray.append('https://smite.gamepedia.com/Nu_Wa')
URLArray.append('https://smite.gamepedia.com/Odin')
URLArray.append('https://smite.gamepedia.com/Osiris')
URLArray.append('https://smite.gamepedia.com/Pele')
URLArray.append('https://smite.gamepedia.com/Poseidon')
URLArray.append('https://smite.gamepedia.com/Ra')
URLArray.append('https://smite.gamepedia.com/Raijin')
URLArray.append('https://smite.gamepedia.com/Rama')
URLArray.append('https://smite.gamepedia.com/Ratatoskr')
URLArray.append('https://smite.gamepedia.com/Ravana')
URLArray.append('https://smite.gamepedia.com/Scylla')
URLArray.append('https://smite.gamepedia.com/Serqet')
URLArray.append('https://smite.gamepedia.com/Set')
URLArray.append('https://smite.gamepedia.com/Skadi')
URLArray.append('https://smite.gamepedia.com/Sobek')
URLArray.append('https://smite.gamepedia.com/Sol')
URLArray.append('https://smite.gamepedia.com/Sun_Wukong')
URLArray.append('https://smite.gamepedia.com/Susano')
URLArray.append('https://smite.gamepedia.com/Sylvanus')
URLArray.append('https://smite.gamepedia.com/Terra')
URLArray.append('https://smite.gamepedia.com/Thanatos')
URLArray.append('https://smite.gamepedia.com/The_Morrigan')
URLArray.append('https://smite.gamepedia.com/Thor')
URLArray.append('https://smite.gamepedia.com/Thoth')
URLArray.append('https://smite.gamepedia.com/Tyr')
URLArray.append('https://smite.gamepedia.com/Ullr')
URLArray.append('https://smite.gamepedia.com/Vamana')
URLArray.append('https://smite.gamepedia.com/Vulcan')
URLArray.append('https://smite.gamepedia.com/Xbalanque')
URLArray.append('https://smite.gamepedia.com/Xing_Tian')
URLArray.append('https://smite.gamepedia.com/Ymir')
URLArray.append('https://smite.gamepedia.com/Zeus')
URLArray.append('https://smite.gamepedia.com/Zhong_Kui')
AbilityID = 0
GodID = 0
GodURL = "https://smiteapi.adammackle.com/god/"
for URL in URLArray:
    GodID += 1
    response = requests.get(URL, timeout=5)
    content = BeautifulSoup(response.content, "html.parser")
    AllInfo = content.findAll("tbody")
    AbilityInfo = AllInfo[1].findAll('table', attrs={"class": "wikitable"})
    for i in range(5):
        AbilityID += 1
        Ability = AbilityInfo[i]
        AbilityNameArray = []
        AbilityName = Ability.tr.text.strip().split(" - ")
        AbilityNameArray.append(AbilityName[0])
        AbilityNameArray.append(AbilityName[1])
        parts = Ability.findAll("td")
        print("Creating " + AbilityNameArray[1])
        AbilityObject = {
            "Abilities": [
                {
                    "PutRequest": {
                        "Item": {
                            "ID": {
                                "S": str(AbilityID)
                            },
                            "Name": {
                                "S": AbilityNameArray[1]
                            },
                            "Description": {
                                "S": parts[5].text.strip()
                            },
                            "Slot":{
                                "S": AbilityNameArray[0]
                            },
                            "Picture":{
                                "S": parts[4].img['src'].strip()
                            },
                            "God":{
                                "M": {
                                    "ID": {
                                        "S": str(GodID)
                                    },
                                    "URL": {
                                        "S": GodURL + str(GodID)
                                    }
                                }
                            }
                        }
                    }
                }
            ]
        }
        with open(ScriptPath + AbilityNameArray[1] + '.json', 'w') as outfile:
            json.dump(AbilityObject, outfile)
