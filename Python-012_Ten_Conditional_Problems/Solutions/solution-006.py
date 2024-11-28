# QS.06. Transportation Mode Selection

def transportation_mode_on_distance(distance):
    if distance > 15:
        print("Will need a car")
    elif distance >= 3 and distance < 15:
        print("Will need a bike")
    elif distance < 3:
        print("We can walk")


transportation_mode_on_distance(10)
transportation_mode_on_distance(3)
transportation_mode_on_distance(1)
transportation_mode_on_distance(16)