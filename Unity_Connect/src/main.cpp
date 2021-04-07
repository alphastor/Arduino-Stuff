#include <Arduino.h>

char py_input;                         // variable for user input
int row[] = {2,3,4,5,6,7,8,9};           // array of row pin numbers
int col[] = {10,11,12,A4,A0,A1,A2,A3};   // array of column pin numbers

void setup()
{
  Serial.begin(9600);

  for(int i = 0;i<8;i++)   // iterate over the pins
  {
    pinMode(row[i],OUTPUT);  // initialize the output pins
    pinMode(col[i],OUTPUT);  // initialize the output pins
  }
}

void loop()
{
if(Serial.available()>0)
{
  py_input = Serial.read();
  if(py_input == 'A'){
    digitalWrite(row[0],LOW);
    digitalWrite(col[0],HIGH);
  }
////////////////////////////////ROW_1////////////////////////////////
  if(py_input == 'B'){
    digitalWrite(row[0],LOW);
    digitalWrite(col[1],HIGH);
  }
  else{
    digitalWrite(row[0],HIGH);
    digitalWrite(col[1],LOW);
  }
////////////////////////////
  if(py_input == 'C'){
    digitalWrite(row[0],LOW);
    digitalWrite(col[2],HIGH);
  }
  else{
    digitalWrite(row[0],HIGH);
    digitalWrite(col[2],LOW);
  }
////////////////////////////
  if(py_input == 'D'){
    digitalWrite(row[0],LOW);
    digitalWrite(col[3],HIGH);
  }
  else{
    digitalWrite(row[0],HIGH);
    digitalWrite(col[3],LOW);
  }
////////////////////////////
  if(py_input == 'E'){
    digitalWrite(row[0],LOW);
    digitalWrite(col[4],HIGH);
  }
  else{
    digitalWrite(row[0],HIGH);
    digitalWrite(col[4],LOW);
  }
////////////////////////////
  if(py_input == 'F'){
    digitalWrite(row[0],LOW);
    digitalWrite(col[5],HIGH);
  }
  else{
    digitalWrite(row[0],HIGH);
    digitalWrite(col[5],LOW);
  }
////////////////////////////
  if(py_input == 'G'){
    digitalWrite(row[0],LOW);
    digitalWrite(col[6],HIGH);
  }
  else{
    digitalWrite(row[0],HIGH);
    digitalWrite(col[6],LOW);
  }
////////////////////////////
  if(py_input == 'H'){
    digitalWrite(row[0],LOW);
    digitalWrite(col[7],HIGH);
  }
  else{
    digitalWrite(row[0],HIGH);
    digitalWrite(col[7],LOW);
  }

////////////////////////////////ROW_2////////////////////////////////
  if(py_input == 'I'){
    digitalWrite(row[1],LOW);
    digitalWrite(col[1],HIGH);
  }
  else{
    digitalWrite(row[1],HIGH);
    digitalWrite(col[1],LOW);
  }
////////////////////////////
  if(py_input == 'J'){
    digitalWrite(row[1],LOW);
    digitalWrite(col[2],HIGH);
  }
  else{
    digitalWrite(row[1],HIGH);
    digitalWrite(col[2],LOW);
  }
////////////////////////////
  if(py_input == 'K'){
    digitalWrite(row[1],LOW);
    digitalWrite(col[3],HIGH);
  }
  else{
    digitalWrite(row[1],HIGH);
    digitalWrite(col[3],LOW);
  }
////////////////////////////
  if(py_input == 'L'){
    digitalWrite(row[1],LOW);
    digitalWrite(col[4],HIGH);
  }
  else{
    digitalWrite(row[1],HIGH);
    digitalWrite(col[4],LOW);
  }
////////////////////////////
  if(py_input == 'M'){
    digitalWrite(row[1],LOW);
    digitalWrite(col[5],HIGH);
  }
  else{
    digitalWrite(row[1],HIGH);
    digitalWrite(col[5],LOW);
  }
////////////////////////////
  if(py_input == 'N'){
    digitalWrite(row[1],LOW);
    digitalWrite(col[6],HIGH);
  }
  else{
    digitalWrite(row[1],HIGH);
    digitalWrite(col[6],LOW);
  }
////////////////////////////
  if(py_input == 'O'){
    digitalWrite(row[1],LOW);
    digitalWrite(col[7],HIGH);
  }
  else{
    digitalWrite(row[1],HIGH);
    digitalWrite(col[7],LOW);
  }

////////////////////////////////ROW_3////////////////////////////////

  if(py_input == 'P'){
    digitalWrite(row[0],LOW);
    digitalWrite(col[1],HIGH);
  }

  if(py_input == 'C'){
    digitalWrite(row[0],LOW);
    digitalWrite(col[2],HIGH);
  }

  if(py_input == 'D'){
    digitalWrite(row[0],LOW);
    digitalWrite(col[3],HIGH);
  }

  if(py_input == 'E'){
    digitalWrite(row[0],LOW);
    digitalWrite(col[4],HIGH);
  }

  if(py_input == 'F'){
    digitalWrite(row[0],LOW);
    digitalWrite(col[5],HIGH);
  }

  if(py_input == 'G'){
    digitalWrite(row[0],LOW);
    digitalWrite(col[6],HIGH);
  }

  if(py_input == 'H'){
    digitalWrite(row[0],LOW);
    digitalWrite(col[7],HIGH);
  }

}
}