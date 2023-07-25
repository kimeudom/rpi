import serial
import wave
import struct

# Serial port settings
# /dev/ttyACM0

SERIAL_PORT = "/dev/ttyACM0"
BAUD_RATE = 9600

# WAV file settings
WAV_FILENAME = 'test.audio.wav'
CHANNELS = 1
SAMPLE_WIDTH = 2  # 2 bytes per sample for 16-bit audio
SAMPLE_RATE = 44100  # 44.1KHz CD quality sound

# Serial port config
ser = None
try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE)
except serial.SerialException as e:
    print(f"Error oppening serial port: {e}")
    exit(1)

# Create the WAV file
try:
    wf = wave.open(WAV_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(SAMPLE_WIDTH)
    wf.setframerate(SAMPLE_RATE)
except Exception as e:
    print(f"Error creating the WAV file: {e}")
    ser.close()
    exit(1)

try:
    while True:
        data = ser.readline().strip()
        sensorValue = int(data)
        value = struct.pack('<h', sensorValue)
        wf.writeframes(value)
except KeyboardInterrupt:
    pass


# Closing the connection
ser.close()
