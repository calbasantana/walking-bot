<p align="center">
  <img src="media/photos/walkingbot.jpg" alt="Walking Bot" width="500"/>
</p>

# Introduction

I have been trying, over several years, to develop a walking robot. I've come across many issues, from not enough servos to too many servos (and having a heavy robot that couldn't walk). This repository highlights the latest iteration of this walking robot.

# Materials

The following materials need to be purchased for this walking robot (links included):

* [12V 5200mAh Battery (X1, $32.99 ea.)](https://www.amazon.com/KBT-5200mAh-Rechargeable-Replacement-Compatible/dp/B0C242DYT1/ref=sr_1_7?crid=1SIDJOUAQQIE8&dib=eyJ2IjoiMSJ9.6A_VA_8qcZroVXD4hbJG-_0zYHsfztkOuL_j0ZI-qVZ90qAFC3pD6ulImms8gsOluSv09c7E2UkUkAfOtg5ae5XctOkT6waX_H6I7cpZZVHjBornF08RjtB9Y06umyWruwKf0tWKJxI-95cVymsCEPRJSuEBwIOSYjAC6JxqDxNQfWa0c5tolPITw42kGHjWYQf4jIHa1VIvBFsTsKh1URHNKBJIWVgipW1xOpEBSAbN1YSQjgVpYk5lICj7d30b3omKCGwQFhlaXov5YLSx2Zy_6XYpxYl9xzKJ_VgvtaY.gubT1TkzdsS7j0zriC8-6xLCnk4GDlg6R8FMsayGwtU&dib_tag=se&keywords=kbt%2Blithium%2Bion%2Bbattery&qid=1750712377&sprefix=kbt%2Blithium%2Bion%2Bbatter%2Caps%2C124&sr=8-7&th=1)
* [MG995 Servo (X8, $31.98 total)](https://www.amazon.com/Deegoo-FPV-Servo-MG995-Metal-Gear/dp/B07NQJ1VZ2/ref=sr_1_6?crid=1LRVW3LG4KGXD&dib=eyJ2IjoiMSJ9.cY6Rczg-OlaZeR22jUS8vOk7vd9JDTpqytGHpfWNxOlzQFdnAyPecryWF9KDcFX2pL2ia-pAG7zC4S_txmg_kkIxSdgtMvAg5yYaYJXFxklBoDVtZkeQmMhHJeYMrFIZERKQjOgSn0kTTQoBDRdeNHMaPW0c1Y-ldS6d29fXGHAN4X-1OEOwR2qHJR3leqAmfDyGmyF0VcpU1VPgNbuj1m3jghHgpEpPwSluAZ7lHcDHbbXuN0xwk1KAV87xcVZwunwntDmgJEUvePrW3sspIzfqw44Cj5WJN4kLdVq3MMA.C5VbtW8-uepQ90Cg2UnQXSa3J9jt21Cqt-MqjfxltAM&dib_tag=se&keywords=mg995%2Bservo&qid=1750712406&sprefix=mg995%2Bservo%2Caps%2C133&sr=8-6&th=1)
* [Servo 2040 from Pimoroni (X1, $24 total)](https://shop.pimoroni.com/products/servo-2040?variant=39800591679571)

The total estimated cost of this walking robot is around **$88.97**, but that can fluctuate based on deals and other things.

# Walking Bot Body

I designed the walking bot on OnShape and printed it using my Prusa Mini.

## CAD Model

Below you will see my CAD model for this walking robot.

<p align="center">
  <img src="media/screenshots/walkingbot_CAD_Model.png" alt="Walking Bot CAD Model" width="500"/>
</p>

### Base of Walking Bot


### Legs of Walking Bot

### Feet of Walking Bot



## Specifications & Material(s)
Below you can find the printer and material used.
## 3D Printer
Original Prusa Mini+
## Material(s)
* [Grey ANYCUBIC 1kg, 1.75mm Filament ($13.99)](https://www.amazon.com/dp/B0834W5L3L?ref_=ppx_hzsearch_conn_dt_b_fed_asin_title_3)
# Software
PrusaSlicer

[PRUSA SLICER IMAGE]

## Settings
  Layer Height: .2mm \
  Infill: 50% \
  Supports: None \
  Estimated Printing Time: 1 hour and 17 minutes

## Assembly



Here's a video of a rover after assembly and testing.

# Programming

Thonny is used as the programming platform. Students can install this application on their own non-chromebook devices using the instructions below.

Go to the official [Thonny](https://thonny.org/) website and download the application. Then, depending on your operating system, continue as follows:

**For Windows**: Install the 64-bit version. Then, go to this [website](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers) to install a driver, which will allow USB access to Thonny so it can connect to the ESP32 via USB. Go to Downloads, then click CP210x VCP Windows. Once downloaded, use the x64 .exe file to install the driver. \
**For Mac**: Install using the first option with .pkg. Then, go to this [website](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers) to install a driver, which will allow USB access to Thonny so it can connect to the ESP32 via USB. Go to Downloads, then click CP210x VCP Mac OSX Driver. Then click on the .dmg file to install; **it will ask you to give access at some point in the settings, make sure to allow it access otherwise it won’t work**. \
**For Linux**: It is recommended that you use the flatpak installation method if you already have flatpak in your system. If you do not have flatpak in your system, you may install it from the terminal via your default package manager; see this [website](https://flatpak.org/setup/) for specific directions if you are unsure. You may need to use “sudo chmod a+rw /dev/ttyUSB0” to open up the USB connection each time you connect the ESP32.

Rovers are programmed in microPython. Below you will find some instructions on how to program the rover, which requires that both .py files in this repostory (main.py and rover.py) are uploaded to the ESP32.

# Tips
