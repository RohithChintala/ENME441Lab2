import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
pwm1= GPIO.PWM(4, 1)
pwm2= GPIO.PWM(17, 1)
pwm3= GPIO.PWM(27, 1)
pwm2.start(0)
pwm1.start(0)

def myCallback(channel):
  if channel == 16:
    for d1 in range(100):
      pwm1.ChangeDutyCycle(d1)
      sleep(0.005)
    for i in range(100):
      decrease = 100-i
      pwm1.ChangeDutyCycle(i)
      sleep(.005)

  if channel == 21:
    for d2 in range(101):
      pwm1.ChangeDutyCycle(d2)
      sleep(0.005)
    for i in range(100):
      decrease = 100-i
      pwm1.ChangeDutyCycle(i)
      sleep(.005)
    

GPIO.add_event_detect(16, GPIO.RISING, callback=myCallback, bouncetime=500)
GPIO.add_event_detect(21, GPIO.RISING, callback=myCallback, bouncetime=500)
try:
 while 1:
  pwm3.start(50)
except KeyboardInterrupt:
 print('\nExiting')
  

pwm1.stop()
pwm2.stop()
pwm3.stop()
GPIO.cleanup()
