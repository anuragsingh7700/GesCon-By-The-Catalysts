import cv2
import mediapipe as mp
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

        thumbState = 'UNKNOW'

        indexFingerState = 'UNKNOW'
        middleFingerState = 'UNKNOW'
        ringFingerState = 'UNKNOW'
        littleFingerState = 'UNKNOW'
        thumbRight = False
        thumbLeft = False
        recognizedHandGesture = None
        if (landmarks[4]['y'] < landmarks[3]['y'] < landmarks[5]['y'] < landmarks[9]['y'] < landmarks[13]['y'] <
                landmarks[17]['y'] and landmarks[6]['x'] < landmarks[7]['x']):
            print ( 'Thumbs Up' )

        elif (landmarks[4]['y'] > landmarks[3]['y'] > landmarks[5]['y'] > landmarks[9]['y'] > landmarks[13]['y'] >
              landmarks[17]['y'] and landmarks[6]['x'] < landmarks[7]['x']):
            print ( 'Thumbs down' )

        if label.strip () == 'Left':
            print ( 'left' )
            pseudoFixKeyPoint = landmarks[2]['x']

            if pseudoFixKeyPoint < landmarks[3]['x'] < landmarks[4]['x']:
                thumbState = 'OPEN'
            elif pseudoFixKeyPoint > landmarks[3]['x'] > landmarks[4]['x']:
                thumbState = 'CLOSE'

        else:

            pseudoFixKeyPoint = landmarks[2]['x']

            if pseudoFixKeyPoint < landmarks[3]['x'] < landmarks[4]['x']:
                thumbState = 'CLOSE'
            elif pseudoFixKeyPoint > landmarks[3]['x'] > landmarks[4]['x']:
                thumbState = 'OPEN'

        if (pseudoFixKeyPoint < landmarks[3]['x'] < landmarks[4]['x'] and landmarks[4]['x'] >
                landmarks[17]['x']):
            thumbRight = True
        elif (pseudoFixKeyPoint > landmarks[3]['x'] > landmarks[4]['x'] and landmarks[4]['x'] <
              landmarks[17]['x']):
            thumbLeft = True

        pseudoFixKeyPoint = landmarks[6]['y']
        if pseudoFixKeyPoint > landmarks[7]['y'] > landmarks[8]['y']:
            indexFingerState = 'OPEN'
        elif pseudoFixKeyPoint < landmarks[7]['y'] < landmarks[8]['y']:
            indexFingerState = 'CLOSE'

        pseudoFixKeyPoint = landmarks[10]['y']
        if pseudoFixKeyPoint > landmarks[11]['y'] > landmarks[12]['y']:
            middleFingerState = 'OPEN'
        elif pseudoFixKeyPoint < landmarks[11]['y'] < landmarks[12]['y']:
            middleFingerState = 'CLOSE'

        pseudoFixKeyPoint = landmarks[14]['y']
        if pseudoFixKeyPoint > landmarks[15]['y'] > landmarks[16]['y']:
            ringFingerState = 'OPEN'
        elif pseudoFixKeyPoint < landmarks[15]['y'] < landmarks[16]['y']:
            ringFingerState = 'CLOSE'

        pseudoFixKeyPoint = landmarks[18]['y']
        if pseudoFixKeyPoint > landmarks[19]['y'] > landmarks[20]['y']:
            littleFingerState = 'OPEN'
        elif pseudoFixKeyPoint < landmarks[19]['y'] < landmarks[20]['y']:
            littleFingerState = 'CLOSE'

        if thumbState == 'OPEN' and indexFingerState == 'OPEN' and middleFingerState == 'OPEN' and ringFingerState == 'OPEN' and littleFingerState == 'OPEN':
            recognizedHandGesture = "Open Palm" # "FIVE"

        elif thumbState == 'CLOSE' and indexFingerState == 'OPEN' \
                and middleFingerState == 'OPEN' and ringFingerState == 'OPEN' \
                and littleFingerState == 'OPEN':

            # scrolling(landmarks[0]['x']*img_width,landmarks[0]['y']*img_height)
            #     slide(landmarks[0]['x']*img_width,landmarks[0]['y']*img_height,landmarks[9]['x']*img_width,landmarks[9]['y']*img_height)
            #     keyboard.press_and_release('Page Down')

            recognizedHandGesture = 4  # "FOUR"
        elif thumbState == 'CLOSE' and indexFingerState == 'OPEN' \
                and middleFingerState == 'OPEN' and ringFingerState == 'OPEN' \
                and littleFingerState == 'CLOSE':

            recognizedHandGesture = 3  # "THREE"

        elif thumbState == 'OPEN' and indexFingerState == 'OPEN' \
                and middleFingerState == 'CLOSE' and ringFingerState == 'CLOSE' \
                and littleFingerState == 'CLOSE':

            #pressKey ( ges_key['2'] )
            recognizedHandGesture = 2  # "TWO"

        elif thumbState == 'CLOSE' and indexFingerState == 'CLOSE' \
                and middleFingerState == 'CLOSE' and ringFingerState == 'CLOSE' \
                and littleFingerState == 'CLOSE':
            recognizedHandGesture = 'Fist'  # "FIST"

        elif thumbState == 'CLOSE' and indexFingerState == 'OPEN' \
                and middleFingerState == 'OPEN' and ringFingerState == 'CLOSE' \
                and littleFingerState == 'CLOSE':
            recognizedHandGesture = 'Victory'  # "Victory"

        elif (
                thumbState == 'OPEN' and thumbLeft and indexFingerState == 'CLOSE' and middleFingerState == 'CLOSE' and ringFingerState == 'CLOSE' and littleFingerState == 'CLOSE'):
            recognizedHandGesture = 'Thumb Left'
        elif (
                thumbState == 'OPEN' and thumbRight and indexFingerState == 'CLOSE' and middleFingerState == 'CLOSE' and ringFingerState == 'CLOSE' and littleFingerState == 'CLOSE'):
            recognizedHandGesture = 'Thumb Right'


        elif thumbState == 'CLOSE' and indexFingerState == 'OPEN' \
                and middleFingerState == 'CLOSE' and ringFingerState == 'CLOSE' \
                and littleFingerState == 'CLOSE':

            #     keyboard.press('Ctrl')
            recognizedHandGesture = 1  # "1"
        else:
            #     print(landmarks[8]['x'], landmarks[8]['y'])
            #     pyautogui.moveTo(landmarks[8]['x']*1080*2, landmarks[8]['y']*1920*2, duration = 0.1)
            recognizedHandGesture = 0  # "UNKNOW"

        print ( thumbState ,
                indexFingerState ,
                middleFingerState ,
                ringFingerState ,
                littleFingerState ,

                )
        return recognizedHandGesture
