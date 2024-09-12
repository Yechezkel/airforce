import json, aircraftModel , pilotModel, attackModel, targetModel, csv

def load_json(path):
    with open(path, 'r') as file:
        return json.load(file)

path_pilots = 'pilots.json'
path_aircrafts = 'aircrafts.json'
path_targets = 'targets.json'
pilot_models_list = []
aircraft_models_list = []
target_models_list = []
attack_model_list = []


while True:
    choice = int(input(
        "Please choose an action: \n 1 - Load Files \n 2 - Display Attack Recommendation Table \n 3 - Save All Attacks to File \n 4 - Exit \n 5 - Print Aircrafts \n 6 - Print Pilots \n 7 - Print Targets \n: "))

    if choice == 1:

        # with open(path_pilots, 'r') as file:
        #     pilots_json = json.load(file)
        with open(path_aircrafts, 'r') as file:
            aircrafts_json = json.load(file)
        with open(path_targets, 'r') as file:
            targets_json = json.load(file)
        pilots_json = load_json(path_pilots)
        # aircrafts_json = json.load(path_aircrafts)
        # targets_json = json.load(path_targets)

        pilots_list = pilots_json["pilots"]
        aircrafts_list = aircrafts_json["aircrafts"]
        targets_list = targets_json["targets"]

        pilot_models_list = [pilotModel.Pilot(x["name"], x["skill_level"]) for x in pilots_list]
        aircraft_models_list = [aircraftModel.Aircraft(x["type"], x["speed"], x["fuel_capacity"]) for x in
                                aircrafts_list]
        target_models_list = [targetModel.Target(x["City"], x["Priority"]) for x in targets_list]


        for p in pilot_models_list:
            for a in aircraft_models_list:
                for t in target_models_list:
                    attack = attackModel.Attack(t.city, t.priority, p.name, a.type, t.distance, t.weather_score,
                                                p.skill_level, a.speed, a.fuel_capacity, -1)
                    attack.get_mission_fit_score()
                    attack_model_list.append(attack)

        attack_model_list.sort(key=lambda x: x.mission_fit_score, reverse=True)

        # למה זה לא עבד
        # print (target_models_list[0].add_distance_and_weather.get_string())
        # מניפולציות על כל מטרה להוסיף לה מרחק וציון מזג אוויר
        # target_models_list = list(map(lambda t:  t.add_distance_and_weather,target_models_list))
        for target in target_models_list:
            target.add_distance_and_weather()


    elif choice == 2:
        for attack in attack_model_list:
            print(attack.get_string())

    elif choice == 3:
        csv_path = "attacks.csv"
        with open(csv_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=attack_model_list[0].convert_to_dict().keys())
            writer.writeheader()
            for attack in attack_model_list:
                writer.writerow(attack.convert_to_dict())
    elif choice == 4:
        print("Exiting...")
        break
    elif choice == 5:
        print("AirCrafts:")
        for aircraft in aircraft_models_list:
            print(aircraft.get_string())

    elif choice == 6:
        print("Pilots:")
        for pilot in pilot_models_list:
            print(pilot.get_string())

    elif choice == 7:
        print("Targets:")
        for target in target_models_list:
            print(target.get_string())
    else:
        print("Invalid choice. Please try again.")



















