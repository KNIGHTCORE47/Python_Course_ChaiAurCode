# QS.04. Function Returning Multiple Values

import math

radius_of_circle = int(input("Enter the radius(r) of the circle: "))

def circle_with_its_circumference_and_area(r):
    circumference = 2 * (math.pi) * r
    area = (math.pi) * (r**2)

    print(f"Both the area and circumference of a circle given its radius of {r} is approx - {round(area, 3)} and {round(circumference, 3)}")
    


circle_with_its_circumference_and_area(radius_of_circle)