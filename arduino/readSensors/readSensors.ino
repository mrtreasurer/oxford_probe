#define sgn(x) ((x) < 0 ? -1 : ((x) > 0 ? 1 : 0))

int Probe1[5] = {A0, A1, A2, A3, A4};
// int Probe2[5] = {A5,A6,A7,A8,A9};//{A8,A9,A10,A11,A12};
int vdd = 1020*5;
int vdd5 = 1020*5;

void setup(){
  //Serial.begin(9600);
  Serial.begin(57600);
  analogReadResolution(12);
}

void loop(){
  //LogServo();
  LogOxford(Probe1, 0);
  
  Serial.println();
  delay(9);
}

//LogOxfordprobe(DataPinArray[], amount of connected sensors, OCS configuration)
//OCS 0 == raw data, OCS 1 == lin data OCS 2 == sqrt data 3 == windspeed
//OCS Low == LIN 
//OCS High = SQRT

void LogOxford(int data[], int OCS){
  int data_len = sizeof(data);

  for (int i = 0; i <= data_len; i++){
    int ar = analogRead(data[i]);

    switch (OCS) {
      case 0:
        Serial.print(ar);
        break;
      
      case 1:
        Serial.print(OCSlin(ar));
        break;

      case 2:
        Serial.print(OCSsqrt(ar));
        break;

      case 3:
        Serial.print(windSpeed(ar));
        break;
    }
    
    if (i < data_len){
      Serial.print(", ");
    }
  }
}

//Analog read int the linear OCS config
double OCSlin(int a){
  double arOCS = (190.*(double)a/(double)vdd) - 38;
  //arOCS*= -1;
  //arOCS+=0.19;
  return arOCS;
}
//Analog read in the Sqrt OCS config
double OCSsqrt(double a){
  int signa = sgn((a/vdd)-0.5);
  double arOCS = ((a/(vdd*0.40))-1.25);
  arOCS = sq(arOCS);
  arOCS = signa*arOCS*133;
  arOCS += 4.41;
  return arOCS;
}
double windSpeed(double a){
  //p = OCSlin(a);
  double a20 = 1025;
  double vdd = a20*5;
  double DP= -38 + ((190*a)/vdd);
  double pAir = 1.255;
  if (DP<=0){DP=0.00001;}
  double windspeed = sqrt(DP/(0.5*pAir));
  return windspeed;

}
void LogAbsP(int sAbs){
  double absPraw = analogRead(sAbs);
  double absPa= map(absPraw, vdd5*0.1 , vdd5*0.9, 0,344738);
  double absPsi= map(absPraw, vdd5*0.1 , vdd5*0.9, 0,50);
  Serial.print(absPraw);  
  Serial.print(" , ");
  Serial.print(absPsi);  
  Serial.print(" , ");
  Serial.print(absPa);  
}
