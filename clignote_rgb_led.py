import RPi.GPIO as GPIO
import time

# Broche 16 => Rouge
# Broche 20 => Vert
# Broche 21 => Bleu

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

rouge = GPIO.PWM(16, 50)
vert = GPIO.PWM(20, 50)
bleu = GPIO.PWM(21, 50)

i=0
rouge.start(100)
vert.start(i)
bleu.start(i)
for i in range (0, 100, 1):
	rouge.ChangeDutyCycle(100-i)
	bleu.ChangeDutyCycle(i)
	if i <=50 :
		vert.ChangeDutyCycle(2*i)
	if i > 50 :
		vert.ChangeDutyCycle(200 - 2*i)
	time.sleep(0.25)
time.sleep(2)

rouge.stop()
vert.stop()
bleu.stop()
GPIO.cleanup()
	
