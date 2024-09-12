import random
def get_distance_score(distance):
    magic_number = (100/distance)* 150;
    if magic_number > 150:
        return 150;
    if magic_number < 1:
        return 1
    return magic_number

def get_aircraft_fuel_score(aircraft_fuel_Capacity):
    magic_number = (4000/aircraft_fuel_Capacity)*200;
    if magic_number > 200:
        return 200;
    if magic_number < 1:
        return 1
    return magic_number


def get_execution_time_score():
    return random.uniform(1, 100)


def get_pilot_skill_score(pilot_skill):
    return pilot_skill * 20


def get_weather_conditions_score(weather_conditions: int):
    return weather_conditions * 200


def get_priority_score(priority: int):
    return priority * 150/6