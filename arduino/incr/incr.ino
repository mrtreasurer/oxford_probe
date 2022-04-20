int a = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(57600);
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println(a);
  a++;
  delay(9);
}
