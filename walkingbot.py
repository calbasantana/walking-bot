from machine import Pin, PWM
from time import sleep

# LEG SERVOS

# Servo 1 – Rear Right Hip – GPIO 0
servo1 = PWM(Pin(0))
servo1.freq(50)
def move_servo1(angle):
    angle = max(0, min(180, angle))
    duty = int(30 + (angle / 180) * 75)
    servo1.duty_u16(int(duty / 100 * 6553))
def servo1_in(): move_servo1(50)
def servo1_out(): move_servo1(0)

# Servo 2 – Front Right Hip – GPIO 2
servo2 = PWM(Pin(1))
servo2.freq(50)
def move_servo2(angle):
    angle = max(0, min(90, angle))
    duty = int(90 + (angle / 90) * 25)
    servo2.duty_u16(int(duty / 100 * 6553))
def servo2_in(): move_servo2(0)
def servo2_out(): move_servo2(90)

# Servo 3 – Front Left Hip – GPIO 2
servo3 = PWM(Pin(2))
servo3.freq(50)
def move_servo3(angle):
    angle = max(10, min(160, angle))
    duty = int(25 + (angle / 90) * 25)
    servo3.duty_u16(int(duty / 100 * 6553))
def servo3_in(): move_servo3(90)
def servo3_out(): move_servo3(0)

# Servo 4 – Rear Left Hip – GPIO 3
servo4 = PWM(Pin(3))
servo4.freq(50)
def move_servo4(angle):
    angle = max(40, min(180, angle))
    duty = int(95 - (angle / 180) * 75)
    servo4.duty_u16(int(duty / 100 * 6553))
def servo4_in(): move_servo4(90)
def servo4_out(): move_servo4(0)


# FOOT SERVOS


# Servo 5 – Rear Right Foot – GPIO 4
servo5 = PWM(Pin(4))
servo5.freq(50)
def move_servo5(angle):
    angle = max(0, min(180, angle))
    duty = int(90 + (angle / 180) * 75)
    servo5.duty_u16(int(duty / 100 * 6553))
def servo5_up(): move_servo5(90)
def servo5_down(): move_servo5(0)

# Servo 6 – Front Right Foot – GPIO 5
servo6 = PWM(Pin(5))
servo6.freq(50)
def move_servo6(angle):
    angle = max(0, min(90, angle))
    duty = int(95 + (angle / 180) * 75)
    servo6.duty_u16(int(duty / 100 * 6553))
def servo6_up(): move_servo6(80)
def servo6_down(): move_servo6(10)

# Servo 7 – Front Left Foot – GPIO 6
servo7 = PWM(Pin(6))
servo7.freq(50)
def move_servo7(angle):
    angle = max(20, min(260, angle))
    duty = int(20 + (angle / 180) * 25)
    servo7.duty_u16(int(duty / 100 * 6553))
def servo7_up(): move_servo7(0)
def servo7_down(): move_servo7(260)

# Servo 8 – Rear Left Foot – GPIO 7
servo8 = PWM(Pin(7))
servo8.freq(50)
def move_servo8(angle):
    angle = max(20, min(260, angle))
    duty = int(20 + (angle / 180) * 25)
    servo8.duty_u16(int(duty / 100 * 6553))
def servo8_up(): move_servo8(0)
def servo8_down(): move_servo8(260)

# FUNCTIONS

def stand():
    servo1_out()
    servo2_out()
    servo3_out()
    servo4_out()
    servo5_down()
    servo6_down()
    servo7_down()
    servo8_down()
    sleep(0.5)

def collapse():
    servo1_in()
    servo2_in()
    servo3_in()
    servo4_in()
    servo5_up()
    servo6_up()
    servo7_up()
    servo8_up()
    sleep(0.5)

def turn_left():
    servo6_up()
    sleep(0.2)
    servo2_in()
    sleep(0.2)
    servo6_down()
    sleep(0.2)
    servo2_out()
    sleep(0.2)

def walk_forward(steps=1):
    for _ in range(steps):
        # Step 1 – Lift front left
        servo7_up()
        sleep(0.2)
        servo3_in()
        sleep(0.2)
        servo7_down()
        sleep(0.2)
        servo3_out()
        sleep(0.2)

        # Step 2 – Lift rear right
        servo5_up()
        sleep(0.2)
        servo1_in()
        sleep(0.2)
        servo5_down()
        sleep(0.2)
        servo1_out()
        sleep(0.2)

        # Step 3 – Lift front right
        servo6_up()
        sleep(0.2)
        servo2_in()
        sleep(0.2)
        servo6_down()
        sleep(0.2)
        servo2_out()
        sleep(0.2)

        # Step 4 – Lift rear left
        servo8_up()
        sleep(0.2)
        servo4_in()
        sleep(0.2)
        servo8_down()
        sleep(0.2)
        servo4_out()
        sleep(0.2)

# PROGRAM
stand()
walk_forward(10)
collapse()
