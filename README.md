# 초음파 거리 센서에 따른 거북이 제어

## MVP(Minimum Viable Product) : 최소 기능
- 초음파 센서로 장애물을 감지하면 직전하던 거북이가 정지

# 동작 설명
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
