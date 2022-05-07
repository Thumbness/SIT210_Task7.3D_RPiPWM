
import RPi.GPIO as GPIO
import time 

trig_pin = 13
echo_pin = 15
led_pin = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(trig_pin, GPIO.OUT)
GPIO.setup(echo_pin, GPIO.IN)

pwm = GPIO.PWM(led_pin, 100)  
pwm.start(0)

i = 0
maxlumen = 100

try:
    while 1:
        
        GPIO.output(trig_pin, True)
        time.sleep(0.00001)
        GPIO.output(trig_pin, False)

        while GPIO.input(echo_pin)==0:
           pulse_start = time.time()

        while GPIO.input(echo_pin)==1:
           pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start

        distance = pulse_duration * 17150

        distance = round(distance+1.15, 2)
    
        x = maxlumen - distance
        
        print("distance:",distance,"cm")
        if distance <= 100 and distance>=2:
           
           pwm.ChangeDutyCycle(x)
           i=1
           
        elif(distance >100 ):
        
           pwm.ChangeDutyCycle(0)
           i = 1

         
        time.sleep(0.2)
           
        
except KeyboardInterrupt:
    pass        
pwm.stop()      
GPIO.cleanup()