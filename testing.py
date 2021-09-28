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
pwm2.start(0)
pwm1.start(0)

def myCallback(channel):
  print(channel)
  if channel == 26:
    print('26 working')
    for d1 in range(100):
      pwm1.ChangeDutyCycle(d1)
      sleep(0.005)
    for i in range(100):
      decrease = 100-i
      pwm1.ChangeDutyCycle(i)
      sleep(.005)
    pwm1.stop()
  if channel == 21:
    print('21 working')
    for d2 in range(101):
      pwm2.ChangeDutyCycle(d2)
      sleep(0.005)
    for i in range(100):
      decrease = 100-i
      pwm2.ChangeDutyCycle(i)
      sleep(.005)
    pwm2.stop()
    

GPIO.add_event_detect(26, GPIO.RISING, callback=myCallback, bouncetime=500)
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
