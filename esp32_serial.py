import serial
import json
import time
from config import SERIAL_PORT, SERIAL_BAUD_RATE, SERIAL_TIMEOUT

class ESP32Serial:
    def __init__(self, port=SERIAL_PORT, baudrate=SERIAL_BAUD_RATE):
        self.ser = serial.Serial(port, baudrate, timeout=SERIAL_TIMEOUT)
        time.sleep(2)  # Wait for serial connection to initialize

    def send_command(self, var, val):
        try:
            cmd = {"var": var, "val": val}
            self.ser.write((json.dumps(cmd) + "\n").encode())
            self.ser.flush()  # Ensure data is sent
            print(f"Sent: {cmd}")
        except Exception as e:
            print(f"Error sending command to ESP32: {e}")

    def read_response(self):
        try:
            if self.ser.in_waiting:
                response = self.ser.readline().decode().strip()
                print(f"Received: {response}")
                return response
        except Exception as e:
            print(f"Error reading response from ESP32: {e}")
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
