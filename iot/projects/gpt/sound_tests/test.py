import serial
import wave
import struct
import time

# Serial port settings
# /dev/ttyACM1

SERIAL_PORT = "/dev/ttyACM0"
BAUD_RATE = 9600

# WAV file settings
WAV_FILENAME = 'new.test.audio.wav'
CHANNELS = 1
SAMPLE_WIDTH = 2  # 2 bytes per sample for 16-bit audio
SAMPLE_RATE = 44100  # 44.1KHz CD quality sound
SAMPLE_INTERVAL = 1.0/SAMPLE_RATE  # Period of 44.1KHz sampling
DURATION = 10  # 10s hardcoded duration


TOTAL_SAMPLES = int(SAMPLE_RATE * DURATION)

# Serial port config
ser = None
try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE)
except serial.SerialException as e:
    print(f"Error oppening serial port: {e}")
    exit(1)

# Create the WAV file
# Open the WAV file for writing
try:
    wf = wave.open(WAV_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(SAMPLE_WIDTH)
    wf.setframerate(SAMPLE_RATE)

    # Writing data to the .wav file
    start_time = time.time()
    for _ in range(TOTAL_SAMPLES):
        # Read 2 bytes (16-bits) from the serial port
        data = ser.read(2)

        value = struct.unpack('<h', data)[0]
        wf.writeframes(data)

        elapsed_time = time.time() - start_time
        time_to_sleep = SAMPLE_INTERVAL - elapsed_time

        if time_to_sleep > 0:
            time.sleep(time_to_sleep)

        start_time = time.time()

except KeyboardInterrupt:
    pass


# Close the wave file
wf.close()
# Closing the connection
ser.close()
