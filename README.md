<p align="center">
  <img src="media/photos/rover.jpg" alt="PCB Front" width="500"/>
</p>

# Introduction

I have been trying, over several years, to develop a walking robot. I've come across many issues, from not enough servos to too many servos (and having a heavy robot that couldn't walk). This repository highlights the latest iteration of this walking robot.

# Materials

The following materials need to be purchased for this walking robot (links included):

* [12V 5200mAh Battery (X1, $32.99 ea.)](https://www.amazon.com/KBT-5200mAh-Rechargeable-Replacement-Compatible/dp/B0C242DYT1/ref=sr_1_7?crid=1SIDJOUAQQIE8&dib=eyJ2IjoiMSJ9.6A_VA_8qcZroVXD4hbJG-_0zYHsfztkOuL_j0ZI-qVZ90qAFC3pD6ulImms8gsOluSv09c7E2UkUkAfOtg5ae5XctOkT6waX_H6I7cpZZVHjBornF08RjtB9Y06umyWruwKf0tWKJxI-95cVymsCEPRJSuEBwIOSYjAC6JxqDxNQfWa0c5tolPITw42kGHjWYQf4jIHa1VIvBFsTsKh1URHNKBJIWVgipW1xOpEBSAbN1YSQjgVpYk5lICj7d30b3omKCGwQFhlaXov5YLSx2Zy_6XYpxYl9xzKJ_VgvtaY.gubT1TkzdsS7j0zriC8-6xLCnk4GDlg6R8FMsayGwtU&dib_tag=se&keywords=kbt%2Blithium%2Bion%2Bbattery&qid=1750712377&sprefix=kbt%2Blithium%2Bion%2Bbatter%2Caps%2C124&sr=8-7&th=1)
* [MG995 Servo (X8, $31.98 total)](https://www.amazon.com/Deegoo-FPV-Servo-MG995-Metal-Gear/dp/B07NQJ1VZ2/ref=sr_1_6?crid=1LRVW3LG4KGXD&dib=eyJ2IjoiMSJ9.cY6Rczg-OlaZeR22jUS8vOk7vd9JDTpqytGHpfWNxOlzQFdnAyPecryWF9KDcFX2pL2ia-pAG7zC4S_txmg_kkIxSdgtMvAg5yYaYJXFxklBoDVtZkeQmMhHJeYMrFIZERKQjOgSn0kTTQoBDRdeNHMaPW0c1Y-ldS6d29fXGHAN4X-1OEOwR2qHJR3leqAmfDyGmyF0VcpU1VPgNbuj1m3jghHgpEpPwSluAZ7lHcDHbbXuN0xwk1KAV87xcVZwunwntDmgJEUvePrW3sspIzfqw44Cj5WJN4kLdVq3MMA.C5VbtW8-uepQ90Cg2UnQXSa3J9jt21Cqt-MqjfxltAM&dib_tag=se&keywords=mg995%2Bservo&qid=1750712406&sprefix=mg995%2Bservo%2Caps%2C133&sr=8-6&th=1)
* [Servo 2040 from Pimoroni (X1, $24 total)](https://shop.pimoroni.com/products/servo-2040?variant=39800591679571)

The total estimated cost of this wlaking robot is around $88.97, but that can fluctuate based on deals and other things.

# Walking Bot Body

I designed the walking bot on OnShape and printed it using my Prusa Mini.

## CAD Model

Below you will see my CAD model for this walking robot.

<p align="center">
  <img src="media/screenshots/rover_CAD.png" alt="Rover CAD Model" width="500"/>
</p>

## 3D Printing

### Materials
* [Grey ANYCUBIC 1kg, 1.75mm Filament ($13.99)](https://www.amazon.com/dp/B0834W5L3L?ref_=ppx_hzsearch_conn_dt_b_fed_asin_title_3)

### 3D Printer
Original Prusa Mini+ \
**Software** \
PrusaSlicer \
**Settings** \
Layer Height: .2mm \
Infill: 50% \
Supports: Everywhere \
Estimated Printing Time: ~ 2hours.

## Assembly

Once all parts have been lasercut and 3D printed, it is time for assembly. I highly suggest starting off with hot gluing all parts that need to be hot glued and waiting for a bit for them to dry. After doing this, it is recommended to assemble in the following order:

* Place and screw the PCB. Make sure the ESP32 and motor drivers are on it.
* Screw the motor mounts to the board.
* Place the DC motors inside the motor mounts and screw them in, being very careful with their cables. I recommend placing the motors such that the cables coming out of them face towards the center of the rover (this way they won't get caught on stuff).
* Screw the wheels onto the DC motors.
* Connect the motors in the desired locations, using cable jumpers if necessary. **Black goes on GND and red on VCC**. It is recommended to have one motor in each of the numbered slots (like 1A, 2A, 3A, and 4A).
* Connect the battery adapter cables.
* Connect the batteries to test that all components work. **IMPORTANT**: If running the default code, it will have all motors moving forward, so if some wheels are spinning backwards, you can change the orientation of the motor connections such that the black cable is on VCC and red is on GND; **this only works to reverse the drive of motors, do not try this with the batteries**. Remove once you've confirmed all components seem to be working OK. Report any issues.

Here's a video of a rover after assembly and testing.

https://github.com/user-attachments/assets/2081dea4-9fc1-44c9-863f-5ba131637c97

# Programming

Thonny is used as the programming platform. Students can install this application on their own non-chromebook devices using the instructions below.

Go to the official [Thonny](https://thonny.org/) website and download the application. Then, depending on your operating system, continue as follows:

**For Windows**: Install the 64-bit version. Then, go to this [website](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers) to install a driver, which will allow USB access to Thonny so it can connect to the ESP32 via USB. Go to Downloads, then click CP210x VCP Windows. Once downloaded, use the x64 .exe file to install the driver. \
**For Mac**: Install using the first option with .pkg. Then, go to this [website](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers) to install a driver, which will allow USB access to Thonny so it can connect to the ESP32 via USB. Go to Downloads, then click CP210x VCP Mac OSX Driver. Then click on the .dmg file to install; **it will ask you to give access at some point in the settings, make sure to allow it access otherwise it won’t work**. \
**For Linux**: It is recommended that you use the flatpak installation method if you already have flatpak in your system. If you do not have flatpak in your system, you may install it from the terminal via your default package manager; see this [website](https://flatpak.org/setup/) for specific directions if you are unsure. You may need to use “sudo chmod a+rw /dev/ttyUSB0” to open up the USB connection each time you connect the ESP32.

Rovers are programmed in microPython. Below you will find some instructions on how to program the rover, which requires that both .py files in this repostory (main.py and rover.py) are uploaded to the ESP32.

## Programming Your Rover

To program your rover, first open up the Thonny application. Then, follow the instructions below.

1. Remove your ESP32 from your rover. Trying to connect to it while it is connected to the rover might damage the ESP32, so it is best to remove it and then connect to it.

2. Press the STOP/Start button. At the bottom of the screen, you should see ">>>". This should indicate the ESP32 is connected.

3. Go to File -> Open. Select from micropython device. Here, you should be able to open up the main.py file.

4. You should also be able to open rover.py file to see available functions. Essentially, the most important three pieces of code are the following:

  * **rover.move_motor(motor_num, direction, speed)**: You should input the motor number, the direction (forward or backward), and speed (100 - 1000). For example, rover.move_motor(1, forward, 300) moves motor 1 at a speed of 300 forward. You can have multiple motors move at the same time by having them on separate, but sequential lines like so:
    * rover.move_motor(1, forward, 300)
    * rover.move_motor(2, forward, 300) \
  These two lines of code move motors 1 and 2 forward at a speed of 300.
  * **sleep(time)**: This piece of code decides how long the previous piece of code runs for before moving to the next. If placed right after the two pieces of code from the last bullet point, it will move those two motors forward at a speed of 300 for 10 seconds before moving to the next piece of code. Decimals are allowed.
  * **gradual_stop_all(direction="forward", initial_speed=700)**: This piece of code gradually stops all motors. No edits are necessary. However, if you would like to match the speed with the speed from previous line of code, you may do so.

# Tips
