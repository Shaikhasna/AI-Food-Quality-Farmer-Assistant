nutrition_db = {
    "apple": {"calories": 52, "fiber": 2.4, "sugar": 10},
    "banana": {"calories": 96, "fiber": 2.6, "sugar": 12},
    "orange": {"calories": 47, "fiber": 2.4, "sugar": 9}
}

def get_nutrition(food):

    return nutrition_db.get(food, {})