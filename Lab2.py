import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)  #sets gpio to bcm mode
GPIO.setup(4, GPIO.OUT) #sets pin 4 as output
GPIO.setup(17, GPIO.OUT) #sets pin 17 as output
GPIO.setup(27, GPIO.OUT) #sets pin 27 as output
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #sets pin 26 as pull down input
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #sets pin 21 as pull down input
pwm1= GPIO.PWM(4, 1) #creates pwm object at 1 hz for pin 4
pwm2= GPIO.PWM(17, 1) #creates pwm object at 1 hz for pin 17
pwm3= GPIO.PWM(27, 1) #creates pwm object at 1hz for pin 27


def myCallback(pin): #defines myCallback function
  if pin == 26: #checks if button for pin 26 is pressed
    pwm1.start(0) #starts pwm1 at 0 hz
    for i in range(100): #iterates i to 100
      pwm1.ChangeDutyCycle(i) #increases duty cycle with i
      sleep(.005) #sleeps for 5ms between duty cycle changes
    for i in range(100): #increase i to 100
      d = 100-i #defines d to decrease as i increases
      pwm1.ChangeDutyCycle(d) #decreases duty cycle with d
      sleep(.005) #sleeps for 5ms between duty cycle changes
    pwm1.stop() #stops pwm1
 
  if pin == 21: #checks if button for pin 21 is pressed
    pwm2.start(0) #starts pwm2 at 0 hz
    for i in range(100): #iterates i to 100
      pwm2.ChangeDutyCycle(i) #increases duty cycle with i
      sleep(.005) #sleeps for 5 ms between duty cycle changes 
    for i in range(100): #iterates i to 100 
      d = 100-i #defines d to decrease as i increases
      pwm2.ChangeDutyCycle(d) #decreases duty cycle with d
      sleep(.005) #sleeps for 5 ms between duty cycle changes
    pwm2.stop() #stops pwm2
    
#creates callback for each button to run myCallback with press
GPIO.add_event_detect(26, GPIO.RISING, callback=myCallback, bouncetime=200) 
GPIO.add_event_detect(21, GPIO.RISING, callback=myCallback, bouncetime=200)
try: 
 while 1:
  pwm3.start(50) #starts pwm3 at 50% duty cycle to run continuously
except KeyboardInterrupt:
 print('\nExiting')

  
#stops all pwm cycles and runs GPIO cleanup
pwm1.stop() 
pwm2.stop()
pwm3.stop()
GPIO.cleanup()
