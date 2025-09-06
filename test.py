import time
import json
import serial

# Try different serial ports - ESP32 connection
# Common ports: /dev/serial0, /dev/ttyAMA0, /dev/ttyS0, /dev/ttyUSB0
try:
    ser = serial.Serial("/dev/serial0", 115200, timeout=1)
except:
    try:
        ser = serial.Serial("/dev/ttyAMA0", 115200, timeout=1)
    except:
        try:
            ser = serial.Serial("/dev/ttyS0", 115200, timeout=1)
        except:
            print("ERROR: Could not open serial port!")
            ser = None

time.sleep(2)  # Give time for connection

upperGlobalIP = 'UPPER IP'
pitch, roll = 0, 0

def setUpperIP(ipInput):
    global upperGlobalIP
    upperGlobalIP = ipInput

def send_command(var, val):
    """Send JSON command to ESP32"""
    if ser is None:
        print("Serial port not available!")
        return

    try:
        dataCMD = json.dumps({'var': var, 'val': val, 'ip': ""})
        ser.write(dataCMD.encode())
        ser.flush()  # Ensure data is sent
        print(f"Sent: {dataCMD}")
    except Exception as e:
        print(f"Error sending command: {e}")

# Movement functions matching ESP32 expectations
def forward(speed=100):
    send_command("move", 1)  # case 1: moveFB = 1
    print('robot-forward')

def backward(speed=100):
    send_command("move", 5)  # case 5: moveFB = -1
    print('robot-backward')

def left(speed=100):
    send_command("move", 2)  # case 2: moveLR = -1
    print('robot-left')

def right(speed=100):
    send_command("move", 4)  # case 4: moveLR = 1
    print('robot-right')

def stopLR():
    send_command("move", 6)  # case 6: moveLR = 0
    print('robot-stop-LR')

def stopFB():
    send_command("move", 3)  # case 3: moveFB = 0
    print('robot-stop-FB')

def stop():
    # Stop all movement
    stopFB()
    time.sleep(0.1)
    stopLR()
    print('robot-stop-all')

# Gesture controls (if ESP32 supports these)
def lookUp():
    send_command("ges", 1)
    print('robot-lookUp')

def lookDown():
    send_command("ges", 2)
    print('robot-lookDown')

def lookStopUD():
    send_command("ges", 3)
    print('robot-lookStopUD')

def lookLeft():
    send_command("ges", 4)
    print('robot-lookLeft')

def lookRight():
    send_command("ges", 5)
    print('robot-lookRight')

def lookStopLR():
    send_command("ges", 6)
    print('robot-lookStopLR')

# Function modes
def steadyMode():
    send_command("funcMode", 1)
    print('robot-steady')

def jump():
    send_command("funcMode", 4)
    print('robot-jump')

def handShake():
    send_command("funcMode", 3)
    print('robot-handshake')

def stayLow():
    send_command("funcMode", 2)
    print('robot-stay-low')

# Light control
def lightCtrl(colorName, cmdInput):
    colorNum = 0
    if colorName == 'off':
        colorNum = 0
    elif colorName == 'blue':
        colorNum = 1
    elif colorName == 'red':
        colorNum = 2
    elif colorName == 'green':
        colorNum = 3
    elif colorName == 'yellow':
        colorNum = 4
    elif colorName == 'cyan':
        colorNum = 5
    elif colorName == 'magenta':
        colorNum = 6
    elif colorName == 'cyber':
        colorNum = 7

    send_command("light", colorNum)
    print(f'robot-light-{colorName}')

# Buzzer control
def buzzerCtrl(buzzerCtrl, cmdInput):
    send_command("buzzer", buzzerCtrl)
    print(f'robot-buzzer-{buzzerCtrl}')

# Test functions
def test_serial_connection():
    """Test if ESP32 is receiving commands"""
    print("Testing serial connection...")
    if ser:
        print(f"Serial port: {ser.name}")
        print(f"Baudrate: {ser.baudrate}")
        print("Sending test forward command...")
        forward()
        time.sleep(1)
        print("Sending stop command...")
        stop()
        print("Check ESP32 serial monitor for responses")
    else:
        print("No serial connection available")

def test_movement_sequence():
    """Test all movement functions"""
    print("Starting movement test sequence...")

    print("1. Forward for 2 seconds")
    forward()
    time.sleep(2)
    stopFB()
    time.sleep(1)

    print("2. Backward for 2 seconds")
    backward()
    time.sleep(2)
    stopFB()
    time.sleep(1)

    print("3. Left turn for 2 seconds")
    left()
    time.sleep(2)
    stopLR()
    time.sleep(1)

    print("4. Right turn for 2 seconds")
    right()
    time.sleep(2)
    stopLR()
    time.sleep(1)

    print("5. Test functions")
    print("   - Light blue")
    lightCtrl('blue', '')
    time.sleep(1)

    print("   - Jump")
    jump()
    time.sleep(3)

    print("   - Handshake")
    handShake()
    time.sleep(5)

    print("   - Light off")
    lightCtrl('off', '')

    print("Movement test complete!")

if __name__ == '__main__':
    try:
        print("Robot control initialized")
        if ser:
            print(f"Connected to: {ser.name}")
        else:
            print("WARNING: No serial connection!")

        print("\nAvailable functions:")
        print("- test_serial_connection()")
        print("- test_movement_sequence()")
        print("- forward(), backward(), left(), right()")
        print("- stop(), stopFB(), stopLR()")
        print("- jump(), handShake(), steadyMode()")
        print("- lightCtrl('color', ''), buzzerCtrl(value, '')")

        # Uncomment one of these to run tests:
        # test_serial_connection()
        # test_movement_sequence()

        # Interactive mode
        print("\nType 'help' for commands, 'quit' to exit")
        while True:
            try:
                cmd = input("Robot> ").strip().lower()

                if cmd == 'quit' or cmd == 'exit':
                    break
                elif cmd == 'help':
                    print("Commands: forward, backward, left, right, stop")
                    print("         jump, handshake, test, connection")
                elif cmd == 'forward' or cmd == 'f':
                    forward()
                elif cmd == 'backward' or cmd == 'b':
                    backward()
                elif cmd == 'left' or cmd == 'l':
                    left()
                elif cmd == 'right' or cmd == 'r':
                    right()
                elif cmd == 'stop' or cmd == 's':
                    stop()
                elif cmd == 'jump' or cmd == 'j':
                    jump()
                elif cmd == 'handshake' or cmd == 'h':
                    handShake()
                elif cmd == 'test':
                    test_movement_sequence()
                elif cmd == 'connection':
                    test_serial_connection()
                elif cmd.startswith('light'):
                    parts = cmd.split()
                    color = parts[1] if len(parts) > 1 else 'blue'
                    lightCtrl(color, '')
                else:
                    print("Unknown command. Type 'help' for options.")

            except KeyboardInterrupt:
                break

    except KeyboardInterrupt:
        print("\nExiting robot control...")
    finally:
        if ser:
            stop()  # Stop robot before exit
            ser.close()
        print("Goodbye!")
