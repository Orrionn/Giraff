import cv2
import numpy as np
from ultralytics import YOLO

model = YOLO("yolov8n.pt")  # загружается автоматически

def detect_giraffes(file):
    img = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)
    results = model(img)

    boxes = []
    for box in results[0].boxes:
        cls = int(box.cls)
        if cls == 24:  # giraffe
            x1, y1, x2, y2 = box.xyxy[0].tolist()
            boxes.append([x1, y1, x2 - x1, y2 - y1])

    # сохраняем изображение с боксами
    output_img = results[0].plot()
    cv2.imwrite('app/static/result.jpg', output_img)

    return {
        'count': len(boxes),
        'boxes': boxes
    }