FROM python:3
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . /zmq/
WORKDIR /zmq/
# RUN sudo usermod -a -G video developer