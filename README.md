# Time-To-Go-Home
[![Build Status](https://travis-ci.com/mmphego/time-to-go-home.svg?branch=master)](https://travis-ci.com/mmphego/time-to-go-home)
![GitHub](https://img.shields.io/github/license/mmphego/time-to-go-home.svg)

## The Story


## Installation

A program to send desktop notifications.

If running `XUbuntu`:
*   `sudo apt install xfce4-notifyd`
else:
*   `sudo apt-get install libnotify-bin`

`pip install -U .`

## Usage

```bash
eta_to_home.py -h

usage: eta_to_home.py [-h] [--loglevel LOG_LEVEL] --config CONFIG_INFO

optional arguments:
  -h, --help            show this help message and exit
  --loglevel LOG_LEVEL  log level to use, default [INFO], options [INFO,
                        DEBUG, ERROR]
  --config CONFIG_INFO, -c CONFIG_INFO
                        Config file containing origin, destination and gmaps
                        API key

```
Usage:
    `eta_to_home.py -c ~/.secrets/gmaps_secret.ini`

What's in the secrets file:

```bash
# cat ~/.secrets/gmaps_secret.ini
[Google Maps]
origin = ''
dest = ''
googlemaps_api = ''
```

## Oh, Thanks!

By the way... Click if you'd like to [say thanks](https://saythanks.io/to/mmphego)... :) else *Star* it.

✨🍰✨

## Feedback

Feel free to fork it or send me PR to improve it.

