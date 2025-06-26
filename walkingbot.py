from machine import Pin, PWM
from time import sleep

# =====================
# === LEG SERVOS ======
# =====================

# Servo 1 – Rear Right Hip – GPIO 21
servo1 = PWM(Pin(21), freq=50)
def move_servo1(angle):
    angle = max(0, min(180, angle))
    duty = int(30 + (angle / 180) * 75)
    servo1.duty(duty)
def servo1_in(): move_servo1(90)
def servo1_out(): move_servo1(0)

# Servo 2 – Front Right Hip – GPIO 18
servo2 = PWM(Pin(18), freq=50)
def move_servo2(angle):
    angle = max(0, min(90, angle))
    duty = int(90 + (angle / 90) * 25)
    servo2.duty(duty)
def servo2_in(): move_servo2(0)
def servo2_out(): move_servo2(90)

# Servo 3 – Front Left Hip – GPIO 23
servo3 = PWM(Pin(23), freq=50)
def move_servo3(angle):
    angle = max(10, min(160, angle))
    duty = int(25 + (angle / 90) * 25)
    servo3.duty(duty)
def servo3_in(): move_servo3(90)
def servo3_out(): move_servo3(0)

# Servo 4 – Rear Left Hip – GPIO 19
servo4 = PWM(Pin(19), freq=50)
def move_servo4(angle):
    angle = max(40, min(180, angle))
    duty = int(95 - (angle / 180) * 75)
    servo4.duty(duty)
def servo4_in(): move_servo4(90)
def servo4_out(): move_servo4(0)

# =====================
# === FOOT SERVOS =====
# =====================

# Servo 5 – Rear Right Foot – GPIO 5
servo5 = PWM(Pin(5), freq=50)
def move_servo5(angle):
    angle = max(0, min(180, angle))
    duty = int(90 + (angle / 180) * 75)
    servo5.duty(duty)
def servo5_up(): move_servo5(90)
def servo5_down(): move_servo5(10)

# Servo 6 – Front Right Foot – GPIO 17
servo6 = PWM(Pin(17), freq=50)
def move_servo6(angle):
    angle = max(0, min(90, angle))
    duty = int(95 + (angle / 180) * 75)
    servo6.duty(duty)
def servo6_up(): move_servo6(90)
def servo6_down(): move_servo6(15)

# Servo 7 – Front Left Foot – GPIO 18
servo7 = PWM(Pin(18), freq=50)
def move_servo7(angle):
    angle = max(20, min(260, angle))
    duty = int(20 + (angle / 180) * 25)
    servo7.duty(duty)
def servo7_up(): move_servo7(0)
def servo7_down(): move_servo7(260)

# Servo 8 – Rear Left Foot – GPIO 22
servo8 = PWM(Pin(22), freq=50)
def move_servo8(angle):
    angle = max(20, min(260, angle))
    duty = int(20 + (angle / 180) * 25)
    servo8.duty(duty)
def servo8_up(): move_servo8(0)
def servo8_down(): move_servo8(260)

# =============================
# === LOCOMOTION FUNCTIONS ====
# =============================

def forward_step(delay=0.4):
    servo3_up()
    servo1_up()
    servo4_up()
    sleep(delay)
    servo3_out()
    servo1_out()
    servo4_out()
    sleep(delay)
    servo3_down()
    servo1_down()
    servo4_down()
    sleep(delay)

    servo2_up()
    sleep(delay)
    servo2_out()
    sleep(delay)
    servo2_down()
    sleep(delay)

def backward_step(delay=0.4):
    servo3_up()
    servo1_up()
    servo4_up()
    sleep(delay)
    servo3_in()
    servo1_in()
    servo4_in()
    sleep(delay)
    servo3_down()
    servo1_down()
    servo4_down()
    sleep(delay)

    servo2_up()
    sleep(delay)
    servo2_in()
    sleep(delay)
    servo2_down()
    sleep(delay)

def turn_right(delay=0.4):
    servo3_up()
    servo4_up()
    sleep(delay)
    servo3_out()
    servo4_out()
    sleep(delay)
    servo3_down()
    servo4_down()
    sleep(delay)

    servo1_up()
    servo2_up()
    sleep(delay)
    servo1_in()
    servo2_in()
    sleep(delay)
    servo1_down()
    servo2_down()
    sleep(delay)

def turn_left(delay=0.4):
    servo1_up()
    servo2_up()
    sleep(delay)
    servo1_out()
    servo2_out()
    sleep(delay)
    servo1_down()
    servo2_down()
    sleep(delay)

    servo3_up()
    servo4_up()
    sleep(delay)
    servo3_in()
    servo4_in()
    sleep(delay)
    servo3_down()
    servo4_down()
    sleep(delay)

def stand():
    servo1_in()
    servo2_in()
    servo3_in()
    servo4_in()
    servo5_down()
    servo6_down()
    servo7_down()
    servo8_down()

def collapse():
    servo1_in()
    servo2_in()
    servo3_in()
    servo4_in()
    servo5_up()
    servo6_up()
    servo7_up()
    servo8_up()

# =============================
# === STARTUP TEST SEQUENCE ===
# =============================

# stand()
# sleep(1)
# forward_step()
# sleep(1)
# turn_right()
# sleep(1)
# backward_step()
# sleep(1)
# turn_left()
# sleep(1)
# collapse()
