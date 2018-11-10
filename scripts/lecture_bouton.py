import time
from RPi import GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(4, GPIO.OUT)
while True:
        inputval = GPIO.input(17)
        if inputval == 0 :
		GPIO.output(4, GPIO.HIGH)
	if inputval == 1 :
		GPIO.output(4, GPIO.LOW)
        time.sleep(0.1)