##  global select_ges
##
##  thumbState = 'UNKNOW'
##
##  indexFingerState = 'UNKNOW'
##  middleFingerState = 'UNKNOW'
##  ringFingerState = 'UNKNOW'
##  littleFingerState = 'UNKNOW'
##  thumbRight = False
##  thumbLeft = False
##  recognizedHandGesture = None
##
##  pseudoFixKeyPoint = landmarks[2]['x']
##
##  if pseudoFixKeyPoint < landmarks[3]['x'] < landmarks[4]['x']:
##      thumbState = 'CLOSE'
##  elif pseudoFixKeyPoint > landmarks[3]['x'] > landmarks[4]['x']:
##      thumbState = 'OPEN'
##
##  if (pseudoFixKeyPoint < landmarks[3]['x'] < landmarks[4]['x'] and landmarks[4]['x'] >
##          landmarks[17]['x']):
##      thumbRight = True
##  elif (pseudoFixKeyPoint > landmarks[3]['x'] > landmarks[4]['x'] and landmarks[4]['x'] <
##        landmarks[17]['x']):
##      thumbLeft = True
##
##  pseudoFixKeyPoint = landmarks[6]['y']
##  if pseudoFixKeyPoint > landmarks[7]['y'] > landmarks[8]['y']:
##      indexFingerState = 'OPEN'
##  elif pseudoFixKeyPoint < landmarks[7]['y'] < landmarks[8]['y']:
##      indexFingerState = 'CLOSE'
##
##  pseudoFixKeyPoint = landmarks[10]['y']
##  if pseudoFixKeyPoint > landmarks[11]['y'] > landmarks[12]['y']:
##      middleFingerState = 'OPEN'
##  elif pseudoFixKeyPoint < landmarks[11]['y'] < landmarks[12]['y']:
##      middleFingerState = 'CLOSE'
##
##  pseudoFixKeyPoint = landmarks[14]['y']
##  if pseudoFixKeyPoint > landmarks[15]['y'] > landmarks[16]['y']:
##      ringFingerState = 'OPEN'
##  elif pseudoFixKeyPoint < landmarks[15]['y'] < landmarks[16]['y']:
##      ringFingerState = 'CLOSE'
##
##  pseudoFixKeyPoint = landmarks[18]['y']
##  if pseudoFixKeyPoint > landmarks[19]['y'] > landmarks[20]['y']:
##      littleFingerState = 'OPEN'
##  elif pseudoFixKeyPoint < landmarks[19]['y'] < landmarks[20]['y']:
##      littleFingerState = 'CLOSE'
##
##  if thumbState == 'OPEN' and indexFingerState == 'OPEN' and middleFingerState == 'OPEN' and ringFingerState == 'OPEN' and littleFingerState == 'OPEN' and '5' in select_ges:
##      recognizedHandGesture = 5  # "FIVE"
##      #pressKey ( ges_key['5'] )
##
##
##  if thumbState == 'CLOSE' and indexFingerState == 'CLOSE' \
##          and middleFingerState == 'CLOSE' and ringFingerState == 'CLOSE' \
##          and littleFingerState == 'CLOSE' and 'Fist' in select_ges:
##      #pressKey ( ges_key['Fist'] )
##      recognizedHandGesture = 'Fist'  # "FIST"
##
##  print ( thumbState ,
##          indexFingerState ,
##          middleFingerState ,
##          ringFingerState ,
##          littleFingerState ,
##
##          )
##
##  return recognizedHandGesture

# For webcam input:
cap = cv2.VideoCapture(0)
with mp_hands.Hands(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
  while cap.isOpened():
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
        print(hand_landmarks.landmark[0])
        mp_drawing.draw_landmarks(
            image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
        landmark_data = []
        for i in range(21):
          landmark_data.append(hand_landmarks.landmark[i].x)
          landmark_data.append(hand_landmarks.landmark[i].y)
        print(len(landmark_data))
        recognizedHandGesture = recognizeHandGesture(getStructuredLandmarks(landmark_data), label)
        print ('recognized hand gesture: ' , recognizedHandGesture )
        print(len(landmark_data))
##        for point in hand_landmarks.landmark:
##          #print(point)
##          landmark_data.append(point.x)
##          landmark_data.append(point.y)
##          recognizedHandGesture = recognizeHandGesture ( getStructuredLandmarks ( landmark_data ))
##          print ( 'recognized hand gesture: ' , recognizedHandGesture )
    cv2.imshow('Gestures', image)
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()
