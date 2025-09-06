#!/usr/bin/env python3
"""
Configuration file for RoboPaw Bionic Dog Control System
Centralizes all configuration settings to reduce duplication
"""

import os

# Server Configuration
FLASK_HOST = '0.0.0.0'
FLASK_PORT = 5000
WEBSOCKET_PORT = 8888

# Serial Communication
SERIAL_PORT = '/dev/serial0'
SERIAL_BAUD_RATE = 115200
SERIAL_TIMEOUT = 1

# Camera Configuration
CAMERA_WIDTH = 640
CAMERA_HEIGHT = 480
VIDEO_FPS = 24

# Computer Vision Settings
FACE_CASCADE_PATH = os.path.join(os.path.dirname(__file__), 'haarcascade_frontalface_default.xml')
LINE_POS_1 = 440
LINE_POS_2 = 380
LINE_COLOR_SET = 255
FIND_LINE_ERROR = 20
SPEED_MOVE = 100

# Color Detection Settings
COLOR_UPPER = [44, 255, 255]
COLOR_LOWER = [24, 100, 100]

# WebSocket Authentication
WS_USERNAME = 'admin'
WS_PASSWORD = '123456'

# System Monitoring
CPU_TEMP_PATH = '/sys/class/thermal/thermal_zone0/temp'
INFO_UPDATE_INTERVAL = 5  # seconds

# Mobile UI Settings
MOBILE_BREAKPOINT = 768
TOUCH_TARGET_MIN_SIZE = 48  # pixels

# Error Handling
MAX_RETRY_ATTEMPTS = 3
CONNECTION_TIMEOUT = 10  # seconds

# Logging
LOG_LEVEL = 'INFO'
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

# Development/Production
DEBUG = False
PRODUCTION = True

# Robot Movement Commands
ROBOT_COMMANDS = {
    'move': {
        'forward': 1,
        'left': 2,
        'stop_fb': 3,
        'right': 4,
        'backward': 5,
        'stop_lr': 6
    },
    'ges': {
        'look_up': 1,
        'look_down': 2,
        'look_stop_ud': 3,
        'look_left': 4,
        'look_right': 5,
        'look_stop_lr': 6
    },
    'funcMode': {
        'steady': 1,
        'handshake': 3,
        'jump': 4
    },
    'light': {
        'off': 0,
        'blue': 1,
        'red': 2,
        'green': 3,
        'yellow': 4,
        'cyan': 5,
        'magenta': 6,
        'cyber': 7
    }
}

# WebSocket Message Types
WS_MESSAGE_TYPES = {
    'AUTHENTICATION': 'auth',
    'ROBOT_CONTROL': 'robot_control',
    'CAMERA_CONTROL': 'camera_control',
    'SYSTEM_INFO': 'system_info',
    'ERROR': 'error',
    'SUCCESS': 'success'
}

# UI Themes
UI_THEME = {
    'primary_color': '#1976D2',
    'primary_light': '#42A5F5',
    'primary_dark': '#0D47A1',
    'secondary_color': '#FF6F00',
    'success_color': '#4CAF50',
    'warning_color': '#FF9800',
    'error_color': '#F44336',
    'info_color': '#2196F3'
}