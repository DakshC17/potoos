class Weather:
    def __init__(self, city, temperature, condition, humidity, wind_speed, last_updated):
        self.city = city
        self.temperature = temperature
        self.condition = condition
        self.humidity = humidity
        self.wind_speed = wind_speed
        self.last_updated = last_updated
    
    def __str__(self):
        return f"{self.city}: Temp = {self.temperature}°C, Condition = {self.condition}, Humidity = {self.humidity}%, Wind = {self.wind_speed} km/h, Last Updated = {self.last_updated}"
