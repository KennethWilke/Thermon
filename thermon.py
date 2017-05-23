#!/usr/bin/env python
import sys
from argparse import ArgumentParser
from ConfigParser import SafeConfigParser
from thermon import Thermon

# Parse command line and config file
parser = ArgumentParser(description="Poll hwmon data for logging and displaying")
parser.add_argument("config", help="Configuration to run")
args = parser.parse_args()

configparser = SafeConfigParser()
configparser.read(args.config)

config = {'target': {},
          'probes': {}}

if 'target' in configparser.sections():
    for key, value in dict(configparser.items('target' )).iteritems():
        config['target'][key] = value

for section in configparser.sections():
    if section.startswith('probes:'):
        category = section.split(':')[1]
        config['probes'][category] = {'probes': {}}
        for probe, path in dict(configparser.items(section)).iteritems():
            config['probes'][category]['probes'][probe] = path

monitor = Thermon(config)
monitor.run()
