int r=9;
void setup() {
  Serial.begin(9600);
  pinMode(r,OUTPUT);
}

void loop()
{ 
   if(Serial.available())
   {
     int c=Serial.read();
     if (c=='1') 
       digitalWrite(r,HIGH);           
     else if(c=='0')
       digitalWrite(r,LOW);
   }
 }
