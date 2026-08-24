import cv2 #Video manipulation
import time #set a delay
import mediapipe as mp #detect gestures
#open the webcam
cam=cv2.VideoCapture(0)
#setup mediapipe
mp_hands=mp.solutions.hands
hands=mp_hands.Hands()
draw=mp.solutions.drawing_utils
#track the last photo taken
last_photo=0
while True:
    success,frame=cam.read()
    #flip the view
    frame=cv2.flip(frame,1)
    #change rgb
    rgb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    #detect the hand
    result=hands.process(rgb)
    if result.multi_hand_landmarks:
        #detect the first hand up
        hand=result.multi_hand_landmarks[0]
        #draw the landmarks
        draw.draw_landmarks(frame,hand,mp_hands.HAND_CONNECTIONS)
        #check if fingers are raised
        if(hand.landmark[8].y<hand.landmark[6].y and hand.landmark[12].y < hand.landmark[10].y and hand.landmark[16].y<hand.landmark[14].y and hand.landmark[20].y<hand.landmark[18].y):
            current_time=time.time()
            #countdown
            for seconds in range(3,0,-1):
                cv2.putText(frame,str(seconds),(350,250),cv2.FONT_HERSHEY_SIMPLEX,4,(0,255,0),5)
                cv2.imshow("Gesture Photo App",frame)
                cv2.waitKey(1000) #wait for a second
            #take a photo and saving it
            cv2.imwrite("photo.png",frame)
            #save the last time a photo was taken
            last_photo=time.time()
            cv2.putText(frame,"PHOTO TAKEN",(20,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    cv2.imshow("Gesture Photo App",frame)
    if cv2.waitKey(1)&0xFF==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()