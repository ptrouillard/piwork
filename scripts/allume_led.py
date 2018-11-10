import RPi.GPIO as GPIO
import time
import sys

broche = int(sys.argv[1])

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(broche, GPIO.OUT)

GPIO.output(broche, GPIO.HIGH)
