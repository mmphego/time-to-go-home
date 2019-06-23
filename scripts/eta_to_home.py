#!/usr/bin/env python3

import argparse
import logging
from pathlib import Path
from sys import exit
import configparser
from time_to_go_home import TimeToHome

config_parser = configparser.ConfigParser()

logger = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser(description="")

    parser.add_argument(
        "--loglevel",
        dest="log_level",
        default="INFO",
        help="log level to use, default [INFO], options [INFO, DEBUG, ERROR]",
    )
    parser.add_argument(
        "--config",
        "-c",
        dest="config_info",
        required=True,
        help="Config file containing origin, destination and gmaps API key",
    )

    args = vars(parser.parse_args())
    config_file = Path(args.get('config_info')).absolute()
    if config_file:
        config_parser.read(config_file)
        configdict = {
            section: dict(config_parser.items(section)) for section in config_parser.sections()
        }
        configdict = {name: token for k,v in configdict.items() for name, token in v.items()}
        timetohome = TimeToHome(configdict['origin'], configdict['dest'], configdict['googlemaps_api'], log_level=args.get('log_level', "INFO").upper())
        timetohome.notifyMe()


if __name__ == "__main__":
    main()
