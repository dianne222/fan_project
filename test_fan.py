from fan import Fan

def display_fan():
    print("Speed:", fan.get_speed())
    print("Radius:", fan.get_radius())
    print("Color:", fan.get_color())
    print("On:", fan.get_on())

fan = Fan()

display_fan()