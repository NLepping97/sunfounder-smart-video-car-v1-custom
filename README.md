# SunFounder Smart Video Car V1 (Custom)

Custom code, wiring, and setup notes for my **SunFounder Smart Video Car V1** (2017 edition).  
This project re-implements the robot car control from scratch (without the official SunFounder software), using:

- Raspberry Pi 3B
- PCA9685 16-channel 12-bit PWM controller
- TowerPro SG90 9g micro servos (pan/tilt, steering) + 1 Fischertechnik servo
- L298N motor driver for 2 DC drive motors
- SunFounder DC-DC buck converter (12V → 5V power)
- USB camera (included with the kit)

---

## 🚗 Features (planned)

- [ ] Basic motor drive (forward / backward / turn)
- [ ] Steering servo via PCA9685
- [ ] Pan/tilt camera control via PCA9685
- [ ] Web interface with live video
- [ ] Keyboard/gamepad teleop
- [ ] Obstacle avoidance (future)

---

## ⚡ Hardware Overview

### Power
- 12 V adapter / Li-ion pack → **L298N (motors)**  
- 12 V adapter / Li-ion pack → **DC-DC step-down → 5 V** → Raspberry Pi & PCA9685 servo rail  
- Common ground between Pi, PCA9685, L298N, and DC-DC

### Connections
- **Pi ↔ PCA9685 (I²C)**  
  - SDA (GPIO2, pin 3) → SDA  
  - SCL (GPIO3, pin 5) → SCL  
  - 3V3 (pin 1) → VCC  
  - GND (pin 6) → GND  
  - 5 V from buck → V+ (servo rail)  
- **Pi ↔ L298N**  
  - GPIO5 (pin 29) → IN1  
  - GPIO6 (pin 31) → IN2  
  - GPIO12 (pin 32, PWM) → ENA  
  - GPIO16 (pin 36) → IN3  
  - GPIO20 (pin 38) → IN4  
  - GPIO13 (pin 33, PWM) → ENB  
  - GND → GND  
- **Servos ↔ PCA9685**  
  - CH15: Steering servo  
  - CH0: Pan servo  
  - CH1: Tilt servo  
- **Camera**: USB, plugged directly into Pi  

---

## 🖥️ Software

- OS: Raspberry Pi OS Lite (64-bit recommended)  
- Language: Python 3  
- Libraries:  
  - `RPi.GPIO` or `gpiozero` (for motor control)  
  - `smbus2` (for PCA9685 I²C)  
  - `opencv-python` (for camera + vision, optional)  
  - `flask` (for web control, optional)  

---

## 🔧 Usage (WIP)

1. Clone repo:
  ```bash
  git clone https://github.com/NLepping97/sunfounder-smart-video-car-v1-custom.git
  cd sunfounder-smart-video-car-v1-custom
  ```
2. Install dependencies:
  ```bash
  sudo apt update
  sudo apt install python3-pip i2c-tools
  pip3 install smbus2 RPi.GPIO opencv-python flask
  ```

3. Enable I²C on Pi:
  ```bash
  sudo raspi-config
  # Interface Options → I2C → Enable
  ```

4. Test hardware (examples will be in examples/ folder):
  ```bash
  python3 examples/test_servos.py
  python3 examples/test_motors.py
  ```
---

## 📸 Wiring Diagram

- (to be added — see /docs/wiring-diagram.png)

---

## 📚 Notes

- Do not power servos from the Pi’s 5V pin. Use the DC-DC 5V → PCA9685 V+ rail instead.
- If you see undervoltage warnings (⚡ icon), use a 12 V ≥3 A supply or Li-ion pack.
- L298N jumper (5V-EN) should be removed if Pi is powered separately.

---

## 📝 License

MIT License (do what you want, but no warranty).

---

## 🙌 Acknowledgments

Inspired by the SunFounder Smart Video Car Kit (V1, 2017). This repo is a custom reimplementation.
