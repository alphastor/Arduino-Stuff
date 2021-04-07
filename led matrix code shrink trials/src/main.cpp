#include <Arduino.h>

char py_input;
int R[] = {2,3,4,5,6,7,8,9};
int C[] = {10,11,12,A4,A0,A1,A2,A3};

void setup(){
  Serial.begin(9600);
  for(int i=0;i<8;i++){
    pinMode(R[i],OUTPUT);
    pinMode(C[i],OUTPUT);
  }

  for(int i=0;i<8;i++){
    digitalWrite(R[i],HIGH);
    digitalWrite(C[i],LOW);
  }
}

void loop()
{
if(Serial.available()>0){
    py_input = Serial.read();
    if(py_input == 'a'){
        digitalWrite(R[0],LOW);
        digitalWrite(C[0],HIGH);
    }
    if(py_input == 'b'){
        digitalWrite(R[0],LOW);
        digitalWrite(C[1],HIGH);
    }
}
}