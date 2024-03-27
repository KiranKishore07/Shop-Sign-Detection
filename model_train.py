from ultralytics import YOLO


def model_train():
    """
    Train a YOLOv8-L object detection model.

    Parameters:
        None

    Returns:
        None

    Notes:
        - Ensure the 'yolov8l.pt' model weights file is available.
        - Provide the path to the YAML file containing dataset configuration.
        - Set parameters for training: epochs, optimizer, learning rate, image size, etc.
        - Cache images for faster training if desired.
        - Adjust dropout and weight decay for regularization.
    """
  model = YOLO("yolov8l.pt")
  model.train(data="your path to 'YAML' file goes here",
            epochs=30, optimizer = 'Adam', lr0=0.000001, lrf=1, cache=True, 
            imgsz=416, weight_decay=0.0001, dropout=0.1)            