#include <Servo.h>

Servo myservo;  // create Servo object to control a servo
// twelve Servo objects can be created on most boards

int button = 2;
int buttonState = 0;
int pos = 0;    // variable to store the servo position
bool started = false;
bool buttonReleased = true;

void setup() {
  myservo.attach(6);  // attaches the servo on pin 9 to the Servo object
  pinMode(button, INPUT_PULLUP);
  Serial.begin(9600);
}

void loop() {
  int buttonState = digitalRead(button);

  if (!started && buttonState == 0){
    started = true;
    buttonReleased = false;
    delay(200);
  }

  if (buttonState == 1){
    buttonReleased = true;
  }

  if (started){
    for (int i =0;i<10;i++){
      for (pos=0;pos<=180; pos++){
      myservo.write(pos);
      delay(10);
    }

      for(pos=180;pos>=0;pos--){
        myservo.write(pos);
        delay(10);
      }

      Serial.println(0);
      Serial.println(180);
      Serial.println(0);
    }

    started = false;

  }
}