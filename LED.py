import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(3,GPIO.OUT)
GPIO.output(3,False)

while True:
    GPIO.wait_for_edge(17,GPIO.FALLING)
    sw_counter = 0
    while True:
        sw_status = GPIO.input(17)
        if sw_status == 0:
            sw_counter = sw_counter + 1
            if sw_counter >= 30:
                GPIO.output(3,True)
                break
            GPIO.output(3,False)
        else:
            break
time.sleep (0.01)
GPIO.cleanup()
        
