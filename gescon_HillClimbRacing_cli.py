import cv2
import mediapipe as mp
import pydirectinput
import pyautogui
from subprocess import run
from time import sleep
PackageFamilyName = "FINGERSOFT.HILLCLIMBRACING_r6rtpscs7gwyg"
Id="App"
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

select_ges = []
global structuredLandmarks
label = 'Right'

def getStructuredLandmarks(landmarks):
  #print("what " + str(landmarks))
  global structuredLandmarks
  structuredLandmarks = []
  
  for j in range (42):
      if (j % 2 == 1):
          structuredLandmarks.append ( {'x': landmarks[j - 1] , 'y': landmarks[j]} )
  return structuredLandmarks

def recognizeHandGesture(landmarks , label):
        global select_ges

        thumbState = 'UNKNOWN'
        indexFingerState = 'UNKNOWN'
        middleFingerState = 'UNKNOWN'
        ringFingerState = 'UNKNOWN'
        littleFingerState = 'UNKNOWN'
        thumbRight = False
        thumbLeft = False
        recognizedHandGesture = None

        if label.strip () == 'Left':
            print ( 'left' )
            pseudoPoint = landmarks[2]['x']

            if pseudoPoint < landmarks[3]['x'] < landmarks[4]['x']:
                thumbState = 'OPEN'
            elif pseudoPoint > landmarks[3]['x'] > landmarks[4]['x']:
                thumbState = 'CLOSE'

        else:

            pseudoPoint = landmarks[2]['x']

            if pseudoPoint < landmarks[3]['x'] < landmarks[4]['x']:
                thumbState = 'CLOSE'
            elif pseudoPoint > landmarks[3]['x'] > landmarks[4]['x']:
                thumbState = 'OPEN'

        if (pseudoPoint < landmarks[3]['x'] < landmarks[4]['x'] and landmarks[4]['x'] >
                landmarks[17]['x']):
            thumbRight = True
        elif (pseudoPoint > landmarks[3]['x'] > landmarks[4]['x'] and landmarks[4]['x'] <
              landmarks[17]['x']):
            thumbLeft = True

        pseudoPoint = landmarks[6]['y']
        if pseudoPoint > landmarks[7]['y'] > landmarks[8]['y']:
            indexFingerState = 'OPEN'
        elif pseudoPoint < landmarks[7]['y'] < landmarks[8]['y']:
            indexFingerState = 'CLOSE'

        pseudoPoint = landmarks[10]['y']
        if pseudoPoint > landmarks[11]['y'] > landmarks[12]['y']:
            middleFingerState = 'OPEN'
        elif pseudoPoint < landmarks[11]['y'] < landmarks[12]['y']:
            middleFingerState = 'CLOSE'

        pseudoPoint = landmarks[14]['y']
        if pseudoPoint > landmarks[15]['y'] > landmarks[16]['y']:
            ringFingerState = 'OPEN'
        elif pseudoPoint < landmarks[15]['y'] < landmarks[16]['y']:
            ringFingerState = 'CLOSE'

        pseudoPoint = landmarks[18]['y']
        if pseudoPoint > landmarks[19]['y'] > landmarks[20]['y']:
            littleFingerState = 'OPEN'
        elif pseudoPoint < landmarks[19]['y'] < landmarks[20]['y']:
            littleFingerState = 'CLOSE'

        if thumbState == 'OPEN' and indexFingerState == 'OPEN' and middleFingerState == 'OPEN' and ringFingerState == 'OPEN' and littleFingerState == 'OPEN':
            recognizedHandGesture = "Open Palm" # "FIVE"

        elif thumbState == 'CLOSE' and indexFingerState == 'OPEN' \
                and middleFingerState == 'OPEN' and ringFingerState == 'OPEN' \
                and littleFingerState == 'OPEN':

            # scrolling(landmarks[0]['x']*img_width,landmarks[0]['y']*img_height)
            #     slide(landmarks[0]['x']*img_width,landmarks[0]['y']*img_height,landmarks[9]['x']*img_width,landmarks[9]['y']*img_height)
            #     keyboard.press_and_release('Page Down')

            recognizedHandGesture = "4"  # "FOUR"
        elif thumbState == 'CLOSE' and indexFingerState == 'OPEN' \
                and middleFingerState == 'OPEN' and ringFingerState == 'OPEN' \
                and littleFingerState == 'CLOSE':

            recognizedHandGesture = "3"  # "THREE"

        elif thumbState == 'CLOSE' and indexFingerState == 'CLOSE' \
                and middleFingerState == 'CLOSE' and ringFingerState == 'CLOSE' \
                and littleFingerState == 'CLOSE':
            recognizedHandGesture = "Fist"  # "FIST"

        elif thumbState == 'CLOSE' and indexFingerState == 'OPEN' \
                and middleFingerState == 'OPEN' and ringFingerState == 'CLOSE' \
                and littleFingerState == 'CLOSE':
            recognizedHandGesture = "2"  # "Victory"

        elif (
                thumbState == 'OPEN' and thumbLeft and indexFingerState == 'CLOSE' and middleFingerState == 'CLOSE' and ringFingerState == 'CLOSE' and littleFingerState == 'CLOSE'):
            recognizedHandGesture = 'Thumb Left'
        elif (
                thumbState == 'OPEN' and thumbRight and indexFingerState == 'CLOSE' and middleFingerState == 'CLOSE' and ringFingerState == 'CLOSE' and littleFingerState == 'CLOSE'):
            recognizedHandGesture = 'Thumb Right'


        elif thumbState == 'CLOSE' and indexFingerState == 'OPEN' \
                and middleFingerState == 'CLOSE' and ringFingerState == 'CLOSE' \
                and littleFingerState == 'CLOSE':

            recognizedHandGesture = "1" 
        else:
            recognizedHandGesture = "0" 

        #print ( thumbState ,
        #        indexFingerState ,
        #        middleFingerState ,
        #        ringFingerState ,
        #        littleFingerState ,
        #        )
        return recognizedHandGesture

