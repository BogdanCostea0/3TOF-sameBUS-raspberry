from machine import Pin, I2C
from vl53l0x import setup_tofl_device, TBOOT
import utime
from time import sleep

# shutdown pins for each device
device_0_xshut = Pin(16, Pin.OUT)
device_1_xshut = Pin(17, Pin.OUT)
device_2_xshut = Pin(18, Pin.OUT)


# setup i2c bus 0
i2c_0 = I2C(id=0, sda=Pin(0), scl=Pin(1))

# reset procedure for each device
device_0_xshut.value(0)
device_1_xshut.value(0)
device_2_xshut.value(0)
sleep(0.1)
device_0_xshut.value(1)
device_1_xshut.value(1)
device_2_xshut.value(1)

# setting up device 0
print("Setting up device 0")
# keep active just the 1st sensor
device_0_xshut.value(1)
device_1_xshut.value(0)
device_2_xshut.value(0)

utime.sleep_us(TBOOT)

tofl0 = setup_tofl_device(i2c_0, 40000, 12, 8) 

tofl0.set_address(0x31)

# setting up device 1
print("Setting up device 1")
# turn on the 2nd sensor

device_1_xshut.value(1)
utime.sleep_us(TBOOT)

tofl1 = setup_tofl_device(i2c_0, 40000, 12, 8)

tofl1.set_address(0x32)

# setting up device 2
print("Setting up device 2")
# turn on the 3rd sensor

device_2_xshut.value(1)
utime.sleep_us(TBOOT)

tofl2 = setup_tofl_device(i2c_0, 40000, 12, 8)

tofl2.set_address(0x33)

while True:
    print("Distance 1: ", tofl0.ping(), "mm", "Distance 2: ", tofl1.ping(), "mm", "Distance 3: ", tofl2.ping(), "mm")
    sleep(0.1)


