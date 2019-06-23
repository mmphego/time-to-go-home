#!/usr/bin/env python3

import logging
import os
import subprocess
import time

from datetime import datetime

import googlemaps

logger = logging.getLogger(__name__)


class TimeToHome:
    def __init__(self, origin: str, dest: str, api: str, log=logger):
        self.origin = origin
        self.dest = dest
        self.api = api
        self.logger = log

    def sendmessage(self, title, message):
        subprocess.call(["notify-send", title, message])

    def getDrivingTime(self):
        gmaps = googlemaps.Client(key=self.api)
        now = datetime.now()
        try:
            rawDirection = gmaps.directions(self.origin, self.dest, departure_time=now)[0]
        except Exception:
            self.logger.exception("Could not get the actual time and distance of your commute")
            raise
        else:
            legs = rawDirection["legs"][0]
            distance = legs["distance"]["text"]
            duration = legs["duration"]["text"]
            start_address = legs["start_address"]
            end_address = legs["end_address"]
            return {
                "distance": distance,
                "duration": duration,
                "start_address": start_address,
                "end_address": end_address,
            }

    def notifyMe(self):
        try:
            drivingDict = self.getDrivingTime()
            drivetime = float(drivingDict["duration"].split()[0])
        except Exception:
            self.logger.exception("Could not get driving time.")
        else:
            if drivetime < 35:
                msg = "It will take you an average \n<b>~{}/{}</b>\n\nFrom: {} \n\nTo: {}.".format(
                    drivingDict["duration"],
                    drivingDict["distance"],
                    drivingDict["start_address"],
                    drivingDict["end_address"],
                )
                self.sendmessage("Time to go Home", msg)
            else:
                msg = (
                    "Its is not a good idea to go home now, as it might take you over {drivetime} "
                    "to get home"
                )
                self.sendmessage("Don't go Home", msg)
