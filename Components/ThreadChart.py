from PyQt6.QtWidgets import QTableView
import wmi
import psutil
from PyQt6 import QtCore
from PyQt6.QtCore import Qt


class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self._data[0])

class ThreadChart():
    def __init__(self):
        super().__init__()
        self.manager = wmi.WMI()
        self.actual_chart = QTableView()
        self.title_columns = ["Process name", "PID", "Thread Count","Priority","CPU usage" ]
        self.update()
    def update(self):
        self.data = []
        self.data.append(self.title_columns)
        for process in self.manager.Win32_Process():
            temp_data = []
            temp_data.append(process.name)
            temp_data.append(process.ProcessID)
            temp_data.append(process.threadCount)
            temp_data.append(process.Priority)
            temp_data.append("WIP")
            self.data.append(temp_data)
        
        model = TableModel(self.data)
        self.actual_chart.setModel(model)
        self.actual_chart.setFixedSize(400,500)
