from machine import Pin, I2C
from time import sleep

from mpu6050 import MPU6050

# setup i2c bus 1

i2c_1 = I2C(id=1, sda=Pin(26), scl=Pin(27))

# setup mpu6050

mpu = MPU6050()

while True:
    print(mpu.get_gyro_raw)
    sleep(0.1)





