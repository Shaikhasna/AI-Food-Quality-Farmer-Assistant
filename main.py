from src.inference import predict
from src.nutrition import nutrition_db
from src.recommendations import farmer_advice

image="scan.jpg"

food,freshness=predict(image)

print("Food:",food)

print("Freshness:",freshness)

print("Nutrition:",nutrition_db.get(food))

print("Advice:",farmer_advice(freshness))