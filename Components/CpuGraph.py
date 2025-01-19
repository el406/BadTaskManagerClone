import pyqtgraph as pg
import numpy as np
import psutil
import time



class CpuGraph:
    def __init__(self):
     self.timedata = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
     self.usagePercents = list()
     self.plot_widget = pg.PlotWidget() 
     self.plot_widget.setYRange(0,100)
    

    def init(self):
        for i in range(0,16):
            time.sleep(0.01)
            cpu_usage = psutil.cpu_percent(0)
            self.usagePercents.append(cpu_usage)
        self.plot_widget.plot(self.timedata,self.usagePercents)
        return self.plot_widget
        
    def update(self):
      self.usagePercents = self.usagePercents[1:]
      self.usagePercents.append(psutil.cpu_percent(0))
      self.plot_widget.clear()
      self.plot_widget.plot(self.timedata, self.usagePercents)

        
    
