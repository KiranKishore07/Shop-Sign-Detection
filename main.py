import cv2
import pafy
from ultralytics import YOLO
from paddleocr import PaddleOCR
import datetime
import pytz
import pandas as pd


def ocr_processing(frame):
    ocr = PaddleOCR()
    result = ocr.ocr(frame)
    shop_name = ' '.join([line[1][0] for line in result[0]])
    timestamp = datetime.datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%Y-%m-%d %H:%M:%S')
    return shop_name, timestamp


def model_prediction(frame):
    best_model = YOLO("your path to 'best.pt' model goes here")
    predictions = best_model.predict(frame)
    detected_objects = []
    if predictions:
        prediction = predictions[0]
        for box in prediction.boxes:
            class_name = prediction.names[box.cls[0].item()]
            coordinates = box.xyxy[0].tolist()
            coordinates = [round(x) for x in coordinates]
            probability = round(box.conf[0].item(), 2)
            if class_name == 'Shop-Sign' and probability > 0.5:
                print(f'The model has predicted the class {class_name} and its probability is {probability}')
                shop_name, timestamp = ocr_processing(frame)
                detected_object = {
                    'class': class_name,
                    'coordinates': coordinates,
                    'probability': probability,
                    'shop_name': shop_name,
                    'timestamp': timestamp
                }
                detected_objects.append(detected_object)

    return detected_objects


def update_shop_entries(detected_items, shop_entries):
    for obj in detected_items:
        if obj['class'] == 'Shop-Sign' and obj['probability'] > 0.5:
            shop_name = obj['shop_name']
            timestamp = obj['timestamp']
            if shop_name not in shop_entries:
                shop_entries[shop_name] = {'Entry Time': timestamp, 'Exit Time': None}
            else:
                shop_entries[shop_name]['Exit Time'] = timestamp


def process_video():
    video = pafy.new("please specify the YouTube Link here")
    best_stream = video.getbest()
    cap = cv2.VideoCapture(best_stream.url)
    shop_entries = {}

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        detected_items = model_prediction(frame)
        if detected_items:
            update_shop_entries(detected_items, shop_entries)

    df = pd.DataFrame.from_dict(shop_entries, orient='index')
    df.to_excel("your path to 'excel file' goes here")


if __name__ == "__main__":
    process_video()
