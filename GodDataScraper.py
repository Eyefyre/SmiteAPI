from bs4 import BeautifulSoup
import requests, json, re, subprocess, sys, os


ScriptPath = os.path.dirname(os.path.realpath(__file__)) + "\\GodsJSON\\"
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
GodID = 0
AbilityID = 0
AbilityURL = "https://smiteapi.adammackle.com/ability/"

for URL in URLArray:
    response = requests.get(URL, timeout=5)
    content = BeautifulSoup(response.content, "html.parser")
    GodInfoArray = []
    GodID += 1
    if GodID != 1:
        AbilityID += 5
    AllInfo = content.findAll("tbody")
    GodInfo = AllInfo[0].findAll("tr")
    LoreInfo = content.find('div', attrs={"class": "mw-parser-output"})
    LoreAll = LoreInfo.findAll(['h2', 'p'])
    LoreString = ""
    AbilityInfo = AllInfo[1].findAll('table', attrs={"class": "wikitable"})
    AbilityNameArray = []
    for i in range(5):
        AbilityName = AbilityInfo[i].tr.text.strip().split(" - ")
        AbilityNameArray.append(AbilityName[0])
        AbilityNameArray.append(AbilityName[1])
    print("Creating " + GodInfo[0].th.string.strip() + ".json")
    for i in range(5, 15):
        if(LoreAll[i].name == "h2"):
            break
        else:
            LoreString += LoreAll[i].text.strip()
    GodObject = {
        "Gods": [
            {
                "PutRequest": {
                    "Item": {
                        "ID": {
                            "S": str(GodID)
                        },
                        "Name": {
                            "S": GodInfo[0].th.string.lower().strip()
                        },
                        "Description": {
                            "S": GodInfo[3].td.text.strip()
                        },
                        "Pantheon": {
                            "S": GodInfo[4].td.text.strip()
                        },
                        "Class": {
                            "S": GodInfo[6].td.text.strip()
                        },
                        "Picture":{
                            "S": GodInfo[1].img['src'].strip()
                        },
                        "Type":{
                            "S": GodInfo[5].td.text.strip()
                        },
                        "Favor":{
                            "S": GodInfo[10].td.text.strip()
                        },
                        "Gems":{
                            "S": GodInfo[11].td.text.strip()
                        },
                        "Release Date":{
                            "S": GodInfo[9].td.text.strip()
                        },
                        "Difficulty":{
                            "S": GodInfo[8].td.text.strip()
                        },
                        "Lore":{
                            "S": LoreString.strip()
                        },
                        "Abilities": {
                            "L": [
                                {
                                    "M": {
                                        "ID": {
                                            "S": str(AbilityID + 1)
                                        },
                                        "Name": {
                                            "S": AbilityNameArray[1].strip()
                                        },
                                        "Slot": {
                                            "S": AbilityNameArray[0].strip()
                                        },
                                        "URL":{
                                            "S": AbilityURL + str(AbilityID + 1)
                                        }
                                    }
                                },
                                {
                                    "M": {
                                        "ID": {
                                            "S": str(AbilityID + 2)
                                        },
                                        "Name": {
                                            "S": AbilityNameArray[3].strip()
                                        },
                                        "Slot": {
                                            "S": AbilityNameArray[2].strip()
                                        },
                                        "URL":{
                                            "S": AbilityURL + str(AbilityID + 2)
                                        }
                                    }
                                },
                                {
                                    "M": {
                                        "ID": {
                                            "S": str(AbilityID + 3)
                                        },
                                        "Name": {
                                            "S": AbilityNameArray[5].strip()
                                        },
                                        "Slot": {
                                            "S": AbilityNameArray[4].strip()
                                        },
                                        "URL":{
                                            "S": AbilityURL + str(AbilityID + 3)
                                        }
                                    }
                                },
                                {
                                    "M": {
                                        "ID": {
                                            "S": str(AbilityID + 4)
                                        },
                                        "Name": {
                                            "S": AbilityNameArray[7].strip()
                                        },
                                        "Slot": {
                                            "S": AbilityNameArray[6].strip()
                                        },
                                        "URL":{
                                            "S": AbilityURL + str(AbilityID + 4)
                                        }
                                    }
                                },
                                {
                                    "M": {
                                        "ID": {
                                            "S": str(AbilityID + 5)
                                        },
                                        "Name": {
                                            "S": AbilityNameArray[9].strip()
                                        },
                                        "Slot": {
                                            "S": AbilityNameArray[8].strip()
                                        },
                                        "URL":{
                                            "S": AbilityURL + str(AbilityID + 5)
                                        }
                                    }
                                }
                            ]
                        },
                        "Stats": {
                            "L": [
                                {
                                    "M": {
                                        "ID": {
                                            "S": "1"
                                        },
                                        "Name": {
                                            "S": "Health"
                                        },
                                        "Base": {
                                            "S": GodInfo[15].td.text.strip()
                                        }
                                    }
                                },
                                {
                                    "M": {
                                        "ID": {
                                            "S": "2"
                                        },
                                        "Name": {
                                            "S": "Mana"
                                        },
                                        "Base": {
                                            "S": GodInfo[16].td.text.strip()
                                        }
                                    }
                                },
                                {
                                    "M": {
                                        "ID": {
                                            "S": "3"
                                        },
                                        "Name": {
                                            "S": "Move Speed"
                                        },
                                        "Base": {
                                            "S": GodInfo[17].td.text.strip()
                                        }
                                    }
                                },
                                {
                                    "M": {
                                        "ID": {
                                            "S": "4"
                                        },
                                        "Name": {
                                            "S": "Range"
                                        },
                                        "Base": {
                                            "S": GodInfo[18].td.text.strip()
                                        }
                                    }
                                },
                                {
                                    "M": {
                                        "ID": {
                                            "S": "5"
                                        },
                                        "Name": {
                                            "S": "Attack Per Second"
                                        },
                                        "Base": {
                                            "S": GodInfo[19].td.text.strip()
                                        }
                                    }
                                },
                                {
                                    "M": {
                                        "ID": {
                                            "S": "6"
                                        },
                                        "Name": {
                                            "S": "Basic Attack Damage"
                                        },
                                        "Base": {
                                            "S": GodInfo[21].td.text.strip()
                                        }
                                    }
                                },
                                {
                                    "M": {
                                        "ID": {
                                            "S": "7"
                                        },
                                        "Name": {
                                            "S": "Progression"
                                        },
                                        "Base": {
                                            "S": GodInfo[22].td.text.strip()
                                        }
                                    }
                                },
                                {
                                    "M": {
                                        "ID": {
                                            "S": "8"
                                        },
                                        "Name": {
                                            "S": "Magical Protection"
                                        },
                                        "Base": {
                                            "S": GodInfo[25].td.text.strip()
                                        }
                                    }
                                },
                                {
                                    "M": {
                                        "ID": {
                                            "S": "9"
                                        },
                                        "Name": {
                                            "S": "Physical Protection"
                                        },
                                        "Base": {
                                            "S": GodInfo[24].td.text.strip()
                                        }
                                    }
                                },
                                {
                                    "M": {
                                        "ID": {
                                            "S": "10"
                                        },
                                        "Name": {
                                            "S": "HP5"
                                        },
                                        "Base": {
                                            "S": GodInfo[27].td.text.strip()
                                        }
                                    }
                                },
                                {
                                    "M": {
                                        "ID": {
                                            "S": "11"
                                        },
                                        "Name": {
                                            "S": "MP5"
                                        },
                                        "Base": {
                                            "S": GodInfo[28].td.text.strip()
                                        }
                                    }
                                }
                            ]
                        }
                    }
                }
            }
        ]
    }
    
    with open(ScriptPath + GodInfo[0].th.string.strip() + '.json', 'w') as outfile:
        json.dump(GodObject, outfile)
