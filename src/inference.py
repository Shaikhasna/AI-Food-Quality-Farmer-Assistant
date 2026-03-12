import tensorflow as tf
import numpy as np
from PIL import Image
from src.config import MODEL_PATH, IMG_SIZE
from src.market_price import get_market_price

model = tf.keras.models.load_model(MODEL_PATH)

class_names = [
    "freshapple",
    "rottenapple",
    "freshbanana",
    "rottenbanana",
    "freshorange",
    "rottenorange"
]

def predict(image_path):

    img = Image.open(image_path).resize(IMG_SIZE)
    img = np.array(img) / 255.0
    img = np.expand_dims(img, axis=0)

    prediction = model.predict(img)[0]

    index = np.argmax(prediction)

    label = class_names[index]
    confidence = float(prediction[index])

    # Extract food name
    food = label.replace("fresh","").replace("rotten","")

    # Get market price
    price = get_market_price(food)

    return label, confidence, food, price