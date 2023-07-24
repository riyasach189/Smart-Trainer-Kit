const int clock_0_1_hz = A3;
const int clock_1_hz = A4;
const int clock_10_hz = A5;

const int detector_0_1_hz = A0;
const int detector_1_hz = A1;
const int detector_10_hz = A2;

const int input_1 = 10;
const int input_2 = 3;
const int input_3 = 4;
const int input_4 = 5;
const int input_5 = 6;
const int input_6 = 7;
const int input_7 = 8;
const int input_8 = 11;


void setup() {
  
  Serial.begin(9600);
  
  pinMode(clock_0_1_hz,OUTPUT);
  pinMode(clock_1_hz,OUTPUT);
  pinMode(clock_10_hz,OUTPUT);

  pinMode(detector_0_1_hz,INPUT);
  pinMode(detector_1_hz,INPUT);
  pinMode(detector_10_hz,INPUT);

  digitalWrite(clock_0_1_hz,LOW);
  digitalWrite(clock_1_hz,LOW);
  digitalWrite(clock_10_hz,LOW);  

  pinMode(input_1,OUTPUT);
  pinMode(input_2,OUTPUT);
  pinMode(input_3,OUTPUT);
  pinMode(input_4,OUTPUT);
  pinMode(input_5,OUTPUT);
  pinMode(input_6,OUTPUT);
  pinMode(input_7,OUTPUT);
  pinMode(input_8,OUTPUT);  

  digitalWrite(input_1,HIGH);
  digitalWrite(input_2,HIGH);
  digitalWrite(input_3,HIGH);
  digitalWrite(input_4,HIGH);
  digitalWrite(input_5,HIGH);
  digitalWrite(input_6,HIGH);
  digitalWrite(input_7,HIGH);
  digitalWrite(input_8,HIGH);  
}

void loop() {

  digitalWrite(clock_0_1_hz,HIGH);
  for(int j = 0; j < 5; j++)
  {
    digitalWrite(clock_1_hz,HIGH);
    for(int i = 0; i < 5; i++)
    {
      digitalWrite(clock_10_hz,HIGH);
      Serial.print(analogRead(detector_10_hz));
      Serial.print(",");
      Serial.print(analogRead(detector_1_hz));
      Serial.print(",");
      Serial.print(analogRead(detector_0_1_hz));
      Serial.println("");
      delay(50);
      digitalWrite(clock_10_hz,LOW);
      Serial.print(analogRead(detector_10_hz));
      Serial.print(",");
      Serial.print(analogRead(detector_1_hz));
      Serial.print(",");
      Serial.print(analogRead(detector_0_1_hz));
      Serial.println("");
      delay(50);
    }
    digitalWrite(clock_1_hz,LOW);
    for(int i = 0; i < 5; i++)
    {
      digitalWrite(clock_10_hz,HIGH);
      Serial.print(analogRead(detector_10_hz));
      Serial.print(",");
      Serial.print(analogRead(detector_1_hz));
      Serial.print(",");
      Serial.print(analogRead(detector_0_1_hz));
      Serial.println("");
      delay(50);
      digitalWrite(clock_10_hz,LOW);
      Serial.print(analogRead(detector_10_hz));
      Serial.print(",");
      Serial.print(analogRead(detector_1_hz));
      Serial.print(",");
      Serial.print(analogRead(detector_0_1_hz));
      Serial.println("");
      delay(50);
    }
  }
  digitalWrite(clock_0_1_hz,LOW);
  for(int j = 0; j < 5; j++)
  {
    digitalWrite(clock_1_hz,HIGH);
    for(int i = 0; i < 5; i++)
    {
      digitalWrite(clock_10_hz,HIGH);
      Serial.print(analogRead(detector_10_hz));
      Serial.print(",");
      Serial.print(analogRead(detector_1_hz));
      Serial.print(",");
      Serial.print(analogRead(detector_0_1_hz));
      Serial.println("");
      delay(50);
      digitalWrite(clock_10_hz,LOW);
      Serial.print(analogRead(detector_10_hz));
      Serial.print(",");
      Serial.print(analogRead(detector_1_hz));
      Serial.print(",");
      Serial.print(analogRead(detector_0_1_hz));
      Serial.println("");
      delay(50);
    }
    digitalWrite(clock_1_hz,LOW);
    for(int i = 0; i < 5; i++)
    {
      digitalWrite(clock_10_hz,HIGH);
      Serial.print(analogRead(detector_10_hz));
      Serial.print(",");
      Serial.print(analogRead(detector_1_hz));
      Serial.print(",");
      Serial.print(analogRead(detector_0_1_hz));
      Serial.println("");
      delay(50);
      digitalWrite(clock_10_hz,LOW);
      Serial.print(analogRead(detector_10_hz));
      Serial.print(",");
      Serial.print(analogRead(detector_1_hz));
      Serial.print(",");
      Serial.print(analogRead(detector_0_1_hz));
      Serial.println("");
      delay(50);
    }
  }
}

