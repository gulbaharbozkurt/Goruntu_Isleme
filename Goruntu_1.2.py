import cv2

Arac = cv2.CascadeClassifier("Otobus.xml")
Goruntu = cv2.VideoCapture("Otobüs_Video.mp4")

while Goruntu.isOpened():
    ret, frame = Goruntu.read()

    if not ret:
        print(("*" * 15) + "Bitti" + ("*" * 15))
        break

    gri = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gri = cv2.equalizeHist(gri)

    Araclar = Arac.detectMultiScale(gri, 1.1 , 2)

    for x, y, w, h in Araclar:
        cv2.rectangle(frame, (x, y), (x+ w, y + h), (0, 255, 0), 3)
        frame[y: y+h, x: x+w, 2] = 255

    cv2.imshow("GULBAHAR", frame)

    if cv2.waitKey(33) and 0xFF == ord("q"):
        break

Goruntu.release()
cv2.destroyAllWindows()