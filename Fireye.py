>>> import machine
>>> import time
>>> POC = machine.Pin(0, machine.Pin.OUT)
>>> interlock = machine.Pin(1, machine.Pin.OUT)
                           
>>> for i in range(10):
...     POC.on()  
... 


...     time.sleep(10)
...     pin.off()

...     time.sleep(60)
