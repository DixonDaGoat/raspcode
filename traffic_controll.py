import serial
import time

# Set up the serial connection
port = 'COM5'  # Change this to your Arduino's port
baudrate = 9600
ser = serial.Serial(port, baudrate)
time.sleep(2)  # Wait for the connection to establish

def rotate_servo(angle):
    if 0 <= angle <= 180:
        ser.write(f"{angle}\n".encode())  # Send the angle as a string
        time.sleep(0.015)  # Small delay to allow the servo to move
    else:
        print("Angle must be between 0 and 180.")

try:
    while True:
        # Rotate from 0 to 180 degrees
        for i in range(181):
            rotate_servo(i)
        # Rotate back from 180 to 0 degrees
        for i in range(180, -1, -1):
            rotate_servo(i)

except KeyboardInterrupt:
    print("Program stopped by user.")

finally:
    ser.close()  # Close the serial connection when done