from getRankings import generateUniversityList, searchWeb

import concurrent.futures
import json


def createNewFile(propName, preference):
    print(f"Running createNewFile with propName={propName}, preference={preference}")
    try:
        dat = generateUniversityList(propName, searchWeb(propName, preference))
        print(f"{propName},{preference},dat={dat}")

        with open("data_{}_{}.json".format(propName, preference), "w") as f:
            json.dump(dat, f)
    except all as e:
        print(e)
    return True


def searchAllPreferences():
    with open("maps.json") as f:
        map_data = json.load(f)

    with concurrent.futures.ProcessPoolExecutor() as executor:
        for propName, preferenceList in map_data.items():
            for preference in preferenceList:
                print(propName, preference)
                executor.submit(createNewFile, propName, preference)


# searchAllPreferences()
