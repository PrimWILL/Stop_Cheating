"""
This Code is only for test and it doesn't work. this code moved to ./UIsource/Exampage.py
"""


import cv2
import datetime
import numpy as np
import imutils
from imutils.video import FPS
from imutils.video import VideoStream
import time
import os

class control:
    def __init__(self):
        self.VideoSignal = cv2.VideoCapture(0)
        # cheating1 = more than 1 person detected
        self.is_cheating1 = False
        #cheating2 =  paper disappears
        self.is_cheating2 = False
        #cheating3 = cellphone detected
        self.is_cheating3 = False
        #cheating4 = person disappears ( 0 person detected)
        self.is_cheating4 = False
        #cheating5 = motinor disappears
        self.is_cheating5 = False



    def object_detector(self):
        YOLO_net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")

        classes = []
        with open("coco.names", "r") as f:
            classes = [line.strip() for line in f.readlines()]
        layer_names = YOLO_net.getLayerNames()
        output_layers = [layer_names[i[0] - 1] for i in YOLO_net.getUnconnectedOutLayers()]

        while True:

            ret, frame = self.VideoSignal.read()
            h, w, c = frame.shape

            blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
            YOLO_net.setInput(blob)
            outs = YOLO_net.forward(output_layers)

            class_ids = []
            confidences = []
            boxes = []

            for out in outs:


                for detection in out:


                    scores = detection[5:]
                    class_id = np.argmax(scores)
                    confidence = scores[class_id]

                    # 검출 신뢰도
                    if confidence > 0.1:
                        # Object detected
                        # 검출기의 경계상자 좌표는 0 ~ 1로 정규화되어있으므로 다시 전처리
                        center_x = int(detection[0] * w)
                        center_y = int(detection[1] * h)
                        dw = int(detection[2] * w)
                        dh = int(detection[3] * h)
                        # Rectangle coordinate
                        x = int(center_x - dw / 2)
                        y = int(center_y - dh / 2)
                        boxes.append([x, y, dw, dh])
                        confidences.append(float(confidence))
                        class_ids.append(class_id)

            indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.45, 0.4)

            for i in range(len(boxes)):
                if i in indexes:
                    x, y, w, h = boxes[i]
                    label = str(classes[class_ids[i]])
                    score = confidences[i]

                    # bounding box와 confidence score 표시
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 5)
                    cv2.putText(frame, label + str(score), (x, y - 20), cv2.FONT_ITALIC, 0.5, (255, 255, 255), 1)
            print(3)
            cv2.imshow("Webcam", frame)

            self.keyControl()


    def save_picture(self):
        ret, img = self.VideoSignal.read()
        if ret:
            now = datetime.datetime.now()
            date = now.strftime('%Y%m%d')
            hour = now.strftime('%H%M%S')
            user_id = 'student'
            filename = './images/Test_{}_{}_{}.png'.format(date, hour, user_id)
            cv2.imwrite(filename, img)


    #임시 함수. 조건 구현 되면 CheatingDetected으로 이동
    def keyControl(self):
        key = cv2.waitKey(1)
        # 키보드 q 누를시 images폴더에 캡쳐해서 저장
        if(key == ord('q')):
            self.save_picture()
        # 키보드 q 누를시 모든 창 종료
        if(key == ord('p')):
            self.VideoSignal.release()
            cv2.destroyAllWindows()


    def CheatingDetected(self):
        if(self.is_cheating1):
            self.save_picture()
        elif(self.is_cheating2):
            self.save_picture()
        elif (self.is_cheating3):
            self.save_picture()
        elif (self.is_cheating4):
            self.save_picture()
        elif (self.is_cheating5):
            self.save_picture()
