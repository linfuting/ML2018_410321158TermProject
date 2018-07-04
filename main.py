import dlib
import cv2

img = cv2.imread('410321158_01.jpg')
detector = dlib.get_frontal_face_detector()
rects = detector(img, 0)

for i, d in enumerate(rects):
  x1 = d.left()
  y1 = d.top()
  x2 = d.right()
  y2 = d.bottom()
  
  cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 4, cv2.LINE_AA)

cv2.imshow("img", img)

cv2.waitKey(0)
cv2.destroyAllWindows()