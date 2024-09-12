import aircraftModel , pilotModel, attackModel, targetModel, csv, services as sv
from jsonService import load_json

path_pilots = 'pilots.json'
path_aircrafts = 'aircrafts.json'
path_targets = 'targets.json'
pilot_models_list = []
aircraft_models_list = []
target_models_list = []
attack_model_list = []
laoded_allready = False


while True:
    choice = input("Please choose an action: \n 1 - Load Files \n 2 - Display Pilots \n 3 - Display Aircrafts \n 4 - Display Targets \n 5 - Display Attacks \n 6 - Save All Attacks to File \n 7 - Exit \n: ")
    try:
        num = int(choice)
        if 6 >= num >= 2 and not laoded_allready:
            print("The files didn't load yet, You have to load them before trying display or save them.")
    except:
        print("Invalid choice. Please try again.")
        continue

    if choice == "1":

        print("Trying to load")

        try:
            # reading from 3 json files.
            pilots_json = load_json(path_pilots)
            aircrafts_json = load_json(path_aircrafts)
            targets_json = load_json(path_targets)

            # accessing to the data list inside every json.
            pilots_list = pilots_json["pilots"]
            aircrafts_list = aircrafts_json["aircrafts"]
            targets_list = targets_json["targets"]

            # holding the data as lists of the crossponding models instead of lists of dictionaries.
            pilot_models_list = [pilotModel.Pilot(x["name"], x["skill_level"]) for x in pilots_list]
            aircraft_models_list = [aircraftModel.Aircraft( x["type"], x["speed"], x["fuel_capacity"] ) for x in aircrafts_list]
            target_models_list = [targetModel.Target(x["City"], x["Priority"]) for x in targets_list]

            # adding the distance and weather score attribute to every item in targets.
            target_models_list = list( map( lambda t:  t.add_distance_and_weather(), target_models_list))

            # generating the attack offers by every combination of pilot aircraft and target.
            for p in pilot_models_list:
                for a in aircraft_models_list:
                    for t in target_models_list:
                        attack = attackModel.Attack(t.city, t.priority, p.name, a.type, t.distance, t.weather_score, p.skill_level, a.speed, a.fuel_capacity, -1)
                        attack.get_mission_fit_score()
                        attack_model_list.append(attack)

            # sorting the attacks' list by the score in descending order
            attack_model_list.sort(key=lambda x: x.mission_fit_score, reverse=True)

            # printing a message to the user
            print("The files loaded successfully.")
            laoded_allready = True

        except:

            # printing a message to the user
            print("An error occurred, The files didn't load successfully.")

    elif choice == "2":
        sv.print_list_models("Pilots:",pilot_models_list)

    elif choice == "3":
        sv.print_list_models("AirCrafts:", aircraft_models_list)

    elif choice == "4":
        sv.print_list_models("Targets:", target_models_list)

    elif choice == "5":
        sv.print_list_models("Attacks:", attack_model_list)

    elif choice == "6":
        try:
            csv_path = "attacks.csv"
            with open(csv_path, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=attack_model_list[0].convert_to_dict().keys())
                writer.writeheader()
                for attack in attack_model_list:
                    writer.writerow(attack.convert_to_dict())
            print(f"The attacks saved successfully at {csv_path}")
        except:
            print("An error occurred, The attacks didn't save successfully.")

    elif choice == "7":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")



















