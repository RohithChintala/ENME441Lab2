import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

pwm1= GPIO.PWM(p, 1) 
pwm2= GPIO.PWM(p, 1) 
pwm3= GPIO.PWM(p, 1) 
try: 
	GPIO.add_event_detect(20, GPIO.RISING,  callback=myCallback1, bouncetime=100)
	GPIO.add_event_detect(21, GPIO.RISING,  callback=myCallback1, bouncetime=100)

	pwm3.start(50)


except KeyboardInterrupt:       # stop gracefully on ctrl-C
	print('\nExiting')
  

pwm1.stop()
pwm2.stop()
pwm3.stop()
GPIO.cleanup()

def myCallback1(channel):
  if channel == 20
	  pwm1.start(0)
	  for dc in range(101):     
		  pwm1.ChangeDutyCycle(dc)   # set duty cycle
		  sleep(0.005)               # sleep 10 ms
	  for dc in range(101):     
		  pwm.ChangeDutyCycle(101-dc)   # set duty cycle
		  sleep(0.005)               # sleep 10 ms
  elif channel == 21
	  pwm2.start(0)
	  for dc in range(101):     
		  pwm2.ChangeDutyCycle(dc)   # set duty cycle
		  sleep(0.005)               # sleep 10 ms
	  for dc in range(101):     
		  pwm2.ChangeDutyCycle(101-dc)   # set duty cycle
		  sleep(0.005)               # sleep 10 ms
