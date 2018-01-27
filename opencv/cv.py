import cv2

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()

    edges = cv2.Canny(frame,100,200,apertureSize = 3)
    cv2.imshow('frame',edges)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
