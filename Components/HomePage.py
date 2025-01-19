from PyQt6.QtWidgets import (
    QMainWindow,
    QPushButton, QToolBar,
    QLabel, QVBoxLayout,
    QWidget, QHBoxLayout, 
)
from Components.CpuGraph import CpuGraph
from Components.CpuSpecs import CpuSpecWindow
import PyQt6.QtCore as QtCore
from Components.ThreadChart import ThreadChart
from PyQt6.QtGui import QIcon
# Subclass QMainWindow to customize your application's main window
class Home(QMainWindow):
    #locational formatting
    def __init__(self):
        super().__init__()
        #locational formatting
        toolbar = QToolBar()
        main_layout = QVBoxLayout()
        cpu_thread = QHBoxLayout()
        graph_and_table = QHBoxLayout()
        #Component declarations
        self.cpu_graph = CpuGraph()
        self.thread_table = ThreadChart()

        cpu_info = QPushButton("CPU information")
        refresh_button = QPushButton("Refresh")
        self.setWindowTitle("Eric Lee's special device manager")
        #wmi functionality

        #foramtting layout 
        main_layout.addWidget(QLabel("Eric Lee's special device manager"))
        main_layout.addLayout(cpu_thread)
        cpu_thread.addWidget(QLabel("CPU Graph"))
        cpu_thread.addWidget(QLabel("Threads and Processes"))
        main_layout.addLayout(graph_and_table)
        graph_and_table.addWidget(self.cpu_graph.init())
        graph_and_table.addWidget(self.thread_table.actual_chart)
        main_layout.addWidget(cpu_info)
        main_layout.addWidget(refresh_button)

        self.timer = QtCore.QTimer()
        self.timer.setInterval(600)
        self.timer.timeout.connect(lambda: self.refresh()) 
        self.timer.start()
        cpu_info.clicked.connect(lambda: self.SpecWindow())
        refresh_button.clicked.connect(lambda: self.thread_table.update())

        #finalization
        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)
        self.setFixedSize(800,600)
        self.setWindowIcon(QIcon("Components/Assets/EricCartman.png"))
        self.addToolBar(toolbar)


    def SpecWindow(self):
        self.spec_window = CpuSpecWindow()
        self.spec_window.show()
    def refresh(self):
        self.cpu_graph.update() 
        

        

        
    

        
