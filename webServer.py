#!/usr/bin/python3
# File name   : server.py
# Production  : Upper Ctrl for Robots
# Author	  : WaveShare

import time
import threading
import os
import socket
import info
#websocket
import asyncio
import websockets

import json
import app
from esp32_serial import ESP32Serial
import robot
from config import FLASK_PORT, WEBSOCKET_PORT, WS_USERNAME, WS_PASSWORD

ipaddr_check = "10.18.111.75"


def ap_thread():
	os.system("sudo create_ap wlan0 eth0 WAVE_BOT 12345678")


def wifi_check():
	global ipaddr_check
	time.sleep(5)
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		s.connect(("0.0.0.0", FLASK_PORT))
		ipaddr_check = s.getsockname()[0]
		s.close()
		print(ipaddr_check)
	except Exception as e:
		ap_threading = threading.Thread(target=ap_thread)
		ap_threading.setDaemon(True)
		ap_threading.start()


async def check_permit(websocket):
	while True:
		recv_str = await websocket.recv()
		cred_dict = recv_str.split(":")
		if cred_dict[0] == WS_USERNAME and cred_dict[1] == WS_PASSWORD:
			response_str = "Connected!"
			await websocket.send(response_str)
			return True
		else:
			response_str = "sorry, the username or password is wrong, please submit again"
			await websocket.send(response_str)


async def recv_msg(websocket):
	while True: 
		response = {
			'status' : 'ok',
			'title' : '',
			'data' : None
		}

		try:
			data = await websocket.recv()
			print(f"Received data: {data}")
		except websockets.exceptions.ConnectionClosed:
			print("WebSocket connection closed by client")
			break
		except Exception as e:
			print(f"Error receiving data: {e}")
			break
			
		try:
			data = json.loads(data)
		except json.JSONDecodeError as e:
			print(f'Invalid JSON received: {e}')
			response['status'] = 'error'
			response['title'] = 'invalid_json'
			response['data'] = 'Invalid JSON format received'
			await websocket.send(json.dumps(response))
			continue

		if not data:
			continue

		if isinstance(data,str):
			flask_app.commandInput(data)

			if data == 'forward':
				esp.send_command('move', 1)
			elif data == 'moveBackward':
				esp.send_command('move', 5)
			elif data == 'turnLeft':
				esp.send_command('move', 2)
			elif data == 'turnRight':
				esp.send_command('move', 4)
			elif data == 'stop':
				esp.send_command('move', 3)
			elif 'forward' == data:
				robot.forward()
				print('robot moving forward')

			if 'get_info' == data:
				response['title'] = 'get_info'
				response['data'] = [info.get_cpu_tempfunc(), info.get_cpu_use(), info.get_ram_info()]

			if 'findColor' == data:
				flask_app.modeselect('findColor')
				print('set mode as findColor')

			elif 'scan' == data:
				print('scanning')
				# ds = app.camera_opencv.ultra.checkdist()
				# print(ds)
				radar_send = [[3,60],[10,70],[10,80],[10,90],[10,100],[10,110],[3,120]]
				# radar_send = []
				# for i in range(1,150):
				# 	radar_send.append[ds]
				response['title'] = 'scanResult'
				response['data'] = radar_send
				time.sleep(0.3)
				pass

			elif 'motionGet' == data:
				flask_app.modeselect('watchDog')
				print('set mode as watchDog')

			elif 'stopCV' == data:
				flask_app.modeselect('none')

			#CVFL
			elif 'CVFL' == data:
				flask_app.modeselect('findlineCV')
				print('set mode as findlineCV')

			elif 'CVFLColorSet' in data:
				color = int(data.split()[1])
				flask_app.camera.colorSet(color)

			elif 'CVFLL1' in data:
				pos = int(data.split()[1])
				flask_app.camera.linePosSet_1(pos)

			elif 'CVFLL2' in data:
				pos = int(data.split()[1])
				flask_app.camera.linePosSet_2(pos)

			elif 'CVFLSP' in data:
				err = int(data.split()[1])
				flask_app.camera.errorSet(err)

			# 'defEC' in data: removed fpv.defaultExpCom() since fpv is not defined


		elif(isinstance(data,dict)):
			if data['title'] == "findColorSet":
				color = data['data']
				flask_app.colorFindSet(color[0],color[1],color[2])

		if data != "get_info":
			print(data)
			
		response = json.dumps(response)
		await websocket.send(response)


async def main_logic(websocket, path):
	print("WebSocket client connected")
	await check_permit(websocket)
	await recv_msg(websocket)


if __name__ == '__main__':
	global flask_app

	wifi_check()
	flask_app = app.webapp()
	flask_app.startthread()
	flask_app.sendIP(ipaddr_check)
	
	esp = ESP32Serial()

	while  1:
		try:
			start_server = websockets.serve(main_logic, '0.0.0.0', WEBSOCKET_PORT)
			asyncio.get_event_loop().run_until_complete(start_server)
			print('waiting for connection...')
			break
		except Exception as e:
			print(e)

	try:
		asyncio.get_event_loop().run_forever()
	except Exception as e:
		print(e)
		
	esp.close()
