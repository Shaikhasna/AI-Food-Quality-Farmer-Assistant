import cv2
from src.inference import predict
from src.nutrition import get_nutrition
from src.recommendations import get_advice

cap = cv2.VideoCapture(0)

food_text = ""
fresh_text = ""
conf_text = ""
nutrition_text = ""
advice_text = ""
price_text = ""
confidence = 0

print("Press SPACE to scan")
print("Press Q to quit")

while True:

    ret, frame = cap.read()

    font = cv2.FONT_HERSHEY_DUPLEX

    # -------- TEXT DISPLAY --------

    cv2.putText(frame, food_text,(20,40),font,0.7,(0,0,0),2)
    cv2.putText(frame, fresh_text,(20,65),font,0.6,(0,0,0),2)
    cv2.putText(frame, conf_text,(20,90),font,0.6,(0,0,0),2)

    cv2.putText(frame, nutrition_text,(20,115),font,0.55,(0,0,0),2)
    cv2.putText(frame, price_text,(20,135),font,0.55,(0,0,0),2)

    cv2.putText(frame, advice_text,(20,155),font,0.55,(0,0,0),2)

    # -------- CONFIDENCE BAR --------

    cv2.putText(frame,
                "Prediction Confidence",
                (20,175),
                font,
                0.55,
                (0,0,0),
                2)

    bar_x = 20
    bar_y = 190
    bar_width = 300
    bar_height = 18

    # background bar
    cv2.rectangle(frame,
                  (bar_x,bar_y),
                  (bar_x+bar_width,bar_y+bar_height),
                  (200,200,200),
                  -1)

    # filled bar
    filled_width = int(bar_width * confidence)

    cv2.rectangle(frame,
                  (bar_x,bar_y),
                  (bar_x+filled_width,bar_y+bar_height),
                  (0,200,0),
                  -1)

    cv2.imshow("AI Food Scanner", frame)

    key = cv2.waitKey(1) & 0xFF

    # -------- SPACE → SCAN --------

    if key == 32:

        cv2.imwrite("scan.jpg", frame)

        label, confidence, food, price = predict("scan.jpg")

        if "fresh" in label:
            freshness = "Fresh"
        else:
            freshness = "Spoiled"

        nutrition = get_nutrition(food)

        advice = get_advice(food, freshness.lower())

        food_text = f"Food: {food.capitalize()}"
        fresh_text = f"Freshness: {freshness}"
        conf_text = f"Confidence: {round(confidence*100,2)}%"

        nutrition_text = f"Calories:{nutrition['calories']} Fiber:{nutrition['fiber']}g Sugar:{nutrition['sugar']}g"

        price_text = f"Market Price: ₹{price}/kg"

        advice_text = advice

        print("\n------ Scan Result ------")
        print(food_text)
        print(fresh_text)
        print(conf_text)
        print(nutrition_text)
        print(price_text)
        print("Advice:", advice)
        print("-------------------------")

    # -------- Q → EXIT --------

    if key == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()