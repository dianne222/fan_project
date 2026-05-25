from fan import Fan

fan = Fan()
def display_fan(fan):
    print("Speed:", fan.get_speed())
    print("Radius:", fan.get_radius())
    print("Color:", fan.get_color())
    print("On:", fan.get_on())

fan1 = Fan(Fan.FAST, 10, "yellow", True)
fan2 = Fan(Fan.MEDIUM, 5, "blue", False)

display_fan(fan)