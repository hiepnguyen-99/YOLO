from ultralytics import YOLO

model = YOLO("yolov8/runs/detect/yolov8_bs32_e50_ims640/weights/best.pt")

try:
    results = model.predict(
        source=0,
        conf=0.7,
        show=True,
        name='mycam',
        verbose=False
    )
except KeyboardInterrupt:
    print('Dừng chương trình')