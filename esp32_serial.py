import serial
import json
import time

# Set the correct serial port for your Raspberry Pi
SERIAL_PORT = '/dev/serial0'  # or '/dev/ttyS0' depending on your Pi model
BAUD_RATE = 115200

class ESP32Serial:
    def __init__(self, port=SERIAL_PORT, baudrate=BAUD_RATE):
        self.ser = serial.Serial(port, baudrate, timeout=1)
        time.sleep(2)  # Wait for serial connection to initialize

    def send_command(self, var, val):
        cmd = {"var": var, "val": val}
        self.ser.write((json.dumps(cmd) + "\n").encode())
        print(f"Sent: {cmd}")

    def read_response(self):
        if self.ser.in_waiting:
            response = self.ser.readline().decode().strip()
            print(f"Received: {response}")
            return response
        return None

    def close(self):
        self.ser.close()

if __name__ == "__main__":
    esp = ESP32Serial()
    # Example usage:
    esp.send_command("move", 1)  # Move forward
    time.sleep(0.5)
    esp.send_command("move", 3)  # Stop
    # Read any response from ESP32
    while True:
        resp = esp.read_response()
        if resp:
            break
    esp.close()
