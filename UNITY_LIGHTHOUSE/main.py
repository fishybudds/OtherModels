# Import necessary modules
from machine import Pin
import time

# Initialize LED and button pins
led1 = Pin(15, Pin.OUT)
led2 = Pin(13, Pin.OUT)
ledr = Pin(12, Pin.OUT)
button = Pin(0, Pin.IN, Pin.PULL_UP)

def ledallon():
    led1.on()
    led2.on()
    ledr.on()
    print("LEDs on")
    
def ledalloff():
    led1.off()
    led2.off()
    ledr.off()
    print("LEDs off")
    
def gwmorsecode():
    # --._.--
    # -
    ledr.on()
    time.sleep(0.5)
    ledr.off()
    time.sleep(0.5)
    # -
    ledr.on()
    time.sleep(0.5)
    ledr.off()
    time.sleep(0.5)
    # .
    ledr.on()
    time.sleep(0.25)
    ledr.off()
    time.sleep(0.5)
    # space
    time.sleep(0.5)
    # .
    ledr.on()
    time.sleep(0.25)
    ledr.off()
    time.sleep(0.5)
    # -
    ledr.on()
    time.sleep(0.5)
    ledr.off()
    time.sleep(0.5)
    # -
    ledr.on()
    time.sleep(0.5)
    ledr.off()
    time.sleep(0.5)

    # clear by holding for 1 additional second
    time.sleep(1)
    
# Initialize LED state (off initially)
led1_state = False
led2_state = False
ledy_state = False
start_time = 0
end_time = 0

while True:
    if button.value() == 0:  # Button is pressed
        if start_time == 0:
            start_time = time.ticks_ms()
    else:
        if start_time != 0:
            end_time = time.ticks_ms()
            duration = time.ticks_diff(end_time, start_time)
            print("Button was pressed for {} milliseconds".format(duration))
            
            # Run specific code based on the duration
            if duration < 3000:
                print("Short press detected")
                print(led1.value())
                if led1.value() == 0:
                    ledallon()
                else:
                    ledalloff()
            else:
                print("Long press detected")
                loop_counter = 0
                ledallon()
                while loop_counter < 11:
                        gwmorsecode()
                        loop_counter = loop_counter+ 1
                        print(loop_counter)
                print("Done blinking")
                ledalloff()
                      
            start_time = 0
    time.sleep(0.01)
