import cv2
import zmq

cap = cv2.VideoCapture(0)
# context = zmq.Context()
context = zmq.Context(io_threads=8)
sender = context.socket(zmq.PUSH)
sender.bind("tcp://*:5557")

frame_id = 0
while True:
    ret, frame = cap.read()
    print(frame)
    data = {
        'frame':frame,
        'frame_id':frame_id,
    }
    sender.send_pyobj(data)
    frame_id += 1
    # cv2.imshow('frame',frame)