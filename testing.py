import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
pwm1= GPIO.PWM(4, 1)
pwm2= GPIO.PWM(17, 1)
pwm3= GPIO.PWM(27, 1)


def myCallback(channel):
  if channel == 26:
    pwm1.start(0)
    for i in range(100):
      pwm1.ChangeDutyCycle(i)
      sleep(0.0025)
    for i in range(100):
      d = 100-i
      pwm1.ChangeDutyCycle(d)
      sleep(.0025)
    pwm1.stop()
 
  if channel == 21:
    pwm2.start(0)
    for i in range(100):
      pwm2.ChangeDutyCycle(i)
      sleep(0.0025)
    for i in range(100):
      d = 100-i
      pwm2.ChangeDutyCycle(d)
      sleep(.00025)
    pwm2.stop()
    

GPIO.add_event_detect(26, GPIO.RISING, callback=myCallback, bouncetime=200)
GPIO.add_event_detect(21, GPIO.RISING, callback=myCallback, bouncetime=200)
try:
 while 1:
  pwm3.start(50)
except KeyboardInterrupt:
 print('\nExiting')
 pwm1.stop()
 pwm2.stop()
 pwm3.stop()
 GPIO.cleanup()

  

pwm1.stop()
pwm2.stop()
pwm3.stop()
GPIO.cleanup()
