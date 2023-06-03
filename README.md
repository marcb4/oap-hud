# The OpenAuto Pro Head-Up-Display

Thanks to BlueWave (creators behind OpenAuto Pro) to share their example api.proto and example code!
https://github.com/bluewave-studio/openauto-pro-api/blob/main/api_examples/python/NavigationStatus.py

I needed to change the common folder to commons, because otherwise it tried to find the module `common` as a pip package.

The icon is dynamically genereted by OAP/Android Auto. It reads the current icon and displays it.


# Requirements
On your Client:
```
pip3 install pygame protobuf~=3.19
```

A Raspberry Pi Zero W or any other device that knows python and has a wireless module to connect to your OAP Head Unit.

# Setup
## Prepare your Client
* Clone or Copy all files from this repo to your desired location (eg. `/home/pi/oap-hud`)
* (Optional) Make sure that the IP in line 63 of hud.py matches the IP of your Head Unit
* Make sure your Client automatically connects to WiFi of your OAP Head Unit
* Make sure to install the required python modules as stated in the requirements section
* Make sure that the .service file is properly configured and adjust your script location in line 8 of oap-hud.service

## Adjusting your resolution
If 800 x 600 is not your resolution, make sure to adjust your resolution in line 48 in `hud.py`. You may need to adjust all other surface locations.

## Copy .service file to systemd
```
sudo cp oap-hud.service /etc/systemd/system/oap-hud.service
sudo systemctl daemon-reload
sudo systemctl enable --now oap-hud.service
```
