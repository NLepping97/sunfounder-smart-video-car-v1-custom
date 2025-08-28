from smbus2 import SMBus
import time

ADDRESS = 0x40
FREQUENZ = 50
prescale = round(25_000_000 / (4096 * FREQUENZ) - 1)

with SMBus(1) as bus:
    # Set Servomodule to sleep
    bus.write_byte_data(ADDRESS, 0x00, 0x11)
    time.sleep(0.01)
    bus.write_byte_data(ADDRESS, 0xFE, prescale)
    time.sleep(0.01)
    bus.write_byte_data(ADDRESS, 0x00, 0x21)
    time.sleep(0.01)
    bus.write_byte_data(ADDRESS, 0x01, 0x04)
    time.sleep(0.01)
    bus.write_byte_data(ADDRESS, 0x00, 0xA1)
    print(f"MODE1={bus.read_byte_data(ADDRESS, 0x00):#X}")
    print(f"PRE_SCALE={bus.read_byte_data(ADDRESS, 0xFE):#X}")
    time.sleep(1)
    bus.write_byte_data(ADDRESS, 0xFD, 0x10)
    time.sleep(0.01)
    bus.write_byte_data(ADDRESS, 0x00, 0x11)
    print(f"MODE1={bus.read_byte_data(ADDRESS, 0x00):#04x}")
