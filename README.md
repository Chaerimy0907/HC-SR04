# 01. 초음파 거리 센서에 따른 거북이 제어

## MVP(Minimum Viable Product) : 최소 기능
- 초음파 센서로 장애물을 감지하면 직전하던 거북이가 정지

## 동작 설명
1. Serial 연결
   
2. 데이터 처리
  - 2~200 사이의 값만 받을 수 있게 작성

3. Turtle 기본 설정
  - 스크린 설정
  - 거북이 기본 설정(모양, 속도)

4. main 함수
  - distance 값을 읽을 수 있을 때
  - 그 값이 10 미만인 경우엔 거북이 정지
  - 다른 경우엔 전진
  - ```python
    '''
    거북이가 창에서 사라지지 않게 moving_right 상태변수를 이용하여
    거북이의 x 좌표가 -200 또는 200 일 때 방향을 전환하여 직진함
    '''
    
    x, y = turtle.pos()
    if moving_right and x >= 200:          # 거북이가 오른쪽으로 가고, x가 200 이상일 때
       print("방향 전환")
       turtle.setheading(180)
       moving_right = False
    elif not moving_right and x <= -200:   # 거북이가 왼쪽으로 가고, x가 -200 이하일 때
       print("방향 전환")
       turtle.setheading(0)
       moving_right = True
    ```


### 거리 측정이 불안정하여 코드 수정 필요

# 02. Servo 모터에 따른 거북이 제어

## mvp
- 아두이노에서 스위치를 누르면 서보모터가 일정 횟수 회전 후 Thonny로 신호를 보내 거북이가 앞으로 전진

## 동작 설명
1. 아두이노
- 버튼 핀을 2번으로 설정
- 내부 풀업 저항 사용
- 버튼의 기본값 1(HIGH)
- 서보모터 핀을 6번으로 설정
- 스위치가 눌리면 서보모터 일정 횟수 회전 시작 0->180->0 을 한 번 회전한 것으로 설정
- 회전 후 0,180,0을 Thonny로 전송
- 스위치 신호가 HIGH로 바뀌기 전까지 다시 입력 받지않음

2. Thonny
- serial,time,turtle 모듈 import
- turtle 생성
- serial 연결 성공 여부 확인
- 서보모터의 pos 값 읽기
- 서보모터의 회전 감지
- 0 -> 180 -> 0 을 한 바퀴로 지정하여 총 10번 회전할 시 거북이 50픽셀 전진
- 50ms 후 함수 다시 실행
