import serial
import subprocess
import struct

## GLOBALS
RAW_FILE = 'raw.data.txt'
WAV_FILE = 'output.wav'
BAUD_RATE = 9600
SERIAL_PORT = '/dev/ttyACM0'
SOX_COMMAND = f'sox -r 44100 -c 1 -t raw -b 16 -e signed {RAW_FILE} {WAV_FILE}'

# WAV file settings
CHANNELS = 1
SAMPLE_WIDTH = 2
SAMPLE_RATE = 44100
SAMPLE_INTERVAL = 1.0/ SAMPLE_RATE

# The total number of samples to record
TOTAL_SAMPLES = int(SAMPLE_RATE * SAMPLE_RATE)

def receive_data_from_serial_port(PORT, BAUD_RATE):
    with serial.Serial(PORT, BAUD_RATE) as ser:
        try:
            print("Recording...[CTRL + C to stop]\n")
            with open(RAW_FILE, 'wb') as f:
              while True:
                  # Read two bytes from the serial port (2-bit audio)
                  data = ser.read(2)

                  if not data:
                      break
                  f.write(data)

        except KeyboardInterrupt:
            f.close()
            print("\nRecording saved...")
            return

receive_data_from_serial_port(SERIAL_PORT, BAUD_RATE)

# GENERATING THE HEADER FILE DATA
header = struct.pack('<4sI4s', b'RIFF', 0, b'WAVE')
with open(RAW_FILE, 'rb') as raw_data:
    data_chunk = raw_data.read()
    header += struct.pack('<4sI', b'fmt ', 16) # Size of the format chunk
    header += struct.pack('<HHIIHH', 1, CHANNELS, SAMPLE_RATE, SAMPLE_RATE * SAMPLE_WIDTH * CHANNELS, SAMPLE_WIDTH * CHANNELS, SAMPLE_WIDTH * 8)
    header += struct.pack('<4sI', b'data', len(data_chunk)) # Size of the data chunk

# WRITING THE HEADER FILE TO THE FINAL WAV FILE
with open(WAV_FILE, 'wb') as wav_file:
    wav_file.write(header)
    wav_file.write(data_chunk)

subprocess.run(SOX_COMMAND, shell=True)
