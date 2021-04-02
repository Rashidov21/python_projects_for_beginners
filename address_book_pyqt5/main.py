# -*- coding: utf-8 -*-
# address_book/main.py

import sys

from PyQt5.QtWidgets import QApplication
import views

def main():
    """RP Contacts main function."""
    # Create the application
    app = QApplication(sys.argv)
    # Create the main window
    win = views.Window()
    win.show()
    # Run the event loop
    sys.exit(app.exec())
