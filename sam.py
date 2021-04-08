#!/usr/bin/env python
# coding: utf-8

# In[38]:


import cv2
import time
import os
import pyautogui
import  Handtrackingmodel as ht

wCam,hCam = 1080,720
cap=cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)
ptime=0
detector=ht.handDetector(detectionCon=0.9, trackCon=0.5)

while True:
    success,img=cap.read()
    image=detector.findHands(img)
    mylist=detector.findPosition(img,draw=False)
    if len(mylist)!=0:          
        if((mylist[4][1] < mylist[3][1]) and (mylist[8][2] < mylist[6][2]) and (mylist[12][2] > mylist[10][2]) and (mylist[16][2] > mylist[14][2]) and (mylist[20][2] > mylist[18][2])):
                 cv2.putText(img,"increasing volume",(50,600),cv2.FONT_HERSHEY_SIMPLEX,2,(255,0,0),10)
                 pyautogui.press("volumeup")        
                    
        elif((mylist[4][1] < mylist[3][1]) and (mylist[8][2] < mylist[6][2]) and (mylist[12][2] < mylist[10][2]) and (mylist[16][2] > mylist[14][2]) and (mylist[20][2] > mylist[18][2])):
                 cv2.putText(img,"decreasing volume",(50,600),cv2.FONT_HERSHEY_SIMPLEX,2,(255,0,0),10)
                 pyautogui.press("volumedown") 
                    
        elif(((mylist[4][1] < mylist[3][1]) and (mylist[8][2] < mylist[6][2]) and (mylist[12][2] < mylist[10][2]) and (mylist[16][2] < mylist[14][2]) and (mylist[20][2] > mylist[18][2]))):
                cv2.putText(img,"forwarding video",(50,600),cv2.FONT_HERSHEY_SIMPLEX,2,(255,0,0),10) 
                pyautogui.press("right")

                                     
        elif((mylist[4][1] < mylist[3][1]) and (mylist[8][2] < mylist[6][2]) and (mylist[12][2] < mylist[10][2]) and (mylist[16][2] < mylist[14][2]) and (mylist[20][2] < mylist[18][2])):
                 cv2.putText(img,"backwarding video",(50,600),cv2.FONT_HERSHEY_SIMPLEX,2,(255,0,0),10) 
                 pyautogui.press("left")


        elif((mylist[4][1] > mylist[3][1]) and (mylist[8][2] < mylist[6][2]) and (mylist[12][2] < mylist[10][2]) and (mylist[16][2] < mylist[14][2]) and (mylist[20][2] < mylist[18][2])):
                 cv2.putText(img,"play/pause video",(50,600),cv2.FONT_HERSHEY_SIMPLEX,2,(255,0,0),10)
                 pyautogui.press("space")
                 
                    
        elif((mylist[4][1] < mylist[3][1]) and (mylist[8][2] > mylist[6][2]) and (mylist[12][2] > mylist[10][2]) and (mylist[16][2] > mylist[14][2]) and (mylist[20][2] > mylist[18][2])):
                 cv2.putText(img,"muting volume",(50,600),cv2.FONT_HERSHEY_SIMPLEX,2,(255,0,0),10)
                 pyautogui.press("volumedown",presses=50)
                    
    ctime=time.time()
    FPS=1/(ctime-ptime)
    ptime=ctime
    cv2.putText(img,f"FPS: {int(FPS)}",(50,120),cv2.FONT_HERSHEY_SIMPLEX,2,(255,0,0),3)
    cv2.imshow("image",img)
    if cv2.waitKey(10) & 0xFF == ord('q'):
            break
            
cap.release()
cv2.destroyAllWindows()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


if((mylist[4][1] > mylist[3][1]) and (mylist[8][2] > mylist[6][2]) and (mylist[12][2] > mylist[10][2]) and (mylist[16][2] > mylist[14][2]) and (mylist[20][2] > mylist[18][2])):
                 cv2.putText(img,"it's thumb babe",(50,600),cv2.FONT_HERSHEY_SIMPLEX,2,(255,0,0),10)

