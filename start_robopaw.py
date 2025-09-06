#!/usr/bin/env python3
"""
RoboPaw Bionic Dog Control System Startup Script
This script provides an easy way to start the entire system
"""

import sys
import os
import time
import signal
import subprocess
from config import FLASK_PORT, WEBSOCKET_PORT

def signal_handler(sig, frame):
    """Handle Ctrl+C gracefully"""
    print('\nShutting down RoboPaw system...')
    sys.exit(0)

def check_dependencies():
    """Check if required dependencies are installed"""
    required_packages = [
        'flask', 'flask_cors', 'websockets', 'opencv-python', 
        'pyserial', 'numpy', 'psutil', 'imutils'
    ]
    
    missing_packages = []
    for package in required_packages:
        try:
            __import__(package.replace('-', '_'))
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print(f"Missing required packages: {', '.join(missing_packages)}")
        print("Please install them using: pip3 install " + " ".join(missing_packages))
        return False
    return True

def check_serial_port():
    """Check if serial port is available"""
    from config import SERIAL_PORT
    if os.path.exists(SERIAL_PORT):
        print(f"✓ Serial port {SERIAL_PORT} found")
        return True
    else:
        print(f"⚠ Warning: Serial port {SERIAL_PORT} not found")
        print("Make sure your ESP32 is connected and the port is correct")
        return False

def start_system():
    """Start the RoboPaw system"""
    print("=" * 50)
    print("🤖 RoboPaw Bionic Dog Control System")
    print("=" * 50)
    
    # Check dependencies
    if not check_dependencies():
        return False
    
    # Check serial port
    check_serial_port()
    
    print(f"\n🚀 Starting servers...")
    print(f"   Flask server: http://0.0.0.0:{FLASK_PORT}")
    print(f"   WebSocket server: ws://0.0.0.0:{WEBSOCKET_PORT}")
    
    try:
        # Import and start the web server
        from webServer import main
        print("\n✅ System started successfully!")
        print("📱 Open your browser and navigate to the Flask server URL")
        print("🔧 Use Ctrl+C to stop the system")
        
        # Set up signal handler for graceful shutdown
        signal.signal(signal.SIGINT, signal_handler)
        
        # Start the main system
        main()
        
    except KeyboardInterrupt:
        print("\n👋 Shutting down...")
    except Exception as e:
        print(f"\n❌ Error starting system: {e}")
        return False
    
    return True

def main():
    """Main entry point"""
    if len(sys.argv) > 1 and sys.argv[1] == '--help':
        print("RoboPaw Bionic Dog Control System")
        print("Usage: python3 start_robopaw.py")
        print("       python3 start_robopaw.py --help")
        return
    
    success = start_system()
    if not success:
        sys.exit(1)

if __name__ == '__main__':
    main()