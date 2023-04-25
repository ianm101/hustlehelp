import cv2
import pytesseract

img = cv2.imread("test_img.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
cv2.imshow("Threshold", thresh)
cv2.waitKey(0)
text = pytesseract.image_to_string(thresh)

print(text)