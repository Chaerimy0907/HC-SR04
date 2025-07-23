import serial
import time
import turtle

# Turtle 세팅
s=turtle.getscreen()
s.setup(600,600)
turtle.shape("turtle")

# 전역 변수
connection = None
rotation_count = 0
last_position=[]

# Serial 연결
def connect_sensor(port='COM5'):
    global connection
    try:
        connection = serial.Serial(port,9600)
        time.sleep(2)
        print("연결 성공")
        return True
    except:
        print("연결 실패")
        return False

# Servo 위치 읽기
def read_pos():
    global connection
    if connection and connection.in_waiting>0:
        try:
            data=connection.readline().decode().strip()
            pos=int(data)
            return pos
        except:
            return None
    return None
            
# 회전 감지 / 이동처리
def detect_rotation(pos):
    global last_position,rotation_count
    
    last_position.append(pos)
    if len(last_position)>3:
        last_position.pop(0)
        
    if last_position == [0,180,0]:
        rotation_count += 1
        last_position.clear()
        print(f"총 {rotation_count}회 회전")
        
        # 10번 회전하면 거북이 전진
        if rotation_count % 10 == 0:
            print("전진")
            turtle.forward(50)
            
# 메인
def main():
    if connect_sensor():
        while True:
            pos=read_pos()
            if pos is not None:
                detect_rotation(pos)
            time.sleep(0.05)
            
if __name__=="__main__":
    main()