# For webcam input:
def oncamerafeed(window):
  window.destroy()
  started = False
  cap = cv2.VideoCapture(0)
  #rand = 0
  oldgesture = "Open Palm"
  run('explorer.exe shell:appsFolder\\'+ PackageFamilyName +'!'+Id)
  print("Press Ctrl + C to exit the program!")
  with mp_hands.Hands(
      min_detection_confidence=0.5,
      min_tracking_confidence=0.5, max_num_hands = 1) as hands:
    while cap.isOpened():
    #   pydirectinput.sleep(0.5)
      success, image = cap.read()
      if not success:
        print("Ignoring empty camera frame.")
        # If loading a video, use 'break' instead of 'continue'.
        continue

      # Flip the image horizontally for a later selfie-view display, and convert
      # the BGR image to RGB.
      image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
      # To improve performance, optionally mark the image as not writeable to
      # pass by reference.
      image.flags.writeable = False
      results = hands.process(image)

      # Draw the hand annotations on the image.
      image.flags.writeable = True
      image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
      if results.multi_hand_landmarks:
        
        for hand_landmarks in results.multi_hand_landmarks:
          #print(hand_landmarks.landmark[0])
          mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
          landmark_data = []
        #   print(started)
          if not started:
            if pyautogui.locateOnScreen('gas.png',confidence=0.7) != None:
              started = True
          else:
            for i in range(21):
              landmark_data.append(hand_landmarks.landmark[i].x)
              landmark_data.append(hand_landmarks.landmark[i].y)
            recognizedHandGesture = recognizeHandGesture(getStructuredLandmarks(landmark_data), label)
            if(recognizedHandGesture != oldgesture):
                oldgesture = recognizedHandGesture
                print(recognizedHandGesture)
                if (recognizedHandGesture == 'Open Palm'):
                    pydirectinput.keyUp('right')
                    pydirectinput.keyDown('left')
                    print('left')
                elif (recognizedHandGesture == 'Fist' or recognizedHandGesture == 'Thumb Left' ):
                    pydirectinput.keyUp('left')
                    pydirectinput.keyDown('right')
                    print('right')
                else:
                    pydirectinput.keyUp('right')
                    pydirectinput.keyUp('left')
                    print('none')
                if pyautogui.locateOnScreen('game_end.png', confidence = 0.8, grayscale=True) != None:
                    started = False
      sleep(0.05)
        #   /else:
            #pass
            #print("same")
          #print ('recognized hand gesture: ' , recognizedHandGesture)
          #print(len(landmark_data))

    #   cv2.imshow('Gestures', image)
    #   if cv2.waitKey(5) & 0xFF == 27:
    #     break
  cap.release()

from tkinter import *
if __name__ == "__main__":
    oncamerafeed(Tk())