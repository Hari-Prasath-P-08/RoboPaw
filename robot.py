#!/usr/bin/env/python3
# File name   : robot.py
# Description : Robot interfaces.
import time
import json
import serial
from config import SERIAL_PORT, SERIAL_BAUD_RATE, SERIAL_TIMEOUT, ROBOT_COMMANDS

ser = serial.Serial(SERIAL_PORT, SERIAL_BAUD_RATE, timeout=SERIAL_TIMEOUT)
dataCMD = json.dumps({'var':"", 'val':0, 'ip':""})
upperGlobalIP = 'UPPER IP'


pitch, roll = 0, 0

def send_robot_command(var, val, action_name):
	"""Helper function to send robot commands with error handling"""
	try:
		dataCMD = json.dumps({'var': var, 'val': val})
		ser.write(dataCMD.encode())
		ser.flush()
		print(f'robot-{action_name}')
	except Exception as e:
		print(f'Error sending {action_name} command: {e}')

def setUpperIP(ipInput):
	global upperGlobalIP
	upperGlobalIP = ipInput

def forward(speed=100):
	send_robot_command("move", ROBOT_COMMANDS['move']['forward'], "forward")

def backward(speed=100):
	send_robot_command("move", ROBOT_COMMANDS['move']['backward'], "backward")

def left(speed=100):
	send_robot_command("move", ROBOT_COMMANDS['move']['left'], "left")

def right(speed=100):
	send_robot_command("move", ROBOT_COMMANDS['move']['right'], "right")

def stopLR():
	send_robot_command("move", ROBOT_COMMANDS['move']['stop_lr'], "stop")

def stopFB():
	send_robot_command("move", ROBOT_COMMANDS['move']['stop_fb'], "stop")



def lookUp():
	send_robot_command("ges", ROBOT_COMMANDS['ges']['look_up'], "lookUp")

def lookDown():
	send_robot_command("ges", ROBOT_COMMANDS['ges']['look_down'], "lookDown")

def lookStopUD():
	send_robot_command("ges", ROBOT_COMMANDS['ges']['look_stop_ud'], "lookStopUD")

def lookLeft():
	send_robot_command("ges", ROBOT_COMMANDS['ges']['look_left'], "lookLeft")

def lookRight():
	send_robot_command("ges", ROBOT_COMMANDS['ges']['look_right'], "lookRight")

def lookStopLR():
	send_robot_command("ges", ROBOT_COMMANDS['ges']['look_stop_lr'], "lookStopLR")



def steadyMode():
	send_robot_command("funcMode", ROBOT_COMMANDS['funcMode']['steady'], "steady")

def jump():
	send_robot_command("funcMode", ROBOT_COMMANDS['funcMode']['jump'], "jump")

def handShake():
	send_robot_command("funcMode", ROBOT_COMMANDS['funcMode']['handshake'], "handshake")



def lightCtrl(colorName, cmdInput):
	colorNum = ROBOT_COMMANDS['light'].get(colorName, 0)
	send_robot_command("light", colorNum, f"light-{colorName}")


def buzzerCtrl(buzzerCtrl, cmdInput):
	send_robot_command("buzzer", buzzerCtrl, f"buzzer-{'on' if buzzerCtrl else 'off'}")



if __name__ == '__main__':
    # robotCtrl.moveStart(100, 'forward', 'no', 0)
    # time.sleep(3)
    # robotCtrl.moveStop()
    while 1:
        time.sleep(1)
        pass
