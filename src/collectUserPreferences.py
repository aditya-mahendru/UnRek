import json
from queryLLM import singleQuestionForPreference


def collectPrefernces():
    with open("UserData.json") as f:
        data = json.load(f)

    preferences = data["Preferences"]
    preferencesCopy = preferences.copy()

    for item in preferences:
        val = input(
            singleQuestionForPreference(
                item, True if type(preferences[item]) == type(True) else False
            )
        )

        if type(preferences[item]) == type(True):
            if val.upper() == "YES":
                preferencesCopy[item] = True
            else:
                preferencesCopy[item] = False

        elif type(preferences[item]) == type([]):
            preferencesCopy[item] = val.split(",")

        else:
            preferencesCopy[item] = val

    data["Preferences"] = preferencesCopy

    with open("UserData.json", "w") as f:
        json.dump(data, f)


collectPrefernces()
