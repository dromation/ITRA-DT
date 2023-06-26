# ITRA-DT

This document is used for the technical description of an application. The main purpose of this app is to detect the temperature of different surfaces. It is based on the Open CV library and Kivy Python modules. This app is mandatory for development due to the development of the Parvaform extruder.

ITRA-DT is a name combination from known scientific methods according to ISO standards that cover infrared, thermal, and computer vision systems. 

The application is in the beta stage

Version: 0.5

To-do: 
- add an inverted function to the main app
- add thresholding function
- create class methods for thermal calculations in the main app
- create class methods using matplotlib to generate graphs of Liquidus-Solidus metastates
- create a class to implement K-clustering learning with templates

Files to use:
- itradt.py is the main Python file
- itradt.kv is a Kivy file (you don't need to use that, since code is in main is not using Builder)


This app only runs and displays applied colors on grayscale images. It is still in development, but it will work since temperature templates can be calculated and displayed by using vector matrixes on each RGB channel. It is more explained in the next chapter.


## Thermal Image processing - fake thermal image processing

Cameras such as webcams (internal, external), and others ... all use CMOS sensors, well which really depends on the manufacturer and brand (Sony, Canon, Logitech, Canyon... etc...). These images, which are captured through normal RGB channels, are often displayed as 8-bit images, which means that each channel has only from 0 to 255 values. And they are only 3 of these channels: RED, GREEN, BLUE. As an alternative, many computer vision systems use also the HSV method of image processing. But in the case of thermal image processing, you must know this: images captured using infrared or thermal vision camera, have all 16bit values, which means that each channel has 65535 values. 

To fake thermal images, we must understand 16-bit images. 8-bit image can be converted to 16-bit by using software such as GNU GIMP. But it is not necessary that will work since the thermal image also contains lumination (lux) wavelength on each pixel. To create a fake thermal image, we need to do this: capture an image with the ANYDEPTH method (this gives in-pixel depth information but from 0 - 255 values on each channel), we need to capture a raw image (an alpha image - an image that is not changed, at least for now no gamma corrections and stuff), and normal GRAYSCALE image.
