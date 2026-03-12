def get_market_price(food):

    prices = {
        "apple": 120,
        "banana": 60,
        "orange": 80
    }

    return prices.get(food.lower(), 0)