const int micInput = A0;  // Analog pin for KY-038 sensor
const int BAUD_RATE = 11520;

void setup() {
  Serial.begin(BAUD_RATE);  // Initialize serial communication at specified baud rate
}

void loop() {
  int sensorValue = analogRead(micInput);  // Read the analog value from the sensor
  
  // Convert the analog value to a 16-bit integer in the range -32768 to 32767
  int digitalValue = map(sensorValue, 0, 1023, -32768, 32767);


  // Send the digital audio value as two bytes (16 bits) over the serial port
  Serial.write((digitalValue >> 8) & 0xFF);  // High byte
  Serial.println();
  Serial.write(digitalValue & 0xFF); // Low byte
  Serial.println();

  // Add a small delay for stability (approximate sample rate of 44100 Hz)
  delayMicroseconds(22675);  // Note: This is an approximate value for 44100 KHz sample rate
}
