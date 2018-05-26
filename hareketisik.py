import time
import RPi.GPIO as io
import requests  #buluta veri aktarimi icin kullanilan kutuphane

io.setmode(io.BCM)

pir_pin= 24
power_pin= 23
led_pin= 22

io.setup(pir_pin, io.IN)
io.setup(power_pin, io.OUT)
io.setup(led_pin, io.OUT)
io.output(led_pin, False)
io.output(power_pin, True)

dweetIO = "https://dweet.io/dweet/for/"
myName = "RaspberryPi"
myKey = "ısık" 


while True:
    if io.input(pir_pin):
        print("Power On")
        data= 'isik yandi'
        print(data)
        rqsString = dweetIO+myName+'?'+myKey+'='+str(data)
        print(rqsString)
        rqs = requests.get(rqsString)
        print (rqs.status_code)
        print (rqs.headers)
        print (rqs.content)
        io.output(power_pin, False)
        io.output(led_pin, False)
        time.sleep(20)
        io.output(power_pin, True)
        io.output(led_pin, True)
        data= 'isik söndü'
        print(data)
        time.sleep(5)
        #Send to Cloud, dweet.io
        rqsString = dweetIO+myName+'?'+myKey+'='+str(data)
        print(rqsString)
        rqs = requests.get(rqsString)
        print (rqs.status_code)
        print (rqs.headers)
        print (rqs.content)
    time.sleep(1)