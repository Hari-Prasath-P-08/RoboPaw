# 🤖 RoboPaw - Bionic Dog Control System

A sophisticated web-based control system for robotic dog hardware, featuring real-time video streaming, computer vision capabilities, and intuitive mobile-responsive interface.

## ✨ Features

### 🎮 **Robot Control**
- **Movement Control**: Forward, backward, left, right with speed adjustment
- **Head Movement**: Look up, down, left, right with precise control
- **Special Actions**: Jump, handshake, steady mode
- **Light Control**: Multi-color LED control (blue, red, green, yellow, cyan, magenta, cyber)
- **Audio Feedback**: Buzzer control for audio notifications

### 📹 **Computer Vision**
- **Real-time Video Stream**: Live camera feed with professional UI
- **Face Detection**: Automatic face recognition and tracking
- **Color Tracking**: Custom color detection and following
- **Line Following**: Autonomous line following with CV algorithms
- **Motion Detection**: Watchdog mode for security monitoring

### 🌐 **Web Interface**
- **Modern UI**: Professional Vue.js interface with Vuetify components
- **Mobile Responsive**: Optimized for touch devices and mobile screens
- **Real-time Communication**: WebSocket-based bidirectional control
- **System Monitoring**: Live CPU, RAM, and temperature monitoring
- **Radar Scanning**: Visual radar display for distance measurement

### 🔧 **Technical Features**
- **Modular Architecture**: Clean separation of concerns
- **Error Handling**: Robust error management and recovery
- **Configuration Management**: Centralized settings and constants
- **Cross-platform**: Compatible with Raspberry Pi and ESP32
- **Professional Styling**: Enhanced CSS with modern design patterns

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- Raspberry Pi with camera module
- ESP32 microcontroller
- Required Python packages (see setup.py)

### Installation
1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd RoboPaw
   ```

2. **Run the setup script** (on Raspberry Pi):
   ```bash
   sudo python3 setup.py
   ```

3. **Start the system**:
   ```bash
   python3 start_robopaw.py
   ```

4. **Access the web interface**:
   - Open your browser and navigate to: `http://<raspberry-pi-ip>:5000`
   - Use WebSocket credentials: `admin:123456`

## 📁 Project Structure

```
RoboPaw/
├── 📄 app.py                 # Flask web server
├── 📄 webServer.py          # WebSocket server
├── 📄 robot.py              # Robot control functions
├── 📄 camera_opencv.py      # Computer vision processing
├── 📄 esp32_serial.py       # ESP32 communication
├── 📄 config.py             # Configuration settings
├── 📄 start_robopaw.py      # System startup script
├── 📄 info.py               # System monitoring
├── 📄 base_camera.py        # Camera base class
├── 📄 setup.py              # Installation script
├── 📁 dist/                 # Frontend build files
│   ├── 📄 index.html        # Main HTML file
│   ├── 📁 css/              # Stylesheets
│   ├── 📁 js/               # JavaScript bundles
│   └── 📁 img/              # Images and icons
└── 📄 README.md             # This file
```

## ⚙️ Configuration

All system settings are centralized in `config.py`:

- **Server Ports**: Flask (5000), WebSocket (8888)
- **Serial Communication**: Port, baud rate, timeout
- **Camera Settings**: Resolution, FPS, processing parameters
- **Robot Commands**: Movement, gesture, and function mappings
- **UI Themes**: Colors, styling, responsive breakpoints

## 🎯 Usage

### Basic Robot Control
1. **Movement**: Use the directional buttons or WASD keys
2. **Speed Control**: Adjust the speed slider (0-100)
3. **Head Movement**: Use the camera control buttons or IJKL keys
4. **Special Actions**: Access through the Actions panel

### Computer Vision Features
1. **Face Detection**: Click "Face Detection" to enable/disable
2. **Color Tracking**: Select a color and click "Find Color"
3. **Line Following**: Configure line parameters and enable tracking
4. **Motion Detection**: Enable "Motion Get" for security monitoring

### Mobile Usage
- **Touch Controls**: All buttons are optimized for touch
- **Responsive Layout**: Automatically adapts to screen size
- **Gesture Support**: Smooth scrolling and touch interactions

## 🔧 Development

### Code Organization
- **Modular Design**: Each component has a specific responsibility
- **Error Handling**: Comprehensive error management throughout
- **Configuration**: Centralized settings for easy maintenance
- **Documentation**: Well-documented functions and classes

### Recent Improvements
- ✅ **Port Configuration**: Fixed WebSocket/Flask port conflicts
- ✅ **Error Handling**: Enhanced error management and recovery
- ✅ **Mobile UI**: Improved responsive design and touch controls
- ✅ **Code Cleanup**: Reduced duplication and improved organization
- ✅ **Configuration**: Centralized settings management
- ✅ **UI Polish**: Enhanced visual design and user experience

## 🐛 Troubleshooting

### Common Issues
1. **Serial Port Not Found**: Check ESP32 connection and port configuration
2. **WebSocket Connection Failed**: Verify port 8888 is available
3. **Camera Not Working**: Ensure camera module is properly connected
4. **Mobile UI Issues**: Clear browser cache and refresh

### Debug Mode
Enable debug mode by setting `DEBUG = True` in `config.py`

## 📱 Mobile Support

The interface is fully optimized for mobile devices:
- **Touch-friendly buttons** (48px minimum)
- **Responsive grid layout**
- **Gesture support**
- **Optimized video streaming**
- **Accessibility features**

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source. Please check the license file for details.

## 🙏 Acknowledgments

- **WaveShare** for the original hardware design
- **Vue.js** and **Vuetify** for the frontend framework
- **OpenCV** for computer vision capabilities
- **Flask** and **WebSockets** for real-time communication

---

**RoboPaw** - Bringing advanced robotics control to your fingertips! 🐕🤖