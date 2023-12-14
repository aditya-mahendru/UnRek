import json
from queryLLM import singleQuestionForInfo


def getDataFromQ():
    with open("UserData.json") as f:
        data = json.load(f)

    userData = data["UserInfo"]
    userDataCopy = userData.copy()

    for item in userData:
        val = input(
            singleQuestionForInfo(
                item, "User", True if type(userData[item]) == type(True) else False
            )
        )

        if type(userData[item]) == type(True):
            if val.upper == "YES":
                userDataCopy[item] = True
            else:
                userDataCopy[item] = False
        else:
            userDataCopy[item] = val

    data["UserInfo"] = userDataCopy

    with open("UserData.json", "w") as f:
        json.dump(data, f, indent=2)

    return True


# print(getDataFromQ())
