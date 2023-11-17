import typing
from PyQt5.QtCore import *
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import *
import cv2 as cv
import numpy as np

## CONSTANTS 

BODY_PARTS = { "Nose": 0, "Neck": 1, "RShoulder": 2, "RElbow": 3, "RWrist": 4,
               "LShoulder": 5, "LElbow": 6, "LWrist": 7, "RHip": 8, "RKnee": 9,
               "RAnkle": 10, "LHip": 11, "LKnee": 12, "LAnkle": 13, "REye": 14,
               "LEye": 15, "REar": 16, "LEar": 17, "Background": 18 }

POSE_PAIRS = [ ["Neck", "RShoulder"], ["Neck", "LShoulder"], ["RShoulder", "RElbow"],
               ["RElbow", "RWrist"], ["LShoulder", "LElbow"], ["LElbow", "LWrist"],
               ["Neck", "RHip"], ["RHip", "RKnee"], ["RKnee", "RAnkle"], ["Neck", "LHip"],
               ["LHip", "LKnee"], ["LKnee", "LAnkle"], ["Neck", "Nose"], ["Nose", "REye"],
               ["REye", "REar"], ["Nose", "LEye"], ["LEye", "LEar"] ]

inWidth = 368
inHeight = 368
thr = 0.2


class CamWorker(QObject):
    finished = pyqtSignal()

    @pyqtSlot()
    def __init__(self) -> None:
        super(CamWorker,self).__init__()
        self.working = True
        self.net = cv.dnn.readNetFromTensorflow("graph_opt.pb")
        self.upper_body_parts = ["Nose", "Neck", "RShoulder", "LShoulder", "REye", "LEye"]
        self.cap = cv.VideoCapture(0)
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


    def work(self):
        while self.working:
            hasFrame, frame = self.cap.read()
            if not hasFrame:
                cv.waitKey()
                break

            frameWidth = frame.shape[1]
            frameHeight = frame.shape[0]
            gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))
            
            num_persons = len(faces)
            if num_persons == 0:
                print("please come in frame")
            else :
                print(f"more than one persone detected : {num_persons}")

            self.net.setInput(cv.dnn.blobFromImage(frame, 1.0, (inWidth, inHeight), (127.5, 127.5, 127.5), swapRB=True, crop=False))
            out = self.net.forward()
            out = out[:, :19, :, :]  # MobileNet output [1, 57, -1, -1], we only need the first 19 elements

            assert(len(BODY_PARTS) == out.shape[1])

            points = []
            for i in range(len(BODY_PARTS)):
                # Slice heatmap of corresponding body's part.
                heatMap = out[0, i, :, :]

                # Originally, we try to find all the local maximums. To simplify a sample
                # we just find a global one. However only a single pose at the same time
                # could be detected this way.
                _, conf, _, point = cv.minMaxLoc(heatMap)
                x = (frameWidth * point[0]) / out.shape[3]
                y = (frameHeight * point[1]) / out.shape[2]
                # Add a point if its confidence is higher than the threshold.
                points.append((int(x), int(y)) if conf > thr else None)
            upper_body_visible = all(points[BODY_PARTS[part]] is not None for part in self.upper_body_parts)
        #     if upper_body_visible:
        #         print("Upper body is visible!")
        #     else:
        #         print("not visible!")


            for pair in POSE_PAIRS:
                partFrom = pair[0]
                partTo = pair[1]
                assert(partFrom in BODY_PARTS)
                assert(partTo in BODY_PARTS)

                idFrom = BODY_PARTS[partFrom]
                idTo = BODY_PARTS[partTo]
                # print([partFrom,partTo,idFrom,partTo])

                # if points[idFrom] and points[idTo]:
                #     cv.line(frame, points[idFrom], points[idTo], (0, 255, 0), 3)
                #     cv.ellipse(frame, points[idFrom], (3, 3), 0, 0, 360, (0, 0, 255), cv.FILLED)
                #     cv.ellipse(frame, points[idTo], (3, 3), 0, 0, 360, (0, 0, 255), cv.FILLED)

            t, _ = self.net.getPerfProfile()
            freq = cv.getTickFrequency() / 1000
            #cv.putText(frame, '%.2fms' % (t / freq), (10, 20), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
            if upper_body_visible:
                # cv.putText(frame,"Upper body is visible!",(10,20), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
                print("Upper body is visible!")
                ## do what ever you wanted to do here
                #print("Upper body is visible!")
            else :
                pass
        self.finished.emit() 
        
            # cv.imshow('OpenPose using OpenCV', frame)