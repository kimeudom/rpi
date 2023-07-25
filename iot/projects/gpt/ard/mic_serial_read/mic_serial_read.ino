const int micInput = A0;  // Analog pin for KY-038 sensor
int sensorValue;          // Variable to store the sensor value

void setup() {
  Serial.begin(9600);     // Initialize serial communication at 9600 bps
}

void loop() {
  sensorValue = analogRead(analogPin); // Read the analog value from the sensor
  Serial.println(sensorValue);        // Send the value to the PC
  delay(100);                         // Add a small delay for stability
}
