from gpiozero import LED
from time import sleep

carousel_1=LED(15)
carousel_2=LED(18)
carousel_3=LED(23)

while True:
    carousel_1.on()
    sleep(3)
    carousel_1.off()

    carousel_2.on()
    sleep(3)
    carousel_2.off()
    
    carousel_3.on()
    sleep(3)
    carousel_3.off()

    
