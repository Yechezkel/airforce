import requests, math


def get_weather_score(condition):
    if condition == "Clear":
        return 1.0
    elif condition == "Clouds":
        return 0.7
    elif condition == "Rain":
        return 0.4
    elif condition == "Stormy":
        return 0.2
    else:
        return 0


def haversine_distance(lat1, lon1, lat2, lon2):
    r = 6371.0
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon /2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = r * c
    return distance


def get_distance_from_jerusalem(lat,lon):
    JERU_LAT = 31.769
    JERU_LON = 35.2163
    return haversine_distance(JERU_LAT, JERU_LON, lat, lon)


def get_city_data(city_name):
    API_KEY = "8465630127f4f9221ee7fbf4bb5aacb1"
    BASE_URL_FORECAST_PATH = r"https://api.openweathermap.org/data/2.5/forecast?q="
    url_path = f"{BASE_URL_FORECAST_PATH}{city_name}&appid={API_KEY}"
    response = requests.get(url_path)
    result = {}
    if response.status_code == 200:
        data = response.json()
        result["lat"] = data["city"]["coord"]["lat"]
        result["lon"] = data["city"]["coord"]["lon"]
        result["main"] = data["list"][0]["weather"][0]["main"]
        result["clouds"] = data["list"][0]["clouds"]["all"]
        result["speed"] = data["list"][0]["wind"]["speed"]
        result["dt_txt"] = data["list"][0]["dt_txt"]
        result["distance"] = get_distance_from_jerusalem(result["lat"], result["lon"])
        result["weather_score"] = get_weather_score(result["main"])
    return result

