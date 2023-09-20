class Hero:
    def __init__(self, name, last_hit, denay, agression, safe):
        self.__name = name
        self.__last_hit = last_hit
        self.__denay = denay
        self.__power = 0
        self.__agression = agression
        self.__safe = safe

    # Define getter methods using property decorators
    @property
    def name(self):
        return self.__name

    @property
    def last_hit(self):
        return self.__last_hit

    @property
    def denay(self):
        return self.__denay

    @property
    def power(self):
        return self.__power

    @property
    def agression(self):
        return self.__agression

    @property
    def safe(self):
        return self.__safe

    def setPower(self, power):
        self.__power = power

    def __str__(self):
        return f"Hero: {self.__name}, last hit: {self.__last_hit}, denay: {self.__denay}, power: {self.__power}, agression: {self.__agression}, safe: {self.__safe}"
