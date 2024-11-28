# QS.05. Weather Activity Suggestion

def weather_activity_suggestion(weather_type):
    match weather_type:
        case "Sunny":
            print("Go for a walk")
        case "Rainy":
            print("Read a book")
        case "Snowy":
            print("Build a snowman")

weather_activity_suggestion("Sunny")
weather_activity_suggestion("Rainy")
weather_activity_suggestion("Snowy")