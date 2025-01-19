import sys
from PyQt6.QtWidgets import QApplication 
from Components.HomePage import Home



app = QApplication(sys.argv)
window = Home()    
window.show()

#makes the application run
app.exec()
