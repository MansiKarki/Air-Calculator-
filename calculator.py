import cv2
from cvzone.HandTrackingModule import HandDetector
import time

# Set camera resolution
cap = cv2.VideoCapture(0)
cap.set(3, 1280)  # Width
cap.set(4, 720)   # Height

detector = HandDetector(detectionCon=0.8, maxHands=1)

input_str = ""
result = ""
last_char = None
last_time = 0

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
operators = ['+', '-', '*', '/']

# Constants
INPUT_DELAY = 7 # seconds
font_big = cv2.FONT_HERSHEY_SIMPLEX

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    h, w, _ = img.shape

    # Draw display background
    cv2.rectangle(img, (20, 20), (w - 20, 160), (240, 240, 240), -1)
    cv2.rectangle(img, (20, 170), (w - 20, 250), (220, 220, 255), -1)

    # ✨ Show number positions
    number_y = 340  # 🔼 Adjusted for more vertical spacing

    for i, num in enumerate(numbers):
       cx = int((i + 0.5) * w / 10)
       cv2.circle(img, (cx, number_y), 30, (200, 200, 200), -1)
       cv2.putText(img, num, (cx - 15, number_y + 10), font_big, 1.2, (50, 50, 50), 3)

    # ✨ Show operator positions
    operator_y = 520  # 👈 Increased vertical space between numbers & operators
    for i, op in enumerate(operators):
       cx = int((i + 0.5) * w / 4)
       cv2.circle(img, (cx, operator_y), 30, (200, 200, 200), -1)
       cv2.putText(img, op, (cx - 15, operator_y + 10), font_big, 1.2, (50, 50, 50), 3)


    hands, img = detector.findHands(img, draw=True)
    current_char = ""

    if hands:
        hand = hands[0]
        fingers = detector.fingersUp(hand)
        lmList = hand["lmList"]

        if len(lmList) >= 9:
            x = lmList[8][0]

            # 👆 Index only = numbers
            if fingers == [0, 1, 0, 0, 0]:
                idx = int(x / w * 10)
                idx = min(max(idx, 0), 9)
                current_char = numbers[idx]

                cx = int((idx + 0.5) * w / 10)
                cv2.circle(img, (cx, 300), 60, (0, 255, 0), -1)
                cv2.putText(img, current_char, (cx - 30, 320), font_big, 2, (0, 0, 0), 4)

                # Only add once, and reset after hold
                if last_char != current_char:
                    input_str += current_char
                    last_char = current_char
                    last_time = time.time()
                elif time.time() - last_time > INPUT_DELAY:
                    last_char = None  # Reset after delay

            # ✌️ Index + middle = operators
            elif fingers == [0, 1, 1, 0, 0]:
                idx = int(x / w * 4)
                idx = min(max(idx, 0), 3)
                current_char = operators[idx]

                cx = int((idx + 0.5) * w / 4)
                cv2.circle(img, (cx, 400), 60, (0, 150, 255), -1)
                cv2.putText(img, current_char, (cx - 30, 420), font_big, 2, (0, 0, 0), 4)

                if input_str and input_str[-1] not in operators:
                    if last_char != current_char:
                        input_str += current_char
                        last_char = current_char
                        last_time = time.time()
                    elif time.time() - last_time > INPUT_DELAY:
                        last_char = None  # Reset after delay

            # 👍 Thumb = calculate
            elif fingers == [1, 0, 0, 0, 0]:
                try:
                    result = str(eval(input_str))
                except:
                    result = "Error"
                last_char = None
                last_time = time.time()

            # ✊ Fist = clear
            elif fingers == [0, 0, 0, 0, 0]:
                input_str = ""
                result = ""
                last_char = None
                last_time = time.time()

            else:
                last_char = None

    # Expression and result
    cv2.putText(img, f"Expression: {input_str}", (30, 100), font_big, 1.8, (0, 0,0), 4)
    cv2.putText(img, f"Result: {result}", (30, 230), font_big, 1.5, (0, 0, 0), 3)

    # Usage instructions
    cv2.putText(img, "Index: Numbers | Index+Middle: Operator | Thumb: Evaluate | Fist: Clear",
                (30, h - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (80, 80, 80), 2)

    cv2.imshow("✋ Air Calculator - Large Window", img)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
