import serial
import time
import turtle

connection=None
current_distance=0
moving_right=True

def connect_sensor(port='COM3'):
    global connection
    try:
        connection=serial.Serial(port,9600)
        time.sleep(2)
        print("연결 성공")
        return True
    except:
        print("연결 실패")
        return False
    
def read_distance():
    global connection, current_distance
    if connection and connection.in_waiting>0:
        try:
            data=connection.readline().decode().strip()
            distance=float(data)
            
            if 2<=distance<=200:
                current_distance=distance
                return distance
        except:
            pass
    return None

# Turtle 초기 설정
s=turtle.getscreen()
s.setup(600,600)
turtle.shape("turtle")
turtle.speed=1



def main():
    global moving_right
    if connect_sensor():
        while True:
            dist = read_distance()
            if dist is not None:
                print(f" 거리 : {dist}cm")
                if dist < 10:
                    turtle.speed=0
                    print("장애물 감지 : 멈춤")
                else:
                    turtle.forward(10)
                    x,y=turtle.pos()
                    if moving_right and x>=200:
                        print("방향 전환")
                        turtle.setheading(180)
                        moving_right=False
                    elif not moving_right and x<=-200:
                        print("방향 전환")
                        turtle.setheading(0)
                        moving_right=True
            else:
                print("거리 데이터 없음")
            time.sleep(0.3)
        
if __name__=="__main__":
    main()