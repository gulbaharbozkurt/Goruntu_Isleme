
import cv2

Bisiklet = cv2.CascadeClassifier("Bsklt.xml")
cap = cv2.VideoCapture("Bisiklet_Video.mp4")

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        print("Bitti")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)

    Bisikletler = Bisiklet.detectMultiScale(gray, 1.1, 1)

    for x, y, w, h in Bisikletler:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)
        frame[y: y+h, x: x+w, 2] = 255

    cv2.imshow("Ekran", frame)

    if cv2.waitKey(1) and 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()