class Fan:
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__(self, speed, on=False, radius, color):
        self.__speed = speed
        self.__on = on
        self.__radius = radius
        self.__color = color

    # Getters
    def get_speed(self):
        return self.__speed

    def get_on(self):
        return self.__on

    def get_radius(self):
        return self.__radius

    def get_color(self):
        return self.__color