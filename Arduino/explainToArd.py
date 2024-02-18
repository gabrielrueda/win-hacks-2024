import serial

# Configure the serial port
ser = serial.Serial('COM3', 9600)

# Function to send data to Arduino
def send_data_to_arduino(data):
    ser.write(data.encode())

# try:
#     while True:
#         if msvcrt.kbhit():
            
#             ser.write(key_stroke)

# except KeyboardInterrupt:
#     ser.close()
#     print("Serial port closed.")
