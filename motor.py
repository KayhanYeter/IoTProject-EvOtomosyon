import RPi.GPIO as GPIO
from time import sleep
import requests  #buluta veri aktarimi icin kullanilan kutuphane
GPIO.setmode(GPIO.BCM)
out_pin= 2
GPIO.setup(out_pin, GPIO.OUT)
pwm=GPIO.PWM(out_pin, 50)  #frekans ayari
pwm.start(0)
dweetIO = "https://dweet.io/dweet/for/"    #bulut platformu: dweet.io
myName = "RaspberryPi"
myKey = "Motor" 

def SetAngle(angle):
	duty = angle / 18 + 2
	GPIO.output(out_pin, True)
	pwm.ChangeDutyCycle(duty)
	sleep(1)
	GPIO.output(out_pin, False)
	pwm.ChangeDutyCycle(0)
	
SetAngle(200)
data="MotorCalisiyor"

pwm.stop()

rqsString = dweetIO+myName+'?'+myKey+'='+str(data)
print(rqsString)
rqs = requests.get(rqsString)
print (rqs.status_code)
print (rqs.headers)
print (rqs.content)
GPIO.cleanup()