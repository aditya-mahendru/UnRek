import json


def generate_choices(dictionary):
    choices = []
    file_name_list = []
    for key, values in dictionary.items():
        for value in values:
            choices.append(f"{key} and {value}")
            file_name_list.append((key, value))
    for i, choice in enumerate(choices):
        print(f"{i+1}. {choice}")
    return file_name_list


def load_json(file_name):
    with open(file_name, "r") as f:
        return json.load(f)


def display_content(input_list, preference):
    display = []
    for item in input_list:
        university = item["University"]
        output = item[preference][0]
        display.append({"University": university, preference: output})
    json_string = json.dumps(display, indent=3)
    return json_string


def showFilters():
    while True:
        print("===================Filters===================")
        data = load_json("./maps.json")
        file_names = generate_choices(data)
        print("-----------------------------")
        print("00 : Exit")

        choice = int(input())
        if choice > len(file_names) or choice < 0:
            print("Re-enter the correct choice")
            continue
        elif choice == 0:
            return 0
        else:
            file_name = file_names[choice - 1]
            file_data = load_json(f"./data_{file_name[0]}_{file_name[1]}.json")
            # print(f"./data_{file_name[0]}_{file_name[1]}.json")
            propN = file_name[0]
            print(display_content(file_data, propN))


# showFilters()
