import json
from queryLLM import generateIntersection, checkCountry, summarizeUniData
from regionCode import getRegionCode
from scraper import scrapeDuck

# import wikipedia


def getReport():
    with open("maps.json") as f:
        data = json.load(f)

    allProps = []

    with open("UserData.json") as file:
        fileData = json.load(file)

    country = fileData["Preferences"]["Country"]

    for propName, preferenceList in data.items():
        combined = set()
        for preference in preferenceList:
            with open("data_{}_{}.json".format(propName, preference)) as file:
                dat = json.load(file)
            for item in dat:
                combined.add(item["University"])
        allProps.append(list(combined))

    uniList = checkCountry(generateIntersection(allProps[0], allProps[1]), country)
    # print(uniList)
    return uniList
    # print(json.loads(uniList))

    # for uni in uniList:
    #     # l1 = scrapeDuck(uni, getRegionCode(country), 2)
    #     print(uni)
    #     print(wikipedia.search(uni))
    # dat = summarizeUniData(uni, l1)
    # print(dat)
