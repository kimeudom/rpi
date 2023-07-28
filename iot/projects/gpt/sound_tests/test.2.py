import serial
import subprocess

## GLOBALS
RAW_FILE = 'raw.data.txt'
WAV_FILE = 'output.wav'
BAUD_RATE = 9600
SERIAL_PORT = '/dev/ttyACM0'
SOX_COMMAND = f'sox -r 44100 -c 1 -t raw -b 16 -e signed {RAW_FILE} {WAV_FILE}'

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
subprocess.run(SOX_COMMAND, shell=True)
