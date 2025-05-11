#!/bin/bash
echo "camera stream start"

# Port 8080 kill
pids=$(lsof -t -i:8080)
if [ -n "$pids" ]; then
    echo "포트 8080에서 실행 중인 프로세스 종료: $pids"
    kill -9 $pids
fi

# Python
python3 /dev/raspi/start_camera.py &

device_ip=$(hostname -I | awk '{print $1}')
echo "http://$device_ip:8080/video_feed"
