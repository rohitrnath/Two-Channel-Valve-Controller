void setup() {
 Serial.begin(9600); // put your setup code here, to run once:
 pinMode(13,OUTPUT);
 digitalWrite(13,LOW);

}
char command;
void loop() {
  // put your main code here, to run repeatedly:
  while (Serial.available() > 0){  
    command = Serial.read();
    
    
    if (command == 'X'){
      Serial.println("I");
    digitalWrite(13,HIGH);
    }
    else if(command=='O'){
      delay(1000);
      Serial.println("1IO0003");
      digitalWrite(13,LOW);
    }
    else if(command=='C'){
      delay(8000);
      Serial.println("1IC0901");
      digitalWrite(13,HIGH);
    }
  }
    
}
