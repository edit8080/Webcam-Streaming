# Flask 서버를 이용한 Webcam 스트리밍

## How To Use
1. flask 라이브러리 설치
```
pip install flask
```

2. OpenCV 라이브러리 설치
```
pip install opencv-python
```

3. app.py를 실행한 다음 localhost:5000으로 접속하세요.


만약 카메라가 정상적으로 나오지 않는다면 `camera = cv2.VideoCapture(1)` 의 인덱스를 0으로 수정해주세요.


## Screenshot
![webcam streaming](https://user-images.githubusercontent.com/30149272/114885944-1b6b9e80-9e42-11eb-9b1c-08aa66b7c6b4.jpg)
