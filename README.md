Raspberry-pi-LED-Stip-With-Web-Control
======================================

How to Control RGB LED Stip with the Raspberry Pi  with Web Interface 

items used

Raspberry Pi Model B (from Adafruit)

Adafruit Pi T-Cobbler Breakout Kit (GPIO)

Half size solderless breadboard (from Adafruit)

3x 2n3904 transistors (from digikey)

1m rgb led strip (from Adafruit)

16gb class 4 SD card (from Amazon)

802.11n Wifi Dongle (from Adafruit)

web server with CPannel

12v 2amp power supply 

BeFore you Start 

you need to have Occidentalis Distro From AdaFruit
http://learn.adafruit.com/adafruit-raspberry-pi-educational-linux-distro/occidentalis-v0-dot-2

what to do 

1. Place all the Files in the "For Web Server" folder in the Root of your web server.

2. Place All the Files in the "For Pi" in to the raspberry pi.

3. Hook up all the RGB LED strip with this schematic, at 

4. On the Pi in the Poll.py file find "http://YourWebsite.com/test.php" that are lines 20, 23 and replace the it with the URL that leads to test.php file on your web server.

5. CD to the file containing the python scrip "poll.py" 

6. start the python script with sudo as you are using the the GPIO 

7. to Change the colour go to the URL containing the controller.php like http://yourwebsite.cm/contoller.php 