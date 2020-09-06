import time
import zmq
import numpy

def server():
    print("ZMQ server starting ... ")
    # context = zmq.Context()
    context = zmq.Context(io_threads=8)
    consumer_receiver = context.socket(zmq.PULL)
    consumer_receiver.connect("tcp://localhost:5557")

    consumer_sender = context.socket(zmq.PUSH)
    consumer_sender.bind("tcp://*:5558")
    print("ZMQ server 1 started ! ")
    while True:
        data = consumer_receiver.recv_pyobj()
        print("P:{} - frame:{}".format(1,data['frame_id']))
        consumer_sender.send_pyobj(data)

if __name__ == '__main__':
    server()