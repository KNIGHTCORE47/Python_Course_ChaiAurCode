# QS.04. Fruit Ripeness Checker

def fruite_ripe(fruite_type, fruite_color):
    if fruite_type == "Banana":
        if fruite_color == "Green":
            print("Unripe")
        elif fruite_color == "Yellow":
            print("Ripe")
        elif fruite_color == "Brown":
            print("Overripe")

fruite_ripe("Banana", "Green") 
fruite_ripe("Banana", "Yellow") 
fruite_ripe("Banana", "Brown")