import json, aircraftModel , pilotModel, attackModel, targetModel, csv

def load_json(path):
    with open(path, 'r') as file:
        return json.load(file)




path_pilots = 'pilots.json'
path_aircrafts = 'aircrafts.json'
path_targets = 'targets.json'
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

pilot_models_list = [ pilotModel.Pilot( x["name"], x["skill_level"] ) for x in pilots_list ]
aircraft_models_list = [ aircraftModel.Aircraft( x["type"], x["speed"], x["fuel_capacity"] ) for x in aircrafts_list ]
target_models_list = [ targetModel.Target( x["City"], x["Priority"]  ) for x in targets_list ]


# למה זה לא עבד
# print (target_models_list[0].add_distance_and_weather.get_string())
# מניפולציות על כל מטרה להוסיף לה מרחק וציון מזג אוויר
#target_models_list = list(map(lambda t:  t.add_distance_and_weather,target_models_list))
for target in target_models_list:
    target.add_distance_and_weather()


print("Pilots:")
for pilot in pilot_models_list:
    print(pilot.get_string())
print("AirCrafts:")
for aircraft in aircraft_models_list:
    print(aircraft.get_string())
print("Targets:")
for target in target_models_list:
    print(target.get_string())



attack_model_list = []
for p in pilot_models_list:
    for a in aircraft_models_list:
        for t in target_models_list:
            attack = attackModel.Attack(t.city, t.priority, p.name, a.type, t.distance, t.weather_score ,p.skill_level ,a.speed, a.fuel_capacity,-1)
            attack.get_mission_fit_score()
            attack_model_list.append(attack)

attack_model_list.sort(key=lambda x: x.mission_fit_score, reverse=True)

for attack in attack_model_list:
    print(attack.get_string())


# כתיבה לCSV
csv_path = "attacks.csv"
with open(csv_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=attack_model_list[0].convert_to_dict().keys())
    writer.writeheader()
    for attack in attack_model_list:
        writer.writerow(attack.convert_to_dict())






















































"""
aircrafts_list = [
    {"type": "F-16", "speed": 2400, "fuel_capacity": 5000},
    {"type": "F-35", "speed": 3000, "fuel_capacity": 6000},
    {"type": "MiG-29", "speed": 2450, "fuel_capacity": 4500},
    {"type": "Su-27", "speed": 2500, "fuel_capacity": 5200},
    {"type": "Eurofighter Typhoon", "speed": 2495, "fuel_capacity": 5600},
    {"type": "Rafale", "speed": 2130, "fuel_capacity": 4700},
    {"type": "F/A-18", "speed": 1915, "fuel_capacity": 4900}
]
pilots_list = [
    {"name": "John Doe", "skill_level": 8},
    {"name": "Jane Smith", "skill_level": 6},
    {"name": "Michael Johnson", "skill_level": 7},
    {"name": "Emily Davis", "skill_level": 9},
    {"name": "Robert Brown", "skill_level": 5},
    {"name": "Sarah Wilson", "skill_level": 8},
    {"name": "David Lee", "skill_level": 6},
    {"name": "Chris Walker", "skill_level": 7},
    {"name": "Jessica Miller", "skill_level": 10},
    {"name": "Daniel Harris", "skill_level": 4}
]
"""

