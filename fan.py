class Fan:
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__(self, speed, on=False):
        self.__speed = speed
        self.__on = on