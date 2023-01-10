import cv2

Import numpy as np import wx

from pynput.mouse import Button, Controller

mouse = Controller()

app = (screenx, screeny) = wx.GetDisplaySize() (capturex,capturey) = (788,500) #captures this size frame

cap = cv2.VideoCapture(0) cap.set(3,capturex)

cap.set(4,capturey)

kernelOpen = np.ones((5,5)) #if noise are present other than yellow area kernelClose = np.ones((28,20))

#if noise are present in yellow area

#HSV color range which should be detected

lb = np.array([20, 100, 100]) ub = np.array([120, 255, 255])

cd = 0
while True:

ret, frame = cap.read()

#use HSV of yellow to detect only yellow color imgSeg= cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

#masking and filtering all shades of yellow mask= cv2.inRange (imgSeg, lb, ub) #mask= cv2.resize(mask, (500,400))

#apply morphology to avoid noise

maskOpen = cv2.morphologyEx (mask, cv2.MORPH_OPEN, kernelOpen) #maskOpen = cv2.resize(maskOpen, (500, 400))

maskClose = cv2.morphologyEx (maskOpen, cv2.MORPH_CLOSE, kernelClose) #maskClose = cv2.resize(maskClose, (500,400))

final = maskClose

conts, h = cv2.findContours (maskClose, cv2.RETR_EXTERNAL, cv2.CHAIN APPROX NONE)
ifiteniconts)1-8): #draws the contours of that object which has the highest

bnakiconts, key-cv2.conteurArea) west- tupletbtbl. 1. 01.argnint)1101)

gives the co-ordinate of the left extrere of contour east tupletbibl.: 01.argmax()1101) above for east the right

north tuple(bibit, t. 1).argnin())[0])

south tupletbtbl:, 11.orgmax (31101)

centre x = (west(0)-east (011/2 centre y Inorth101+south[8])/2

cv2.drawcontours(frane, b, -1, 18,255,0), 3)

cv2.circle(frame, west, 6, [0,0,255), -1)

cv2.circle(trane, east, 6, (0,0,255), -1)

cv2.circle(frane, north, 6, (0,0,2551, -1)

ev2.circle(frane, south, 6, (0,8,255), -1)

cv2.circle(frane, (int(centre_xl, int(centre yll, 6, (255,0,0), -1

eplots centre of the area

bint int(cv2.contourArea(b))

if (bint in range(8008, 18000)): #hand is open nouse.release(Button.left) cv2.circle(frame, [int (centre x), int(centre_y)), 6, (255,0,0), -1)

eplots centre of the area

nouse.position = (screenx-(centre_x*screenx/capturex), screeny-(cent

rey screeny/capturey}}

elif(bint in range(2088,7086)): #hand is closed cv2.circle(frane, (int(centre x), int(centre_y)), 10, (255,255,255 1.-11aptors centre of the area nouse.position= (screenx-(centre_x*screenx/capturex), screeny-(cen

tre y screeny/capturey))

nouse.press(Button.left)

cv2.imshow("video", frane) if cv2.waitKey(11 & 0xFF= ord[:exiting

break

cap.release() cv2 destroyAllWindows()