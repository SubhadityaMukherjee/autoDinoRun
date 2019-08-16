import cv2
import numpy as np
from PIL import ImageGrab
import time
import pyautogui
pyautogui.PAUSE = 0

time.sleep(3)


counter = 1

#1480 1345 499 193

img2 = cv2.cvtColor(np.array(ImageGrab.grab()), cv2.COLOR_BGR2RGB)
# x,y,w,h = cv2.selectROI("teno", img2,False,False) #x,y,w,h
x,y,w,h = 1480 ,1345, 499, 193

print(x,y,w,h)

time.sleep(2)
pyautogui.press('space')



bbox = (x,y,x+w,y+h) # left top right bottom
# bbox = (203, 684, 294, 775)
shape = (bbox[3]-bbox[1], bbox[2]-bbox[0], 3)
bg = 255
ref_img2 = np.full(shape, bg)
i = 1

while True:
    img2 = cv2.cvtColor(np.array(ImageGrab.grab(bbox)), cv2.COLOR_BGR2RGB)
    # img2 = img2[y:y+h,x:x+w]

    if bg != img2[0][0][0]:
        bg = img2[0][0][0]
        ref_img2 = np.full(shape, bg)
        i += 1

    if np.subtract(ref_img2, img2).sum() != 0:
        pyautogui.press('space')
        print('[INFO]: Jump')
        # cv2.imwrite(f"images/img2_{counter}.jpg", img2)
        # cv2.imwrite(f"images/full_{counter}.jpg", img2)

    if i % 4 == 0:
        bbox = (bbox[0]+1, bbox[1], bbox[2]+1, bbox[3])
        shape = (bbox[3]-bbox[1], bbox[2]-bbox[0], 3)
        ref_img2 = np.full(shape, bg)
        print(f"update {i}")
        i += 1

    # if cv2.waitKey(1) == 27:
    #     break

    counter+=1

# cv2.destroyAllWindows()

# img = cv2.imread('images/full_11.jpg')
# r = cv2.selectROI(img)
# print(r)
