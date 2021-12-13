import cv2 as cv

original_image = cv.imread("image.jpg")
grayscale_image = cv.cvtColor(original_image, cv.COLOR_BGR2GRAY)
face_cascade = cv.CascadeClassifier("haarcascade_frontalface_alt.xml")
detected_faces = face_cascade.detectMultiScale(grayscale_image, 1.3)

for (col, row, width, height) in detected_faces:
    cv.rectangle(
        original_image,
        (col, row),
        (col + width, row + height),
        (0,255,0),
        2
    )

small = cv.resize(original_image, (0,0), fx=0.3, fy=0.3)
cv.imshow('Image', small)
cv.wait(0)  #sets 0 as the kill key
cv.destroyAllWindows()
