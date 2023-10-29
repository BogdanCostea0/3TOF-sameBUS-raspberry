from imu import MPU6050
from time import sleep
from machine import Pin, I2C

#Shows Pi is on by turning on LED when plugged in
LED = Pin("LED", Pin.OUT)
LED.on()

from imu import MPU6050
from time import sleep
from machine import Pin, I2C

i2c = I2C(1, sda=Pin(26), scl=Pin(27), freq=400000)
imu = MPU6050(i2c)

while True:
    ax=round(imu.accel.x,2)
    ay=round(imu.accel.y,2)
    az=round(imu.accel.z,2)
    gx=round(imu.gyro.x)
    gy=round(imu.gyro.y)
    gz=round(imu.gyro.z)
    tem=round(imu.temperature,2)
    print("ax",ax,"\t","ay",ay,"\t","az",az,"\t","gx",gx,"\t","gy",gy,"\t","gz",gz,"\t","Temperature",tem,"        ",end="\r")
    sleep(0.2) 