import json
import re
import itertools

from queryLLM import searchQuery, summarizeRanking, genJsonRankings
from scraper import scrapeDuck


def searchWeb(propName, preference):
    with open("UserData.json") as f:
        data = json.load(f)

    userInfo = data["UserInfo"]
    preferences = data["Preferences"]

    query = searchQuery(
        [userInfo[propName], propName], [preferences[preference], preference]
    )
    query = re.findall(r'"(.*?)"', query)[0]
    textContent = scrapeDuck(query)

    return textContent


def generateUniversityList(propName, textContent):
    with open("UserData.json") as f:
        data = json.load(f)

    userInfo = data["UserInfo"]

    allRankings = []

    for page in textContent:
        bleh = genJsonRankings(
            summarizeRanking(page, [userInfo[propName], propName]), propName
        )
        print(type(bleh))
        bleh2 = json.loads(bleh)
        print(type(bleh2))
        # print(bleh2)\
        allRankings.extend(bleh2)

    return list(
        map(
            lambda x: {
                "University": x[0],
                propName: list(map(lambda x: x[propName], list(x[1]))),
            },
            itertools.groupby(
                sorted(allRankings, key=lambda x: x["University"]),
                key=lambda x: x["University"],
            ),
        )
    )


# print(generateUniversityList("GPA", searchWeb("GPA", "Country")))
