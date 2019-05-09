import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

PIN_LED = 12
PIN_TRIGGER = 16
PIN_ECHO = 18

GPIO.setup(PIN_LED, GPIO.OUT)
pwm = GPIO.PWM(PIN_LED, 100)

GPIO.setup(PIN_TRIGGER, GPIO.OUT)
GPIO.setup(PIN_ECHO, GPIO.IN)

pwm.start(0)    
print("Waiting for sensor")
time.sleep(2)
    
try:
    while True:
        
        print("Calculating distance")
        
        GPIO.output(PIN_TRIGGER, GPIO.HIGH)
        
        time.sleep(0.00001)
        
        GPIO.output(PIN_TRIGGER, GPIO.LOW)
        
        while GPIO.input(PIN_ECHO) == 0:
            pulse_start_time = time.time()
            
        while GPIO.input(PIN_ECHO) == 1:
            pulse_end_time = time.time()
            
        pulse_duration = pulse_end_time - pulse_start_time
        distance = round(pulse_duration * 17150, 2)

        #Multiply distance by 10 to make max brightness at 10cm
        if (100 - distance * 10 > 0):
            outputVal = 100 - distance * 10
        #If out out range, turn LED off
        else:
            outputVal = 0
        pwm.ChangeDutyCycle(outputVal)
            
        print("Distance: ", distance, "cm")
        time.sleep(0.1)

except KeyboardInterrupt:
    pass

finally:
    pwm.stop()
    GPIO.cleanup()
