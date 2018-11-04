import RPi.GPIO as GPIO
import time
import sys

broche = int(sys.argv[1])

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(broche, GPIO.OUT)

while True:
	GPIO.output(broche, GPIO.HIGH)
	time.sleep(0.5)

	GPIO.output(broche, GPIO.LOW)
	time.sleep(0.5)
