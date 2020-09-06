import cv2
import zmq
import time
# context = zmq.Context()
context = zmq.Context(io_threads=8)
zmq_socket = context.socket(zmq.PULL)
zmq_socket.connect("tcp://localhost:5558")

count = 0
current = time.time()
while True:
    now = time.time()
    frame = zmq_socket.recv_pyobj()['frame']
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if now > current+1:
        print(count)
        current = now
        count = 0
    count += 1