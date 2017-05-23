class CSVLogger(object):
    def __init__(self, config):
        self.config = config
        self.filehandles = {}
        for category in self.config['probes'].keys():
            csvfile = open('{}.csv'.format(category), 'w')
            probes = ','.join(sorted(config['probes'][category]['probes']))
            csvfile.write('time,{}\n'.format(probes))
            self.filehandles[category] = csvfile

    def write(self, category, timestamp, data):
        csvline = '{}'.format(timestamp)
        for probe in sorted(data.keys()):
            csvline += ',{}'.format(data[probe])
        self.filehandles[category].write(csvline + '\n')
