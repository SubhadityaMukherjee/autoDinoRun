import cv2
import numpy as np
from PIL import ImageGrab
import time
import pyautogui
from selenium import webdriver

# options = webdriver.ChromeOptions()
# options.add_argument('start-maximized')
# driver = webdriver.Chrome(chrome_options = options)

# driver.get("chrome://dino")
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
# ref_img2 = np.full(shape, bg)
ref_img2 = np.full(shape, bg)
# ref_img2 = ref_img2[:300,:500]
i = 1

while True:
    img2 = cv2.cvtColor(np.array(ImageGrab.grab(bbox)), cv2.COLOR_BGR2RGB)
    # driver.save_screenshot('temp.png')
    # img2 = cv2.cvtColor(cv2.imread('temp.png'), cv2.COLOR_BGR2RGB)
    img2 = img2[:300,:500]
    # cann = cv2.Canny(img2,threshold1=200,threshold2=300)

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
        ref_img2 = np.full(shape, bg)[:300,:500]
        print(f"update {i}")
        i += 1

    counter+=1

# driver.close()
