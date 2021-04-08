#include <Arduino.h>

int py_input;                         // variable for user input
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

  for(int i = 0;i<8;i++)
  {
    digitalWrite(row[i],HIGH);
    digitalWrite(col[i],LOW);
  }
}

void loop()
{
if(Serial.available()>0)
{
  py_input = Serial.parseInt();

////////////////////////////////ROW_1////////////////////////////////
  if(py_input == 1){
    digitalWrite(row[0],LOW);
    digitalWrite(col[0],HIGH);
  }
  if(py_input == -1){
    digitalWrite(row[0],LOW);
    digitalWrite(col[0],LOW);
  }
////////////////////////////
  if(py_input == 2){
    digitalWrite(row[0],LOW);
    digitalWrite(col[1],HIGH);
  }
  if(py_input == -2){
    digitalWrite(row[0],LOW);
    digitalWrite(col[1],LOW);
  }
////////////////////////////
  if(py_input == 3){
    digitalWrite(row[0],LOW);
    digitalWrite(col[2],HIGH);
  }
  if(py_input == -3){
    digitalWrite(row[0],LOW);
    digitalWrite(col[2],LOW);
  }
////////////////////////////
  if(py_input == 4){
    digitalWrite(row[0],LOW);
    digitalWrite(col[3],HIGH);
  }
  if(py_input == -4){
    digitalWrite(row[0],LOW);
    digitalWrite(col[3],LOW);
  }
////////////////////////////
  if(py_input == 5){
    digitalWrite(row[0],LOW);
    digitalWrite(col[4],HIGH);
  }
  if(py_input == -5){
    digitalWrite(row[0],LOW);
    digitalWrite(col[4],LOW);
  }
////////////////////////////
  if(py_input == 6){
    digitalWrite(row[0],LOW);
    digitalWrite(col[5],HIGH);
  }
  if(py_input == -6){
    digitalWrite(row[0],LOW);
    digitalWrite(col[5],LOW);
  }
////////////////////////////
  if(py_input == 7){
    digitalWrite(row[0],LOW);
    digitalWrite(col[6],HIGH);
  }
  if(py_input == -7){
    digitalWrite(row[0],LOW);
    digitalWrite(col[6],LOW);
  }
////////////////////////////
  if(py_input == 8){
    digitalWrite(row[0],LOW);
    digitalWrite(col[7],HIGH);
  }
  if(py_input == -8){
    digitalWrite(row[0],LOW);
    digitalWrite(col[7],LOW);
  }

////////////////////////////////ROW_2////////////////////////////////
  if(py_input == 9){
    digitalWrite(row[1],LOW);
    digitalWrite(col[0],HIGH);
  }
  if(py_input == -9){
    digitalWrite(row[1],LOW);
    digitalWrite(col[0],LOW);
  }
////////////////////////////
  if(py_input == 10){
    digitalWrite(row[1],LOW);
    digitalWrite(col[1],HIGH);
  }
  if(py_input == -10){
    digitalWrite(row[1],LOW);
    digitalWrite(col[1],LOW);
  }
////////////////////////////
  if(py_input == 11){
    digitalWrite(row[1],LOW);
    digitalWrite(col[2],HIGH);
  }
  if(py_input == -11){
    digitalWrite(row[1],LOW);
    digitalWrite(col[2],LOW);
  }
////////////////////////////
  if(py_input == 12){
    digitalWrite(row[1],LOW);
    digitalWrite(col[3],HIGH);
  }
  if(py_input == -12){
    digitalWrite(row[1],LOW);
    digitalWrite(col[3],LOW);
  }
////////////////////////////
  if(py_input == 13){
    digitalWrite(row[1],LOW);
    digitalWrite(col[4],HIGH);
  }
  if(py_input == -13){
    digitalWrite(row[1],LOW);
    digitalWrite(col[4],LOW);
  }
////////////////////////////
  if(py_input == 14){
    digitalWrite(row[1],LOW);
    digitalWrite(col[5],HIGH);
  }
  if(py_input == -14){
    digitalWrite(row[1],LOW);
    digitalWrite(col[5],LOW);
  }
////////////////////////////
  if(py_input == 15){
    digitalWrite(row[1],LOW);
    digitalWrite(col[6],HIGH);
  }
  if(py_input == -15){
    digitalWrite(row[1],LOW);
    digitalWrite(col[6],LOW);
  }
////////////////////////////
  if(py_input == 16){
    digitalWrite(row[1],LOW);
    digitalWrite(col[7],HIGH);
  }
  if(py_input == -16){
    digitalWrite(row[1],LOW);
    digitalWrite(col[7],LOW);
  }

// ////////////////////////////////ROW_3////////////////////////////////
//   if(py_input == 'P'){
//     digitalWrite(row[2],LOW);
//     digitalWrite(col[1],HIGH);
//   }
//   else{
//     digitalWrite(row[2],HIGH);
//     digitalWrite(col[1],LOW);
//   }
// ////////////////////////////
//   if(py_input == 'Q'){
//     digitalWrite(row[2],LOW);
//     digitalWrite(col[2],HIGH);
//   }
//   else{
//     digitalWrite(row[2],HIGH);
//     digitalWrite(col[2],LOW);
//   }
// ////////////////////////////
//   if(py_input == 'R'){
//     digitalWrite(row[2],LOW);
//     digitalWrite(col[3],HIGH);
//   }
//   else{
//     digitalWrite(row[2],HIGH);
//     digitalWrite(col[3],LOW);
//   }
// ////////////////////////////
//   if(py_input == 'S'){
//     digitalWrite(row[2],LOW);
//     digitalWrite(col[4],HIGH);
//   }
//   else{
//     digitalWrite(row[2],HIGH);
//     digitalWrite(col[4],LOW);
//   }
// ////////////////////////////
//   if(py_input == 'T'){
//     digitalWrite(row[2],LOW);
//     digitalWrite(col[5],HIGH);
//   }
//   else{
//     digitalWrite(row[2],HIGH);
//     digitalWrite(col[5],LOW);
//   }
// ////////////////////////////
//   if(py_input == 'U'){
//     digitalWrite(row[2],LOW);
//     digitalWrite(col[6],HIGH);
//   }
//   else{
//     digitalWrite(row[2],HIGH);
//     digitalWrite(col[6],LOW);
//   }
// ////////////////////////////
//   if(py_input == 'V'){
//     digitalWrite(row[2],LOW);
//     digitalWrite(col[7],HIGH);
//   }
//   else{
//     digitalWrite(row[2],HIGH);
//     digitalWrite(col[7],LOW);
//   }

// //////////////////////////////ROW_4////////////////////////////////
//   if(py_input == 'W'){
//     digitalWrite(row[1],LOW);
//     digitalWrite(col[1],HIGH);
//   }
//   else{
//     digitalWrite(row[1],HIGH);
//     digitalWrite(col[1],LOW);
//   }
// ////////////////////////////
//   if(py_input == 'X'){
//     digitalWrite(row[1],LOW);
//     digitalWrite(col[2],HIGH);
//   }
//   else{
//     digitalWrite(row[1],HIGH);
//     digitalWrite(col[2],LOW);
//   }
// ////////////////////////////
//   if(py_input == 'Y'){
//     digitalWrite(row[1],LOW);
//     digitalWrite(col[3],HIGH);
//   }
//   else{
//     digitalWrite(row[1],HIGH);
//     digitalWrite(col[3],LOW);
//   }
// ////////////////////////////
//   if(py_input == 'Z'){
//     digitalWrite(row[1],LOW);
//     digitalWrite(col[4],HIGH);
//   }
//   else{
//     digitalWrite(row[1],HIGH);
//     digitalWrite(col[4],LOW);
//   }
// ////////////////////////////
//   if(py_input == 'M'){
//     digitalWrite(row[1],LOW);
//     digitalWrite(col[5],HIGH);
//   }
//   else{
//     digitalWrite(row[1],HIGH);
//     digitalWrite(col[5],LOW);
//   }
// ////////////////////////////
//   if(py_input == 'N'){
//     digitalWrite(row[1],LOW);
//     digitalWrite(col[6],HIGH);
//   }
//   else{
//     digitalWrite(row[1],HIGH);
//     digitalWrite(col[6],LOW);
//   }
// ////////////////////////////
//   if(py_input == 'O'){
//     digitalWrite(row[1],LOW);
//     digitalWrite(col[7],HIGH);
//   }
//   else{
//     digitalWrite(row[1],HIGH);
//     digitalWrite(col[7],LOW);
//   }

}
}