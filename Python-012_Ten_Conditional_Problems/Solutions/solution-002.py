# QS.02. Movie Ticket Pricing

def movie_ticket_price(age, weekday = "Friday"):
    if age < 18:
        if weekday == "Wednesday":
            print("Your Movie Ticket Price is $6")
        else:
            print("Your Movie Ticket Price is $8")
    else:
        if weekday == "Wednesday":
            print("Your Movie Ticket Price is $10")
        else:
            print("Your Movie Ticket Price is $12")

movie_ticket_price(26, "Wednesday")
movie_ticket_price(16, "Sunday")
movie_ticket_price(16, "Wednesday")




# Short hand method

age = 26
day = "Wednesday"

price = 12 if age >= 18 else 8

if day == "Wednesday":
    # price = price - 2
    price -= 2

print("Ticket price for you is $",price)
    