import time
from RPi import GPIO
b1=17
print b1
GPIO.setmode(GPIO.BCM)
GPIO.setup(b1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
while True:
        inputval = GPIO.input(b1)
        print inputval
        time.sleep(1)
