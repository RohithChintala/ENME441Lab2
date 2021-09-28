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
pwm3= GPIO.PWM(27, 2)


def myCallback(channel):
  print(channel)
  if channel == 26:
    pwm1.start(0)
    print('26 working')
    for d in range(100):
      pwm1.ChangeDutyCycle(d)
      sleep(0.005)
    for i in range(100):
      decrease = 100-i
      pwm1.ChangeDutyCycle(decrease)
      sleep(.005)
    pwm1.stop()
 
  if channel == 21:
    pwm2.start(0)
    print('21 working')
    for c in range(100):
      pwm2.ChangeDutyCycle(c)
      sleep(0.005)
    for f in range(100):
      decrease = 100-f
      pwm2.ChangeDutyCycle(decrease)
      sleep(.005)
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
