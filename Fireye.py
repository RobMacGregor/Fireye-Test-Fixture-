>>> import machine
>>> import time
>>> POC = machine.Pin(0, machine.Pin.OUT)
>>> interlock = machine.Pin(1, machine.Pin.OUT)
>>> fan = machine.Pin(2, machine.Pin.OUT)                  
>>> for i in range(10):
...     POC.on()  
...     interlock.on()
...     fan.off()

...     time.sleep(10)
...     POC.off()
...     fan.on()
...     time.sleep(60)

