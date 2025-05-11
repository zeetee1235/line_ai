# line_ai

## 프로젝트 개요
Line AI는 LINE 메신저와 인공지능을 연동하여 자연스러운 대화 경험을 제공하는 서비스입니다.

## 팀 정보
- 팀명: CrowdSync  
- 팀장: 이건형  
- 팀원: 최요한  

## 특별한 감사
- 김나혜

## 사용 방법
1. 저장소 클론  
   ```bash
   git clone https://github.com/your-org/line_ai.git
   cd line_ai
   ```
2. 환경 변수 설정  
   프로젝트 루트에 `.env` 파일을 생성하고 아래 값을 추가하세요.
   ```env
   LINE_CHANNEL_SECRET=your_line_secret
   LINE_CHANNEL_ACCESS_TOKEN=your_line_token
   OPENAI_API_KEY=your_openai_key
   ```
3. 의존성 설치  
   ```bash
   npm install
   ```
4. 애플리케이션 실행  
   ```bash
   npm start
   ```
5. 웹훅 URL 설정  
   LINE Developers 콘솔에서 애플리케이션의 웹훅 URL을  
   `https://your-domain.com/webhook` 형태로 등록하세요.

6. Raspberry Pi에 raspi 폴더 배치  
   - 로컬의 `raspi/` 폴더를 Pi로 복사  
     ```bash
     scp -r raspi/ pi@<raspberry_ip>:/home/pi/line_ai/
     ```
   - 또는 Pi에서 직접 클론  
     ```bash
     ssh pi@<raspberry_ip>
     git clone https://github.com/zeetee1235/line_ai_raspi.git raspi
     ```
   - Pi에 접속 후 스크립트 실행  
     ```bash
     cd raspi
     ./start_stream.sh
     ```

## 프로젝트 구조
- `src/` : 소스 코드  
- `config/` : 설정 파일  

## 문의
버그 제보 및 기능 요청은 이슈 페이지에 남겨주세요.