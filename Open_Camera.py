import shutil
import cv2

cam = cv2.VideoCapture(0)
cv2.namedWindow("Smile")


def image_taker(a):
    img_counter = a
    ret, frame = cam.read()
    cv2.imshow("Smile! You Are Being Hacked!", frame)
    img_name = "You've_Been_Hacked_{}.png".format(img_counter)
    cv2.imwrite(img_name, frame)
    # Takes a picture from the webcam and then moves the image to the folder from which the file was deleted.
    src = img_name
    dst = "C:\\Users\\elsda\\Desktop\\HackMe"
    shutil.copy(src, dst)

