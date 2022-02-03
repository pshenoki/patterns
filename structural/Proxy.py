from abc import ABC, abstractmethod
from time import time, sleep

WEATHER_SITE = {'Moscow': 20}


class WeatherChecker(ABC):
    @abstractmethod
    def get_weather(self):
        pass


class MoscowWeatherChecker(WeatherChecker):
    def __init__(self, site):
        self.site = site
        self.name = 'Moscow'

    def get_weather(self):
        return self.site[self.name]


class ProxyMoscowWeatherChecker(WeatherChecker):
    def __init__(self, weather_checker, seconds_passed):
        self.weather_checker = weather_checker
        self.seconds_passed = seconds_passed
        self.cash = {}
        self.registered = time()

    def get_weather(self):
        time_now = time()
        if self.weather_checker.name in self.cash and time_now - self.registered < self.seconds_passed:
            print('Weather from cash:')
            return self.cash[self.weather_checker.name]
        else:
            self.cash[self.weather_checker.name] = self.weather_checker.get_weather()
            print('Weather from site:')
            self.registered = time()
            return self.weather_checker.get_weather()


if __name__ == '__main__':
    moscow_weather = MoscowWeatherChecker(WEATHER_SITE)
    proxy_moscow = ProxyMoscowWeatherChecker(moscow_weather, seconds_passed=2)

    print(proxy_moscow.get_weather())
    print(proxy_moscow.get_weather())
    sleep(3)
    print(proxy_moscow.get_weather())
    print(proxy_moscow.get_weather())
