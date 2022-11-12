import numpy as np
import cv2

cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

def main():
  while True:
    try:
      ret, frame = cap.read()
      
      # image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

      

      cv2.imshow("Feed",frame)

      if cv2.waitKey(1) == ord("q"):
        break
    except Exception as e:
      print("Camera failed to launch.")
      break
  cap.release()
  cv2.destroyAllWindows

if __name__ == '__main__':
  main()