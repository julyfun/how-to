---
title: macos-link-and-upload-code
date: 2024-01-15 19:38:46
tags: ["hardwares", "arduino"]
---
* Board type: Arduino Uno
* IDE: Arduino IDE 2.2.1
* MacOS 13.4

* Download Arduino IDE for mac (for free on official website)
* Install ch34x driver. (To put simply, Ch340 is basically a USB bus convert chip. It allows the USB to be converted to serial interface, serial signals to USB etc. You can even think of Ch340 as a trader of some sort!)
* Link your mac and your arduino with a usb cable. (maybe a hub is needed). The board shows two red lights. One could be flashing before uploading code.
* In arduino IDE there is a default piece of code. In your menu bar, choose Tools -> Board -> Arduino AVR Boards -> Arduino Uno. And Tools -> Port -> `/dev/cu.usbserial-140`.
* Press the right arrow button in arduino IDE, this compiles and uploads the code.

## VSCode

You can use VSCode Arduino extension instead of Arduino IDE. Everything is easy.

