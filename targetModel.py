import  cityDataServices


class Target:

    def __init__(self, city, priority, distance=-1 , weather_score=""):
        self.city = city
        self.priority = priority
        self.distance = distance
        self.weather_score = weather_score


    def get_string(self):
        return f"city: {self.city}, priority: {self.priority}, distance: {self.distance}, forecast: {self.weather_score}."


    def add_distance_and_weather(self):
        data = cityDataServices.get_city_data(self.city)
        self.distance = data["distance"]
        self.weather_score = data["weather_score"]


