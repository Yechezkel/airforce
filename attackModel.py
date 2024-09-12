import scores as sc


class Attack:

    def __init__(self, target_city, priority,assigned_pilot , assigned_aircraft, distance, weather_conditions, pilot_skill, aircraft_speed, aircraft_fuel_Capacity, mission_fit_score):
        self.target_city = target_city
        self.priority = priority
        self.assigned_aircraft = assigned_aircraft
        self.assigned_pilot = assigned_pilot
        self.distance = distance
        self.weather_conditions = weather_conditions
        self.pilot_skill = pilot_skill
        self.aircraft_speed = aircraft_speed
        self.aircraft_fuel_Capacity = aircraft_fuel_Capacity
        self.mission_fit_score = mission_fit_score

    def get_string(self):
        return (
            f"Target City: {self.target_city},   "
            f"Priority: {self.priority},  "
            f"Assigned Pilot: {self.assigned_pilot},   "
            f"Assigned Aircraft: {self.assigned_aircraft},   "
            f"Distance: {self.distance},  "
            f"Weather Conditions: {self.weather_conditions},   "
            f"Pilot Skill: {self.pilot_skill},   "
            f"Aircraft Speed: {self.aircraft_speed},   "
            f"Aircraft Fuel Capacity: {self.aircraft_fuel_Capacity},   "
            f"Mission Fit Score: {self.mission_fit_score}."
        )

    def get_mission_fit_score(self):
         score = sc.get_distance_score(self.distance)
         score += sc.get_priority_score(self.priority)
         score += sc.get_pilot_skill_score(self.pilot_skill)
         score += sc.get_aircraft_fuel_score(self.aircraft_fuel_Capacity)
         score += sc.get_weather_conditions_score(self.weather_conditions)
         score += sc.get_execution_time_score()
         self.mission_fit_score = score


    def convert_to_dict(self):
        return {
            "Target City": self.target_city,
            "Priority": self.priority,
            "Assigned Pilot": self.assigned_pilot,
            "Assigned Aircraft": self.assigned_aircraft,
            "Distance": self.distance,
            "Weather Conditions": self.weather_conditions,
            "Pilot Skill": self.pilot_skill,
            "Aircraft Speed": self.aircraft_speed,
            "Aircraft Fuel Capacity": self.aircraft_fuel_Capacity,
            "Mission Fit Score": self.mission_fit_score
        }








""" 
def get_string(self):
    return f"name: {self.type}, skill level: {self.speed}, fuel capacity: {self.fuel_capacity}."
    

Target city
priority
assigned pilot
assigned aircraft
distance (km)
weather conditions
pilot skill
aircraft speed (km/h)
fuel Capacity (km)
mission fit score
"""