from getRankings import generateUniversityList, searchWeb

import concurrent.futures
import json


def createNewFile(propName, preference):
    with open("data_{}_{}.json".format(propName,preference), "w") as f:
        json.dump(generateUniversityList(propName, searchWeb(propName, preference)), f)


def searchAllPreferences():
    with open("UserData.json") as f:
        data = json.load(f)

    userInfo = data["UserInfo"]
    preferences = data["Preferences"]

    with open("maps.json") as f:
        map_data = json.load(f)

    with concurrent.futures.ProcessPoolExecutor() as executor:
        for propName, preferenceList in map_data.items():
            for preference in preferenceList:
                executor.submit(createNewFile, propName, preference)

    


searchAllPreferences()
