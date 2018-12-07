import serial

ser = serial.Serial()
ser.baudrate = 19200
ser.port = '/dev/tty.usbserial-A9005ztM'

try:
    ser.open()
except Exception, e:
    print(e)

print(ser.is_open)

while True:
    f = open("demo.text", "a")
    f.write(ser.readline())
    f.close()
