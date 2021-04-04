#include <Arduino.h>

char py_input;
// 2-dimensional array of row pin numbers:
int R[] = {2,3,4,5,6,7,8,9};  
// 2-dimensional array of column pin numbers:
int C[] = {10,11,12,A4,A0,A1,A2,A3};    
  
unsigned char biglove[8][8] =     //the big "heart"   
{  
  1,1,0,0,0,0,1,1,  
  1,0,0,0,0,0,0,1,  
  0,0,0,0,0,0,0,0,  
  0,0,0,0,0,0,0,0,  
  0,0,0,0,0,0,0,0,  
  0,0,0,0,0,0,0,0,  
  0,0,0,0,0,0,0,0,  
  0,0,0,0,0,0,0,0,  
};  
  
unsigned char smalllove[8][8] =      //the small "heart" 
{  
  0,0,0,0,0,0,0,0,  
  0,0,0,0,0,0,0,0,  
  0,0,1,0,0,1,0,0,  
  0,1,1,1,1,1,1,0,  
  0,1,1,1,1,1,1,0,  
  0,0,1,1,1,1,0,0,  
  0,0,0,1,1,0,0,0,  
  0,0,0,0,0,0,0,0,  
};  
  
void setup()  
{  
  Serial.begin(9600);
   // iterate over the pins:
  for(int i = 0;i<8;i++)  
  // initialize the output pins:
  {  
    pinMode(R[i],OUTPUT);  
    pinMode(C[i],OUTPUT);  
  }  
}  

void Clear()                          
{  
  for(int i = 0;i<8;i++)  
  {  
    digitalWrite(R[i],HIGH);  
    digitalWrite(C[i],LOW);  
  }  
}

void Display(unsigned char dat[8][8])    
{  
  for(int c = 0; c<8;c++)  
  {  
    digitalWrite(C[c],HIGH);//use thr column 
    //loop
    for(int r = 0;r<8;r++)  
    {  
      digitalWrite(R[r],dat[r][c]);  
    }  
    delay(1);  
    Clear();  //Remove empty display light
  }  
}

void loop()  
{  
if(Serial.available()>0){
    py_input = Serial.read();
    if(py_input == 'a'){
        Display(biglove);
    }
}

    // Display(biglove);
//   for(int i = 0 ; i < 100 ; i++)        //Loop display 100 times 
//   {  
//     Display(biglove);                   //Display the "Big Heart"  
//   }  
//   for(int i = 0 ; i < 50 ; i++)         //Loop display 50 times
//   {     
//     Display(smalllove);                 //Display the "small Heart" 
//   }  
}  
  
