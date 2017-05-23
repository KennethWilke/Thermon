#!/usr/bin/env python
import time
import sys
from ssh import SSHConnection
from getpass import getpass, getuser
from outputs import *

class Thermon(object):
    def __init__(self, config):
        self.config = config
        self.connect()
        self.outputs = []
        self.add_output(CSVLogger)
        self.add_output(MatplotlibPlotter)

    def add_output(self, constructor):
        self.outputs.append(constructor(self.config))
    def connect(self):
        if 'host' in self.config['target']:
            host = self.config['target']['host']
        else:
            host = raw_input('Target host: ')

        if 'username' in self.config['target']:
            username = self.config['target']['username']
        else:
            username = raw_input('Target username: ')

        if 'password' in self.config['target']:
            password = self.config['target']['password']
        else:
            password = getpass()

        self.target = SSHConnection(host, username, password)

    def run(self):
        self.start_time = time.time()
        while True:
            try:
                for category in self.config['probes'].keys():
                    timestamp, data = self.poll_data(category)
                    for output in self.outputs:
                        output.write(category, timestamp, data)
                time.sleep(0.5)
            except KeyboardInterrupt:
                print 'Quitting'
                sys.exit(0)

    def poll_data(self, category):
        polltime = round(time.time() - self.start_time, 3)
        probedata = {}
        probes = self.config['probes'][category]['probes']

        for probe, path in probes.iteritems():
            data_raw = self.target.call('cat {}'.format(path))[0].strip()
            probedata[probe] = int(data_raw)

        return polltime, probedata
