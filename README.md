# Line AI 프로젝트: 객체 인식 및 스트리밍 솔루션

![Project Banner](images/Line_Ai.png)

## 프로젝트 소개
Line AI 프로젝트는 **YOLOv3 기반의 객체 인식 시스템**과 **실시간 비디오 스트리밍** 기능을 제공하며, 실시간 감지와 스트리밍을 통해 빠르게 상황을 파악하고 대응할 수 있도록 설계되었습니다.

## 프로젝트 개요
- **목표**: 실시간 객체 감지를 통한 정보 제공 및 경보 시스템 구축.
- **주요 기능**:
  - 실시간 비디오 스트림 전송 및 객체 인식.
  - 라즈베리파이 기반의 경량 모듈 설치 지원.
  - 사용자 친화적인 검색 인터페이스 제공.
- **개발 환경**: Fedora Linux, Python, OpenCV, Flask, YOLOv3
- **개발 기간**: 2025년 5월 10일 ~ 2025년 5월 11일

## 팀 정보
- **팀명**: CrowdSync  
- **팀장**: 이건형  
- **팀원**: 최요한  

## 특별한 감사
- **김나혜**: 기획 및 디자인 기여자.
- **함형민 교수님**: 기술 지원 제공.

## 📂 설치 및 설정 가이드

### 1️⃣ 필수 패키지 설치
```sh
sudo dnf install opencv poppler-utils
pip install numpy opencv-python
```

### 2️⃣ YOLOv3 모델 파일 다운로드
```sh
wget https://pjreddie.com/media/files/yolov3.weights -O models/yolov3.weights
wget https://raw.githubusercontent.com/pjreddie/darknet/master/cfg/yolov3.cfg -O models/yolov3.cfg
wget https://github.com/msindev/YOLO-v3-Object-Detection/blob/master/coco.names -O models/coco.names
```

### 3️⃣ 라즈베리파이 설정 및 배포
라즈베리파이 환경에서 솔루션을 실행하는 두 가지 방법:

#### 방법 A: 로컬의 raspi 폴더 복사
```sh
scp -r raspi/ pi@<raspberry_ip>:/home/pi/line_ai/
```

#### 방법 B: 라즈베리파이에서 직접 클론
```sh
ssh pi@<raspberry_ip>
git clone https://github.com/zeetee1235/line_ai_raspi.git
```

라즈베리파이에서 스트리밍 시작:
```sh
cd raspi
./start_stream.sh
```

### 4️⃣ 애플리케이션 실행
로컬에서 메인 애플리케이션 실행:
```sh
/bin/python /home/dev/line_ai/src/main.py
```

## 📊 시스템 아키텍처 개요
- **데이터 소스**: 실시간 비디오 스트림 (IP 또는 USB 카메라)
- **백엔드**: Flask 웹 서버를 통한 스트리밍 제공
- **딥러닝 모델**: YOLOv3를 통한 객체 감지 및 분석
- **클라이언트**: 웹 검색 인터페이스 제공

## 🔍 사용자 웹 인터페이스
프로젝트는 `/home/dev/line_ai/src/index.html`와 `script.js`를 활용하여, 사용자가 매장 이름이나 주소로 검색하고, 결과를 쉽게 확인할 수 있도록 설계되었습니다.

## 🛠 환경 설정
환경 설정 값은 `/home/dev/line_ai/src/config.json` 파일에서 관리합니다.  
예시:
```json
{
    "raspberry_pi_ip": "192.168.xxx.xx",
    "port": "8080"
}
```

## 💡 추가 정보
- **비디오 스트리밍 URL**: 예시) `http://192.168.xxx.xx:8080/video_feed`   
- **YOLOv3 가중치 저장파일 손상**: 가끔 .weights 파일이 손상된 상태로 다운로드가 되는 경우가 있습니다. 그럴 경우 아래 연락처로 연락 바랍니다.

## 📞 문의 및 지원
문제 발생이나 기능 개선 요청은 깃허브 이슈 페이지 또는 아래 이메일로 연락주시기 바랍니다:  
**Contact**: zeetee1235@gmail.com

---
