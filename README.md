# Simple Arduino Handheld GPS Navigator

Sorry, but all screens, comments and descriptions are in Russian. 
I'll fix it later if have anouth time.

- gps.ino -- program of Navigator
- libraries/ -- a pack of third party libs, you should add it to your arduino home dir
- images/ -- a screens for LCD-display and small python script for converting 3bytes-BMP to C-bytes string

# Features

- Displays 100 points of track
- Shows moving direction as arrow
- You can set custon target point
- Shows distance to target point
- You can clear point 
- You can set current point as target point

# Hardware

- Nokia 5110 84x48 graphical monochrome display onpins 4, 5, 6, 7, 8, 9 (it is possible to change)
- IMEA UART GPS module on pins 2 and 3 (can not change)
- Three buttons connecting to GND at 10, A5 and A4 pins (it is possible to change)

# GPS-навигатор на Ардуино
