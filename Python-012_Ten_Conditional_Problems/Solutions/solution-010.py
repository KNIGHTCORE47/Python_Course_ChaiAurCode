# QS.10. Pet Food Recommendation

def pet_food_recommendation(species, age):
    if species == "Dog":
        if age < 2:
            print("Give Puppy Food")
        else:
            print("Give Dog Food")
    elif species == "Cat":
        if age > 5:
            print("Give senior cat food")
        else:
            print("Give kitten food")


pet_food_recommendation("Dog", 1)
pet_food_recommendation("Dog", 5)
pet_food_recommendation("Cat", 3)
pet_food_recommendation("Cat", 6)