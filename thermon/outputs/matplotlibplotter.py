import matplotlib.pyplot as plt
import matplotlib.animation as animation
import threading


class MatplotlibPlotter(object):
    def __init__(self, config):
        self.config = config
        self.sampletimes = []
        self.probedata = {}
        for category in config['probes'].keys():
            self.probedata[category] = {}
            thread = threading.Thread(target=plotThread, args=(self, category))
            thread.start()

    def write(self, category, timestamp, data):
        self.sampletimes.append(timestamp)
        for metric, value in data.iteritems():
            if metric not in self.probedata[category]:
                self.probedata[category][metric] = [value]
            else:
                self.probedata[category][metric].append(value)


def plotThread(plotter, category):
    fig = plt.figure()
    subplot = fig.add_subplot(1, 1, 1) 

    def animate(i):
        ''' This function is called by matplotlib for each update '''
        subplot.clear()
        for probe in sorted(plotter.probedata[category].keys()):
            data_len = min(len(plotter.sampletimes),
                           len(plotter.probedata[category][probe]))
            subplot.plot(plotter.sampletimes[0:data_len],
                         plotter.probedata[category][probe][0:data_len],
                         label=probe)
        subplot.legend()

    # Kick off matplotlib
    ani = animation.FuncAnimation(fig, animate, interval=1000)
    plt.show()
