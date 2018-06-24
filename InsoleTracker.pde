import processing.serial.*;
PrintWriter output;
Serial mySerial;

String myString = null; //a variable to collect serial data
int nl = 100; //ASCII code for carage return in Serial
float myVal; //float for storing converted ascii serial data

void setup() {
  size(1440,850); //setting size of output screen for demo
  
  //link processing to serial port 
  String myPort = Serial.list()[1];
  mySerial = new Serial(this, myPort, 9600); 
  
  output = createWriter("FSRData.csv"); //declaring the output file for data storage
}//setup

void draw() {
  
  while (mySerial.available() > 0){
    myString = mySerial.readStringUntil(10); //STRIPs data of serial port
    
   
    if(myString != null){
      background(0);
      myVal = float(myString); //takes data from serial and turns it into a number
      fill(255,0,0,127);
      rect(0,200,width,25);
      fill(255,0,0,127);
      rect(width,200,width,25);
      
      myVal = myVal/100*height;
      fill(209);
      rectMode(CENTER);
      rect(width/2, height-(myVal/2), 800, myVal);
      
      println(myVal);
    }// data was on the serial port
  }// do something if there is data in the port
  
  output.println(myVal);  // Write the "Force Vector" at time whatever to the file
}

void keyPressed() {
  output.flush();  // Writes the remaining data to the file
  output.close();  // Finishes the file
  exit();  // Stops the program
}
