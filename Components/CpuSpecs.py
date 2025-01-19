from PyQt6.QtWidgets import (
    QLabel, QVBoxLayout, QWidget, QFileIconProvider
)
from PyQt6.QtGui import QIcon
import wmi


class CpuSpecWindow(QWidget):
    def __init__(self):    
        super().__init__()
        self.spec_layout = QVBoxLayout()
        w = wmi.WMI()
        
        self.setWindowTitle("CPU INFO")
        self.setWindowIcon(QIcon("Components/Assets/Info.png"))
        self.spec_layout.addWidget(QLabel("CPU INFO"))
        for cpu in w.Win32_Processor():
            self.spec_layout.addWidget(QLabel("Cpu Name: " + str(cpu.name)))
            self.spec_layout.addWidget(QLabel("Max Clock Speed: " + str(cpu.MaxClockSpeed)))
            self.spec_layout.addWidget(QLabel("Number of Cores: " + str(cpu.NumberOfCores)))
        self.setLayout(self.spec_layout)
        self.setFixedSize(300,300)
        
