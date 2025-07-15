# app/detector/yolo_detector.py
import cv2
import numpy as np
import sqlite3
from datetime import datetime
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

def detect_giraffes(file):
    """file — объект UploadedFile из Flask"""
    img = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)
    results = model(img)

    boxes = []
    for b in results[0].boxes:
        if int(b.cls) == 24:  # giraffe
            x1, y1, x2, y2 = b.xyxy[0].tolist()
            boxes.append([x1, y1, x2 - x1, y2 - y1])

    # Рисуем и сохраняем
    out = results[0].plot()
    cv2.imwrite("app/static/result.jpg", out)

    # Запись в БД — только тут, где есть `file`
    conn = sqlite3.connect("history.db")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS requests(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            filename TEXT,
            count INTEGER
        )
    """)
    conn.execute("INSERT INTO requests (timestamp, filename, count) VALUES (?,?,?)",
                 (datetime.now().isoformat(), file.filename, len(boxes)))
    conn.commit()
    conn.close()

    return {"count": len(boxes)}