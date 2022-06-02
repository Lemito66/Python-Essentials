import cv2 as cv
import sys
image = cv.imread(cv.samples.findFile(
    "C:\\Users\\lemit\\Documents\\Python Scripts\\OpenCv\\starry_night.jpg"))
if image is None:
    sys.exit("No se pudo leer la imagen")
cv.imshow("Pantalla", image)
k = cv.waitKey(0)
if k == ord("s"):
    cv.imwrite("C:\\Users\\lemit\\Documents\\Python Scripts\\OpenCv\\starry_night.jpg", image)
