import cv2
import numpy as np
import sys
import json
import os

try:
    config_path = os.path.join(os.path.dirname(__file__), "config.json")
    with open(config_path, "r") as f:
        config = json.load(f)
except FileNotFoundError:
    config = {}

ip = config.get("raspberry_pi_ip", "192.168.XXX.XXX")  # 수정: "ip" → "raspberry_pi_ip"
port = config.get("port", 8080)
stream_url = f"http://{ip}:{port}/?action=stream"  # 라즈베리파이의 스트리밍 URL
cap = cv2.VideoCapture(stream_url)
if cap.isOpened():
    print("비디오 스트림 연결 성공:", stream_url)
else:
    print("비디오 스트림 연결 실패:", stream_url)

def load_yolo():
    cfg_path = "/home/dev/line_ai/models/yolov3.cfg"
    weights_path = "/home/dev/line_ai/models/yolov3.weights"
    # Check if configuration and weights files exist
    if not os.path.exists(cfg_path) or not os.path.exists(weights_path):
        print(f"ERROR: YOLO config or weights file not found: {cfg_path} or {weights_path}")
        sys.exit(1)
    
    # 추가: cfg 파일에 유효한 내용(빈 줄이 아닌)이 있는지 검사
    with open(cfg_path, "r", encoding="utf-8", errors="replace") as f:
        lines = f.readlines()
    meaningful_lines = [line for line in lines if line.strip()]
    if not meaningful_lines:
        print(f"ERROR: YOLO config file appears to be empty or invalid: {cfg_path}")
        print("       Please download the official yolov3.cfg from:")
        print("       https://raw.githubusercontent.com/pjreddie/darknet/master/cfg/yolov3.cfg")
        sys.exit(1)
    
    try:
        net = cv2.dnn.readNetFromDarknet(cfg_path, weights_path)
    except cv2.error as e:
        print("DEBUG: 첫 5줄의 cfg 파일 내용:", lines[:5])
        print(f"ERROR: Failed to load YOLO network: {e}")
        sys.exit(1)
    net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
    net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA) 

    # YOLO 출력 레이어의 이름을 가져옴 (scalar index 오류 방지)
    try:
        # OpenCV >=4.7: 바로 이름 리스트를 반환
        output_layers = net.getUnconnectedOutLayersNames()
    except AttributeError:
        # 이전 버전 호환: 인덱스 flatten 처리
        layer_names = net.getLayerNames()
        outs = net.getUnconnectedOutLayers()
        outs = outs.flatten() if hasattr(outs, "flatten") else [int(outs)]
        output_layers = [layer_names[i - 1] for i in outs]

    # 변경: coco.names 위치 지정 및 존재 검사
    names_path = "/home/dev/line_ai/models/coco.names"
    if not os.path.exists(names_path):
        print(f"ERROR: coco.names file not found: {names_path}")
        print("       Please download it from:")
        print("       https://raw.githubusercontent.com/pjreddie/darknet/master/data/coco.names")
        sys.exit(1)
    with open(names_path, "r") as f:
        classes = [line.strip() for line in f.readlines()]
    return net, classes, output_layers

def detect_people(image_path):
    image = cv2.imread(image_path)
    height, width, _ = image.shape

    # 이미지를 YOLO에 맞게 blob으로 변환
    blob = cv2.dnn.blobFromImage(image, 1/255.0, (416, 416), swapRB=True, crop=False)
    net, classes, output_layers = load_yolo()
    net.setInput(blob)
    outs = net.forward(output_layers)

    person_count = 0
    # 각 검출 결과를 처리함
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            # 감지된 객체가 사람이고 신뢰도가 충분할 경우 처리함
            if classes[class_id] == "person" and confidence > 0.5:
                person_count += 1
    return person_count

# 실시간 비디오 프레임 처리를 위한 새 함수
def detect_people_in_frame(frame):
    height, width, _ = frame.shape
    # 프레임을 YOLO에 맞게 blob으로 변환
    blob = cv2.dnn.blobFromImage(frame, 1/255.0, (416, 416), swapRB=True, crop=False)
    net, classes, output_layers = load_yolo()
    net.setInput(blob)
    outs = net.forward(output_layers)
    person_count = 0
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if classes[class_id] == "person":
                print("DEBUG: detected person with confidence", confidence)  # 디버그 출력
            if confidence > 0.3:  # 기존 threshold를 낮춤
                person_count += 1
    return person_count

if __name__ == "__main__":
    net, classes, output_layers = load_yolo()  # load YOLO model once
    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame_count += 1
        if frame_count % 3 == 0:  # 3번째 프레임마다 YOLO 적용
            blob = cv2.dnn.blobFromImage(frame, 1/255.0, (416, 416), swapRB=True, crop=False)
            net.setInput(blob)
            detections = net.forward(output_layers)
            print(f"DEBUG: Frame {frame_count} detections: {detections}")  # 추가 로그
            # ...optional processing of detections...
        cv2.imshow("Frame", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
