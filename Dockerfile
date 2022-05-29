FROM python:3.10
WORKDIR /app
COPY requirements.txt ./requirements.txt
# RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 8501
COPY . /app
RUN cd object_detection_and_ocr/yolov5 && python detect_and_ocr.py --weights ../best.pt --img 416 --conf 0.4 --source a.jpg --crop --dest .
ENTRYPOINT ["streamlit", "run"]
CMD ["app.py"]



