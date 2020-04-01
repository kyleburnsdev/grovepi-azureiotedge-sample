# GrovePI+ with Azure IoT Edge

## Overview

This sample is built on top of Microsoft's IoT Edge Python Tutorial, which can can found at https://docs.microsoft.com/en-us/azure/iot-edge/tutorial-python-module and adds support for interacting with Dexter Industries' GrovePi+, which is a board that allows easy connection of sensors and actuators and comes with an SDK to interact with the hardware. Some of the main changes to get this running were included:

- Changed the base image in the dockerfile to Raspbian Stretch because the Dexter software depended on this distribution
- Added the "pi" user, making the user a sudoer. This was required because the Dexter tools have a hard requirement on being run (or at least installed) as the "pi" user
- Updated deployment template to give privileged to the module for /sys:/sys (the whole host system). In reality, this should be much more targeted to give only what is absolutely necessary for I/O

## Pre-requisites

- Raspberry Pi hardware
- GrovePi+ board
- Grove LED Bar connected to port D5 (different port requires code change in main.py)
- Azure Container Registry instance
- Azure IoT Hub instance
- Raspberry Pi configured with Azure IoT Edge as described at https://docs.microsoft.com/en-us/azure/iot-edge/how-to-install-iot-edge-linux
- RECOMMENDED: complete the Python tutorial mentioned above to ensure that your development environment is set up correctly and learn how to deploy code to Azure IoT Edge devices

## Potential future enhancements (feel free to shoot me a PR)

- Add bi-directional communication with the IoT Hub to make IoT Edge more than just a runtime container and distribution mechanism for the container
- Integrate more sensors and actuators
- Iterate on optimizing the image (maybe create a base image for other Azure IoT Edge modules using the GrovePi+)

## Warrantee

This code is intended for educational purposes to help learn more about the various technologies used. It is not intended to be the basis of any production solution and is not supported in any way by me or my employer.
