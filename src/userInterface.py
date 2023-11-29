import json


def showFilters():
    with open("maps.json") as f:
        data = json.load(f)
    print(
        "There are two types of filters, you can choose one or multiple (separated by commas) depnding on your requirements:"
    )

    prefSet = set()
    userInfo = set()

    for item in data:
        userInfo.add(item)
        for pref in data[item]:
            prefSet.add(pref)

    print("User Info:")
    userInfo = list(userInfo)
    for i, item in enumerate(userInfo, start=1):
        print("{}.{}".format(i, item))

    userChoice = input()

    print("Preferences")
    prefSet = list(prefSet)
    for i, item in enumerate(prefSet, start=1):
        print("{}.{}".format(i, item))

    prefChoice = input()

    return True


def initUserInterface():
    print("====================UnRek====================")

    while True:
        print("1: Generate Overall Report")
        print("2 : Browse and Select Filters")
        print("3 : Re-Enter Information")
        print("-----------------------------")
        print("00 : Exit")
        choice = input()

        if choice == "2":
            showFilters()
        elif choice == "3":
            return -1
        elif choice == "00":
            return 0


print(initUserInterface())
